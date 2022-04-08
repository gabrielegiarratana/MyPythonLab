class Person:
    def __init__(self):
        self.name = None
        self.age = None

    def __str__(self):
        return f"A person with name {self.name} and age {self.age}"


class PersonBuilder:

    def __init__(self, person=Person()):
        self.person = person

    def set_name(self, name):
        self.person.name = name
        return self

    def set_age(self, age):
        self.person.age = age
        return self

    def build(self):
        return self.person


if __name__ == "__main__":
    pb = PersonBuilder()
    person = pb.set_name("gabriele").set_age(41).build()
    print(person)
