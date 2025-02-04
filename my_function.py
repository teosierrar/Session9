def greet():
    """
    :return:
    """
    print("Hello!")

greet()
greet()


def greet2(name):
    print(f"Hello {name}")

    greet2("James")
    greet2("Bob")

def average(a,b):
        """
        Average the two numbers
        :param a: first number
        :param b: second number
        :return: float, average of a and b
        """
        average = (a+b)/2
        return average

print(average(10,20))

def divide(x,y=2):
    """
    Divide x by y
    :param x: first number
    :param y: second number
    :return: float, the division result
    """
    if y==0:
        return None
    return x/y

print(divide(10,20))
print(divide(10,0))
print(divide(10,1))
print(divide(1,10))
print(divide(30))

def bond(first_name="James", last_name="Bond"):
    print(f"{last_name}, {first_name} {last_name}")

def introduce(name):
    print(f"The name is: {name}")

print(bond("James", "Smith"))
introduce(bond("James", "Bond"))