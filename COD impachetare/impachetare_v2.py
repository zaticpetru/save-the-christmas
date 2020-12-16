class copil:
    def __init__(self, UUID, name, age, gender, favorite_color, Country, City, street, number, cadouri=None):
        self.UUID = UUID
        self.name = name
        self.age = age
        self.gender = gender
        self.favorite_color = favorite_color
        self.adresa = adresa(Country, City, street, number)
        self.cadouri = cadouri
    def impachetare(self):
        for i in self.cadouri:
            setattr(i, "ambalaj", self.favorite_color)
        delattr(self, "favorite_color")

class adresa:
    def __init__(self, Country, City, street, number):
        self.Country = Country
        self.City = City
        self.street = street
        self.number = number

class cadou:
    def __init__(self, obiect, cantitate, adjective, UID):
        self.obiect = obiect
        self.cantitate = cantitate
        self.adjective = adjective
        self.UID = UID

# f = copil("123", "John", "12", "boy", "Red", "Romania", "Bucuresti", "Mihai Viteazu", "54", [cadou("Masina", "1", "Albastra", "1234"), cadou("Telefon", "1", "Negru", "1235")])
# g = copil("223", "Ion", "14", "boy", "Black", "Moldova", "Chisinau", "Stefan Cel Mare", "12", [cadou("Phone", "1", "Ros", "3235")])
# print(g.favorite_color)
# f.impachetare()
# g.impachetare()
# print(g.cadouri[0].ambalaj)
# print(g.cadouri)
