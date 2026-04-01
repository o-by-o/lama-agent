"""
Генерация PDF-презентации: Роль буддизма в ценностном пространстве Большой Евразии
Формат: A4 landscape (альбомная ориентация)
"""

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import inch, mm, cm
from reportlab.lib.colors import HexColor, Color, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import os

# ─── Page setup ──────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = landscape(A4)  # 841.89 x 595.28 points

# ─── Colors ──────────────────────────────────────────────────────────────────
DARK_BG     = HexColor('#0D0D14')
CARD_BG     = HexColor('#1E1C2E')
GOLD        = HexColor('#C9A962')
GOLD_BRIGHT = HexColor('#E8CB7B')
WHITE_C     = HexColor('#F2F0EB')
SUBTLE      = HexColor('#9A97A8')
ACCENT_LINE = HexColor('#3A3652')

# ─── Paths ───────────────────────────────────────────────────────────────────
IMG_DIR   = "/Users/oboton/Music/Docs/Presentation_Project"
LOGO_PATH = os.path.join(IMG_DIR, "logo.png")
OUTPUT    = "/Users/oboton/Music/Docs/Буддизм_и_Большая_Евразия.pdf"

# ─── Font registration ──────────────────────────────────────────────────────
# Try to find a system font that supports Cyrillic
FONT_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Italic.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial.ttf",
]

font_regular = "Helvetica"
font_bold = "Helvetica-Bold"
font_italic = "Helvetica-Oblique"

# Register Arial if available (supports Cyrillic)
if os.path.exists("/System/Library/Fonts/Supplemental/Arial.ttf"):
    pdfmetrics.registerFont(TTFont('Arial', '/System/Library/Fonts/Supplemental/Arial.ttf'))
    font_regular = 'Arial'
