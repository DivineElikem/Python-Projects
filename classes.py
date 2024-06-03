class Person:
    fname = ""
    lname = ""
    def __init__(self, age ) -> None:
        self.page = age


p1 = Person(age=23)
p1.fname = "Divine"

p2 = Person(age=21)
p2.lname = "Acquah"

Person.fname = "Elikem"
Person.lname = "Ackah"

print(p1.fname, p1.lname, p1.page)