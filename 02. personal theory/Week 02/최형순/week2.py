def solution(n):
    answer = []
    tmp = [[0 for x in range(n)] for y in range(n)]
    
    cnt = n
    sum = 1
    x, y = -1, 0
    while cnt != 0:
        for k in range(cnt):
            x += 1
            tmp[x][y] = sum
            sum += 1
        cnt -= 1
        if cnt == 0:
            break
        for k in range(cnt):
            y += 1
            tmp[x][y] = sum
            sum += 1
        cnt -= 1
        if cnt == 0:
            break
        for k in range(cnt):            
            x -= 1
            y -= 1
            tmp[x][y] = sum
            sum += 1
        cnt -=1
        
        
    for x in tmp:
        for y in x:
            if y != 0:
                answer.append(y)
    return answer

print(solution(4))