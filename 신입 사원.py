import sys
from heapq import heappush, heappop, heapify

def solution(l, arr):
  answer = 0
  if l <= 2: return answer if l == 1 else sum(arr)
  heapify(arr)
  while len(arr) > 1:
    s = heappop(arr)+heappop(arr)
    answer += s
    heappush(arr, s)
  return answer

rl = sys.stdin.readline
n = int(rl())
arr = [int(rl()) for _ in range(n)]
answer = solution(n, arr)
print(answer)