import sys
import csv
import json
from pathlib import Path

def main():

    try:
        file_arg = sys.argv[1]
        option = sys.argv[2]
        ip_to_search = sys.argv[3]
    except IndexError:
        print("Erreur : nombre d'arguments incorrect.")
        print("Syntaxe : python ip_log.py nom_fichier.csv -ip adresse_ip")
        return

    try:
        if option != "-ip":
            raise ValueError("Le second argument doit être '-ip'.")
    except ValueError as e:
        print("Erreur :", e)
        return

    file_path = Path(file_arg)

    if not file_path.exists() or not file_path.is_file():
        print(f"Erreur : le fichier '{file_path}' n'existe pas.")
        return

    count = 0
    try:
        with file_path.open("r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # sauter l'en-tête
            for row in reader:
                if row and row[0] == ip_to_search:
                    count += 1
    except Exception as e:
        print("Erreur lors de la lecture du fichier CSV :", e)
        return

    print(f"Nombre d’occurrences de l’adresse IP {ip_to_search} : {count}")

    json_path = Path("historique_ip.json")

    if json_path.exists():
        try:
            with json_path.open("r", encoding="utf-8") as jf:
                historique = json.load(jf)
        except json.JSONDecodeError:
            historique = []
    else:
        historique = []

    historique.append({ip_to_search: count})

    try:
        with json_path.open("w", encoding="utf-8") as jf:
            json.dump(historique, jf, indent=4)
    except Exception as e:
        print("Erreur lors de l’écriture du fichier JSON :", e)

if __name__ == "__main__":
    main()
