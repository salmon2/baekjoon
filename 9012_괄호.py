stack = []
str_ = []

num = int(input())
for i in range(num):
    result = 0
    stack.clear()
    str_= input()
    for c in str_:
        if c == '(':
            stack.append(c)
        elif c== ')':
            if not stack:
                result = 1
            else:
                stack.pop()
    if result == 1 or stack:
        print('NO')
    else:
        print('YES')


    
    
