from sys import stdin

def solution(n):
  answer = ""
  table = [10, 1*60, 5*60] # 10, 60, 300
  if n % 10 != 0: return -1
  answer += str(n // table[2]) + " "
  n %= table[2]
  answer += str(n // table[1]) + " "
  n %= table[1]
  answer += str(n // table[0])
  return answer

read = stdin.readline
# n = int(read())
n = 100
answer = solution(n)
print(answer)