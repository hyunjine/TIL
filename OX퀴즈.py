def solution(quiz):
    express = []
    answer = []
    for i in quiz:
        a = i.index("=")
        arr1 = i[:a-1].split(' ')
        arr2 = i[a+2:].split(' ')
        arr1[1] += "1"
        c = int(arr1[1]) * int(arr1[2])
        d = int(arr1[0]) + c
        e = "X" if d != int(arr2[0]) else "O"
        answer.append(e)
        
    return answer