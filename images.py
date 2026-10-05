# Génère les images de la signature perso à partir du visuel Canva et de la photo de profil
from PIL import Image, ImageDraw, ImageFilter, ImageChops

TELECHARGEMENTS = "/Users/thomasriviere/Downloads/"
BLEU = (72, 82, 196, 255)
BLEU_FONCE = (43, 51, 153, 255)

# --- Photo : noir et blanc, contour blanc façon sticker, dans un cercle bleu ---
ph = Image.open(TELECHARGEMENTS + "Photo de Profil.png").convert("RGBA")
W, H = ph.size
work = ph.convert("RGB")
for seed in [(0, 0), (W - 1, 0), (0, H - 1), (W - 1, H - 1), (W // 2, 2), (2, H // 2), (W - 3, H // 2)]:
    ImageDraw.floodfill(work, seed, (255, 0, 255), thresh=40)
masque = ImageChops.difference(work, Image.new("RGB", (W, H), (255, 0, 255))).convert("L").point(lambda p: 255 if p > 10 else 0)
masque = masque.filter(ImageFilter.MedianFilter(5))
gris = ph.convert("L").convert("RGBA")
gris.putalpha(masque)

S = 480
fond = Image.new("RGBA", (S, S), (0, 0, 0, 0))
# cercle en dégradé bleu
degrade = Image.new("RGBA", (S, S))
d = ImageDraw.Draw(degrade)
for y in range(S):
    t = y / S
    d.line([(0, y), (S, y)], fill=tuple(round(BLEU[i] + (BLEU_FONCE[i] - BLEU[i]) * t) for i in range(3)) + (255,))
cercle = Image.new("L", (S, S), 0)
ImageDraw.Draw(cercle).ellipse((0, 0, S - 1, S - 1), fill=255)
fond.paste(degrade, (0, 0), cercle)

taille = int(S * 1.0)
perso = gris.resize((taille, taille), Image.LANCZOS)
a = perso.split()[3]
contour = Image.new("RGBA", perso.size, (255, 255, 255, 0))
contour.putalpha(a.filter(ImageFilter.MaxFilter(15)))
calque = Image.new("RGBA", (S, S), (0, 0, 0, 0))
pos = ((S - taille) // 2, S - taille + 10)
calque.alpha_composite(contour, pos)
calque.alpha_composite(perso, pos)
# on garde la personne dans le cercle (le bas est coupé par le cercle)
calque.putalpha(ImageChops.multiply(calque.split()[3], cercle))
fond.alpha_composite(calque)
fond.resize((240, 240), Image.LANCZOS).save("images/photo.png")

# --- Icônes et réseaux, découpés dans le visuel Canva ---
src = Image.open(TELECHARGEMENTS + "SIGNATURE DE MAIL_RIVIERE THOMAS.png").convert("RGB")

def icone_blanche(boite, nom):
    # glyphe blanc sur fond transparent : l'opacité vient de la clarté du pixel
    im = src.crop(boite).convert("L")
    bas = min(im.getdata())
    alpha = im.point(lambda p: max(0, min(255, (p - bas) * 255 // max(1, 255 - bas))))
    sortie = Image.new("RGBA", im.size, (255, 255, 255, 0))
    sortie.putalpha(alpha)
    b = alpha.point(lambda p: 255 if p > 40 else 0).getbbox()
    sortie = sortie.crop(b)
    c = max(sortie.size) + 2
    carre = Image.new("RGBA", (c, c), (255, 255, 255, 0))
    carre.alpha_composite(sortie, ((c - sortie.width) // 2, (c - sortie.height) // 2))
    carre.resize((32, 32), Image.LANCZOS).save(f"images/icone-{nom}.png")

for nom, boite in {"tel": (684, 226, 716, 254), "mail": (684, 266, 716, 294), "web": (684, 306, 716, 338), "lieu": (684, 346, 716, 378)}.items():
    icone_blanche(boite, nom)

def reseau(boite, nom):
    # icône carrée aux coins arrondis, coins transparents
    im = src.crop(boite).convert("RGBA").resize((96, 96), Image.LANCZOS)
    m = Image.new("L", (96, 96), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, 95, 95), radius=20, fill=255)
    im.putalpha(m)
    im.resize((48, 48), Image.LANCZOS).save(f"images/{nom}.png")

for nom, x in {"instagram": 1306, "linkedin": 1414, "tiktok": 1470}.items():
    reseau((x, 399, x + 46, 445), nom)
