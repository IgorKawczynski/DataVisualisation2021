# GRA PAPIER-KAMIEN-NOZYCE-STWORZONA OBIEKTOWO

class Gracze:

    def __init__(self, gracz1, gracz2, wybor):
        self.gracz1 = gracz1
        self.gracz2 = gracz2
        self.wybor = wybor


class Gra:

    def __init__(self, nowagra):
        self.nowagra = nowagra


class Punktacja:

    def __init__(self, runda, ktowygral):
        self.runda = runda
        self.ktowygral = ktowygral