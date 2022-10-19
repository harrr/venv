def addition():
    a = int(input("Enter a number "))
    b = int(input("Enter b number "))
    print(a + b)

def user_info(name, age = 19, city="Helsinki"):
    '''
    :param name:
    :param age:
    :param city:
    :return:
    '''
    print("{} is {} years old, from {}".format(name, age, city))

user_info("Abigale", 42, "Malmo")
user_info("Finn", 14)
user_info("Jane")
user_info(city="NY", name="Anet")