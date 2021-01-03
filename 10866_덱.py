from sys import stdin
q = []
f = []
for i in range(int(stdin.readline())):
    cmd = stdin.readline().split(' ')
    if cmd[0][-1] == '\n':
        cmd[0] = cmd[0][0:-1]

    if cmd[0] == 'push_back':
        q.append(int(cmd[1][:-1]))
    elif cmd[0] == 'push_front':
        q.insert(0,cmd[1][:-1])
    elif cmd[0] == 'pop_front':
        if q:
            print(q[0])
            del q[0]
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if q:
            print(q[-1])
            del q[-1]
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)