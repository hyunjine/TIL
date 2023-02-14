import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse = True)

answer = 0
for i in range(n):
  ae = a[i]
  be = b[i]
  answer += ae * be

print(answer)