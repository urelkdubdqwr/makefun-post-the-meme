from PIL import Image, ImageDraw, ImageFont

W = H = 1200
BG = "#0b0f14"
CARD_FILL = "#151b23"
CARD_OUTLINE = "#2a3441"
BELL = "#f5c518"
TITLE = "#f2f5f9"
SUB = "#8b96a5"
CARD_TEXT = "#e8edf2"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

f_title = ImageFont.truetype(BOLD, 120)
f_sub = ImageFont.truetype(REG, 44)
f_card = ImageFont.truetype(REG, 42)
f_card_b = ImageFont.truetype(BOLD, 42)
f_bottom = ImageFont.truetype(BOLD, 88)


def center(text, font, y, fill):
    bbox = d.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    d.text(((W - w) / 2 - bbox[0], y), text, font=font, fill=fill)


def draw_bell(cx, cy, h):
    # bell body: a rounded triangle-ish polygon
    bw = h * 0.72
    top = cy - h / 2
    bot = cy + h / 2 - h * 0.12
    d.polygon(
        [
            (cx, top),
            (cx + bw / 2, bot),
            (cx - bw / 2, bot),
        ],
        fill=BELL,
    )
    # base bar
    bar = h * 0.14
    bx0 = cx - bw / 2 - h * 0.06
    bx1 = cx + bw / 2 + h * 0.06
    by1 = bot + bar
    d.rounded_rectangle([bx0, bot, bx1, by1], radius=bar / 2, fill=BELL)
    # clapper
    r = h * 0.1
    d.ellipse([cx - r, by1, cx + r, by1 + 2 * r], fill=BELL)


# Top title
center("3:07 AM", f_title, 60, TITLE)
center("you: asleep.", f_sub, 210, SUB)

# Cards
cards = [
    ("make.fun", " \u2014 bounty #48 entered"),
    ("make.fun", " \u2014 bot built"),
    ("make.fun", " \u2014 leaderboard topped"),
    ("make.fun", " \u2014 you got paid"),
]
card_w = 980
card_h = 150
gap = 28
radius = 18
total = len(cards) * card_h + (len(cards) - 1) * gap
start_y = 330 + (H - 330 - 380 - total) // 2

for i, (bold_part, rest) in enumerate(cards):
    y = start_y + i * (card_h + gap)
    x0 = (W - card_w) / 2
    x1 = x0 + card_w
    d.rounded_rectangle([x0, y, x1, y + card_h], radius=radius, fill=CARD_FILL, outline=CARD_OUTLINE, width=3)

    cy = y + card_h / 2
    draw_bell(x0 + 70, cy, 36)

    # text: bold "make.fun" then regular rest
    tx = x0 + 130
    bbox = d.textbbox((0, 0), bold_part, font=f_card_b)
    d.text((tx, cy - (bbox[3] - bbox[1]) / 2 - bbox[1]), bold_part, font=f_card_b, fill=CARD_TEXT)
    bbox2 = d.textbbox((0, 0), rest, font=f_card)
    d.text((tx + (bbox[2] - bbox[0]), cy - (bbox2[3] - bbox2[1]) / 2 - bbox2[1]), rest, font=f_card, fill=CARD_TEXT)

# Bottom
center("we are not the same.", f_bottom, H - 190, TITLE)

img.save("meme.png")

with Image.open("meme.png") as im:
    size = im.size
import os
b = os.path.getsize("meme.png")
print("size:", size)
print("bytes:", b)
assert size == (1200, 1200), "bad size"
assert b < 4_000_000, "too big"
