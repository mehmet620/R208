# obj_livre.py
from obj_couleur import Couleur
from Ex1 import Auteur

class Livre(Couleur):
    nombre_total_livres = 0

    def __init__(self, titre, auteur, isbn=None, annee_publication=None):
        Livre.nombre_total_livres += 1
        self.id = Livre.nombre_total_livres
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn if isbn is not None else "N/A"
        self.annee_publication = annee_publication if annee_publication is not None else "inconnue"
        self.disponible = True

    def __str__(self):
        dispo = "Dispo" if self.disponible else "NON Dispo"
        return (
            f"{self.id}. : '{self.titre}' de {self.auteur.prenom} {self.auteur.nom} "
            f"(ISBN: {self.isbn}, publié en {self.annee_publication}) - {dispo}"
        )


if __name__ == "__main__":
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    verne = Auteur("VERNE", "Jules", "France", "08/02/1828")

    print("Création de 3 instances de Livre et affichage...")
    livre_1 = Livre("Les Piliers de la Terre", follett, "9782130428114", "1989")
    livre_2 = Livre("Une Colonne de Feu", follett, "9782221157695", "2017")
    livre_2.disponible = False
    livre_3 = Livre("Vingt Mille Lieues sous les mers", verne, "9782070364234", "1870")

    print(livre_1)
    print(livre_2)
    print(livre_3)
