from obj_auteur import Auteur
from obj_membre import Membre
from obj_livre import Livre
from obj_couleur import Couleur

import json

class Bibliotheque(Couleur):
    """Classe représentant une bibliothèque contenant des auteurs, des livres et des membres."""
    def __init__(self, fichier_auteurs_json, fichier_livres_json, fichier_membres_json):
        self.fichier_auteurs_json = fichier_auteurs_json
        self.fichier_livres_json = fichier_livres_json
        self.fichier_membres_json = fichier_membres_json
        self.auteurs = []
        self.livres = []
        self.membres = []

    def charger_auteurs(self, flag_affi = False):
        """Charge une liste d'auteurs depuis un fichier JSON."""
        try:
            with open(self.fichier_auteurs_json, "r", encoding="utf-8") as f:
                data_json = json.load(f)
                for item in data_json:
                    self.auteurs.append(Auteur(item["nom"], item["prenom"], item["pays"], item["date_naissance"]))
            if flag_affi: print(f"----> {Bibliotheque.ROUGE}{len(self.auteurs)} auteurs ont été chargés depuis {self.fichier_auteurs_json}.{Bibliotheque.NO_COLOR}")
        except Exception as e:
            print(f"Erreur lors du chargement des auteurs : {e}")

    def charger_livres(self, flag_affi = False):
        """Charge une liste de livres depuis un fichier JSON."""
        try:
            with open(self.fichier_livres_json, "r", encoding="utf-8") as f:
                data_json = json.load(f)
                for item in data_json:
                    auteur_trouve = self.__check_auteur(item["auteur_nom"], item["auteur_prenom"])
                    if auteur_trouve:
                        self.livres.append(Livre(item["titre"], auteur_trouve, item["isbn"], item["annee_publication"]))
                    else:
                        print(f"{Bibliotheque.ROUGE}Auteur inconnu pour le livre {Bibliotheque.MAGENTA}'{item['titre']}'{Bibliotheque.NO_COLOR}")
                        print(f"{Bibliotheque.BLEU}Le livre {Bibliotheque.MAGENTA}'{item['titre']}'{Bibliotheque.BLEU} n'est pas ajouter à la bibliothèque...{Bibliotheque.NO_COLOR}")
            if flag_affi: print(f"----> {Bibliotheque.ROUGE}{len(self.livres)} livres ont été chargés depuis {self.fichier_livres_json}.{Bibliotheque.NO_COLOR}")
        except Exception as e:
            print(f"Erreur lors du chargement des livres : {e}")

    def charger_membres(self, flag_affi = False):
        """Charge une liste de membres depuis un fichier JSON."""
        try:
            with open(self.fichier_membres_json, "r", encoding="utf-8") as f:
                data_json = json.load(f)
                for item in data_json:
                    self.membres.append(Membre(item["nom"], item["prenom"], item["date_naissance"]))
            if flag_affi: print(f"----> {Bibliotheque.ROUGE}{len(self.membres)} membres ont été chargés depuis {self.fichier_membres_json}.{Bibliotheque.NO_COLOR}")
        except Exception as e:
            print(f"Erreur lors du chargement des membres : {e}")

    def __check_auteur(self, nom_a_trouver, prenom_a_trouver):
        for auteur in self.auteurs:
            if auteur.nom == nom_a_trouver and auteur.prenom == prenom_a_trouver:
                return auteur
        return None

if __name__ == "__main__":
    def affiche_tout(bibliotheque):
        print(f"\n{'-' * 20} Auteurs {'-' * 20}")
        for auteur in bibliotheque.auteurs:
            print(auteur)
        print(f"\n{'-' * 20} Livres {'-' * 20}")
        for livre in bibliotheque.livres:
            print(livre)
        print(f"\n{'-' * 20} Membres {'-' * 20}")
        for membre in bibliotheque.membres:
            print(membre)

    # Creation de l'instance et chargement des données JSON
    biblio = Bibliotheque("Auteurs.json", "Livres.json", "Membres.json")
    biblio.charger_auteurs(True)
    biblio.charger_livres(True)
    biblio.charger_membres(True)
    affiche_tout(biblio)

    input(f"\n\t\t{Bibliotheque.CYAN}Appuyer sur Entrée pour voir une seconde bibliothèque incomplete...{Bibliotheque.NO_COLOR}")
    # Mise en evidence du problème de livres associés à des auteurs n'existant pas dans les données de la bibliothèque
    biblio_test = Bibliotheque("Auteurs.json", "Livres.json", "Membres.json")
    # On ne charge pas les données JSON des auteurs mais on en créé un seul !!!
    biblio_test.auteurs.append(Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949"))
    biblio_test.charger_livres(True)
    # On ne charge pas les membres...
    affiche_tout(biblio_test)
