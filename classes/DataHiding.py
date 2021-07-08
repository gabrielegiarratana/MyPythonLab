class Esempio:
    def __init__(self):
            self.nome = "nome attributo senza underscore"
            self._nome = "nome attributo con singolo underscore"
            self.__nome = "nome attributo con doppio underscore" #name mangling


if __name__ == "__main__":

    istanza = Esempio()

    print(istanza.nome) #attributo pubblico
    print(istanza._nome) #posso accedere ma non dovrei

    # print(istanza.__nome) #non posso accedere perchè il nome è storpiato (name mangling)

    #per accedere all'attributo devo scriverlo in modo differente:
    print(istanza._Esempio__nome)