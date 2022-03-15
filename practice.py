# oop
class PlayerCharacter:
    #     class object attribute

    def __init__(self, name, age):

        self.name = name
        if (age > 18):
            self.age = age
        else:
            print("not up to age")

    def run(self):
        print(f'my name is {self.name}')


print("             player 1")
player1 = PlayerCharacter(input('name: '), int(input('age: ')))

print("             player 2")
player2 = PlayerCharacter(input('name: '), int(input('age: ')))






















