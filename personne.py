# -- definition ==
class Personne:
    def __init__(self,nom = "", age = 0):
        self.nom = nom
        self.age = age

#        print("constructeur personne " + nom)
    def Se_Presenter(self):
        if self.nom == "":
            nom = input("merci de saisir votre nom: ")
            self.nom = nom
        info_personne = "bonjour je m'appelle " + self.nom
        if self.age == 0:
            print(info_personne)
        if self.age > 0:
            info_personne += " et j'ai " + str(self.age) + " ans"
            print(info_personne)
            if self.Est_Majeur():
                print("je suis majeur")
            else:
                print("je suis mineur")

    def Est_Majeur(self):
        return self.age >= 18


# -- utilisation --

personne1 = Personne("André", 30)
personne2 = Personne("Philippe", 12)
personne3 = Personne()
personne1.Se_Presenter()
personne2.Se_Presenter()
personne3.Se_Presenter()
