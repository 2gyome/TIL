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

#235.
def convert_int(number):
    
convert_int("1,234,567")