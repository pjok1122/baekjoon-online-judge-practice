def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0
    deleted = 1

    while(deleted):
        deleted = 0
        #제거 대상 블록을 찾고 소문자로 변경하는 로직
        for i in range(len(board)-1):
            for j in range(len(board[0])-1):
                # 4개가 쌓였을 경우.
                current = board[i][j].upper()
                if current!='.' and current == board[i][j+1].upper() == board[i+1][j].upper() == board[i+1][j+1].upper():
                    deleted = 1
                    for k in range(2):
                        for l in range(2):
                            if (board[i+k][j+l].isupper()):
                                answer+=1
                                board[i+k][j+l] = board[i+k][j+l].lower()

        #제거된 블록을 제거(.으로 교체)하고 위에 있는 블록을 아래로 내리는 로직
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j].islower()):
                    for k in range(i,0,-1):
                        board[k][j] = board[k-1][j]
                    board[0][j] = '.'


    return answer

# print(solution(4,5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6,6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
# print(solution(2,2, ["AA", "AA"]))
# print(solution(3,2, ["AA", "AA", "BA"]))
# print(solution(2,2, ["AA", "AB"]))
# print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"]))  #대표 반례 - 닶 : 12
# print(solution(6,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]))  #대표 반례 - 닶 : 8

