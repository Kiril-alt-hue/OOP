class RationalValueError(Exception):
    def __init__(self, operand1, operand2, operation, message="Непідтримуваний тип операнда для операції"):
        super().__init__()
        self.message = message
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation

    def __str__(self):
        return f"{self.message}, {self.operation=}, {type(self.operand1)=}, {type(self.operand2)=}"