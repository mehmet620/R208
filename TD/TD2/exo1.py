import random

liste= []
for index in range(10):
    liste.append(random.randint(1,100))
print(liste)
while True:
    try:
        index=int(input("veuillez saisir un index :"))
        print(liste[index])
    except IndexError:
        print(f"error:l'index {index} n'est pas dans la liste([{-len(liste)};{len(liste)-1})")
    except ValueError:
        print(f"ERREUR :La valeur saisie doit etre un nombre !")