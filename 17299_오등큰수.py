from sys import stdin
result = []
stack = []
F = []

num = int(stdin.readline())
nums = stdin.readline().split()


for i in range(num):
    nums[i] = int(nums[i]) 
    result.append(-1) 
F = [0 for _ in range(1000002)]

for i in range(num):
    F[nums[i]] = F[nums[i]] + 1


for i in range(num):
    while stack and F[nums[i]] > F[nums[stack[-1]]]:
        result[stack[-1]] = nums[i]
        stack.pop()
    stack.append(i)


for i in range(num):
    print(result[i], end = ' ')
    
