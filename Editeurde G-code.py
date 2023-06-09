import numpy as np
import matplotlib.pyplot as plt

def pourcentage_couches_par_phases(nbr_phases):
    """"
    Fonction qui demande à l'utilisateur quel pourcentage de couche il veut attribuer à chaque phase.

    Argument :
    nbr_phases : le nombre de phases total pour le projet

    Retour :
    pourcentages_couches_par_phases : liste des poucentages de couches pour chaque phases
    """

    # Initialisation d'une liste pour stocker les pourcentages de couches par phases
    pourcentages_couches_par_phases = []
    # Initialisation d'une variable qui fait la somme des pourcentages attribué à chaque phase au fur et à mesure
    somme_pourcentage = 0
    # Boucle qui demande à l'utilisateur de renseigner le pourcentage de couche pour chaque phase
    for i in range (0,nbr_phases-1,1) :
        #On demande le poucentage pour chaque phases
        pourcentage = int(input("Renseignez le poucentage de couches pour la phase  N°{} : ".format(i+1)))
        #On vérifie que l'utilisateur rentre bien des pourcentages cohérents
        if pourcentage >= 100 :
            somme_pourcentage = somme_pourcentage-pourcentage
            pourcentage = int(input("Merci de renseigner un pourcentage inférieur ou égale à 100 pour la phase N°{} : ".format(i+1)))
        somme_pourcentage += pourcentage
        # On ajoute ce pourcentage à un tableau qui les contiendra tous
        pourcentages_couches_par_phases.append(pourcentage)
    #On calcule automatiquement le pourcentage de la dernière phase, comme ça il n'y a pas d'érreur
    pourcentages_couches_par_phases.append(100-somme_pourcentage)
    return pourcentages_couches_par_phases

def nombre_couches_par_phases(nbr_phases, pourcentages,nbr_total_couches) :
    """
    Fonction qui calcule le nombre de couches pour chaque phases
    :param nbr_phases: nombre total de phases du projet
    :param pourcentages: Liste contenant les pourcentages de couches par phases (obtenus avec la fonction pourcentage_couches_par_phases)
    :param nbr_total_couches: nombre total de couches que possède le projet
    :return nbr_couches : liste du nombre de couches pour chaque phase
    """
    # Initialisation de liste du nombre de couches par phases
    nbr_couches = []
    # On boucle par rapport au nombre de phases totales
    for i in range (0,nbr_phases,1) :
        nbr_couches_par_phases = round(nbr_total_couches*pourcentages[i]/100)
        nbr_couches.append(nbr_couches_par_phases)
    return nbr_couches

def calculer_nombre_couche_total(g_code_entree):
    """
    FOnction qui récupère l'information dans le g_code du nombre total de couche du projet
    :param g_code_entree: Fichier G-code
    :return: Nombre de couche total du projet
    """
    with open(g_code_entree,'r') as g_code :
        lignes = g_code.readlines()
    # Variable qui compte le nombre de couches
    nb_couches = 0
    for ligne in lignes:
        # Toutes les lignes qui commencent par 'LAYER' correspondent à une nouvelle couche
        if ligne.startswith(';LAYER'):
            nb_couches += 1
    print("Le G_code possède",nb_couches,"couches")
    return nb_couches


def vitesses_phases(nbr_phases,nbr_couches):
    """
    Fonction qui calcule l'évolution de la vitesse par rapport au nombre de couches
    :param nbr_phases: Nombre total de phases du projet
    :param nbr_couches: Nombre total de couches du projet
    :return vitesse: liste des vitesses pour chaque couche
    """
    # Initialisation des lis
    vitesses_phases = []
    vitesses = []
    # On demande d'abord à l'utilisateur d'indiquer la vitesse de départ
    vitesse_ini = float(input("Renseignez la vitesse de départ : "))
    vitesses_phases.append(vitesse_ini)
    for i in range(1,nbr_phases+1,1): #changer la
        vitesse = float(input("Renseignez la vitesse à atteindre à la fin de la phase {}: ".format(i)))
        vitesses_phases.append(vitesse)
        vites = np.linspace(vitesses_phases[i-1],vitesses_phases[i],nbr_couches[i-1]) #changer la
        vitesses+=vites.tolist() #changé la
    return vitesses

