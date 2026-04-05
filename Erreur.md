- on ne cree pas d'objet dans draw() car ca ralenti juste pour rien 
-> tout creer dans init direct 
-> draw() juste pour afficher 

- utiliser la classe au lieu de l'objet 
-> toujours cibler l'objet avec self.classeConcerne

- screen.width n'existe pas 
-> utiliser screen.get_width pour avoir la width de quelque chose 

creer tout dans init ne pas passer au objet 

On ne peut redimensionner un groupe d'image , il faut faire une boucle en global pour l'emplacement % au sceen ou pour le scale 

1. L'Erreur à éviter (IndexError)
Problème : Si on demande l'image n°6 alors que notre liste n'en contient que 6 (indexées de 0 à 5), le jeu plante immédiatement.
Cause : Calculer l'index avant de vérifier si le compteur a dépassé la taille de la liste. C'est comme essayer de lire une page qui n'existe pas dans un livre.
2. Fonctionnement du mécanisme (Le duo Counter / Index)
Pour ralentir l'animation sans figer le jeu (qui tourne à 60 FPS) :
animation_speed (0.2) : C'est la force avec laquelle on pousse les pages. Plus c'est petit, plus c'est lent.
self.counter : C'est un nombre à virgule qui monte de 0.2 à chaque tour de boucle. Il sert de "réservoir de temps".
self.index = int(self.counter) : C'est le traducteur. La fonction int() gomme la virgule. L'index ne change (0 -> 1 -> 2) que lorsque le counter franchit un nombre entier.
len(self.images) : C'est la barrière de sécurité (la longueur de la liste).
3. Logique de calcul dans draw()
L'ordre des lignes est crucial pour la sécurité du programme :
Incrémentation : counter += speed (Le temps avance).
Sécurité (La Barrière) : if counter >= len 
 counter = 0 (On remet à zéro AVANT de lire l'index pour éviter le crash).
Traduction : index = int(counter) (On transforme le temps en numéro de page propre).
Affichage : screen.blit(images[index]) (On affiche l'image finale).
