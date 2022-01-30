#211.
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")

#212.
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)

#213. - 요구하는 argument가 없으면 에러 뜸
# def 함수(문자열) :
#     print(문자열)
# 함수()

#214
# def 함수(a, b) :
#     print(a + b)
#
# 함수("안녕", 3)

#215. 216.
def print_with_smile(문자열):
    print(f"{문자열}:D")
print_with_smile("하이루~~")


#217.
def print_upper_price(price):
    print(price*1.3)

#218.
def print_sum(a,b):
    print(a+b)

#219.
def print_arithmetic_operation(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
print_arithmetic_operation(3,4)

#220.
def print_max(a, b, c):
    result = a
    if result < b:
        result = b
    if result < c:
        result = c
    print(result)

print_max(1, 562,24563467)