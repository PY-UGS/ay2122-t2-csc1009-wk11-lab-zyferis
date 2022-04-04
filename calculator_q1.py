class Calculator:

    def __init__(self):
        self.input1 = float(input("Enter float input 1 : "))
        self.input2 = float(input("Enter float input 2 : "))

    def adder(self):
        return self.input2 + self.input1

    def subtractor(self):
        return self.input1 - self.input2

    def multiplier(self):
        return self.input1 * self.input2

    def divider(self):
        return self.input1 / self.input2

    def clear(self):
        self.input1 = self.input2 = 0
        print("After clear, input1: " , self.input1 ," input2:",  self.input2)


result = Calculator()
print("Adding input1 and input2: ", result.adder())
print("Subtracting input1 with input2: ",result.subtractor())
print("Mutitplying input1 with input2: ", result.multiplier())
print ("Dividing input1 with input2: ",result.divider())

result.clear()

