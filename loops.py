'''
fruits = ["apple", "orange", "olive"]

for fruit in fruits:
    print("Eat an {}".format(fruit))

for number in range(3, 12):
    if number == 6:
        print("Skip 6")
        continue
    print("Number {}".format(number))

temp = 43

while temp > 32:
    print("Water is still OK: {}".format(temp))
    temp -= 2
'''

for number in range(1, 14):
    if number == 13:
        print("13!")
        pass
    else:
        print("Number {}".format(number))
