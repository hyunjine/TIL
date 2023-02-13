def solution(board):
    answer = 0
    l = len(board)
    dx = (-1, 1, 0, 0, 1, 1, -1, -1)
    dy = (0, 0, -1, 1, -1, 1, 1, -1)
    dn = len(dx)
    for i in range(l):
        for j in range(l):
            if board[i][j] == 1:
                for k in range(dn):
                    rx = i + dx[k]
                    ry = j + dy[k]
                    if rx >= 0 and rx < l and ry >= 0 and ry < l:
                        if board[rx][ry] != 1: 
                            board[rx][ry] = 2
                        
    for i in range(l):
        for j in range(l):
            if board[i][j] == 0:
                answer += 1
    
    return answer