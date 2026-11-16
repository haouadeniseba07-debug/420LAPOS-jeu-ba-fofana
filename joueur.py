class Joueur:

    def __init__(self, nom):
        self.nom = nom


class JoueurHumain(Joueur):

    def __init__(self, nom):
        super().__init__(nom)


class JoueurAutomatique(Joueur):

    def __init__(self, nom):
        super().__init__(nom)