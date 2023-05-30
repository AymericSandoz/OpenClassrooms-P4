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
