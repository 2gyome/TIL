#71. 비어있는 튜플
my_variable = ()
print(type(my_variable))

#72.
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

#73. 숫자만 있는 튜플은 int
print(type((1))) # int
print(type(1,)) # int

#74. 오류 찾기 -- 튜플은 원소값 변경 불가능함
t = (1, 2, 3)
print(t[0])

#75. 괄호 없어도 튜플로 저장 가능
t = 1, 2, 3, 4, 5
print(type(t))

#76.
t = ('a', 'b', 'c')
t = ('A', 'B', 'C')
print(t)

#77. 튜플을 리스트로 변환
interest = ('삼성전자', 'LG전자', 'Hyundai')
print(type(tuple(interest)))


#78. 리스트를 튜플로 변환
interest = ['삼성전자', 'LG전자', 'Hyundai']
print(type(list(interest)))

#79.튜플 언패킹
temp = ('apple', 'banana', 'cake')
a,b,c = temp
print(a, b, c)

#80. range 함수
even = [i for i in range(2,99,2)]
data = tuple(range(2,100,2))
print(tuple(even))
print(data)