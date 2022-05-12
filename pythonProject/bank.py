class person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("이름 :",self.name)

class client(person):
    def __init__(self, name, age, gender, asset):
        super().__init__(name,age,gender)
        self.asset = asset

    def showasset(self):
        print("자산 :",self.asset)

    def receive(self, owner, money):
        self.owner = owner
        owner.asset = owner.asset - money
        self.asset = self.asset + money


class clerk(person):
    def __init__(self, name, age, gender, bank):
        super().__init__(name,age,gender)
        self.bank = bank

class child(person):
    def __init__(self, name, age, gender, preschool):
        super().__init__(name,age,gender)
        self.preschool = preschool

