class PlayerCharacterr:
    # Class Object Attribute
    membership = True

    def __init__(self, name="Anonymous", age=0):
        if age > 18:
            self.name = name  # attributes
            self.age = 25

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name} and my age is {self.age}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things1(num1, num2):
        return num1 + num2


player1 = PlayerCharacterr('Arfiz')
player1.attack = 12
player1.adding_things(2, 5)

player1.run()
print(player1.attack)
# help(player1)
