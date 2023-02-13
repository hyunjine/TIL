from collections import deque

def solution(score):
    result = [0] * len(score)
    answer = {}
    for i,v in enumerate(score):
        try: answer[sum(v)].append(i)
        except: answer[sum(v)] = [i]
    arr = sorted(answer.keys())
    count = 1
    while arr:
        temp = count
        for i in answer[arr.pop()]:
            result[i] = temp
            count += 1

    return result