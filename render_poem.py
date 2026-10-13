#!/usr/bin/env python3
"""Render poem.txt as a clean claim image (PNG) for poidh bounty #1463."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

HERE = Path(__file__).parent
poem = (HERE / "poem.txt").read_text().strip()
stanzas = poem.split("\n\n")
assert len(stanzas) == 10, len(stanzas)

W, H = 1700, 2400
BG = (250, 246, 238); INK = (29, 39, 51); ACCENT = (176, 116, 42); MUTED = (110, 104, 92)
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

title_f = ImageFont.truetype(SANS_B, 66)
sub_f = ImageFont.truetype(SANS, 31)
body_f = ImageFont.truetype(SERIF, 40)
foot_f = ImageFont.truetype(SANS, 26)

M = 150
d.text((M, 105), "October Poem for poidh", font=title_f, fill=INK)
d.text((M, 200), "Ten stanzas for the tenth month — proof, bounties, and pics or it didn't happen.", font=sub_f, fill=MUTED)
d.line([(M, 285), (W - M, 285)], fill=ACCENT, width=4)

y = 330
LH = 54; GAP = 30
for s in stanzas:
    for line in s.splitlines():
        d.text((M, y), line, font=body_f, fill=INK)
        y += LH
    y += GAP

d.line([(M, H - 130), (W - M, H - 130)], fill=ACCENT, width=3)
d.text((M, H - 100), "Original poem for poidh bounty #1463 (Base) · Full text also in the claim and repo.", font=foot_f, fill=MUTED)
img.save(HERE / "poem.png")
print("saved", HERE / "poem.png", img.size)
