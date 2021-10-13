class Shoes(object):
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    def __str__(self):
        return f"brand: {self._brand}, model: {self._model}"

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model


class RunningShoes(Shoes):
    def __init__(self, brand, model, category):
        super().__init__(brand, model)
        self._category = category

    def __str__(self):
        return f"brand: {super().brand}, model: {super().model}, category: {self._category}"


if __name__ == "__main__":
    s = Shoes("D&J", "luxury")
    print(s)
    sc = RunningShoes("Brooks", "Adrenaline", "A3")
    print(sc)
