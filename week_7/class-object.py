# How to create a class
# To avoid repetiton
# Modularize
# Functions

class Parent:
    def __init__(self, firstname, lastname, age, country, qlf, city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.qlf = qlf
        self.skills = []
        self.hobbies = []

    def get_person_info(self):
        full_name = self.firstname + ' ' + self.lastname
        return f'{full_name} is {self.age}. He lives in {self.city}, {self.country}. He is a {self.qlf} degree holder. He has {len(self.skills)} skills.'

    def get_person_skills(self):
        return self.skills

    def add_skill(self, skill):
        self.skills.append(skill)

    def get_person_hobbies(self):
        return self.hobbies

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)


# Instantiating

p1 = Parent('Asab', 'Yeta', 250, 'Finland', 'MSC')
p2 = Parent('Lidiya', 'Tekl', 28, 'Finland', 'Bsc', 'Espoo')

print(p1.firstname)
print(p1.lastname)


print(p2.firstname)
print(p2.lastname)

p2.add_skill('Python')
p2.add_skill('Flask')
p2.add_skill('Django')
print(p2.get_person_skills())
print(p2.get_person_info())

skills = ['HTML', 'CSS', 'Sass', 'JS', 'React', 'Redux', 'Node', 'Python']

for skill in skills:
    p1.add_skill(skill)

print(p1.get_person_info())


class Child(Parent):
    def __init__(self, firstname, lastname, age, country, qlf, gender, city='Helsinki'):
        super().__init__(firstname, lastname, age, country, qlf, city)
        self.gender = gender

    def get_person_info(self):
        gender = 'He' if self.gender.lower() == 'male' else 'She'
        full_name = self.firstname + ' ' + self.lastname
        return f'{full_name} is {self.age}. {gender} lives in {self.city}, {self.country}. {gender} is a {self.qlf} degree holder. {gender} has {len(self.skills)} skills.'


c1 = Child('Antti', 'Nurminen', 28, 'Finland', 'BSc','Male')
c2 = Child('Joohana', 'Nurminen', 24, 'Finland', 'BSc', 'Female')
print(c1.get_person_info())
print(c2.get_person_info())

