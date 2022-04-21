def solution(s):
    answer = True
    chk = []
    
    for i in s:
      if i == "(":
        chk.append(i)

      else:
        # 비어 있으면
        if not chk:
          answer = False
          break
        # 비어있지 않으면
        else:
          chk.pop()

  # 리스트가 비어 있는지 확인
    if chk:
      answer = False

    return answer