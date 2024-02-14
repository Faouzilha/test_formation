from func import estTermine

#######################################################################
#
#          Programme principal
#
#
#######################################################################
if __name__ == "__main__":
    liste_courses = [] #tableau dynamique 
    while True:
        nom_course = input("Mettre un nom de course, pour arrêter mettre exit\n")    
        if estTermine(nom_course):
            break
        elif nom_course != "":
            liste_courses.append(nom_course)
        
    for i in range(len(liste_courses)):
        print(liste_courses[i])
