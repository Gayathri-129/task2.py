class Calculator:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        print(self.x+self.y)
    def subtract(self):
        print(self.y-self.x)
    def multiply(self):
        print(self.x*self.y)
    def divide(self):
        print(self.y/self.x)

obj = Calculator(10, 94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()