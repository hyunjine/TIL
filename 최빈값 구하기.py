def solution(array):
    answer = 0
    arr = list(set(array))
    
    dic = {}
    max = 0
    for i in arr:
        m = array.count(i)
        if max < m:
            max = m
        try: dic[m].append(i)
        except: dic[m] = [i]
    

    if len(dic[max]) > 1:
        return -1
    return dic[max][0]