def solution(n):
    answer = []
    row, col = -1, 0
    data = 1
    matrix = [ [0 for j in range(1, i+1)] for i in range(1, n+1)]

    for direction in range(n):
        for check in range(direction, n):
            if direction%3 == 0:#Column Side
                row += 1
            elif direction%3 == 1:#Row Side
                col += 1
            else:#Diagonal Side
                row-=1
                col-=1
            matrix[row][col] = data
            data += 1
            
    for element in matrix:
        answer+=element
    
    return answer

print("n = 4 :", solution(4))
print("n = 5 :", solution(5))
print("n = 6 :", solution(6))
