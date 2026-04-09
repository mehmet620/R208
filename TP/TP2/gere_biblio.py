#from mediatheque import Bibliotheque, Ihm
from obj_bibliotheque import Bibliotheque
from obj_ihm import Ihm

FICHIER_JSON_AUTEURS = "Auteurs.json"
FICHIER_JSON_LIVRES = "Livres.json"
FICHIER_JSON_MEMBRES = "Membres.json"


if __name__ == "__main__":
    biblio = Bibliotheque(FICHIER_JSON_AUTEURS, FICHIER_JSON_LIVRES, FICHIER_JSON_MEMBRES)
    biblio.charger_auteurs()
    biblio.charger_livres()
    biblio.charger_membres()
    ihm = Ihm(biblio)
    while(True):
        if ihm.choix == 0:
            ihm.menu_accueil()
        elif ihm.choix == 1:
            ihm.menu_lister_auteurs()
        elif ihm.choix == 2:
            ihm.menu_lister_livres()
        elif ihm.choix == 3:
            ihm.menu_lister_membres()
        elif ihm.choix == 4:
            ihm.menu_lister_emprunts()
        elif ihm.choix == 5:
            ihm.menu_emprunter()
        elif ihm.choix == 6:
            ihm.menu_restituer()
        elif ihm.choix == 7:
            ihm.menu_ajouter_auteur()
        elif ihm.choix == 8:
            ihm.menu_ajouter_livre()
        elif ihm.choix == 9:
            ihm.menu_supprimer_livre()
        elif ihm.choix == 10:
            ihm.menu_ajouter_membre()
        elif ihm.choix == 11:
            ihm.menu_supprimer_membre()
        elif ihm.choix == 12:
            break
