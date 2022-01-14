from stack import*

# REVERSE A STRING
s = Stack()
string = "the coder school"

for i in string:
    s.push(i)
for i in range(len(string)):
    print(s.peek(), end="")
    s.pop()
print()