> ## 클로저 (Closure)
> - 함수 안의 함수를 결과로 반환할 때, 그 내부 함수를 '클로저(Closure)' 라고 합니다.
> - 사용되는 곳
>   - 콜백(Callback) 함수에 사용
>   - 함수의 순차적 실행
>   - 데코레이터 함수

<br>

### 1.클래스(Class) 사용하기

    class Mul:
    def __init__(self, m):
        self.m = m

    def mul(self, n):
        return self.m * n

    if __name__ == "__main__":
        mul3 = Mul(3)
        mul5 = Mul(5)

        print(mul3.mul(10)) 
        print(mul5.mul(10)) 

30   
50  

<br>

### 2.클로저(Closure) 사용하기

    def mul(m):           # 외부 함수
        def wrapper(n):   # 내부 함수 (클로저)
            return m * n
        return wrapper

    if __name__ == "__main__":
        mul3 = mul(3)    # m = 3 인 wrapper 함수가 mul3 에 저장 
        mul5 = mul(5)    # m = 5 인 wrapper 함수가 mul5 에 저장

        print(mul3(10))  # m = 3, n = 10 인 wrapper 함수가 실행
        print(mul5(10))  # m = 5, n = 10 인 wrapper 함수가 실행

30   
50 

<br>

> ## 데코레이터 (Decorator)
> - 'decorate'는 '꾸미다, 장식하다'라는 뜻으로 함수를 꾸며주는 함수.
> - 함수를 인수로 받는 클로저
> - @를 이용한 어노테이션으로 사용
> - 사용되는 곳
>   - 반복되는 작업을 여러 함수에 적용할 경우
>   - 기존 함수를 수정하지 않고 추가 기능을 구현하고 싶을 경우

    import time

    def func1(a, b):
        start = time.time()
        print("함수가 실행됩니다.")
    
        val = a + b
    
        end = time.time()
        print("함수 수행시간: %f 초" % (end-start))
    
        return val

    if __name__ == "__main__":
        result = func1(1, 2)
        print(result)

함수가 실행됩니다.   
함수 수행시간: 0.000791 초   
3   

    def func2(a, b):
        start = time.time()
        print("함수가 실행됩니다.")
    
        val = a * b
    
        end = time.time()
        print("함수 수행시간: %f 초" % (end-start))
    
        return val

    if __name__ == "__main__":
        result = func2(1, 2)
        print(result)

함수가 실행됩니다.   
함수 수행시간: 0.001003 초   
2   

### 데코레이터 만들기

~~~
def func1(a, b):
    val = a + b   
    return val

def func2(a, b):
    val = a * b   
    return val
~~~

    
