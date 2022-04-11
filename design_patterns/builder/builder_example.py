class Person:
    def __init__(self):
        self.name = None
        self.age = None

    def __str__(self):
        return f"A person with name {self.name} and age {self.age}"


class PersonBuilder:

    def __init__(self,
                 person=None):  # Beware of http://www.omahapython.org/IdiomaticPython.html#default-parameter-values
        self.person = person or Person()

    def set_name(self, name):
        self.person.name = name
        return self

    def set_age(self, age):
        self.person.age = age
        return self

    def build(self):
        return self.person


if __name__ == "__main__":
    personBuilderA = PersonBuilder()
    personaA = personBuilderA.set_name("person_a").set_age(40).build()
    personBuilderB = PersonBuilder()
    personB = personBuilderB.set_name("person_b").set_age(30).build()
    print(personaA)
    print(personB)