if os.path.exists("/System/Library/Fonts/Supplemental/Arial Bold.ttf"):
    pdfmetrics.registerFont(TTFont('ArialBold', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
    font_bold = 'ArialBold'
if os.path.exists("/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"):
    pdfmetrics.registerFont(TTFont('ArialBI', '/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf'))
if os.path.exists("/System/Library/Fonts/Supplemental/Arial Italic.ttf"):
    pdfmetrics.registerFont(TTFont('ArialItalic', '/System/Library/Fonts/Supplemental/Arial Italic.ttf'))
    font_italic = 'ArialItalic'


# ─── Slide data ──────────────────────────────────────────────────────────────
slides_data = [
    {
        "type": "title",
        "title": "Роль буддизма\nв ценностном пространстве\nБольшой Евразии",
        "subtitle": "Буддийская Традиционная Сангха России",
    },
    {
        "type": "content",
        "title": "Исторический контекст",
        "image": "img_historical.png",
        "points": [
            "Буддизм — одна из старейших духовных традиций человечества, существующая более 2 500 лет",
            "Как мировая религия буддизм распространился по всей Азии, сформировав единое культурное пространство",
            "Общие ценности — ненасилие, сострадание, поиск истины — объединяют народы Евразии",
            "Буддийские монастыри — живые центры сохранения, изучения и передачи традиций",
        ],
    },
    {
        "type": "content_right",
        "title": "Буддизм в евразийском\nкультурном пространстве",
        "image": "img_cultural.png",
        "points": [
            "Буддийская цивилизация охватывает народы Центральной, Восточной и Юго-Восточной Азии",
            "Единое духовное пространство: общая священная литература, иконография, архитектура, этика",
            "Буддийские культурные коды — основа диалога между цивилизациями Большой Евразии",
            "Искусство, медицина, образование — плоды межкультурного буддийского обмена",
        ],
    },
    {
        "type": "content",
        "title": "Буддийская философия\nкак основа ценностного диалога",
        "image": "img_philosophy.png",
        "points": [
            "Взаимозависимость — все явления связаны между собой",
            "Сострадание — основа ненасильственного взаимодействия цивилизаций",
            "Серединный путь: отказ от крайностей как метод гармонизации отношений",
            "Стремление к просветлению ради блага всех существ",
        ],
    },
    {
        "type": "content_right",
        "title": "Этика ненасилия\nи миростроительство",
        "image": "img_nonviolence.png",
        "points": [
            "Принцип ненасилия — основополагающая ценность буддийской этики",
            "Буддийские традиции мирного диалога и современные миротворческие инициативы",
            "Притча о «раскалённом угле»: культура вражды разрушает прежде всего самого носителя",
            "Внутренняя собранность и самоконтроль — залог мира во внешних отношениях",
        ],
    },
    {
        "type": "content",
        "title": "Буддизм\nи современные вызовы",
        "image": "img_modern.png",
        "points": [
            "Высокая адаптивность буддизма к условиям цифровизации и социальных трансформаций",
            "Буддийская критика алчности: альтернатива логике бесконечного потребления",
            "Притча о «плоте»: технологии — инструмент, а не самоцель; ценностное ядро неизменно",
            "Осознанность и умеренность — буддийский ответ на экологические и духовные кризисы",
        ],
    },
    {
        "type": "content_right",
        "title": "Россия\nи евразийский буддизм",
        "image": "img_historical.png",
        "points": [
            "Буддизм — часть духовного фундамента российской идентичности наряду с православием и исламом",
            "Буддийские регионы: Бурятия, Калмыкия, Тыва — живые мосты к цивилизациям Востока",
            "Раскрытие «внутреннего Востока» России: созерцательное, сострадательное сознание",
            "Притча о горчичном зерне: за различием традиций — единый опыт человеческой уязвимости",
        ],
    },
    {
        "type": "content",
        "title": "Роль буддизма сегодня:\nключевые аспекты",
        "image": "img_today.png",
        "points": [
            "Миротворческая функция: мирное взаимодействие и взаимопроникновение культур",
            "Нравственный ориентир: этика ненасилия, сострадания и личной ответственности",
            "Интеграционный потенциал: укрепление горизонтальных связей в Большой Евразии",
            "Противовес вестернизации: сохранение культурной самобытности народов",
            "Диалог государства и духовенства: гармонизация общественных отношений",
        ],
    },
    {
        "type": "conclusion",
        "title": "Заключение",
        "image": "img_conclusion.png",
        "points": [
            "Роль буддизма в ценностном пространстве Большой Евразии сохраняется и возрастает",
            "Традиционные духовные учения помогают нащупывать пути к справедливому и устойчивому миропорядку",
            "Основа — взаимное уважение, сострадание и осознание глубинной взаимосвязанности всех существ",
            "Буддийская мудрость — ресурс для преодоления кризисов и построения гармоничного будущего",
        ],
    },
]


# ─── Drawing helpers ─────────────────────────────────────────────────────────

def draw_bg(c):
    """Full page dark background."""
    c.setFillColor(DARK_BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def draw_rect(c, x, y, w, h, fill_color=None, stroke_color=None, stroke_width=0.5, radius=0):
    """Draw rectangle (y is from bottom)."""
    c.saveState()
    if fill_color:
        c.setFillColor(fill_color)
    if stroke_color:
        c.setStrokeColor(stroke_color)
        c.setLineWidth(stroke_width)
    if radius > 0:
        c.roundRect(x, y, w, h, radius, fill=1 if fill_color else 0,
                    stroke=1 if stroke_color else 0)
    else:
        c.rect(x, y, w, h, fill=1 if fill_color else 0,
               stroke=1 if stroke_color else 0)
    c.restoreState()


def draw_image(c, img_path, x, y, w, h):
    """Draw image maintaining aspect ratio, cropping to fill."""
    if not os.path.exists(img_path):
        draw_rect(c, x, y, w, h, fill_color=CARD_BG, stroke_color=ACCENT_LINE)
        return

    # Clip to the target area
    c.saveState()
    clip_path = c.beginPath()
    clip_path.roundRect(x, y, w, h, 4)
    c.clipPath(clip_path, stroke=0)

    img = Image.open(img_path)
    img_w, img_h = img.size
    img_aspect = img_w / img_h
    box_aspect = w / h

    if img_aspect > box_aspect:
        # Wider image — fit height, center horizontally
        draw_h = h
        draw_w = h * img_aspect
        draw_x = x - (draw_w - w) / 2
        draw_y = y
    else:
        # Taller image — fit width, center vertically
        draw_w = w
        draw_h = w / img_aspect
        draw_x = x
        draw_y = y - (draw_h - h) / 2

    c.drawImage(img_path, draw_x, draw_y, draw_w, draw_h,
                preserveAspectRatio=False, mask='auto')
    c.restoreState()


def draw_logo(c, x, y, size=30):
    """Draw logo."""
    if os.path.exists(LOGO_PATH):
        c.drawImage(LOGO_PATH, x, y, size, size, mask='auto')


def draw_text(c, text, x, y, font=None, size=12, color=WHITE_C):
    """Draw single line of text. y is baseline."""
    c.saveState()
    c.setFillColor(color)
    c.setFont(font or font_regular, size)
    c.drawString(x, y, text)
    c.restoreState()


def draw_multiline(c, text, x, y, font=None, size=12, color=WHITE_C, leading=None):
    """Draw multi-line text (split by \\n). Returns y after last line."""
    if leading is None:
        leading = size * 1.25
    lines = text.split('\n')
    cy = y
    for line in lines:
        draw_text(c, line, x, cy, font=font, size=size, color=color)
        cy -= leading
    return cy


def draw_wrapped_text(c, text, x, y, max_width, font=None, size=12,
                      color=WHITE_C, leading=None):
    """Word-wrap text to fit max_width and draw it (pixel-accurate)."""
    if leading is None:
        leading = size * 1.35
    fn = font or font_regular

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip() if current_line else word
        if pdfmetrics.stringWidth(test_line, fn, size) <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    cy = y
    for line in lines:
        draw_text(c, line, x, cy, font=fn, size=size, color=color)
        cy -= leading
    return cy


def draw_bullet_points(c, points, x, y, max_width, size=11, color=WHITE_C, spacing=42):
    """Draw bullet points with gold square markers."""
    cy = y
    for point in points:
        # Gold square bullet
        dot_size = 5
        draw_rect(c, x, cy + 2, dot_size, dot_size, fill_color=GOLD)

        # Text (wrapped)
        text_x = x + 16
        text_w = max_width - 16
        cy = draw_wrapped_text(c, point, text_x, cy, text_w,
                               font=font_regular, size=size, color=color)
        cy -= (spacing - size * 1.35)  # additional gap between bullets
    return cy


def draw_footer(c):
    """Standard footer bar."""
    # Thin line
    draw_rect(c, 0, 32, PAGE_W, 0.5, fill_color=ACCENT_LINE)
    # Logo
    draw_logo(c, 20, 8, size=20)
    # Text
    draw_text(c, "Буддийская Традиционная Сангха России  ·  sangharussia.ru",
              46, 14, font=font_italic, size=6.5, color=SUBTLE)


# ─── Slide builders ──────────────────────────────────────────────────────────

def title_slide(c, data):
    draw_bg(c)

    # Right side: background photo — Иволгинский Дацан
    img_path = os.path.join(IMG_DIR, "img_russia.png")
    right_start = PAGE_W * 0.48
    draw_image(c, img_path, right_start, 0, PAGE_W - right_start, PAGE_H)

    # Dark overlay on right photo
    c.saveState()
    c.setFillColor(Color(0.05, 0.05, 0.08, alpha=0.6))
    c.rect(right_start, 0, PAGE_W - right_start, PAGE_H, fill=1, stroke=0)
    c.restoreState()

    # Solid left panel
    draw_rect(c, 0, 0, right_start, PAGE_H, fill_color=DARK_BG)

    # Top gold line
    draw_rect(c, 30, PAGE_H - 18, PAGE_W * 0.42, 1.5, fill_color=GOLD)

    # Logo
    logo_size = 55
    draw_logo(c, 40, PAGE_H - 95, size=logo_size)

    # Org name next to logo
    draw_text(c, "Буддийская Традиционная", 105, PAGE_H - 68,
              font=font_regular, size=9, color=GOLD)
    draw_text(c, "Сангха России", 105, PAGE_H - 80,
              font=font_regular, size=9, color=GOLD)

    # Main title
    title_lines = data["title"].split('\n')
    title_y = PAGE_H - 170
    for line in title_lines:
        draw_text(c, line, 40, title_y, font=font_bold, size=22, color=WHITE_C)
        title_y -= 34

    # Gold separator
    draw_rect(c, 40, title_y - 10, PAGE_W * 0.32, 1.5, fill_color=GOLD)

    # Bottom accent
    draw_text(c, "☸  sangharussia.ru", 40, 45,
              font=font_regular, size=8, color=SUBTLE)

    # Bottom gold line
    draw_rect(c, 30, 18, PAGE_W * 0.42, 1.5, fill_color=GOLD)


def content_slide_left_image(c, data):
    """Image on left, text on right."""
    draw_bg(c)

    img_path = os.path.join(IMG_DIR, data["image"])
    margin = 25
    img_x = margin
    img_y = margin + 15
    img_w = PAGE_W * 0.38
    img_h = PAGE_H - margin * 2 - 15

    # Card bg behind image
    draw_rect(c, img_x - 3, img_y - 3, img_w + 6, img_h + 6,
              fill_color=CARD_BG, stroke_color=ACCENT_LINE, radius=6)

    # Image
    draw_image(c, img_path, img_x, img_y, img_w, img_h)

    # Right content
    text_x = img_x + img_w + 30
    text_w = PAGE_W - text_x - margin

    # Title
    title_y = PAGE_H - 50
    title_y = draw_multiline(c, data["title"], text_x, title_y,
                             font=font_bold, size=19, color=WHITE_C, leading=24)

    # Gold line
    draw_rect(c, text_x, title_y - 8, min(text_w * 0.6, 200), 1.5, fill_color=GOLD)

    # Bullet points
    draw_bullet_points(c, data["points"], text_x, title_y - 30,
                       max_width=text_w, size=10.5, spacing=38)

    draw_footer(c)


def content_slide_right_image(c, data):
    """Text on left, image on right."""
    draw_bg(c)

    img_path = os.path.join(IMG_DIR, data["image"])
    margin = 25
    img_w = PAGE_W * 0.38
    img_h = PAGE_H - margin * 2 - 15
    img_x = PAGE_W - margin - img_w
    img_y = margin + 15

    # Card bg behind image
    draw_rect(c, img_x - 3, img_y - 3, img_w + 6, img_h + 6,
              fill_color=CARD_BG, stroke_color=ACCENT_LINE, radius=6)

    # Image
    draw_image(c, img_path, img_x, img_y, img_w, img_h)

    # Left content
    text_x = margin + 10
    text_w = img_x - text_x - 30

    # Title
    title_y = PAGE_H - 50
    title_y = draw_multiline(c, data["title"], text_x, title_y,
                             font=font_bold, size=19, color=WHITE_C, leading=24)

    # Gold line
    draw_rect(c, text_x, title_y - 8, min(text_w * 0.6, 200), 1.5, fill_color=GOLD)

    # Bullet points
    draw_bullet_points(c, data["points"], text_x, title_y - 30,
                       max_width=text_w, size=10.5, spacing=38)

    draw_footer(c)


def conclusion_slide(c, data):
    """Conclusion slide — same layout as content_slide_left_image for visual consistency."""
    draw_bg(c)

    img_path = os.path.join(IMG_DIR, data["image"])
    margin = 25
    img_x = margin
    img_y = margin + 15
    img_w = PAGE_W * 0.38
    img_h = PAGE_H - margin * 2 - 15

    # Card bg behind image
    draw_rect(c, img_x - 3, img_y - 3, img_w + 6, img_h + 6,
              fill_color=CARD_BG, stroke_color=ACCENT_LINE, radius=6)

    # Image
    draw_image(c, img_path, img_x, img_y, img_w, img_h)

    # Right content
    text_x = img_x + img_w + 30
    text_w = PAGE_W - text_x - margin

    # Title
    title_y = PAGE_H - 50
    title_y = draw_multiline(c, data["title"], text_x, title_y,
                             font=font_bold, size=19, color=WHITE_C, leading=24)

    # Gold line
    draw_rect(c, text_x, title_y - 8, min(text_w * 0.6, 200), 1.5, fill_color=GOLD)

    # Bullet points
    draw_bullet_points(c, data["points"], text_x, title_y - 30,
                       max_width=text_w, size=10.5, spacing=38)

    draw_footer(c)


# ─── Build PDF ───────────────────────────────────────────────────────────────

c = canvas.Canvas(OUTPUT, pagesize=landscape(A4))
c.setTitle("Роль буддизма в ценностном пространстве Большой Евразии")
c.setAuthor("Буддийская Традиционная Сангха России")

for i, slide_data in enumerate(slides_data):
    stype = slide_data["type"]
    if stype == "title":
        title_slide(c, slide_data)
    elif stype == "content":
        content_slide_left_image(c, slide_data)
    elif stype == "content_right":
        content_slide_right_image(c, slide_data)
    elif stype == "conclusion":
        conclusion_slide(c, slide_data)

    if i < len(slides_data) - 1:
        c.showPage()

c.save()
print(f"✅ PDF saved: {OUTPUT}")
