import sys
input = sys.stdin.readline
n = int(input().rstrip())

c = -1
for b in range(int(n/3)+1):
  isOut = False
  for a in range(int(n/5)+1):
    if (5*a)+(3*b) == n:
      c = a+b
      isOut = True
      break
  if isOut: break

print(c)