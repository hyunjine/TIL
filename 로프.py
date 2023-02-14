import sys
input = sys.stdin.readline
# n = int(input())
# arr = [int(input()) for _ in range(n)]

arr = [3,3,3,10]
n = len(arr)
arr.sort(reverse=True)
weight = 0
for i in range(0, n):
  next = arr[i]*(i+1)
  if weight < next:
    weight = next
print(weight)