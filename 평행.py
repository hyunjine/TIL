def solution(dots):
    answer = []
    l = len(dots)
    for i in range(l):
        j = i + 1
        while j < l:
            a = dots[i]
            b = dots[j]
            ax = dots[j][0] - dots[i][0]
            ay = dots[j][1] - dots[i][1]
            answer.append(ax / ay)
            j += 1
    a = len(set(answer))
    print(answer, a)
    if a < len(answer): return 1
    else: return 0

    return answer