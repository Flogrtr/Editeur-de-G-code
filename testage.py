def repasser_sans_extrusion(chemin_fichier,chemin_fichier_sortie):
    with open(chemin_fichier, 'r') as g_code:
        lignes = g_code.readlines()
        position_x_a_reutiliser = []
        position_y_a_reutiliser = []
    with open(chemin_fichier_sortie, 'w') as g_code_sortie:
        for ligne in lignes:
            if ligne.startswith('G1'):
                valeurs = ligne.split()
                for valeur in valeurs:
                    if valeur.startswith('X'):
                        position_x_a_reutiliser.append(float(valeur[1:]))
                    if valeur.startswith('Y'):
                        position_y_a_reutiliser.append(float(valeur[1:]))
                    if valeur.startswith('E') and float(valeur[1:])==0 and position_x_a_reutiliser!=[] and position_y_a_reutiliser!=[]:
                        position_x_a_reutiliser.pop()
                        position_y_a_reutiliser.pop()
            elif ligne.startswith(';LAYER'):
                for i in range(len(position_x_a_reutiliser)):
                    g_code_sortie.write(f'G0 X{position_x_a_reutiliser[i]} Y{position_y_a_reutiliser[i]}\n')
                position_x_a_reutiliser = []
                position_y_a_reutiliser = []
            g_code_sortie.write(ligne)


repasser_sans_extrusion('cubeebtx','cubesortie')