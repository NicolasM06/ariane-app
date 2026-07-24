@echo off
title Ariane V5 Paiements
cd /d "%~dp0"

if not exist index.html (
  echo ERREUR : index.html est introuvable dans ce dossier.
  echo Clique d'abord sur "Extraire tout", puis relance ce fichier depuis le dossier extrait.
  pause
  exit /b 1
)

echo Lancement d'Ariane sur http://localhost:8093/index.html?v=507
where py >nul 2>nul
if %errorlevel%==0 (
  start http://localhost:8093/index.html?v=507
  py -m http.server 8093
) else (
  start http://localhost:8093/index.html?v=507
  python -m http.server 8093
)
pause
