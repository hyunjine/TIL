import math

def solution(dots):
    sx = []
    sy = []
    for i in dots:
        sx.append(i[0])
        sy.append(i[1])
    sx = sorted(sx)
    sy = sorted(sy)
    answer = (sx[-1] - sx[0]) * (sy[-1] - sy[0])
    return answer