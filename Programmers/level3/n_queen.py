answer = 0

def solution(n):
    col_visited = [0]*n
    left_cross_visited = [0]*(2*n)
    right_cross_visited = [0]*(2*n)
    for i in range(n):
        visited(col_visited, left_cross_visited, right_cross_visited, 0, i, 1)
        dfs(1, col_visited, left_cross_visited, right_cross_visited)
        visited(col_visited, left_cross_visited, right_cross_visited, 0, i, 0)

    return answer        

def visited(col, left, right, depth, index, value):
    col[index] = value
    left[depth+index] = value
    right[depth + len(col) - index - 1] = value

def is_visited(col, left, right, depth, i):
    
    if col[i] or left[depth+i] or right[depth + len(col) - i - 1]:
        return True
    else:
        return False

def dfs(depth, col, left_cross, right_cross):

    if depth == len(col):
        global answer
        answer+=1
        return None

    else:
        # 각 자리에 놓아본다.
        for i in range(len(col)):
            if not is_visited(col, left_cross, right_cross, depth, i):
                 visited(col, left_cross, right_cross, depth, i, 1)
                 dfs(depth+1, col, left_cross, right_cross)
                 visited(col, left_cross, right_cross, depth, i, 0)

                 
print(solution(5))
