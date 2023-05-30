# Editeur de G-code Manuel utilisateur

Importation des bibliothèques :
Assurez-vous d'avoir installé les bibliothèques nécessaires : numpy et matplotlib.pyplot.
 
Chargement du fichier G-code :
Assurez-vous d'avoir le fichier G-code que vous souhaitez modifier.

Modification des paramètres :
Le programme offre plusieurs fonctionnalités de modification, telles que l'ajustement des vitesses, des températures, des déplacements et de l'extrusion.
Utilisez les différentes fonctions fournies par le programme pour obtenir les paramètres de modification souhaités. Par exemple, vous pouvez utiliser les fonctions vitesses_phases(), temperature_phases(), deplacement_x(), deplacement_y(), pourcentage_extrusion() pour obtenir les valeurs correspondantes.
Stockez ces valeurs dans des variables appropriées.

Application des modifications :
Utilisez la fonction modification_gcode() en passant les paramètres appropriés pour modifier le fichier G-code. Par exemple :

Résultats :
La fonction modification_gcode() renverra le chemin vers le fichier de sortie modifié.
Vous pouvez utiliser ce chemin pour accéder au fichier modifié et l'utiliser dans votre processus d'impression 3D.