class ZeroDivisonDenominatorError(Exception):
    def __init__(self, numerator, denominator, message = "Знаменник не може бути нулем"):
        super().__init__()
        self.message = message
        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        return f"{self.message = }, {self.numerator = }, {self.denominator = }"