import sys

def solution(n, target):
  answer = 1
  while target > n:
    if str(target)[-1] == '1':
      target = int(str(target)[:-1])
    elif target % 2 == 0:
      target = target // 2
    else:
      break
    answer += 1 
  return answer if target == n else -1

rl = sys.stdin.readline
# n, target = map(int, rl().split())
n, target = 2, 162
answer = solution(n, target)
print(answer)