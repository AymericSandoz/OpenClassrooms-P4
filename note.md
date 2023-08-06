#NOTE P4

##Qu’est-ce que le MVC ?
Le MVC est une approche d’architecture de logiciel. Il divise les responsabilités du système en 3 parties distinctes :

Modèle : Le modèle contient les informations relatives à l’état du système. Ce sont les fonctionnalités brutes de l’application.

Vue : La vue présente les informations du modèle à l’utilisateur. Elle sert d’interface visuelle et/ou sonore pour l’utilisateur.

Contrôleur : Le contrôleur garantit que les commandes utilisateurs soient exécutées correctement, modifiant les objets du modèle appropriés, et mettant à jour l’application. C’est finalement les rouages de l’application, et c’est la couche qui apporte une interaction avec l’utilisateur.

##Difficultées et questions
###Semaine du 14 avril
Problème avec les importations relatives

A quoi servent les fichier init.py

Impossible de faire fonctionner un input en utilisant la flèche en haut à gauche Run Code. marche que quand je fais python main.py

Dans views.py à quoi sert self par exemple ? A rien on est d'accord ? A quoi sert Init ? En gros quand utiliser init

ctr Y contraire de crt Z

il faut que je configure flake
Il ne faut pas que qu'il y ai de views dans les models. J'ai pas eu le temps de m'en occuper

19/05
Trois remarques principales :
Je ne met pas correctement à jour mon instance de modèle tournament
Il ne faut pas que qu'il y ai de views dans les models. J'ai pas eu le temps de m'en occuper

26/05
FOnction pour apparier les joeurs pour les rounds > 1, je ne sais pas comment la faire
J'ai enlever toutes le views des models
Est-ce que ma gestion des erreurs dans les inputs(while True, try except est bonne ou pas ?)
Je voudrais qu'on parcours les parcours les views et les modèles ensemble pour me dire ce qui doit être dans les controllers, car ce n'est pas clair pour moi.

30/05
J'ai du mal à vérifier que ma fonction pour apparier les joueurs aux autres roud que le 2 fonctionne bien

Faire un diagramme de flux pour la présentation sur draw.io (diagram.net)

RIch

06/06
1-Comprendre l'erreur qui se produit dans Views ligne 25 pour la fonction go_back_to_menu_or_exit_programme

2- comprendre pourquoi je ne peux pas importer Views dans utils -- problème de circular import ?

3- J'ai commencé la réorganisation des views et controllers : Que mettre en nom de classe et en nom de fichier ?

4- Tuto Git ! PAsser de commit sans avoir peur de tout casser.

15/06
Entrer end date à la fin d'un tournoi automatiuement

Lors de l'enregistrment de joeur à la fédé checker les input ID et

#ligne de commande pour générer le rapport flake 8 :
flake8 --format=html --htmldir=flake-report main.py utils.py models/game.py models/player.py models/tournament.py models/round.py views/menu_view.py views/players_view.py views/games_view.py views/tournaments_view.py controllers/menu_controller.py controllers/player_controller.py controllers/tournament_controller.py

## Pas terminé :

Vérifier la fonction qui génère les matchs :

Vérifier qu'il y'a au moins 8 joeurs dans le tournoi lors d el'inscription de sjoeurs


##### Test codings games

@Property

__str__
__str__ est une méthode spéciale qui définit la représentation sous forme de chaîne de caractères d'un objet.


*args : C'est une syntaxe utilisée pour passer un nombre variable d'arguments non-clé à une fonction. L'étoile (*) avant le paramètre args permet d'indiquer que tous les arguments positionnels supplémentaires doivent être collectés dans un tuple

kwargs

