import sys
from heapq import heappush
from heapq import heappop

input = sys.stdin.readline
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
n = 11
arr = [
  [1, 4],
  [3, 5],
  [0, 6],
  [3, 8],
  [5, 7],
  [5, 9],
  [6, 10],
  [8, 11],
  [8, 12],
  [2, 13],
  [12, 14]  
]

heap = []
for a in arr:
  heappush(heap, (a[1], a))

table = [-1, -1]
v = 0
while heap:
  a = heappop(heap)[1]
  if table[1] <= a[0]:
    table[1] = a[1]
    v += 1

print(v)
    
  
