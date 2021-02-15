'''
class MyClassWithPropertyDecorator:

    def __init__(self, val):
        self.value = val

    @property
    def value(self):
        print("getter")
        return self.value

    @value.setter
    def value(self, new_val):
        print("setter")
        if new_val > 100:
            self.value = 100
        else:
            self.value = new_val

obj = MyClassWithPropertyDecorator(5)
print(obj.value)
print(obj.value)
obj.value = 500

print(obj._value)
'''


# When I removed "_" it is showing error and setter goes in loop
# I haven't kept the getter module name and object name identical and it worked.

class MyClassWithPropertyDecorator:

    def __init__(self, val):
        self.value = val

    @property
    def val(self):
        print("getter")
        return self.value

    @val.setter
    def val(self, new_val):
        print("setter")
        if new_val > 100:
            self.value = 100
        else:
            self.value = new_val


obj1 = MyClassWithPropertyDecorator(5)

print(obj1.value)

obj1.val = 500
print(obj1.value)
