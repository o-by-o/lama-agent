"""
Генерация PDF-презентации: Святые места Бурятии
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
OUTPUT    = "/Users/oboton/Music/Docs/Святые_места_Бурятии.pdf"

# ─── Font registration ──────────────────────────────────────────────────────
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
        "title": "Святые места Бурятии —\nуникальный ресурс\nдля развития паломничества\nи религиозного туризма",
        "subtitle": "Буддийская Традиционная Сангха России",
    },
    {
        "type": "content",
        "title": "Иволгинский дацан —\nдуховная столица буддизма\nв России",
        "image": "/Users/oboton/Music/Docs/ivolginsky_photo_only_filter_png_1773867091786.png",
        "points": [
            "Главный буддийский монастырский комплекс страны — «Гандан Геже Даши Чойнхорлин», основан в 1945 году",
            "Десять дуганов-храмов, пять субурганов-ступ, оранжерея со священным деревом Бодхи",
            "Буддийский университет «Даши Чойнхорлин» — единственное учебное заведение буддийской философии в России",
            "Десятки тысяч паломников ежегодно; развитая инфраструктура — гостиница, столовая, Галерея искусств",
        ],
    },
    {
        "type": "content_right",
        "title": "Нетленное тело\nХамбо Ламы Этигэлова",
        "image": "/Users/oboton/Music/Docs/lama_bw_editorial_png_1773868082909.png",
        "points": [
            "XII Пандито Хамбо Лама Этигэлов погрузился в медитацию в 1927 году в позе лотоса",
            "В 2002 году саркофаг официально вскрыт — тело нетленно спустя 75 лет без мумификации",
            "С точки зрения естественных наук это явление необъяснимо — тело сохраняет позу без подпорок",
            "Ежегодный Праздник Хамбо Ламы Этигэлова — масштабное событие с молебном и спортивными состязаниями",
        ],
    },
    {
        "type": "content",
        "title": "Гора Бархан-Уула —\nсвященная вершина\nБаргузинской долины",
        "image": "/Users/oboton/Music/Docs/mountains_magazine_filter_png_1773868505221.png",
        "points": [
            "Одна из главных святынь Баргузинской долины, упоминаемая в древних тибетских текстах",
            "Охраняет буддийское учение с севера; место медитации великого йогина Соодой-ламы",
            "Ежегодный молебен «Барха тахилга» и паломнические восхождения на вершину горы",
            "Первое место на конкурсе «7 чудес природы Бурятии» в 2009 году (30 000+ голосов)",
        ],
    },
    {
        "type": "content_right",
        "title": "Лик богини Янжимы —\nнерукотворное чудо\nБаргузинского района",
        "image": "/Users/oboton/Music/Docs/yanzhima_magazine_filter_png_1773868771111.png",
        "points": [
            "В 2005 году на скале близ села Ярикта обнаружен нерукотворный образ танцующей богини",
            "Янжима (Сарасвати) — богиня искусств, наук, мудрости и покровительница материнства",
            "Хамбо лама Аюшеев обнаружил лик во время медитации при поисках буддийских реликвий",
            "Рядом возведён «Дворец богини Янжимы»; место взято под опеку Сангхой России",
        ],
    },
    {
        "type": "content",
        "title": "Ступа Джарун Хашор —\n«Ступа, исполняющая\nжелания»",
        "image": "/Users/oboton/Music/Docs/stupa_magazine_filter_png_1773867556689.png",
        "points": [
            "Аналог великой ступы Бодхнатх в Непале; высота 33 м, основание 44×44 м",
            "13 ступенек символизируют путь избавления от земных мук и погружения в Нирвану",
            "Первоначально построена в 1919 г., разрушена в 1937 г., восстановлена и освящена в 2001 г.",
            "В центре — учительский храм с 64 окошками и портретами, дуганы Авалокетишвары и 21-й Тары",
        ],
    },
    {
        "type": "content_right",
        "title": "Скала Шаманка\n(мыс Бурхан) —\nсвятыня Байкала",
        "image": "img_shamanka.png",
        "points": [
            "Одна из девяти святынь Азии — двухвершинная скала на острове Ольхон, озеро Байкал",
            "Место встречи шаманской и буддийской традиций; сквозная Шаманская пещера длиной 12 м",
            "Здесь совершались культовые обряды и паломничества со времён первых шаманов",
            "Государственный природно-исторический памятник; археологические находки эпохи неолита",
        ],
    },
    {
        "type": "content",
        "title": "Сакральная география\nБурятии — сеть\nпаломнических маршрутов",
        "image": "/Users/oboton/Music/Docs/buddhist_sites_collage_magazine_filter_png_1773872819730.png",
        "points": [
            "Сандаловый Будда «Зандан Жуу» — первая скульптура Будды, созданная при его жизни (высота 2,18 м)",
            "Этигэловский святой источник — комплекс целебных ключей, каждый помогает от определённых болезней",
            "Более 260 лет буддийской традиции — живая сеть дацанов, ступ и святынь мирового значения",
        ],
    },
    {
        "type": "conclusion",
        "title": "Заключение",
        "image": "/Users/oboton/Music/Docs/river_canyon_magazine_filter_png_1773871238014.png",
        "points": [
            "Святыни Бурятии — уникальный ресурс для паломничества и религиозного туризма в масштабах России",
            "Нетленное тело Хамбо Ламы Этигэлова — явление, не имеющее аналогов в мире",
            "Иволгинский дацан, сакральные горы, источники — целостное духовное пространство",
            "Сангха России готова к сотрудничеству в создании паломнических маршрутов",
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
    img_path = "/Users/oboton/Music/Docs/buddha_rock_magazine_filter_png_1773869713360.png"
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
    title_y = PAGE_H - 160
    for line in title_lines:
        draw_text(c, line, 40, title_y, font=font_bold, size=20, color=WHITE_C)
        title_y -= 30

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
c.setTitle("Святые места Бурятии — паломничество и религиозный туризм")
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
