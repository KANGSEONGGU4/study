#https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    
    result = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result.add(numbers[i] + numbers[j])
    
    answer = sorted(list(result))
    return answer