def temperature_phases(nbr_phases,nbr_couches):
    temperature_phases = []
    temperatures = []
    # On demande d'abord à l'utilisateur d'indiquer la vitesse de départ
    temperature_ini = float(input("Renseignez la température de départ : "))
    temperature_phases.append(temperature_ini)
    for i in range(1,nbr_phases+1,1):
        temperature = float(input("Renseignez la temperature à atteindre à la fin de la phase {}: ".format(i)))
        temperature_phases.append(temperature)
        temp = np.linspace(temperature_phases[i-1],temperature_phases[i],nbr_couches[i-1])
        temperatures+=temp.tolist()
    return temperatures
### Calcul extrusion
# Fonction  qui prend un tableau en entrée et qui retourne un la valeur moyenne des valeurs du tableau
def calculer_moyenne(tableau):
    somme = sum(tableau)
    moyenne = somme / len(tableau)
    return moyenne

# Fonction qui prend deux tableaux en entrée et qui retourne un seul tableau contenant la valeur maximale entre les valeurs absolues des deux tableaux
def maximum_absolu(tableau_1, tableau_2):
    resultat = []
    for i in range(len(tableau_1)):
        valeur_1 = abs(tableau_1[i])
        valeur_2 = abs(tableau_2[i])
        # Compare les deux valeurs absolues des valeurs des deux tableaux et conserve la valeur maximale
        valeur_max = max(valeur_1, valeur_2)
        # Ajoute la valeur dans le tableau resultat qui sera retourné
        resultat.append(valeur_max)
    return resultat

# Fonction qui prend un tableau en entrée et qui retourne un tableau contenant la correspondance en % par rapport à la moyenne des valeurs du tableau
def pourcentage_moyenne_tableau (tableau):
    # Calcule la moyenne du tableau
    moyenne_tableau = calculer_moyenne(tableau)
    # Création du tableau dans lequel les valeurs seront écrites
    pourcentage_moyenne_tableau = [0]*len(tableau)
    i = 0
    for i in range(len(tableau)) :
        # Calcul permettant d'obtenir le pourcentage par rapport à la moyenne de la valeur i du tableau mis en entrée
        pourcentage_moyenne_tableau[i] = 100*tableau[i]/moyenne_tableau
    return (pourcentage_moyenne_tableau)

# Fonction qui prend deux tableaux en entrée et qui retourne un tableau contenant le pourcentage du gonflement à l'extrudat.
# Attention : Il est important de mettre en tableau_1 le tableau correpsondant à celui de la température et en tableau_2 celui correspondant à celui de la vitesse.
def pourcentage_gonflement_extrudat (tableau_1, tableau_2) :
    # Création du tableau dans lequel les valeurs de le pourcentage du gonflement à l'extrudat seront insérées
    pourcentage_gonflement_extrudat = [0]*len(tableau_1)
    i = 0
    for i in range(len(tableau_1)) :
        # Calcul permettant d'obtenur le pourcentage du gonflement à l'extrudat à partir des valeurs des deux tableaux de température et de vitesse.
        pourcentage_gonflement_extrudat[i] = (-pourcentage_moyenne_tableau(tableau_1)[i] + pourcentage_moyenne_tableau(tableau_2)[i])/2
    return (pourcentage_gonflement_extrudat)

