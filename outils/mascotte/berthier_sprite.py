"""Génère le personnage pixel art « Berthier » en SVG (24 × 32 pixels).
Usage : python berthier_sprite.py <sortie.svg>
"""
import sys

W, H = 24, 32
g = [['.'] * W for _ in range(H)]

def rect(x0, y0, x1, y1, c):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            g[y][x] = c

def px(x, y, c):
    g[y][x] = c

# ── Tête ──
rect(6, 1, 17, 11, 'S')                 # visage
rect(7, 1, 16, 1, 'S')
px(5, 6, 'S'); px(5, 7, 's'); px(18, 6, 'S'); px(18, 7, 's')   # oreilles
# cheveux noirs, raie sur le côté, front qui se dégarnit, tempes grises (la cinquantaine)
rect(7, 0, 16, 1, 'H'); rect(6, 1, 6, 1, '.'); rect(17, 1, 17, 1, '.')
rect(6, 2, 9, 2, 'H'); rect(13, 2, 17, 2, 'H')                  # front dégarni au milieu
rect(11, 0, 14, 0, 'h'); px(14, 1, 'h'); px(8, 1, 'h')           # reflets
px(9, 0, 'r'); px(15, 2, 'r'); px(7, 2, 'r')                    # quelques cheveux gris
rect(6, 3, 7, 3, 'H'); rect(16, 3, 17, 3, 'H'); px(8, 3, 'H')
rect(6, 4, 6, 4, 'H'); rect(17, 4, 17, 4, 'H')
rect(6, 5, 6, 6, 'r'); rect(17, 5, 17, 6, 'r')                  # tempes grises
px(11, 2, 's')                                                   # ride sur le front
# lunettes
rect(7, 6, 10, 6, 'G'); rect(13, 6, 16, 6, 'G')                 # monture épaisse en haut (lunettes « browline »)
rect(11, 6, 12, 6, 'G')                                         # pont
rect(7, 7, 10, 7, 'g'); rect(13, 7, 16, 7, 'g')                 # verres clairs
px(9, 7, 'E'); px(14, 7, 'E')                                   # yeux
rect(8, 8, 9, 8, 'n'); rect(14, 8, 15, 8, 'n')                  # cernes
px(6, 6, 'G'); px(17, 6, 'G')                                   # branches
# sourcils
rect(8, 4, 9, 4, 'H'); rect(14, 4, 15, 4, 'H')
# nez, moustache, bouche
px(11, 8, 's'); px(12, 8, 's')
rect(9, 9, 14, 9, 'M'); px(8, 10, 'M'); px(15, 10, 'M'); px(7, 9, 's'); px(16, 9, 's')  # moustache + rides des joues
rect(10, 10, 13, 10, 'm')
rect(7, 11, 16, 11, 's')                                        # ombre du menton
# cou
rect(10, 12, 13, 12, 's')

# ── Corps ──
rect(5, 13, 18, 24, 'V')                                        # gilet
rect(5, 13, 5, 13, '.'); rect(18, 13, 18, 13, '.')
for y, (a, b) in zip(range(13, 19), [(8, 15), (9, 14), (9, 14), (10, 13), (10, 13), (11, 12)]):
    rect(a, y, b, y, 'W')                                       # chemise (col en V)
rect(8, 13, 8, 13, 'w'); rect(15, 13, 15, 13, 'w')              # col
rect(11, 13, 12, 13, 't')                                       # nœud de cravate
rect(11, 14, 12, 19, 'T'); px(11, 20, 'T'); px(12, 20, 't')     # cravate
px(9, 20, 'v'); px(9, 22, 'v')                                  # boutons du gilet
rect(5, 14, 5, 24, 'v'); rect(18, 14, 18, 24, 'v')              # ombre des côtés
# bras
rect(3, 14, 4, 22, 'V'); rect(19, 14, 20, 19, 'V')
rect(3, 23, 4, 23, 'S')                                         # main gauche
# calculatrice tenue contre le corps (main droite)
rect(14, 18, 19, 24, 'C')
rect(15, 19, 18, 19, 'D')                                       # écran
for y in (21, 23):
    for x in (15, 17):
        px(x, y, 'c')
px(19, 21, 'S'); px(20, 20, 'S'); px(20, 21, 'S')               # main droite

# ── Jambes ──
rect(6, 25, 17, 28, 'P')
rect(11, 27, 12, 28, '.')
rect(6, 29, 10, 29, 'P'); rect(13, 29, 17, 29, 'P')
rect(5, 30, 10, 30, 'B'); rect(13, 30, 18, 30, 'B')

# ── Contour automatique ──
filled = [[c != '.' for c in row] for row in g]
for y in range(H):
    for x in range(W):
        if g[y][x] == '.':
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < W and 0 <= ny < H and filled[ny][nx]:
                    g[y][x] = 'K'
                    break

PALETTE = {
    'K': '#16171a',  # contour
    'S': '#f1c7a3', 's': '#d9a37f',          # peau
    'H': '#2f2b2c', 'h': '#554f51', 'r': '#9a9da3',  # cheveux noirs, reflet, tempes grises
    'G': '#2a1d14', 'g': '#e6eefc', 'E': '#16171a', 'f': '#a9b0bb',  # lunettes, verres, yeux, monture fine
    'M': '#2b2829', 'm': '#b9786a', 'n': '#b88378',  # moustache, bouche, cernes
    'W': '#f2f3f5', 'w': '#c9ced8',          # chemise
    'T': '#4f8cff', 't': '#2f63c9',          # cravate (bleu de l'app)
    'V': '#c29a45', 'v': '#9a7632',          # gilet moutarde
    'P': '#4a4e59', 'B': '#2b1e15',          # pantalon gris, chaussures marron
    'C': '#c9ccd3', 'c': '#6b7079', 'D': '#3ecf8e',  # calculatrice
}

out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W*10}" height="{H*10}" shape-rendering="crispEdges">',
       '<title>Berthier</title>']
for y in range(H):
    x = 0
    while x < W:
        c = g[y][x]
        if c == '.':
            x += 1
            continue
        x0 = x
        while x < W and g[y][x] == c:
            x += 1
        out.append(f'<rect x="{x0}" y="{y}" width="{x - x0}" height="1" fill="{PALETTE[c]}"/>')
out.append('</svg>')
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out))
print('\n'.join(''.join(r) for r in g))
