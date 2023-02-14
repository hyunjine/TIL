import sys
input = sys.stdin.readline
price = int(input())
answer = 0

price = 1000 - price
rest = [500,100,50,10,5,1]
for r in rest:
  answer += price // r
  price %= r

print(answer)