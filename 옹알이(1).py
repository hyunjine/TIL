def solution(babbling):
    answer = 0
    for word in babbling:
        start = 0        
        while True:
            can = ["aya", "ye", "woo", "ma"]
            include = False
            while can:
                a = can.pop()
                l = len(a)
                if a == word[start:start+l]:
                    start += l
                    include = True
                    break
            if not include:
                break
        if start == len(word):
            answer += 1
    return answer