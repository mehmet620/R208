import sys
from pathlib import Path

if len(sys.argv) < 5:
    print("Erreur : il faut au minimum 4 arguments après le nom du script.")
    print("Syntaxe : python db_moy.py fichier.txt NOM Prenom note1 [note2] [note3] ...")
    sys.exit(1)

f_path = Path(sys.argv[1]).resolve()

nom = sys.argv[2].upper()
prenom = sys.argv[3].capitalize()

notes_str = sys.argv[4:]
notes = []

try:
    for n in notes_str:
        notes.append(float(n))
except ValueError:
    print("Erreur : toutes les notes doivent être des nombres.")
    sys.exit(1)

moyenne = sum(notes) / len(notes)

with open(f_path, mode='a', newline='') as file:
    file.writelines(f"{nom}, {prenom}, {round(moyenne, 1)}\n")

print(f"La moyenne de {prenom} {nom} a été mise dans {str(f_path)}")
