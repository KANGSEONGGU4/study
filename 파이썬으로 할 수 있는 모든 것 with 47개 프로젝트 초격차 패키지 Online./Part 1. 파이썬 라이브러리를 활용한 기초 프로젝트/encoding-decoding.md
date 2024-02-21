<img width="597" alt="image" src="https://github.com/KANGSEONGGU4/study/assets/132239219/f138c06c-c90a-4525-b728-c208a9dd2c4c">   


>  ## 인코딩 (Encoding)
> 
>  - 인코딩 = 코드화 = 암호화 = 부호화
>  - '컴퓨터에서 인코딩은 동영상이나 문자 인코딩 뿐 아니라 사람이 인지할 수 있는 형태의 데이터를 약속된 규칙에 의해 컴퓨터가 사용하는 0과 1로 변환하는 과정을 통틀어 말합니다'
>  - 'ASCII','URL인코딩','HTML인코딩','Base64인코딩','유니코드인코딩' 등이 존재

  		# 문자열 (사람이 이해할 수 있는 형식)
  		a = "Life is too shot"
  		type(a)

str

    # utf-8 인코딩 (가장 많이 사용되는 유니코드 인코딩)
    b = a.encode('utf-8')
    type(b)

bytes


    print(b)

b'Life is too short'   

    # 한글 인코딩 예시
    a = '한글'
    a.encode('utf-8')

b'\xed\x95\x9c\xea\xb8\x80'
