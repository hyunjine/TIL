def solution(a, b):
    m = min(a,b)
    for i in range(m, 0, -1):
        if a % i == 0 and b % i == 0:
            m = i
            break
    b //= m
    idx = 2
    while idx <= b:
        if b % idx == 0:
            if idx not in [2,5]:
                return 2
            b //= idx
        else:
            idx += 1
    
    return 1