# Fonction qui prend deux tableaux en entrée et qui retourne un tableau contenant le pourcetnage du coefficient de correction a sur ou sous extruder.
# Attention : Il est important de mettre en tableau_1 le tableau correpsondant à celui de la température et en tableau_2 celui correspondant à celui de la vitesse.
def pourcentage_correction_appliquee (tableau_1, tableau_2) : #tableau 1 correspond à la temp et tableau 2 correspond à la vitesse
    # Demande à l'utilisateur de rentrer la valeur du coefficient correctif de l'extrudat souhaité.
    coefficient_correction = int(input('Entrez la valeur du coefficeint correctif de l\'extrudat souhaité de la sorte [-X%;+X%] : '))
    # Calcul le minimum du pourcentage du gonflement à l'extrudat.
    valeur_min = min(pourcentage_gonflement_extrudat(tableau_1, tableau_2))
    # Calcul le maximum du pourcentage du gonflement à l'extrudat.
    valeur_max = max(pourcentage_gonflement_extrudat(tableau_1, tableau_2))
    # Retiens la valeur maximale entre la valeur absolue du minimum et du maximum
    max_val_abs = max(abs(valeur_max), abs(valeur_min))
    # Création du tableau dans lequel seront insérées les valeurs du pourcentage de sur ou sous extrusion à appliquer par rapport au minimum.
    pourcentage_extrusion_min = [0]*len(pourcentage_gonflement_extrudat(tableau_1, tableau_2))
    # Création du tableau dans lequel seront insérées les valeurs du pourcentage de sur ou sous extrusion à appliquer par rapport au maximum.
    pourcentage_extrusion_max = [0]*len(pourcentage_gonflement_extrudat(tableau_1, tableau_2))
    # Création du tableau dans lequel seront insérées les valeurs du pourcentage de sur ou sous extrusion à appliquer dans le meilleur des cas.
    # C'est à dire la plus grande valeur entre la valeur absolue entre le minimum et le maximum.
    pourcentage_extrusion_final = [0]*len(pourcentage_gonflement_extrudat(tableau_1, tableau_2))
    i = 0
    for i in range(len(pourcentage_gonflement_extrudat(tableau_1, tableau_2))) :
        # Calcul les valeurs par rapport au minimum à insérer dans le tableau à partir des deux tableaux de vitesse et de température.
        pourcentage_extrusion_min[i] = pourcentage_gonflement_extrudat(tableau_1, tableau_2)[i]* (-coefficient_correction) / abs((valeur_min*100))
    for i in range(len(pourcentage_gonflement_extrudat(tableau_1, tableau_2))):
        # Calcul les valeurs par rapport au maximum à insérer dans le tableau à partir des deux tableaux de vitesse et de température.
        pourcentage_extrusion_max[i] = pourcentage_gonflement_extrudat(tableau_1, tableau_2)[i]*coefficient_correction / (abs(valeur_max*100))
    for i in range(len(pourcentage_gonflement_extrudat(tableau_1, tableau_2))):
        # Condition pour que la valeurs ne dépasse pas l'intervalle saisi par l'utilisateur.
        if pourcentage_extrusion_max[i] == coefficient_correction/100 or pourcentage_extrusion_min[i] == coefficient_correction/100 :
            pourcentage_extrusion_final[i] = coefficient_correction/100
            # Condition qui permet de prendre la plus grande valeur entre la valeur absolue entre le minimum et le maximum si la valeur maximale est différente de 0..
        elif max_val_abs!=0:
            pourcentage_extrusion_final[i] = maximum_absolu(pourcentage_extrusion_max, pourcentage_extrusion_min)[i]
    return (pourcentage_extrusion_final)


###modification du code
def modification_gcode(chemin_fichier,nouvelles_vitesses,nouvelles_temperatures,deplacement_x,deplacement_y,pourcentage_extrusion):

    #Lecture du fichier G-code
    with open(chemin_fichier,'r') as g_code :
        lignes = g_code.readlines()

    #Écriture des nouvelles vitesses dans le G-code
    with open("cube_intermediaire.gcode",'w') as g_code :
        i = -1
        for ligne in lignes :

            if ligne.startswith('G1') :

                #On extrait d'abord la valeur de la vitesse d'impression
                vitesse = None
                x = None
                y = None
                extrusion=None
                valeurs = ligne.split()
                for valeur in valeurs :
                    if valeur.startswith('F') :
                        vitesse = float(valeur[1:])
                        break
                    if valeur.startswith('X') :
                        x = float(valeur[1:])
                        break
                    if valeur.startswith('Y') :
                        y = float(valeur[1:])
                        break
                    if valeur.startswith('E') :
                        extrusion = float(valeur[1:])
                        break

                #On ajoute la nouvelle vitesse d'impression et on ajoute les lignes de temperature
                if vitesse is not None :
                    nouvelle_vitesse = nouvelles_vitesses[i]
                    nouvelle_temperature = nouvelles_temperatures[i]
                    nouvelle_ligne = ligne.replace(f'F{vitesse}', f'F{nouvelle_vitesse:.3f}')
                    nouvelle_ligne += '\nM104 S' + str(nouvelle_temperature) + '\nM109 S' + str(nouvelle_temperature) + '\n'
                    ligne = nouvelle_ligne
                else :
                    nouvelle_ligne = ligne

                if x is not None :
                    nouveau_x = x + deplacement_x
                    nouvelle_ligne = ligne.replace(f'X{x}', f'Y{nouveau_x:.3f}')
                    ligne = nouvelle_ligne

                if y is not None :
                    nouveau_y = y + deplacement_y
                    nouvelle_ligne = ligne.replace(f'Y{y}', f'Y{nouveau_y:.3f}')

                if extrusion is not None :
                    nouveau_extrusion = extrusion*(1+pourcentage_extrusion[i])
                    nouvelle_ligne = ligne.replace(f'E{extrusion}', f'E{nouveau_extrusion:.3f}')
                # Écriture de nouvelle ligne dans le fichier
                g_code.write(nouvelle_ligne)


            elif ligne.startswith(';LAYER:') or ligne.startswith(';LAYER_C'):
                i += 1
                g_code.write(ligne)
            else :
                g_code.write(ligne)
    #chemin_sortie = "chemin_vers_fichier_sortie.gcode"
    return "cube_intermediaire.gcode"

