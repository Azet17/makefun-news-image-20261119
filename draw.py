#!/usr/bin/env python3
"""Render the 19 November 2026 world-news front page (1024x1024 PNG).

Drawn fresh with Pillow: masthead + six story panels, geometric
pictograms only, no photos, no copied artwork.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 232)
INK = (20, 20, 20)
PANEL = (255, 253, 246)
RED = (176, 42, 32)
NAVY = (31, 58, 95)
TEAL = (14, 110, 105)
GOLD = (176, 124, 20)
PURPLE = (94, 58, 138)
SLATE = (70, 80, 95)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def center(draw, cx, y, text, fnt, fill=INK):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text,
              font=fnt, fill=fill)


# ---------------------------------------------------------------- pictograms
def pic_skyline(d, x, y, s):
    """Neon city skyline with sun (GTA VI / Vice City)."""
    d.rectangle([x, y, x + s, y + s], fill=(24, 24, 46))
    d.ellipse([x + s * 0.58, y + s * 0.10, x + s * 0.90, y + s * 0.42],
              fill=(255, 120, 90))
    for bx, bw, bh in ((0.04, 0.20, 0.55), (0.28, 0.16, 0.75),
                       (0.48, 0.22, 0.62), (0.74, 0.18, 0.85)):
        d.rectangle([x + s * bx, y + s * (1 - bh), x + s * (bx + bw),
                     y + s * 0.96], fill=(52, 52, 86))
    for i in range(5):
        d.rectangle([x + s * (0.08 + i * 0.18), y + s * 0.55,
                     x + s * (0.11 + i * 0.18), y + s * 0.60],
                    fill=(255, 214, 90))
    d.rectangle([x, y + s * 0.96, x + s, y + s], fill=(255, 120, 90))


def pic_capitol(d, x, y, s):
    """US Capitol dome and columns."""
    d.ellipse([x + s * 0.32, y + s * 0.06, x + s * 0.68, y + s * 0.42],
              fill=NAVY)
    d.rectangle([x + s * 0.48, y, x + s * 0.52, y + s * 0.08], fill=NAVY)
    d.rectangle([x + s * 0.28, y + s * 0.40, x + s * 0.72, y + s * 0.48],
                fill=NAVY)
    for i in range(5):
        cx = x + s * (0.14 + i * 0.18)
        d.rectangle([cx, y + s * 0.52, cx + s * 0.07, y + s * 0.86],
                    fill=NAVY)
    d.rectangle([x + s * 0.08, y + s * 0.86, x + s * 0.92, y + s * 0.94],
                fill=RED)
    d.rectangle([x + s * 0.04, y + s * 0.94, x + s * 0.96, y + s],
                fill=NAVY)


def pic_cyclone(d, x, y, s):
    """Spiral storm with rain."""
    cx, cy = x + s * 0.5, y + s * 0.44
    for r, a0, a1 in ((0.44, 20, 300), (0.33, 200, 120), (0.22, 20, 300),
                      (0.12, 200, 120)):
        d.arc([cx - s * r, cy - s * r, cx + s * r, cy + s * r], a0, a1,
              fill=TEAL, width=7)
    d.ellipse([cx - s * 0.05, cy - s * 0.05, cx + s * 0.05, cy + s * 0.05],
              fill=TEAL)
    for i, dx in enumerate((-0.30, -0.10, 0.12, 0.32)):
        d.polygon([(x + s * (0.5 + dx), y + s * 0.86),
                   (x + s * (0.5 + dx - 0.045), y + s * 0.97),
                   (x + s * (0.5 + dx + 0.045), y + s * 0.97)],
                  fill=(40, 110, 180))


def pic_euro(d, x, y, s):
    """Euro coin and stacked coins."""
    d.ellipse([x + s * 0.08, y + s * 0.06, x + s * 0.72, y + s * 0.70],
              fill=GOLD)
    d.ellipse([x + s * 0.16, y + s * 0.14, x + s * 0.64, y + s * 0.62],
              outline=(120, 84, 10), width=4)
    f = font(SANS_B, int(s * 0.42))
    d.text((x + s * 0.40 - d.textlength("\u20ac", font=f) / 2, y + s * 0.13),
           "\u20ac", font=f, fill=(90, 60, 5))
    for i, w in enumerate((0.30, 0.24, 0.18)):
        d.rectangle([x + s * (0.62 - w / 2), y + s * (0.78 + i * 0.075),
                     x + s * (0.62 + w / 2), y + s * (0.84 + i * 0.075)],
                    fill=NAVY)


def pic_voyager(d, x, y, s):
    """Deep-space probe with dish and stars."""
    for sx, sy in ((0.10, 0.10), (0.88, 0.16), (0.16, 0.78), (0.92, 0.72)):
        d.ellipse([x + s * sx - 3, y + s * sy - 3, x + s * sx + 3,
                   y + s * sy + 3], fill=GOLD)
    d.ellipse([x + s * 0.05, y + s * 0.05, x + s * 0.95, y + s * 0.95],
              outline=SLATE, width=3)
    d.polygon([(x + s * 0.36, y + s * 0.36), (x + s * 0.76, y + s * 0.26),
               (x + s * 0.70, y + s * 0.48), (x + s * 0.30, y + s * 0.58)],
              fill=NAVY)
    d.ellipse([x + s * 0.06, y + s * 0.56, x + s * 0.32, y + s * 0.82],
              outline=RED, width=6)
    d.line([x + s * 0.32, y + s * 0.64, x + s * 0.48, y + s * 0.48],
           fill=RED, width=5)
    d.line([x + s * 0.72, y + s * 0.30, x + s * 0.88, y + s * 0.16],
           fill=NAVY, width=5)


def pic_globe(d, x, y, s):
    """Globe with a lightning bolt (conflict in the Gulf)."""
    cx, cy = x + s * 0.5, y + s * 0.5
    d.ellipse([x + s * 0.06, y + s * 0.06, x + s * 0.94, y + s * 0.94],
              fill=(36, 90, 140))
    d.ellipse([x + s * 0.30, y + s * 0.06, x + s * 0.70, y + s * 0.94],
              outline=(180, 220, 240), width=4)
    d.line([x + s * 0.06, y + s * 0.50, x + s * 0.94, y + s * 0.50],
           fill=(180, 220, 240), width=4)
    d.arc([x + s * 0.06, y + s * 0.24, x + s * 0.94, y + s * 0.76],
          200, 340, fill=(180, 220, 240), width=4)
    d.polygon([(x + s * 0.56, y + s * 0.14), (x + s * 0.34, y + s * 0.58),
               (x + s * 0.50, y + s * 0.58), (x + s * 0.40, y + s * 0.88),
               (x + s * 0.66, y + s * 0.44), (x + s * 0.50, y + s * 0.44)],
              fill=(255, 214, 90))


STORIES = [
    ("CULTURE \u00b7 GAMING", RED, pic_skyline,
     "VICE CITY OPENS ITS DOORS",
     "After 13 years, Grand Theft Auto VI unlocks at midnight around "
     "the world, starting in New Zealand."),
    ("POLITICS \u00b7 USA", NAVY, pic_capitol,
     "JEFFRIES NOMINATED FOR SPEAKER",
     "House Democrats pick Hakeem Jeffries 251\u201311, putting him on "
     "course to be the first Black Speaker."),
    ("WEATHER \u00b7 INDIA", TEAL, pic_cyclone,
     "CYCLONE AKVAN BEARS DOWN ON INDIA",
     "A severe storm in the Bay of Bengal nears the Andhra\u2013Odisha "
     "coast; red alerts issued, schools shut."),
    ("EUROPE \u00b7 UKRAINE", GOLD, pic_euro,
     "EU PLANS \u20ac45BN LOAN FOR UKRAINE",
     "Brussels proposes a \u20ac45 billion loan to fund Kyiv next year, "
     "to be repaid once Russia pays reparations."),
    ("SCIENCE \u00b7 SPACE", PURPLE, pic_voyager,
     "VOYAGER 1, ONE LIGHT-DAY AWAY",
     "NASA's 1977 probe reaches one light-day from Earth \u2014 about "
     "26 billion km \u2014 after 49 years in space."),
    ("CONFLICT \u00b7 THE GULF", SLATE, pic_globe,
     "US AND IRAN TRADE FIRE IN THE GULF",
     "US strikes a missile site on Qeshm Island; Iran hits US bases "
     "in Bahrain and Kuwait."),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 4], fill=INK)
    f_title = font(SERIF_B, 78)
    center(d, W // 2, 26, "THE WORLD TODAY", f_title)
    d.line([28, 122, W - 28, 122], fill=INK, width=3)
    d.line([28, 128, W - 28, 128], fill=INK, width=1)
    f_date = font(SANS_B, 37)
    center(d, W // 2, 134, "THURSDAY 19 NOVEMBER 2026", f_date, fill=RED)
    f_sub = font(SANS, 17)
    center(d, W // 2, 184, "SIX STORIES FROM AROUND THE GLOBE",
           f_sub)

    # ---- story grid: 2 cols x 3 rows ----
    gx, gy = 24, 216
    pw, ph, gut = 480, 238, 16
    f_tag = font(SANS_B, 16)
    f_head = font(SANS_B, 27)
    f_sum = font(SANS, 19)

    for i, (tag, colour, pic, head, summ) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = gx + col * (pw + gut)
        y = gy + row * (ph + gut)
        d.rectangle([x, y, x + pw, y + ph], fill=PANEL, outline=INK, width=2)
        # tag strip
        d.rectangle([x + 2, y + 2, x + pw - 2, y + 30], fill=colour)
        d.text((x + 12, y + 7), tag, font=f_tag, fill=(255, 255, 255))
        # pictogram
        pic(d, x + 14, y + 44, 108)
        # headline, right of pictogram
        hx, hw = x + 136, pw - 150
        lines = wrap(d, head, f_head, hw)[:3]
        ly = y + 42
        for ln in lines:
            d.text((hx, ly), ln, font=f_head, fill=INK)
            ly += 31
        # summary, full width below
        sy = y + 162
        for ln in wrap(d, summ, f_sum, pw - 28)[:3]:
            d.text((x + 14, sy), ln, font=f_sum, fill=(40, 40, 40))
            sy += 24

    # ---- footer ----
    d.line([28, 978, W - 28, 978], fill=INK, width=2)
    f_foot = font(SANS, 15)
    center(d, W // 2, 990,
           "Sources: Reuters \u00b7 AP \u00b7 NPR \u00b7 India Meteorological "
           "Department \u00b7 Financial Times \u00b7 NASA",
           f_foot, fill=(60, 60, 60))

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
