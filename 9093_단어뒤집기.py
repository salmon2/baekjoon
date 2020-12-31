num = int(input())
for i in range(num):
    stack = []
    result = ''
    line = input()
    for c in line:
        if c == ' ':
            while stack:
                result = result + stack.pop()
            result = result + ' '
        else:
            stack.append(c)
    while stack:
        result = result + stack.pop()
    print(result)