###Fonction suplémentaire (rechauffer)
def repasser_sans_extrusion(chemin_fichier):
    with open(chemin_fichier, 'r') as g_code:
        lignes = g_code.readlines()
        position_x_a_reutiliser = []
        position_y_a_reutiliser = []
        j=0 #initiation d'un compteur pour l'inversion des couches de remplissage
    with open("cubefinal.gcode", 'w') as g_code_sortie:
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
            elif ligne.startswith(';LAYER') or ligne.startswith(';LAYER_C'):
                if j%2==0: #inversion des couches
                    position_x_a_reutiliser=position_x_a_reutiliser[::-1]
                    position_y_a_reutiliser=position_y_a_reutiliser[::-1]
                j+=1 # iteration du compteur d'inversion
                for i in range(len(position_x_a_reutiliser)):
                    g_code_sortie.write(f'G0 X{position_x_a_reutiliser[i]} Y{position_y_a_reutiliser[i]}\n')
                position_x_a_reutiliser = []
                position_y_a_reutiliser = []
            g_code_sortie.write(ligne)
    #chemin_fichier_sortie = "cubefinal.gcode"
    return "cubefinal.gcode"

# Mains
def main():
    # Dictionnaire couches
    #couches = {}
    #Entrer le nom du fichier
    g_code_entree=(input('Renseignez le nom du fichier : '))
    # On demande à l'utilisateur le nombre de phases qu'il souhaite pour son projet
    nbr_phases = int(input("Renseignez le nombre de phases que doit comporter votre projet : "))
    # On demande à l'utilisateur le nombre total de couches qu'il souhaite avoir pour son projet
    nbr_couches_total = calculer_nombre_couche_total(g_code_entree)
    # Fonction qui demande à l'utilisateur le poucentage de couches par phase qu'il souhaite avoir.
    pourcentage = pourcentage_couches_par_phases(nbr_phases)
    # Fonction qui calcule le nombre de couches par phases
    nbr_couches = nombre_couches_par_phases(nbr_phases,pourcentage,nbr_couches_total)
    #Deplacement
    deplacement_x=int(input('Renseignez le déplacement en x (en mm) : '))
    deplacement_y=int(input('Renseignez le déplacement en y (en mm) : '))
    # Fonction qui demande à l'utilisateur de rentrer les vitesses qu'il souhaite pour chaque phases
    nouvelles_vitesses = vitesses_phases(nbr_phases, nbr_couches)
    print(len(nouvelles_vitesses))
    #print(nouvelles_vitesses)

    # Fonction qui demande à l'utilisateur de rentrer les températures qu'il souhaite pour chaque phase
    nouvelles_temperatures = temperature_phases(nbr_phases,nbr_couches)
    print(len(nouvelles_temperatures))

    #Fonction de correction de l'extrudat
    pourcentage_extrusion=pourcentage_correction_appliquee(nouvelles_temperatures,nouvelles_vitesses)
    #Fonction d'intégration des modifications au Gcode
    chemin_sortie=modification_gcode(g_code_entree,nouvelles_vitesses, nouvelles_temperatures, deplacement_x, deplacement_y,pourcentage_extrusion)

    #Rechauffage sans extrusion
    gcode_final=repasser_sans_extrusion(chemin_sortie)

    #print(nouvelles_temperatures)
    #Profil de vitesse
    plt.plot(range(1, nbr_couches_total + 1), nouvelles_vitesses)
    plt.xlabel('Couches')
    plt.ylabel('Vitesse')
    plt.title('Profil de la vitesse lors de l\'impression')
    plt.grid(True)
    plt.show()

    #Profil de temperature
    plt.plot(range(1, nbr_couches_total + 1), nouvelles_temperatures)
    plt.xlabel('Couches')
    plt.ylabel('Temperature')
    plt.title('Profil de la temperature lors de l\'impression')
    plt.grid(True)
    plt.show()

    #Fonction qui modifie le g-code au niveau de la vitesse
    #modification_gcode()
    return()


#MAIN
main()