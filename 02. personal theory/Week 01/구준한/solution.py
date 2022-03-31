def solution(progresses, speeds):
  # 살짝 무지성 버전

    answer = []

    p = progresses
    s = speeds
    c = 0

    while (len(p) != 0):
      for i in range(len(p)):
        p[i] += s[i]
        
      c = 0
      if p[0] >= 100:
        c += 1
        p.pop(0)
        s.pop(0)

        if len(p) != 0:
          for i in range(len(p)):
            if p[i] >= 100:
              c += 1
            else:
              break

          if c > 1:
            del p[:c-1]
            del s[:c-1]

      if c > 0:
        answer.append(c)

    return answer
