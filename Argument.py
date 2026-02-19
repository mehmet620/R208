import sys

if len(sys.argv) < 2:
    print(f"aucun argument apresle nom du script {sys.argv[0]}")

else:
    for arg in sys.argv:
        print(f'/t--> {arg}')