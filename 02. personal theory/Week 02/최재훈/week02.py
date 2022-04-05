def solution(n):
    answer = []
    matrix = [[0 for i in range(n)] for j in range(n)]
    # 초깃값 설정
    for a in range(n):
        matrix[a][0] = a+1
        
        if a==n-1:
            for last_com in range(1, n):
                matrix[a][last_com] = a+1+last_com
    
    print(matrix)

    return answer

print(solution(5))