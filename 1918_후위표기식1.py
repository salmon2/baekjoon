
stack = []
stack2 = []
number = []

q = input()
sen = []
sen.append('(')

for c in q:
    if c == '+' or c == '-' or c == '*' or c =='/':
        sen.append(')')
        sen.append(c)
        sen.append('(')
    else:
        sen.append(c)
sen.append(')')

print(sen)

for c in q:
    if c == '(' or c == '+' or c == '*' or c == '/' or c == '-':
        stack2.append(c)
    elif c == ')':
        while True:
            a = stack2.pop()
            if a == '(':
                break
            else:
                stack.append(a)
    else:
        stack.append(c)

while stack2:
    stack.append(stack2.pop())
    
for c in stack:
    print(c)









