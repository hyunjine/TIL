def carculate(arr, x1, x2):
    if len(arr) > 0:
        m1 = max(x1)
        m2 = max(x2)
        if m1 < m2: arr.add(m1 + 1)
        else: arr.add(m2 + 1)
def get_len(arr):
    return 0 if len(arr) == 0 else max(arr) - min(arr)
            
def solution(lines):
    answer = 0
    a1 = set(list(range(lines[0][0], lines[0][1])))
    a2 = set(list(range(lines[1][0], lines[1][1])))
    a3 = set(list(range(lines[2][0], lines[2][1])))
    b1 = a1 & a2
    b2 = a1 & a3
    b3 = a2 & a3
    carculate(b1, a1, a2)
    carculate(b2, a1, a3)
    carculate(b3, a2, a3)
    answer += get_len(b1)
    answer += get_len(b2)
    answer += get_len(b3)
    answer -= get_len(b1 & b2 & b3) * 2
    return answer