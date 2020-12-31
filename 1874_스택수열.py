stack = []
out = []
count = 1
isnot = False

num = int(input())
for i in range(num):
    s = int(input())
    while count <= s:
        stack.append(count)
        out.append('+')
        count = count + 1
    pop = stack.pop()
    out.append('-')
    if pop != s:
        isnot = True
        break

if isnot:
    print('NO')
else:
    print(out)
            