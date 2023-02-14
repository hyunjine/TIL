import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
answer = 0
while arr:
  p = arr.pop()
  answer += k // p
  k %= p
print(answer)