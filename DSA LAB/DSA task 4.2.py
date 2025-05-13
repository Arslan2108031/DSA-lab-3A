class PostfixEvaluator:
    def __init__(self):
        self.stack = []

    def evaluate(self, expression):

        tokens = expression.split()
        
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }

        for token in tokens:
            if token.isdigit():
                self.stack.append(int(token))
            elif token in operators: 
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                result = operators[token](operand1, operand2)
                self.stack.append(result)

        return self.stack[-1]

expression = "5 1 2 + 4 * + 3 -"
evaluator = PostfixEvaluator()
result = evaluator.evaluate(expression)
print("Result:", result)
