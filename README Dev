# Editeur de G-code Manuel Developpeur

## Importation des bibliothèques :
Assurez-vous d'avoir installé les bibliothèques nécessaires : numpy et matplotlib.pyplot.

## Fontion 'pourcentage_couches_par_phases(nbr_phases)'
Cette fonction permet de demander à l'utilisateur de saisir le pourcentage de couches pour chaque phase du projet. Elle retourne une liste contenant les pourcentages de couches par phase.

## Fonction 'nombre_couches_par_phases(nbr_phases, pourcentages, nbr_total_couches)'
Cette fonction calcule le nombre de couches pour chaque phase en fonction des pourcentages de couches et du nombre total de couches. Elle retourne une liste contenant le nombre de couches par phase.

## Fonction 'calculer_nombre_couche_total(g_code_entree)'
Cette fonction calcule le nombre total de couches d'un fichier G-code en comptant le nombre de lignes commençant par ";LAYER". Elle affiche également le nombre de couches et le retourne.

## Fonction 'vitesses_phases(nbr_phases, nbr_couches)'
Cette fonction demande à l'utilisateur de saisir les vitesses à atteindre à la fin de chaque phase du projet. Elle retourne une liste contenant les vitesses correspondantes à chaque couche.

## Fonction 'temperature_phases(nbr_phases, nbr_couches)'
Cette fonction demande à l'utilisateur de saisir les températures à atteindre à la fin de chaque phase du projet. Elle retourne une liste contenant les températures correspondantes à chaque couche.

## Fonction 'calculer_moyenne(tableau)'
Cette fonction calcule la moyenne des valeurs d'un tableau.

## Fonction 'pourcentage_moyenne_tableau(tableau)'
Cette fonction calcule le pourcentage de chaque valeur du tableau par rapport à la moyenne du tableau. Elle retourne une liste contenant les pourcentages correspondants.

## Fonction 'pourcentage_gonflement_extrudat(tableau_1, tableau_2)'
Cette fonction calcule le pourcentage de gonflement de l'extrudat entre deux tableaux en utilisant la moyenne des pourcentages. Elle retourne une liste contenant les pourcentages de gonflement.

## Fonction 'maximum-absolu(tabelau_1, tableau_2)'
Cette fonction permet de construire un tableau contenant la valeur absolue maximale de deux autres tableaux qui sont pris en entrée. Elle retourne un seul tableau.

## Fonction 'pourcentage_correction_appliquee(tableau_1, tableau_2)'
Cette fonction applique une correction sur les pourcentages de gonflement en utilisant un coefficient de correction fourni par l'utilisateur. Elle retourne une liste contenant les pourcentages de correction appliqués.

## Fonction 'modification_gcode(chemin_fichier, nouvelles_vitesses, nouvelles_temperatures, deplacement_x, deplacement_y, pourcentage_extrusion)'
Cette fonction effectue les modifications nécessaires dans le fichier G-code en remplaçant les vitesses, les températures et en appliquant les corrections d'extrusion. Elle crée un nouveau fichier G-code avec les modifications et retourne le chemin du fichier de sortie.

## Fonction 'repasser_sans_extrusion(chemin_fichier)'
Cette fonction permet de repasser sur le G-code sans extrusion, en inversant les couches de remplissage. Elle crée un nouveau fichier G-code avec les modifications et retourne le chemin du fichier de sortie.

## Fonction 'maint()'
Fonction qui récupère les donnnées renseignées par l'utilisateur et qui utilise toutes les fonctions afin de les cadencer et de les ordonner dans le bon ordre pour récupérer le fichier final.
