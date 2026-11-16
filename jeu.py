import random
from sauvegarde import Sauvegarde

class Jeu:

    def __init__(self):

        self.nombre_secret = random.randint(1, 100)

        self.sauvegarde = Sauvegarde()

    def jouer(self):

        trouve = False

        print("=== DEVINE LE NOMBRE ===")

        while not trouve:

            nombre = int(input("Entre ton nombre : "))

            if nombre == self.nombre_secret:

                print("Bravo ! Tu as trouvé.")
                trouve = True

            elif nombre < self.nombre_secret:

                print("Trop petit !")

            else:

                print("Trop grand !")