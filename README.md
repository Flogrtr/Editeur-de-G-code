# Editeur de G-code Manuel utilisateur
Ce code est destiné à la gestion des paramètres d'impression en fonction du nombre de couches et des différentes phases d'un projet d'impression 3D. Il permet de calculer le nombre de couches par phase, d'obtenir les vitesses et les températures correspondantes, de modifier un fichier G-code avec les nouvelles valeurs et de générer un fichier de sortie.

## Importation des bibliothèques :
Assurez-vous d'avoir installé les bibliothèques nécessaires : numpy et matplotlib.pyplot.
 
## Chargement du fichier G-code :
Assurez-vous d'avoir le fichier G-code que vous souhaitez modifier. Assurez-vous de l'avoir placé dans le même fichier que là où se trouve le code python.

## Modification des paramètres :
Le programme offre plusieurs fonctionnalités de modifications, telles que l'ajustement des vitesses, des températures, des déplacements et de l'extrusion.
Utilisez les différentes fonctions fournies par le programme pour obtenir les paramètres de modifications souhaités. Par exemple, vous pouvez utiliser les fonctions vitesses_phases(), temperature_phases(), deplacement_x(), deplacement_y(), pourcentage_extrusion() pour obtenir les valeurs correspondantes.
Stockez ces valeurs dans des variables appropriées.

## Application des modifications :
Utilisez la fonction modification_gcode() en passant les paramètres appropriés (les vitesses, les températures, les coordonnées et l'extrusion selon les nouvelles valeurs spécifiées) pour modifier le fichier G-code. 

## Résultats :
La fonction modification_gcode() renverra le chemin vers le fichier de sortie modifié.
Vous pouvez utiliser ce chemin pour accéder au fichier modifié et l'utiliser dans votre processus d'impression 3D.
