def DFS(numbers, depth, current_sum, target):
    
    if(depth < len(numbers) - 1):
        DFS(numbers, depth+1, current_sum + numbers[depth+1], target)
        DFS(numbers, depth+1, current_sum - numbers[depth+1], target)

    if(depth == len(numbers)-1 and current_sum == target):
        global answer
        answer = answer + 1

def solution(numbers, target):
    global answer
    answer = 0
    DFS(numbers, -1, 0, target)

    print(answer)



solution([1,1,1,1,1], 3)