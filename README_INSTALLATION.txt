ARIANE V5 — PAIEMENT RÉEL TYPE SHOPIFY/SUMUP

Cette version ajoute une vraie structure paiement :
- onglet Paiements
- URL backend cachant Stripe
- bouton Connecter paiement
- test backend
- bouton acheter dans le créateur de site
- export HTML avec bouton qui crée une session de paiement via backend
- backend Node.js / Express / Stripe inclus dans le dossier backend-paiements

Important :
Shopify/SumUp n'ont pas “pas d'API”.
Ils cachent l'API côté serveur.
Cette V5 fait la même logique : l'utilisateur ne voit pas l'API dans le bouton, mais le backend s'en occupe.

Lancement frontend :
http://localhost:8093/index.html?v=507

Lancement backend :
1. Ouvre backend-paiements/.env
2. Mets STRIPE_SECRET_KEY=sk_test_...
3. Lance backend-paiements/lancer-backend-windows.bat
4. Dans Ariane > Paiements, mets http://localhost:4242
5. Clique Tester backend

Fichiers importants :
- index.html : application Ariane
- backend-paiements/server.js : backend paiement
- backend-paiements/.env.example : configuration
- backend-paiements/README_BACKEND.md : explication backend
