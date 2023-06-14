# Projet 4

Ce projet est une application Python conçue dans le cadre du parcours python d' OpenClassrooms. C'est une application qui permet de gérer des tournois d'échec.

## Installation

1. Clonez ce dépôt GitHub sur votre machine locale :

```shell
git clone https://github.com/AymericSandoz/OpenClassrooms-P4.git
```

2. Installez les dépendances du projet :

```shell
pip install -r requirements.txt
```

## Utilisation

1. Assurez-vous d'être dans le répertoire racine du projet.

2. Exécutez l'application avec la commande suivante :

```shell
python main.py
```

### Rapport flake 8

Il est possible de générer un rapport flake8 en utilisant la comande suivante :

```shell
flake8 --format=html --htmldir=flake-report main.py utils.py models/game.py models/player.py models/tournament.py models/round.py views/menu_view.py views/players_view.py views/games_view.py views/tournaments_view.py controllers/menu_controller.py controllers/player_controller.py controllers/tournament_controller.py
```
