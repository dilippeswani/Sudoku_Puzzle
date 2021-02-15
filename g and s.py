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

# print(dilip.value)
# print(dilip.value)
# dilip.vue = 500æ
#æ
# print(dilip.value)