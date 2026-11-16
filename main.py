import tkinter as tk
import random
from sauvegarde import Sauvegarde

nombre_secret = random.randint(1, 100)

def verifier():

    try:

        nombre = int(entree.get())

        if nombre == nombre_secret:

            s = Sauvegarde()
            s.sauvegarder(1)

            resultat.config(text="Bravo ! Tu as trouvé.")

        elif nombre < nombre_secret:

            resultat.config(text="Trop petit !")

        else:

            resultat.config(text="Trop grand !")

    except:

        resultat.config(text="Entre un nombre valide")

fenetre = tk.Tk()
fenetre.title("Devine le nombre")
fenetre.geometry("400x300")

titre = tk.Label(
    fenetre,
    text="DEVINE LE NOMBRE",
    font=("Arial", 16)
)
titre.pack(pady=10)

instruction = tk.Label(
    fenetre,
    text="Trouve le nombre entre 1 et 100"
)
instruction.pack()

entree = tk.Entry(fenetre)
entree.pack(pady=10)

bouton = tk.Button(
    fenetre,
    text="Valider",
    command=verifier
)
bouton.pack(pady=10)

resultat = tk.Label(
    fenetre,
    text=""
)
resultat.pack(pady=10)

fenetre.mainloop()