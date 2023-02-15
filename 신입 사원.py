import sys
rl = sys.stdin.readline
def solution(arr):
  n = len(arr)
  if n < 3: return n
  answer = 0
  dic = {}
  for a in arr: dic[a[0]] = a
  min = int(1e9)
  for i in range(1, n+1):
    item = dic[i][1]
    dic[i] = (dic[i], min)
    if item < min: 
      answer += 1
      min = item
  return answer
n = int(rl())
arr = []
for _ in ' '*n:
  arr.append([list(map(int, rl().split())) for i in range(int(rl()))])
for i in range(n):
  answer = solution(arr[i])
  print(answer)