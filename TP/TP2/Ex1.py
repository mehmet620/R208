# obj_auteur.py

from obj_couleur import Couleur

class Auteur(Couleur):
    nombre_total_auteurs = 0

    def __init__(self, nom, prenom, pays=None, date_naissance=None):
        Auteur.nombre_total_auteurs += 1
        self.id = Auteur.nombre_total_auteurs
        self.nom = nom.upper()
        self.prenom = prenom


        self.pays = pays if pays is not None else "Inconnu"
        self.date_naissance = date_naissance if date_naissance is not None else "Inconnue"


    def __str__(self):
        return (
            f"{self.id}. : {self.prenom} {self.nom} "
            f"(nÃ©(e) le {self.date_naissance} en {self.pays})"
        )



if __name__ == "__main__":
    print("CrÃ©ation de 3 instances de Auteur et affichage...")

    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    verne = Auteur("VERNE", "Jules", "France", "08/02/1828")
    bridou = Auteur("BRIDOU", "Justin", None, None)

    print(follett)
    print(verne)
    print(bridou)

    print(bridou.date_naissance)
    print(bridou.pays)
    print(bridou.date_naissance)