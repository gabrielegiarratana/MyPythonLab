class Peso:
    def __init__(self, gr):
        self._kg = gr / 1000

    def _get_gr(self):  # metodo protetto, da non usare all'esterno
        return self._kg * 1000

    def _set_gr(self, gr):  # metodo protetto, da non usare all'esterno
        if gr >= 0:
            self._kg = gr / 1000
        else:
            self._kg = 0

    gr = property(
        _get_gr, _set_gr
    )  # definisce gr come una property e vengono passati setter e getter


class PesoConDecoratore:
    def __init__(self, gr):
        self._kg = gr / 1000

    @property
    def gr(self):  # è il nome visibile dall'esterno
        return self._kg * 1000

    @gr.setter
    def gr(self, gr):  # metodo protetto, da non usare all'esterno
        # nb il metodo getter e setter hanno lo stesso nome in questo caso
        if gr >= 0:
            self._kg = gr / 1000
        else:
            self._kg = 0


if __name__ == "__main__":
    print("senza decoratore")
    p = Peso(1200)
    print(p.gr)
    p.gr = 1600
    print(p.gr)

    print("con decoratore")
    p = PesoConDecoratore(1200)
    print(p.gr)
    p.gr = 1600
    print(p.gr)
