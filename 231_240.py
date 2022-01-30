#231.
# def n_plus_1 (n) :
#     result = n + 1
#
# n_plus_1(3)
# print (result)
# 함수 내부에서 사용한 변수는 외부에서 접근 불가능함

#232.
def make_url(string):
    return f"www.{string}.com" #    url = "www." + string + ".com"
result = make_url("naver")
print(result)

#233.
def make_list(string):
    result = []
    for s in string:
        result.append(s)
    return result
list_string = make_list("abcd")
print(list_string)

#문자열 list로 변형
#def make_list (string) :
    # return list(string)

#234
def pickup_even(pickup):
    result = []
    for i in pickup:
        if i % 2 == 0:
            result.append(i)
    return result

pickup_even([3, 4, 5, 6, 7, 8])

#235. String 으로 받아 정수로 반환하는
def convert_int(hi):
    return int(hi.replace(',',''))
convert_int("1,234,567")

#236. 반환 후 바인딩
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

#237. 중첩된 함수 -> 안쪽에서부터 시작
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

#238,
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

#239.
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

#240.
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
