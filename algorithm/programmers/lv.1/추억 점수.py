# https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        count = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                b = name.index(photo[i][j])
                count += yearning[b]
            else:
                continue
        answer.append(count)
    return answer
