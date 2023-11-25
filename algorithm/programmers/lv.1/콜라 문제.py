#https://school.programmers.co.kr/learn/courses/30/lessons/132267
def solution(a, b, n):
    count = 0
    empty = n
    
    while empty // a > 0  :
        count += empty // a *b
        empty = (empty //a) * b + (empty % a)
    
    return count
