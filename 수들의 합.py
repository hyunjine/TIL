import sys
input = sys.stdin.readline
# n = int(input())

n = 200
sum = 0
answer = 0
for i in range(1, n+1):
  sum += i
  if n in range(sum, sum+i+1):
    answer = i
    break
print(answer)