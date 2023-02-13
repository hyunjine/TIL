def solution(id_pw, db):
    answer = ''
    arr = [i for i in db if i[0] == id_pw[0]]
    if not arr:
        return "fail"
    arr2 = [i for i in arr if i[1] == id_pw[1]]
    if not arr2:
        return "wrong pw"
    return "login"