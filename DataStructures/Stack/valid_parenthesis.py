from stack import*


# VERIFY EQUATION IS CORRECTLY PARENTHESIZED
s2 = Stack()
equation = "(((8+3)+(4-3)))"
underflow = False

for i in equation:
    if i == "(":
        s2.push("(")
    elif i == ")":
        underflow = s2.is_empty()
        s2.pop()

if s2.is_empty() and not underflow:
    print("correct")
else:
    print("FALSE")