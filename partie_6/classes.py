class Cybertruck:
    marque = "Tesla"
    modele = "Cybertruck"
    annee = 2023

    def klaxonner(self):
        print("Tut tut !")


class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def klaxonner(self):
        print("Tut tut !")


cybertruck = Cybertruck()

corolla = Voiture(marque="Toyota", modele="Corolla", annee=2022)

Voiture.klaxonner(corolla)
