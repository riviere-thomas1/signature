# Génère la signature perso : apercu.html (images locales) et signature.html (images hébergées sur GitHub Pages)
BASE_EN_LIGNE = "https://riviere-thomas1.github.io/signature/images/"
POSTE = "Chef de projet Marketing et Communication"

def signature(base):
    img = lambda f: base + f
    bleu, bleu_fonce = "#2B3399", "#1A1F5E"
    police = "Helvetica, Arial, sans-serif"
    contact = lambda icone, texte, lien: f'''<tr>
<td width="24" style="padding:3px 0;vertical-align:middle;"><img src="{img(icone)}" width="16" height="16" alt="" style="display:block;border:0;"></td>
<td style="padding:3px 0;vertical-align:middle;font-family:{police};font-size:13px;line-height:16px;letter-spacing:0.3px;">{f'<a href="{lien}" style="color:#ffffff;text-decoration:none;">{texte}</a>' if lien else f'<span style="color:#ffffff;">{texte}</span>'}</td>
</tr>'''
    reseau = lambda f, nom, lien: f'<td style="padding-left:6px;"><a href="{lien}"><img src="{img(f)}" width="24" height="24" alt="{nom}" style="display:block;border:0;"></a></td>'
    # Fond bleu uni en secours (bgcolor) pour les messageries qui ignorent les dégradés
    return f'''<table cellpadding="0" cellspacing="0" border="0" bgcolor="{bleu}" style="border-collapse:collapse;font-family:{police};color:#ffffff;background-color:{bleu};background-image:linear-gradient(135deg,{bleu} 0%,{bleu_fonce} 100%);border-radius:10px;">
<tr><td style="padding:18px 22px;">
<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
<tr>
<td style="vertical-align:middle;padding-right:22px;"><img src="{img('photo.png')}" width="120" height="120" alt="Thomas Rivière" style="display:block;border:0;"></td>
<td style="vertical-align:middle;">
<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
<tr><td style="font-family:{police};font-size:22px;line-height:26px;font-weight:700;color:#ffffff;">RIVIERE Thomas</td></tr>
<tr><td style="padding:7px 0 10px 0;"><span style="display:inline-block;background-color:#ffffff;color:{bleu};font-family:{police};font-size:12px;line-height:14px;font-weight:700;padding:5px 12px;border-radius:12px;">{POSTE}</span></td></tr>
<tr><td>
<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
{contact('icone-tel.png', '+262 692 25 59 84', 'tel:+262692255984')}
{contact('icone-mail.png', 'thomas.riviere.pro@icloud.com', 'mailto:thomas.riviere.pro@icloud.com')}
{contact('icone-web.png', 'linktr.ee/ixmthomas', 'https://linktr.ee/ixmthomas')}
{contact('icone-lieu.png', 'Saint-André, La Réunion', None)}
</table>
</td></tr>
<tr><td style="padding-top:10px;">
<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;"><tr>
<td style="vertical-align:middle;font-family:{police};font-size:12px;color:#ffffff;padding-right:4px;">Retrouvez-moi sur</td>
{reseau('instagram.png', 'Instagram', 'https://www.instagram.com/ixmthomas/')}
{reseau('linkedin.png', 'LinkedIn', 'https://www.linkedin.com/in/riviere-thomas/')}
{reseau('tiktok.png', 'TikTok', 'https://www.tiktok.com/@ixmthomas')}
</tr></table>
</td></tr>
</table>
</td>
</tr>
</table>
</td></tr>
</table>'''

page = lambda corps: f'<!DOCTYPE html>\n<html><head><meta charset="utf-8"><title>Signature Thomas</title></head><body style="margin:24px;background:#ffffff;">\n{corps}\n</body></html>\n'

open("apercu.html", "w").write(page(signature("images/")))
open("signature.html", "w").write(page(signature(BASE_EN_LIGNE)))
