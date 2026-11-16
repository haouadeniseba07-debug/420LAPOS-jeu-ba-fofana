import json

class Sauvegarde:

    def sauvegarder(self, score):

        with open("score.json", "w") as fichier:
            json.dump({"score": score}, fichier)