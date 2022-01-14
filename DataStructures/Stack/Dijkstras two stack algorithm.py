from stack import *

equation = "(5+((2/4)*(2+3)))"
operandStack = Stack()
operatorStack = Stack()

for i in equation:
    if i.isdigit():
        operandStack.push(int(i))
    if i in("+", "-", "*", "/"):
        operatorStack.push(i)
    if i == ")":
        operator = operatorStack.peek()
        operatorStack.pop()
        operand_1 = operandStack.peek()
        operandStack.pop()
        operand_2 = operandStack.peek()
        operandStack.pop()
        if operator == "+":
            operandStack.push(operand_2 + operand_1)
        if operator == "-":
            operandStack.push(operand_2 - operand_1)
        if operator == "*":
            operandStack.push(operand_2 * operand_1)
        if operator == "/":
            operandStack.push(operand_2 / operand_1)
result = operandStack.peek()
print(result)

