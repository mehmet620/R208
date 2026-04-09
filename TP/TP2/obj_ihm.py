from datetime import datetime
from obj_auteur import Auteur
from obj_membre import Membre
from obj_livre import Livre
from obj_couleur import Couleur

class Ihm(Couleur):
    """ Interface Homme-Machine (IHM) pour la gestion d'une flotte de véhicules. """
    def __init__(self, biblio):
        """Constructeur : Initialise l'IHM avec les listes d'auteurs, de livres et de membres.
        :argument auteurs: Liste des auteurs.
        :argument livres: Liste des livres.
        :argument membres: Liste des membres. """
        self.biblio = biblio
        self.choix = 0

    def menu_accueil(self):
        """ Affiche le menu principal et attend l'entrée de l'utilisateur. """
        print("\n" * 100)
        print(f"\t{Ihm.BLEU}1.  {Ihm.NO_COLOR}Lister tous les auteur(e)s.")
        print(f"\t{Ihm.BLEU}2.  {Ihm.NO_COLOR}Lister tous les livres.")
        print(f"\t{Ihm.BLEU}3.  {Ihm.NO_COLOR}Lister tous les membres.")
        print(f"\t{Ihm.BLEU}4.  {Ihm.NO_COLOR}Lister tous les emprunts.")
        print(f"\t{Ihm.BLEU}5.  {Ihm.NO_COLOR}Emprunt d'un livre.")
        print(f"\t{Ihm.BLEU}6.  {Ihm.NO_COLOR}Restitution d'un livre.")
        print()
        print(f"\t{Ihm.BLEU}7.  {Ihm.NO_COLOR}Ajouter un(e) auteur(e).")
        print(f"\t{Ihm.BLEU}8.  {Ihm.NO_COLOR}Créer un livre.")
        print(f"\t{Ihm.BLEU}9.  {Ihm.NO_COLOR}Supprimer un livre.")
        print(f"\t{Ihm.BLEU}10. {Ihm.NO_COLOR}Créer un(e) membre.")
        print(f"\t{Ihm.BLEU}11. {Ihm.NO_COLOR}Radier un(e) membre.")
        print(f"\t{Ihm.BLEU}12. {Ihm.NO_COLOR}Quitter.")
        print()
        self.__attendre_choix_ligne(range(1, 13), f"\t{Ihm.ROUGE}--> {Ihm.NO_COLOR}Choisissez une action {Ihm.VERT}(numéro){Ihm.NO_COLOR} : ")

    def menu_lister_auteurs(self):
        """ Affiche la liste des auteurs. """
        print("\n" * 100)
        self.__affiche_select_auteurs(None)
        input(f"\t\t{Ihm.CYAN}Appuyer sur Entrée pour continuer...{Ihm.NO_COLOR}")
        self.choix = 0

    def menu_lister_livres(self):
        """ Affiche la liste des livres. """
        print("\n" * 100)
        self.__affiche_select_livres(None)
        input(f"\t\t{Ihm.CYAN}Appuyer sur Entrée pour continuer...{Ihm.NO_COLOR}")
        self.choix = 0

    def menu_lister_membres(self):
        """ Affiche la liste des membress. """
        print("\n" * 100)
        self.__affiche_select_membres()
        input(f"\t\t{Ihm.CYAN}Appuyer sur Entrée pour continuer...{Ihm.NO_COLOR}")
        self.choix = 0

    def menu_lister_emprunts(self):
        """ Affiche la liste des emprunts. """
        print("\n" * 100)
        print(f"\n{'-'*20} Emprunts {'-'*20}")
        for membre in self.biblio.membres:
            membre.lister_emprunts()
        print()
        input(f"\t\t{Ihm.CYAN}Appuyer sur Entrée pour continuer...{Ihm.NO_COLOR}")
        self.choix = 0

    def menu_emprunter(self):
        """
        Permet l'emprunt d'un livre par un membre.
        Propose le choix du membre et le choix des livres...
        """
        print("\n" * 100)
        index_livre = self.__affiche_select_livres("Choisissez le livre qu'il ou elle veut emprunter")
        index_membre = self.__affiche_select_membres("Choisissez le ou la membre qui souhaite emprunter un livre")

        self.biblio.membres[index_membre].emprunter_livre(self.biblio.livres[index_livre])
        input(f"\n\t\t{Ihm.CYAN}Appuyer sur Entrée pour continuer...{Ihm.NO_COLOR}")
        self.choix = 0

    def menu_restituer(self):
        """
        Permet la restitution d'un livre emprunté par un membre.
        Propose le choix du membre et le choix des emprunts pour ce membre...
        """
        print("\n" * 100)
        index_membre = self.__affiche_select_membres("Choisissez le ou la membre qui souhaite restituer un livre")
        if len(self.biblio.membres[index_membre].livres_empruntes) > 0:
            print()
            self.__affiche_emprunts(index_membre)
            print()
            choix_possible = []
            dico_index_id = {}
            for index, emprunt in enumerate(self.biblio.membres[index_membre].livres_empruntes):
                choix_possible.append(emprunt.id)
                dico_index_id[emprunt.id] = index

            self.__attendre_choix_ligne(choix_possible, f"\t{Ihm.ROUGE}------> {Ihm.NO_COLOR}Choisissez le livre qu'il ou elle veut restituer {Ihm.VERT}(numéro){Ihm.NO_COLOR} : ")
            id_choix = self.choix

            livre_restitue = self.biblio.membres[index_membre].livres_empruntes[dico_index_id[id_choix]]
            self.biblio.membres[index_membre].restituer_livre(livre_restitue)
            print(f"\t{Ihm.ROUGE}----------> {Ihm.NO_COLOR}Le livre {Ihm.BLEU}{livre_restitue.id}. {Ihm.NO_COLOR}'{Ihm.MAGENTA}{livre_restitue.titre}{Ihm.NO_COLOR}' a bien été retiré de la liste des emprunts de {Ihm.VERT}{self.biblio.membres[index_membre].prenom} {self.biblio.membres[index_membre].nom}{Ihm.NO_COLOR}...")
        else:
            self.__affiche_emprunts(index_membre)
        input(f"\n\t\t{Ihm.CYAN}Appuyer sur Entrée pour continuer...{Ihm.NO_COLOR}")
        self.choix = 0

    def menu_ajouter_auteur(self):
        """
        Méthode qui ajoute un auteur de la liste des auteurs.
        Cette méthode demande successivement toutes les valeurs de 'nom', 'prenom', 'pays' et 'date_naissance' du nouvel auteur.
        Les 'nom' et 'prenom' ne peuvent pas être des strings vides.
        Lorsque 'pays' est une string vide, la valeur 'None' lui est affecté.
        La date de naissance est validée par la méthode : __verifie_date(date_naissance)
        Si l'année de naissance saisie est égale à "01/01/1900", la valeur 'None' lui est affecté.
        --> Chaque fois que la donnée saisie n'est pas valide, la demande est réitérée ...
        Lorsque les quatre données sont valides, il y a création de l'instance avec le constructeur : self.biblio.Auteur(...)
        Puis, ajout de cette instance à la liste des auteurs : self.biblio.auteurs !
        Pour finir, Un message indiquant la création de l'auteur est affiché.
        """
        print("\n" * 100)   # Vide l'affichage du terminal par 100 lignes vides

        #**************************************************
        #   A COMPLETER (à la place de la ligne suivante !)
        print(f"\t{Ihm.ROUGE}A coder...{Ihm.NO_COLOR}")
        # *************************************************

        input(f"\n\t\t{Ihm.CYAN}Appuyer sur Entrée pour continuer...{Ihm.NO_COLOR}") # attend que 'Return' soit enfoncé
        self.choix = 0     # on revient au menu d'accueil...

    def menu_ajouter_livre(self):
        """
        Méthode qui ajoute un livre de la liste des livres.
        Cette méthode commence par afficher les auteurs de la liste d'auteurs puis demande le numéro d'id de l'auteur du nouveau livre.
        Pour cela, un appel de la méthode : __affiche_select_auteurs(texte) est réalisé.
        L'instance de 'Ayteur' correspondant à cet id est récupérée.
        Cette méthode demande ensuite et successivement toutes les valeurs de 'titre', 'isbn' et 'annee_publication' du nouveau livre.
        Les 'titre' ne peut pas être une string vide.
        Lorsque 'isbn' est une string vide, la valeur 'None' lui est affecté.
        L'année de publication doit être un entier. Si la valeur 0 est saisie, la valeur 'None' lui est affecté.
        --> Chaque fois que la donnée saisie n'est pas valide, la demande est réitérée ...
        Lorsque les quatre données sont valides, il y a création de l'instance avec le constructeur : self.biblio.Livre(...)
        Puis, ajout de cette instance à la liste des auteurs : self.biblio.livres !
        Pour finir, Un message indiquant la création du livre est affiché.
        """
        print("\n" * 100)

        # **************************************************
        #   A COMPLETER (à la place de la ligne suivante !)
        print(f"\t{Ihm.ROUGE}A coder...{Ihm.NO_COLOR}")
        # *************************************************

        input(f"\n\t\t{Ihm.CYAN}Appuyer sur Entrée pour continuer...{Ihm.NO_COLOR}") # attend que 'Return' soit enfoncé
        self.choix = 0     # on revient au menu d'accueil...

    def menu_supprimer_livre(self):
        """
        Méthode qui supprime un livre de la liste des livres.
        Cette méthode commence par afficher la liste des livres puis demande le numéro d'id de celui qui doit être supprimé.
        Pour cela, un appel de la méthode : __affiche_select_livres(texte) est réalisé.
        L'instance de 'Livre' correspondant à cet id est récupéré.
        Si le livre est emprunté :
        -   Un message indiquant l'impossibilité de suppression est affiché.
        Si le livre n'est pas emprunté :
        -   Un message indiquant la possibilité de suppression est affiché.
        -   Une confirmation de suppression est demandée.
        -   Après confirmation, suppression de cette instance de la liste des livres : self.biblio.livres
        -   Pour finir, Un message indiquant la suppression du livre est affiché.
        ATTENTION : Comme il ne faut pas de "trou" dans les numéros d'id ex : 1, 2, 3, 5, 6, 7 (manque 4)
        Au sein d'une itération dans la liste des livres, il y a décrémentation tous les id qui sont supérieurs à celui du livre supprimé...
        """
        print("\n" * 100)   # Vide l'affichage du terminal par 100 lignes vides

        # **************************************************
        #   A COMPLETER (à la place de la ligne suivante !)
        print(f"\t{Ihm.ROUGE}A coder...{Ihm.NO_COLOR}")
        # *************************************************

        input(f"\n\t\t{Ihm.CYAN}Appuyer sur Entrée pour continuer...{Ihm.NO_COLOR}") # attend que 'Return' soit enfoncé
        self.choix = 0     # on revient au menu d'accueil...

    def menu_ajouter_membre(self):
        """
        Méthode qui ajoute un membre de la liste des membres.
        Cette méthode demande successivement toutes les valeurs de 'nom', 'prenom' et 'date_naissance' du nouveau membre.
        Les 'nom' et 'prenom' ne peuvent pas être des strings vides.
        La date de naissance est validée par la méthode : __verifie_date(date_naissance)
        --> Chaque fois que la donnée saisie n'est pas valide, la demande est réitérée ...
        Lorsque les trois données sont valides, il y a création de l'instance avec le constructeur : self.biblio.Membre(...)
        Puis, ajout de cette instance à la liste des auteurs : self.biblio.membres !
        Pour finir, Un message indiquant la création du membre est affiché.
        """
        print("\n" * 100)   # Vide l'affichage du terminal par 100 lignes vides

        # **************************************************
        #   A COMPLETER (à la place de la ligne suivante !)
        print(f"\t{Ihm.ROUGE}A coder...{Ihm.NO_COLOR}")
        # *************************************************

        input(f"\n\t\t{Ihm.CYAN}Appuyer sur Entrée pour continuer...{Ihm.NO_COLOR}") # attend que 'Return' soit enfoncé
        self.choix = 0     # on revient au menu d'accueil...

    def menu_supprimer_membre(self):
        """
        Méthode qui supprime un membre de la liste des membres.
        Cette méthode commence par afficher la liste des membres puis demande le numéro d'id de celui qui doit être supprimé.
        Pour cela, un appel de la méthode : __affiche_select_membres(texte) est réalisé.
        L'instance de 'Membre' correspondant à cet id est récupéré.
        Si le membre a un emprunt en cours :
        -   Un message indiquant l'impossibilité de suppression est affiché.
        Si le membre n'a pas d'emprunt en cours :
        -   Un message indiquant la possibilité de suppression est affiché.
        -   Une confirmation de suppression est demandée.
        -   Après confirmation, suppression de cette instance de la liste des membres : self.biblio.membres
        -   Pour finir, Un message indiquant la suppression du membre est affiché.
        ATTENTION : Comme il ne faut pas de "trou" dans les numéros d'id ex : 1, 2, 3, 5, 6, 7 (manque 4)
        Au sein d'une itération dans la liste des membres, il y a décrémentation tous les id qui sont supérieurs à celui du membre supprimé...
        """
        print("\n" * 100)   # Vide l'affichage du terminal par 100 lignes vides

        # **************************************************
        #   A COMPLETER (à la place de la ligne suivante !)
        print(f"\t{Ihm.ROUGE}A coder...{Ihm.NO_COLOR}")
        # *************************************************

        input(f"\n\t\t{Ihm.CYAN}Appuyer sur Entrée pour continuer...{Ihm.NO_COLOR}") # attend que 'Return' soit enfoncé
        self.choix = 0      # on revient au menu d'accueil...

    def __affiche_select_membres(self, texte = None):
        """
        Si 'texte' est égale à None, la liste des membres est affichée. C'est tout !!!
        Si 'texte' contient une string non vide, la méthode effectue :
            -   l'affichage de la liste des membres.
            -   une demande de choix d'un numéro d'id avec la méthode : self.__attendre_choix_ligne()
            -   le numéro d'index du membre choisi dans la liste des membres est retourné...
        """
        print(f"\n{'-' * 20} Membres {'-' * 20}")
        for membre in self.biblio.membres:
            print(membre)
        print()
        if texte:
            self.__attendre_choix_ligne(range(1,1+len(self.biblio.membres)), f"\t{Ihm.ROUGE}-->{Ihm.NO_COLOR} {texte} {Ihm.VERT}(numéro){Ihm.NO_COLOR} : ")
            return self.choix - 1

    def __affiche_select_auteurs(self, texte):
        """
        Si 'texte' est égale à None, la liste des auteurs est affichée. C'est tout !!!
        Si 'texte' contient une string non vide, la méthode effectue :
            -   l'affichage de la liste des auteurs.
            -   une demande de choix d'un numéro d'id avec la méthode : self.__attendre_choix_ligne()
            -   le numéro d'index de l'auteur choisi dans la liste des auteurs est retourné...
        """
        print(f"\n{'-' * 20} Auteurs {'-' * 20}")
        for auteur in self.biblio.auteurs:
            print(auteur)
        print()
        if texte:
            self.__attendre_choix_ligne(range(1, 1 + len(self.biblio.auteurs)),f"\t{Ihm.ROUGE}-->{Ihm.NO_COLOR} {texte} {Ihm.VERT}(numéro){Ihm.NO_COLOR} : ")
            return self.choix - 1

    def __affiche_select_livres(self, texte):
        """
        Si 'texte' est égale à None, la liste des livres est affichée. C'est tout !!!
        Si 'texte' contient une string non vide, la méthode effectue :
            -   l'affichage de la liste des livres.
            -   une demande de choix d'un numéro d'id avec la méthode : self.__attendre_choix_ligne()
            -   le numéro d'index du livre choisi dans la liste des livres est retourné...
        """
        print(f"\n{'-' * 20} Livres {'-' * 20}")
        for livre in self.biblio.livres:
            print(livre)
        print()
        if texte:
            self.__attendre_choix_ligne(range(1,1+len(self.biblio.livres)), f"\t{Ihm.ROUGE}-->{Ihm.NO_COLOR} {texte} {Ihm.VERT}(numéro){Ihm.NO_COLOR} : ")
            return self.choix - 1

    def __affiche_emprunts(self, index_membre):
        """
        Affiche la liste des emprunts d'un membre
        :Argument index_membre : Index du membre dans la liste des membres.
        """
        membre = self.biblio.membres[index_membre]
        if membre.livres_empruntes:
            print(f"{Ihm.ROUGE}\t----> {Ihm.VERT}{membre.prenom} {membre.nom}{Ihm.NO_COLOR} a emprunté les livres suivants :")
            for livre in membre.livres_empruntes:
                print(f"{Ihm.BLEU}\t\t- {livre.id}.\t{Ihm.MAGENTA}{livre.titre} de {livre.auteur.prenom} {livre.auteur.nom}{Ihm.NO_COLOR}")
        else:
            print(f"\t{Ihm.ROUGE}----> {Ihm.NO_COLOR}{membre.prenom} {membre.nom} {Ihm.ROUGE}n'a aucun livre emprunté{Ihm.NO_COLOR}.")

    def __attendre_choix_ligne(self, liste_choix_possibles, texte):
        """
        Attend en boucle une réponse valide de l'utilisateur.
        :Argument liste_choix_possible: Est une liste ou un range qui contient les valeurs des choix de réponses possibles de l'utilisateur.
                                        Exemples : range(1,10) ou [1, 2, 3, 4, 5, 6, 7] ou aussi [3, 7]
        :Argument texte: Texte affiché pour commenter la nature de la saisie.
        :retour: True si choix valide, False sinon.
        """
        while True:
            try:
                self.choix = int(input(texte))
                if self.choix in liste_choix_possibles:
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f"\t{Ihm.ROUGE}************ Erreur : choix invalide...{Ihm.NO_COLOR}")

    @staticmethod
    def __verifie_date(valeur_date):
        """
        Cette méthode teste si une string est une date valide.
        Retour: - None si elle n'est pas valide
                - la date avec une correction du format si elle est valide
        """
        try:
            date_valide = datetime.strptime(valeur_date, "%d/%m/%Y").date().strftime("%d/%m/%Y")
            return date_valide
        except ValueError:
            return None
