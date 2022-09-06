# IHM_Projet
Documentation technique de l'interface Homme-Machine communicante avec la google coral dev board

Application : 

L'objectif de cette IHM est de recevoir les informations provenants de la carte embarquée google coral dev board. Les données arrivent traitées.

L'écran contient un carrousel permettant la reception des images analysées par le programme sur la coral. Il y a également un tableau permettant de récapituler le nombre de détections selon le lieu et la date / l'heure.

Un graphique vient conclure la page, on voit afficher le nombre de détections selon le type d'objet.

L'application est dévéloppée en python (framework flask) pour la partie Back et en HTML/CSS pour la partie Front.

Heroku : 

Heroku est une plateforme permettant l'hebergement, le deploiement et la maintenance de notre IHM, merci de suivre les instructions dans la documention python d'Heroku afin de set-up votre environnement de travail : https://devcenter.heroku.com/categories/python-support

Procédure de modification de l'IHM :

Pour un nouvel arrivant sur le projet, merci de cloner le dossier contenant les différents programmes permettant de maintenir l'IHM. Ensuite merci de lier votre IDE avec Git hub afin de pouvoir push vos modifications et ensuite attendre qu'un merge soit effectué. L'ensemble des modifications autorisées seront directement deployées en environnement de developpement. 

En cas de déploiement en environnement de test (staging), merci de bien vouloir utiliser l'app web Heroku.



