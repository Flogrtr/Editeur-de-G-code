nombre_section_temperature=int(input("Choisir le nombre de morceaux de d'evolution de temperature linéaire"))
liste_T_int=[]
liste_T_final=[]
liste_nb_couche=[]
for i in range(0,nombre_section_temperature+1)

choix_



def changer_la_temperature_au_total(liste_T_int,liste_T_final,liste_nb_couche)
def changer_la_temperature_sur_un_morceau(T_int,T_final,nb_couche,nb_couche_deja_passee)
    T_couche=T_int
    i=1+nb_couche_deja_passee
    with open(xyz-10mm-calibration-cube_0.4n_0.2mm_PLA_MK4_8m.gcode, 'r') as f:
    for line in file:
    while i<=nb_couche+nb_couche_deja_passee:
        if line.startswith(';LAYER:'):
            i+=1
            modified_lines.append(f'M104 S{T_couche}\n')
            T_couche+= (T_final-T_int)/nb_couche
        elif
        modified_lines.append(line)
        