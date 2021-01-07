from sys import stdin
num = int(stdin.readline())

stack = []
number = []

q = input()

for i in range(num):
    o = int(input())
    number.append(o)


for c in q:
    if c == '+':
        one = stack.pop() #A = 65
        
        two = stack.pop()
        
        result = one + two
        stack.append(result)
    elif c == '-':
        one = stack.pop() #A = 65
        
        two = stack.pop()
        
        result = two - one
        stack.append(result)
    elif c == '*':
        one = stack.pop() #A = 65
        
        two = stack.pop()
        
        result = one * two
        stack.append(result)
    elif c == '/':
        one = stack.pop() #A = 65
        
        two = stack.pop()
        
        result = two / one
        stack.append(result)
    
    else:
        stack.append(number[ord(c)-65])

print('%.2f' % stack.pop())











