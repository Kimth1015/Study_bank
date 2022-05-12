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
        self.__asset = asset

    def showasset(self):
        print("자산 :",self.__asset)

    def receive(self, owner, money):
        if type(owner) == client:
            self.owner = owner
            owner.__asset = owner.__asset - money
            self.__asset = self.__asset + money
        else:
            raise ValueError("Go away")


class clerk(person):
    def __init__(self, name, age, gender, bank):
        super().__init__(name,age,gender)
        self.bank = bank

class child(person):
    def __init__(self, name, age, gender, preschool):
        super().__init__(name,age,gender)
        self.preschool = preschool


mike = client('mike',29,'male',10000000)
matini = client('matini',32,'male',10000000)
nick = child('nick',5,'male',10000000)

mike.receive(nick,1000000)
mike.showasset()