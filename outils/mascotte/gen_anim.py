"""Génère les SVG animés de Berthier à partir de la grille de berthier_sprite.py.
Usage : python gen_anim.py <dossier_sortie>
Fichiers produits :
  berthier-anime.svg     : au repos (respire, cligne des yeux, écran de calculatrice qui clignote)
  berthier-parle.svg     : en train de parler (la bouche s'ouvre et se ferme)
  berthier-tete.svg      : tête + épaules, au repos (pour le bouton de l'assistant)
  berthier-tete-fixe.svg : tête + épaules, sans animation (à côté de chaque message)
"""
import os, sys, runpy, io, contextlib

here = os.path.dirname(os.path.abspath(__file__))
out_dir = sys.argv[1]
tmp = os.path.join(here, '_static.svg')
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(os.path.join(here, 'berthier_sprite.py'), run_name='__main__') if False else None
# berthier_sprite.py écrit le SVG et imprime la grille : on récupère ses variables en l'exécutant.
sys.argv_backup = sys.argv
sys.argv = ['berthier_sprite.py', tmp]
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(os.path.join(here, 'berthier_sprite.py'))
sys.argv = sys.argv_backup
g, P, W, H = ns['g'], ns['PALETTE'], ns['W'], ns['H']

HEAD_ROWS = range(0, 13)   # tête + cou : elle « respire » (descend d'un pixel)

def rects(rows, cols=range(W), grid=None):
    grid = grid or g
    out = []
    for y in rows:
        x = 0
        cs = list(cols)
        while x < W:
            c = grid[y][x]
            if c == '.' or x not in cs:
                x += 1
                continue
            x0 = x
            while x < W and grid[y][x] == c and x in cs:
                x += 1
            out.append(f'<rect x="{x0}" y="{y}" width="{x - x0}" height="1" fill="{P[c]}"/>')
    return '\n'.join(out)

STYLE = """<style>
.head{animation:breathe 2.4s infinite}
.blink{opacity:0;animation:blink 4.2s infinite}
.screen{animation:screen 1.2s infinite}
.mouth{opacity:0;animation:talk .3s infinite}
@keyframes breathe{0%,54%{transform:translateY(0)}55%,100%{transform:translateY(1px)}}
@keyframes blink{0%,93%{opacity:0}94%,98%{opacity:1}99%,100%{opacity:0}}
@keyframes screen{0%,60%{opacity:1}61%,100%{opacity:.55}}
@keyframes talk{0%,49%{opacity:0}50%,100%{opacity:1}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>"""

eye_lids = f'<g class="blink"><rect x="9" y="7" width="1" height="1" fill="{P["g"]}"/><rect x="14" y="7" width="1" height="1" fill="{P["g"]}"/>' \
           f'<rect x="8" y="7" width="2" height="1" fill="{P["s"]}" opacity=".0"/></g>'
# paupières : on remplace les yeux par une petite ligne couleur peau ombrée
eye_lids = f'<g class="blink"><rect x="8" y="7" width="3" height="1" fill="{P["s"]}"/><rect x="13" y="7" width="3" height="1" fill="{P["s"]}"/></g>'
mouth_open = '<g class="mouth"><rect x="10" y="10" width="4" height="1" fill="#5a2a24"/><rect x="11" y="11" width="2" height="1" fill="#5a2a24"/></g>'
screen = f'<rect class="screen" x="15" y="19" width="4" height="1" fill="{P["D"]}"/>'

def svg(view, parts, size):
    vx, vy, vw, vh = view
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vx} {vy} {vw} {vh}" width="{vw*size}" height="{vh*size}" '
            f'shape-rendering="crispEdges"><title>Berthier</title>' + '\n'.join(parts) + '</svg>')

body = rects(range(13, H))
head = rects(HEAD_ROWS)
full_view = (0, 0, W, H)
bust_view = (3, 0, 18, 18)   # tête + épaules, carré

files = {
    'berthier-anime.svg': svg(full_view, [STYLE, body, screen, f'<g class="head">{head}{eye_lids}</g>'], 10),
    'berthier-parle.svg': svg(full_view, [STYLE, body, screen, f'<g class="head">{head}{eye_lids}{mouth_open}</g>'], 10),
    'berthier-tete.svg': svg(bust_view, [STYLE, rects(range(13, 18)), f'<g class="head">{head}{eye_lids}</g>'], 10),
    'berthier-tete-fixe.svg': svg(bust_view, [rects(range(13, 18)), head], 10),
}
for name, content in files.items():
    open(os.path.join(out_dir, name), 'w', encoding='utf-8').write(content)
    print('écrit', name)
os.remove(tmp)
