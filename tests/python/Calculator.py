class Calculator:
    def __init__(self):
        self.result = 0

    def enter(self, number):
        self.result = number

    def add(self):
        self.result += self.result

    def result(self):
        return self.result

def test_calculator(calculator):
    calculator = Calculator()
    return calculator
