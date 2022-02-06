#31. 문자열 합치기
a = "3"
b = "4"
print(a + b)

#32. 문자열 곱하기
print("hi"*3)

#33.
print('-'*80)

#34.
t1 = "python"
t2 = "java"
t = t1 +' ' + t2 + ' '
print(t * 4)

#35. % formatting 사용
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : %s 나이: %d" % (name1, age1))
print("이름 : %s 나이 : %d" % (name2, age2))

#36..format 메서드
print("이름 : {} 나이 : {}".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2))

#37.f string
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")

#38.컴마 제거하기
상장주식주 = "5,979,782,550"
print(int(상장주식주.replace(',','')))

#39. 문자열 슬라이싱
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])

#40. strip 매서드
data = "     삼성전자     "
print(data.strip())