def add(*args):
    result = 0
    for x in args: result += x
    return result

print(add(1,2,3,6,5,8))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["k"]
    n *= kwargs["g"]
    print(n)

calculate(3, k=2, g=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.mode = kw["model"]

my_car = Car(make="Nissan", model="Fir")
print(my_car.mode)