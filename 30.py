from sys import stdin as s
import time


def solution(n,start):
  n.sort(reverse = True)
  s = sum(n)
  if s % 3 == 0 and n[-1] == 0:
    for i in n:
      print(i, end="")
    print("")
  else:
    print(-1)
  print("Spend Time:", time.time() - start)

n = list(s.readline().rstrip())
print(n)
# n = list(map(int, s.readline().rstrip()))
# start = time.time()
# solution(n,start)