def solution(num, total):
    answer = [1001] * num
    a = total // num
    if num % 2 != 0:
        c = num // 2
        answer[c] = a
        for i in range(1, c+1):
            answer[c+i] = a+i
            answer[c-i] = a-i
    else:
        c = num // 2
        if a * num < total:
            c -= 1
        answer[c] = a
        for i in range(1, c+1):
            print(a, i)
            answer[c+i] = a+i
            answer[c-i] = a-i
        if answer[-1] == 1001:
            answer[-1] = answer[-2] + 1
        else:
            answer[0] = answer[1] - 1
    return answer