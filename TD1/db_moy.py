import sys
from pathlib import Path

if len(sys.argv) < 5:
    print("Erreur : il faut au minimum 4 arguments après le nom du script.")
    print("Syntaxe : python db_moy.py fichier.txt NOM Prenom note1 [note2] [note3] ...")
    sys.exit()

nom_fichier = sys.argv[1]
f_path = Path(nom_fichier)

nom = sys.argv[2].upper()
prenom = sys.argv[3].capitalize()
notes = sys.argv[4:]

try:
    for note in notes:
        total += float(note)
    moyenne = total / len(notes)

with open(f_path, mode='a', newline='') as file:
    file.writelines(f"{nom}, {prenom}, {round(moyenne, 1)}\n")

