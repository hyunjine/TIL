def solution(common):
    answer = 0
    a = common[0]
    b = common[1]
    c = b - a
    if common[2] == common[1] + c:
        return common[-1] + c
    else:
        c = b // a
        return common[-1] * c