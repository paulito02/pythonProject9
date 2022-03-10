# ceating a dice game

from random import randrange
for i in range(0, 3):   # roll the die three times
    value = randrange(1, 6)  # generate random number in the range 1....6
   # show the die
print("+-------+")
if value == 1:
        print("|       |")
        print("|   *   |")
        print("|       |")
elif value == 2:
        print("| *     |")
        print("|       |")
        print("|     * |")
elif value == 3:
        print("|     * |")
        print("|   *   |")
        print("| *     |")
elif value == 4:
        print("| *   * |")
        print("|       |")
        print("| *   * |")
elif value == 5:
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
elif value == 6:
        print("| * * * |")
        print("| * * * |")
        print("| * * * |")
else:
        print(" *** error: illegal die value ***")
print("+-------+")