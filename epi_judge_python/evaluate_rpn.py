from test_framework import generic_test

'''
https://en.wikipedia.org/wiki/Reverse_Polish_notation

The following algorithm evaluates postfix expressions using a stack, with the expression processed from left to right:

for each token in the postfix expression:
  if token is an operator:
    operand_2 ← pop from the stack
    operand_1 ← pop from the stack
    result ← evaluate token with operand_1 and operand_2
    push result back onto the stack
  else if token is an operand:
    push token onto the stack
result ← pop from the stack

'''
def evaluate(expression):
    results = []
    for token in expression.split(','):
        if token in ['+', '-', '*', '/']:
            y = results.pop()
            x = results.pop()
            if token == '+':
                results.append(x + y)
            elif token == '-':
                results.append(x - y)
            elif token == '*':
                results.append(x * y)
            else:
                results.append(int(x / y))
        else:
            results.append(int(token))

    return results.pop()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
