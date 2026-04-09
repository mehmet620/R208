# obj_membre.py
from Ex2 import Livre
from Ex1 import Auteur

class Membre:
    nombre_total_membres = 0

    def __init__(self, nom, prenom, date_naissance):
        Membre.nombre_total_membres += 1
        self.id = Membre.nombre_total_membres
        self.nom = nom.upper()
        self.prenom = prenom.capitalize()
        self.date_naissance = date_naissance
        self.livres_empruntes = []

    def __str__(self):
        return f"{self.id}. : {self.prenom} {self.nom} (né(e) le {self.date_naissance})"

    def lister_emprunts(self):
        if not self.livres_empruntes:
            print(f"/// {self.prenom} {self.nom} n'a aucun livre emprunté.")
            return

        print(f"-> {self.prenom} {self.nom} a emprunté les livres suivants :")
        for i, livre in enumerate(self.livres_empruntes, 1):
            print(f"- {i}. {livre.titre} de {livre.auteur.prenom} {livre.auteur.nom}")

    def emprunter_livre(self, livre):
        if not livre.disponible:
            print(f"----> Le livre '{livre.titre}' est déjà emprunté.")
            return

        livre.disponible = False
        self.livres_empruntes.append(livre)
        print(f"----> {self.prenom} {self.nom} a emprunté '{livre.titre}'.")

    def restituer_livre(self, livre):
        if livre in self.livres_empruntes:
            livre.disponible = True
            self.livres_empruntes.remove(livre)
            print(f"--------> {self.prenom} {self.nom} a restitué '{livre.titre}'.")
