# Archive — Ariane complète (avant le recentrage)

Cette branche garde **la version d'Ariane d'avant le recentrage sur les créateurs
qui vendent sur les marchés** (novembre 2026). Elle sert de réserve : rien ici
n'est en ligne, la branche `main` reste la version officielle.

Version archivée : commit `79ab838` (dernier commit avant le recentrage).

## Ce qui a été retiré de `main` et où le retrouver

### 1. Les 7 pages cachées du menu

| Page | `data-page` | Ce qu'elle fait |
|---|---|---|
| Commandes | `commandes` | Suivi des commandes clients (statuts, livraison) |
| Stats produits | `produits-stats` | Statistiques par produit |
| Factures | `factures` | Création de factures, PDF, relances des impayées |
| Clients | `clients` | Fiches clients et historique d'achats |
| Calendrier | `calendrier` | Tâches, échéances fiscales, rappels |
| Paiements | `paiements-v5` | Connexion Stripe / PayPal pour encaisser en ligne |
| Site web | `site-builder` | Créateur de mini-site avec bouton « acheter » |

**Bonne nouvelle : leur code est toujours dans `main`.** Les pages sont seulement
cachées, pas supprimées. Pour en réactiver une sur `main` :

1. Ouvre `index.html`, cherche le bloc `Recentrage « créateurs sur les marchés »`
   (vers la fin du fichier).
2. Supprime la ligne de la page dans la liste `REDIRECT`
   (par exemple `'factures': 'dashboard',`).
3. Pour le calendrier, supprime aussi dans le bloc `ariane-design-v6` la règle
   `.hero-full-right > .hero-side-item:nth-child(4){display:none !important;}`
   (elle cache la carte « Prochain calendrier » du tableau de bord).

Le menu, la barre mobile et le tableau de bord d'avant sont visibles ici, dans
`index.html` de cette branche.

### 2. L'ancien design (bleu nuit + bleu électrique)

Sur `main`, le nouveau design est un seul bloc `<style id="ariane-design-v6">` à
la fin de `index.html`. **Le supprimer suffit à retrouver l'ancien look** de
l'app (sauf la police : DM Sans / DM Mono ici, Geist sur `main`).

L'ancienne page d'accueil complète est dans `site/index.html` de cette branche.

### 3. L'ancienne page d'accueil (`site/index.html`)

Elle présentait Ariane comme « la compta de ta petite activité » avec factures,
calendrier et mini-site.

⚠️ **Elle contient de faux avis clients** (Léa, Malik, Théo…). Ne les remets
jamais en ligne : en France, publier des avis inventés est une pratique
commerciale trompeuse, interdite par la loi. Remplace-les par de vrais retours
de testeurs.

## Récupérer un fichier de cette archive

Depuis le dossier `ariane-app`, sans changer de branche :

```bash
git fetch origin
git show origin/archive/ariane-complete:site/index.html > ancienne-vitrine.html
```

Ou pour voir toute l'archive dans un dossier à part :

```bash
git worktree add ../ariane-archive archive/ariane-complete
```

Ou directement sur GitHub : choisis la branche `archive/ariane-complete` dans le
menu déroulant des branches.
