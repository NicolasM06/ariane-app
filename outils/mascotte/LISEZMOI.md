# Mascotte Berthier (pixel art)

- `berthier_sprite.py` : le dessin de Berthier, pixel par pixel (grille 24 × 32) et ses couleurs.
- `gen_anim.py` : fabrique les versions animées à partir du dessin.

Pour modifier Berthier (couleur du gilet, lunettes…), change `berthier_sprite.py`, puis depuis ce dossier :

```bash
python gen_anim.py ../../icons
```

Fichiers produits dans `icons/` :
- `berthier-anime.svg` : au repos (respire, cligne des yeux)
- `berthier-parle.svg` : quand l'assistant répond
- `berthier-tete.svg` : tête animée (bouton de l'assistant)
- `berthier-tete-fixe.svg` : tête fixe (à côté des messages)
