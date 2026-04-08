Test

<h1>Points importants iany raha anao jeu tsika pululu</h1>

INITIALISATION
↓
BOUCLE DE JEU (game loop)
   -> INPUT (clavier / souris)
   -> LOGIQUE (mise à jour) -> mampiasa fonction -> nouvelle fonctionnalite (calcul logique)
   -> RENDU (affichage)
   -> Mise a jour du visuel 
↓
FIN

<h1>Ireto ndray ny module essentiel afaka ampiasaintsika</h1>

    # pygame.init() 
-> soit disant intialisation mais je ne sais pas encore comment 

    # pygame.display
-> fenetrage principale (affichage)

    # pygame.event
-> gestion des evenement angamba a ce qu'il parait 
-> element : clavier , souris , fermeture fenetrage

    # pygame.time
-> fluidite / vitesse an'ilay jeu lesy a 

    # pygame.draw
-> toutes les formes a dessiner bien sur mon pululu 
ca represente un element graphique a dessiner a l'ecran ( personnage , ennemi , objet , etc )
Ca regroupe une image , une position via Rect , en bref ireo comportement ahafahana manamora ny mouvement sy les interactions dans le jeu

    # pygame.image
-> changer les sprites (a rechercher)

    # pygame.mixer
-> ca mon gars c'est pour les sons mais c'est optionnel pour l'instant 

<h1>À PRECISER OE TY EXEMPLE DE CHATGPT </h1>

<h3>🧠 Exemple mental (traduction réelle)</h3>

Tant que le jeu tourne :
   lire clavier
   déplacer joueur
   effacer écran
   dessiner joueur
   afficher

   Les erreurs de débutant

<h3>⚠️ À éviter absolument :</h3>

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

    # Tandremana tsara fa kay le izy mande par ordre d'affichage otrany photoshop na gimp, 
    # le izy affiche d'abord le fond, ensuite le titre, 
    # et enfin le bouton par dessus les deux autres. 
    # Raha ovaina ny ordre dia mety tsy hiseho tsara ilay bouton 
    # na ilay titre satria mety ho afenina amin'ny sary hafa izy ireo.

<h1>Ireto avy ny type de cuseur</h1>

    # pygame.SYSTEM_CURSOR_ARROW : 
-> Curseur par défaut (flèche)

    # pygame.SYSTEM_CURSOR_IBEAM : 
-> Curseur de saisie (barre verticale)

    # pygame.SYSTEM_CURSOR_WAIT : 
-> Curseur d'attente (sablier)

    # pygame.SYSTEM_CURSOR_CROSSHAIR : 
-> Curseur de précision (croix)

    # pygame.SYSTEM_CURSOR_WAITARROW : 
-> Curseur d'attente avec flèche

    # pygame.SYSTEM_CURSOR_SIZENWSE : 
-> Curseur de redimensionnement diagonal (haut-gauche à bas-droite)

    # pygame.SYSTEM_CURSOR_SIZENESW : 
-> Curseur de redimensionnement diagonal (haut-droite à bas-gauche)

    # pygame.SYSTEM_CURSOR_SIZEWE : 
-> Curseur de redimensionnement horizontal

    # pygame.SYSTEM_CURSOR_SIZENS : 
-> Curseur de redimensionnement vertical

    # pygame.SYSTEM_CURSOR_SIZEALL : 
-> Curseur de déplacement (quatre flèches)

    # pygame.SYSTEM_CURSOR_NO : 
-> Curseur d'interdiction (cercle barré)

    # pygame.SYSTEM_CURSOR_HAND : 
-> Curseur de main (utilisé pour les liens cliquables)

    # pygame.SYSTEM_CURSOR_APPSTARTING : 
-> Curseur de démarrage d'application (flèche avec cercle)

    # pygame.SYSTEM_CURSOR_HELP : 
-> Curseur d'aide (point d'interrogation)

    # pygame.SYSTEM_CURSOR_ICON : 
-> Curseur d'icône personnalisée (utilisé pour les curseurs personnalisés)

    # pygame.SYSTEM_CURSOR_SIZE : 
-> Curseur de redimensionnement (utilisé pour les curseurs de redimensionnement personnalisés)

Pour pygame.transform.flip(image, flip_x, flip_y) :
- image : l'image à retourner (Surface)
- flip_x : booléen, True pour retourner horizontalement, False pour ne pas retourner
- flip_y : booléen, True pour retourner verticalement, False pour ne pas retourner (pratique si on veut que le personnage marche sur le plafond par exemple)

Mouvement Multi-directionnel :
Pour permettre les diagonales sans bug de vitesse, il faut séparer le traitement de l'axe Horizontal (X) et de l'axe Vertical (Y). Chaque axe doit avoir son propre bloc if/elif. De cette façon, Pygame peut traiter une touche de chaque axe simultanément à chaque rafraîchissement d'image.