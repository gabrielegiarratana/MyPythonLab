class Persona():
    def __init__(self, nome, cognome, sesso="m"):
        self.name = nome
        self.surname = cognome
        self.gender = sesso

# metodo d'istanza
    def introduce(self):
        print(f"I'm {self}")
    def changeSex(self, new_gender):
        self.gender = new_gender



class SquadraCalcio:
        n_squadre = 0 #attributo di classe

        def __init__(self, nome, città, num_giocatori = 22):
            self.nome = nome #attributo d'istanza
            self.città = città
            self.num_giocatori = num_giocatori
            SquadraCalcio.n_squadre += 1

        @classmethod
        def squadre_attive(cls): #definisce un metodo di classe. uso 'cls' al posto di 'self'
            print(f"Ci sono {cls.n_squadre} attive")

        @staticmethod
        def campionato():
            print("Serie A")

        def __str__(self):
            return f"{self.nome}"

        def __repr__(self):
            return f"SquadraCalcio('{self.nome}','{self.città}',{self.num_giocatori})"


if __name__ == "__main__":
    p1 = Persona("Marco", "Rossi")
    print(p1.name)
    print(p1.surname)
    print(p1.gender)
    p1.introduce()
    p1.changeSex("f")
    print(p1.gender)

    s1 = SquadraCalcio("Inter", "Milano")
    s2 = SquadraCalcio("Milan", "Milano")

    SquadraCalcio.squadre_attive()
    SquadraCalcio.campionato()


    print(s1) #usa il dunder method __str__ Se __str__ non fosse dichiarato, nella print verrebbe usato __srepr__
    print(repr(s1))



