from sys import stdin

def solution(n, dis, price):
  answer = 0
  start = 0
  while start < n:
    answer += dis[start] * price[start]
    next = start+1
    totalDis = 0
    while next < n and price[start] < price[next]:
      totalDis += dis[next]
      next += 1
    answer += totalDis * price[start]
    start = next
  return answer

read = stdin.readline
n = int(read())
dis = list(map(int, read().split()))
dis += [0]
price = list(map(int, read().split()))
answer = solution(n, dis, price)
print(answer)