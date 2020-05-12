class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    # def attack(self):
    #     print('do nothing')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        # User.attack(self)
        print(f'attacking with arrow: arrows with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = Wizard('Arfiz', 50, 'arfiz@gmail.com')

# introspection
print(dir(wizard1))
archer1 = Archer('Robin', 100)
# wizard1.attack()
# archer1.attack()

# print(isinstance(wizard1, User))


# def player_attack(char):
#     char.attack()


# for char in [wizard1, archer1]:
#     char.attack()


# player_attack(wizard1)
# player_attack(archer1)
