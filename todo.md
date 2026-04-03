Test

ty important iany raha anao jeu tsika pululu

INITIALISATION
↓
BOUCLE DE JEU (game loop)
   ├── INPUT (clavier / souris)
   ├── LOGIQUE (mise à jour) -> mampiasa fonction -> nouvelle fonctionnalite (calcul logique)
   └── RENDU (affichage)
   └── Mise a jour du visuel 
↓
FIN

Ireto ndray ny module essentiel afaka ampiasaintsika 

pygame.init() 
-> soit disant intialisation mais je ne sais pas encore comment 

pygame.display
-> fenetrage principale (affichage)

pygame.event
-> gestion des evenement angamba a ce qu'il parait 
-> element : clavier , souris , fermeture fenetrage

pygame.time
-> fluidite / vitesse an'ilay jeu lesy a 

pygame.draw
-> toutes les formes a dessiner bien sur mon pululu 

pygame.image
-> changer les sprites (a rechercher)

pygame.mixer
-> ca mon gars c'est pour les sons mais c'est optionnel pour l'instant 

A PRECISER OE TY EXEMPLE DE CHATGPT 

🧠 Exemple mental (traduction réelle)
Tant que le jeu tourne :
   lire clavier
   déplacer joueur
   effacer écran
   dessiner joueur
   afficher

   Les erreurs de débutant

⚠️ À éviter absolument :

❌ oublier la boucle principale
❌ ne pas gérer les événements
❌ ne pas rafraîchir l’écran
❌ mélanger logique et affichage

Points importants

get_pos() : retourne un tuple (x, y) avec les coordonnées

get_pressed() : retourne un tuple de 3 booléens (gauche, milieu, droite)

Utilisez collidepoint() pour vérifier si un point est dans un rectangle

Attention : get_pressed() donne l'état EN CE MOMENT, pas les événements de clic

Pour détecter un clic unique, préférez utiliser pygame.MOUSEBUTTONDOWN dans la boucle d'événements


Pour une classe creer , on doit avoir un constructeur __init__() pour initialiser les attributs de l'objet
puis mettre self devant les attributs pour dire que ce sont des attributs propre a chaque objet de la classe
