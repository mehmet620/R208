import sys

if len(sys.argv) < 2:
    print(f"aucun argument apresle nom du script {sys.argv[0]}")

else:
    print("solution N°1 :")
    for arg in sys.argv:
        print(f'/t--> {arg}')

    print("\nsolution N°2 :")
    for index in range(len(sys.argv)):
        print(f'\t--> {sys.argv[index]}')

    print("\nsolution N°3 :")
    for index, arg in enumerate(sys.argv):
        print(f'\t--> {arg}')
        print(f'\t--> {sys.argv[index]}')

