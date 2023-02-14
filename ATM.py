import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int, input().split()))

answer = []
arr.sort()

total = 0
for i in arr:
  total += i
  answer.append(total)

print(sum(answer))

