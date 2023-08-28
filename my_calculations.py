#msg="roll a dice"
#print(msg, "Hello, World! testinggggg")


class Calculations:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_sum(self):
        return self.a + self.b
    
    def get_sum(self):
        return self.a +  self.c

    def get_difference(self):
        return self.a - self.b

    def get_product(self):
        return self.a * self.b

    def get_quotient(self):
        return self.a / self.b