#입력
N, K = map(int, input().split())
josephus = [i for i in range(1, N + 1)]
result = []
temp = K - 1


for i in range(N):
    if len(josephus) > temp: #위치가 리스트를 넘지 않은 경우
        result.append(josephus.pop(temp)) #답 추가
        temp += K - 1 #다음 위치로 이동
        
    elif len(josephus) <= temp: #위치가 리스트를 넘은 경우
        temp = temp % len(josephus)
        result.append(josephus.pop(temp))
        temp += K - 1

#출력
print("<", end='')
for i in result:
    if i == result[-1]:
        print(i, end = '')
    else:
        print("%s, " %(i), end='')
print(">")