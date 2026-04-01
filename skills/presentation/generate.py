"""
Навык: генерация презентации из текста доклада.

Использование:
  python generate.py доклад.txt [--format pdf|pptx|both]
  python generate.py доклад.pdf [--format pdf|pptx|both]

Процесс:
  1. Извлекает текст из .txt или .pdf
  2. Отправляет текст в Claude API → получает структуру слайдов (JSON)
  3. Рендерит PDF и/или PPTX
"""

import sys
import os
import json
import argparse
import anthropic

# ─── Путь к ресурсам (изображения, логотип) ──────────────────────────────────
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

# ─── Шаблон промпта для Claude ────────────────────────────────────────────────
SYSTEM_PROMPT = """Ты — ассистент, который преобразует текст доклада в структуру слайдов для презентации.

Верни ТОЛЬКО валидный JSON-массив слайдов. Без пояснений, без markdown-блоков — только JSON.

Каждый слайд — объект с полями:
- "type": "title" | "content" | "content_right" | "conclusion"
- "title": строка (можно \\n для переноса)
- "points": список строк с тезисами (для всех типов кроме "title")
- "subtitle": строка (только для type="title")
- "image": имя файла изображения из assets/ (необязательно)

Правила:
- Первый слайд всегда type="title"
- Последний слайд всегда type="conclusion"
- Чередуй "content" и "content_right" для разнообразия
- 3–5 тезисов на слайд, каждый тезис — одно законченное предложение
- Заголовки лаконичны (3–6 слов)
- Оптимальное количество слайдов: 7–12
"""

def extract_text(path: str) -> str:
    """Извлечь текст из .txt или .pdf файла."""
    if path.endswith(".pdf"):
        import fitz
        doc = fitz.open(path)
        return "\n".join(page.get_text() for page in doc)
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()


def text_to_slides(text: str) -> list:
    """Отправить текст в Claude и получить структуру слайдов."""
    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"Преобразуй этот доклад в презентацию:\n\n{text}"
            }
        ]
    )

    raw = message.content[0].text.strip()

    # На случай если модель всё же обернула в ```json ... ```
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]

    return json.loads(raw)


def render(slides_data: list, output_format: str, output_dir: str):
    """Запустить рендеринг в нужный формат."""
    import importlib.util

    results = []

    if output_format in ("pdf", "both"):
        spec = importlib.util.spec_from_file_location(
            "make_pdf", os.path.join(os.path.dirname(__file__), "make_pdf.py")
        )
        mod = importlib.util.module_from_spec(spec)

        # Подменяем slides_data и OUTPUT перед выполнением модуля
        mod.slides_data = slides_data
        output_path = os.path.join(output_dir, "presentation.pdf")
        mod.OUTPUT = output_path

        spec.loader.exec_module(mod)
        results.append(output_path)
        print(f"✅ PDF: {output_path}")

    if output_format in ("pptx", "both"):
        spec = importlib.util.spec_from_file_location(
            "make_presentation",
            os.path.join(os.path.dirname(__file__), "make_presentation.py")
        )
        mod = importlib.util.module_from_spec(spec)
        mod.slides_data = slides_data
        output_path = os.path.join(output_dir, "presentation.pptx")
        mod.OUTPUT = output_path

        spec.loader.exec_module(mod)
        results.append(output_path)
        print(f"✅ PPTX: {output_path}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Генерация презентации из текста доклада")
    parser.add_argument("input", help="Путь к файлу доклада (.txt или .pdf)")
    parser.add_argument("--format", choices=["pdf", "pptx", "both"], default="both",
                        help="Формат вывода (по умолчанию: both)")
    parser.add_argument("--out", default=".", help="Папка для сохранения результата")
    args = parser.parse_args()

    print(f"📄 Читаю текст: {args.input}")
    text = extract_text(args.input)

    print("🤖 Отправляю в Claude, жду структуру слайдов...")
    slides_data = text_to_slides(text)
    print(f"📊 Получено слайдов: {len(slides_data)}")

    # Сохранить JSON рядом для отладки
    json_path = os.path.join(args.out, "slides_data.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(slides_data, f, ensure_ascii=False, indent=2)
    print(f"💾 Структура слайдов: {json_path}")

    render(slides_data, args.format, args.out)


if __name__ == "__main__":
    main()
