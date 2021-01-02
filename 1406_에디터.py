import sys

str_ = []
str2_ = []

str_ = list(sys.stdin.readline()[:-1])


num = int(input())

for i in range(num):
    cmd = input()
    if cmd[0] == 'P':
        str_.append(cmd[2])    
    elif cmd[0] == 'L' and str_:
        str2_.append(str_.pop())
    elif cmd[0] == 'D' and str2_:
        str_.append(str2_.pop())
    elif cmd[0] == 'B' and str_:
        str_.pop()

sys.stdout.write(''.join(str_ + str2_[::-1]))



## 시간복잡도 출처 https://bnzn2426.tistory.com/112