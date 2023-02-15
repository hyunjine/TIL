s = input()
answer = [0, 0]
for i in s.split('1'):
  if i: answer[0] += 1
for i in s.split('0'):
  if i: answer[1] += 1
min(answer)