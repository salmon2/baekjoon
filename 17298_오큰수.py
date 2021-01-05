result = []
stack = []

num = int(input())
nums = input().split(' ')

for i in range(num):
    nums[i] = int(nums[i]) 
    result.append(-1) 

for i in range(num):
    while stack and nums[i] > nums[stack[-1]]:
        result[stack[-1]] = nums[i]
        stack.pop()
    stack.append(i)

for i in range(num):
    print(result[i], end = ' ')
    

