#221.
def print_reverse(string):
    print(string[::-1])
print_reverse("안녕하세욥")

#222.
def print_score(score_list):
    print(sum(score_list)/len(score_list))
print_score([1,2,3])

#223.
def print_even(one_list):
    for i in range(len(one_list)):
        if one_list[i] % 2 == 0:
            print(one_list[i])
print_even([1, 3, 2, 10, 12, 11, 15])

#224. 딕셔너리에서 키 값만 출력하기
def print_keys(one_dict):
    for key in one_dict:
        print(key)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

#225.
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dict, value):
    print(dict[value])
print_value_by_key(my_dict, "10/26")


#226. --> 틀ㄹ림
def print_5xn(string):
    length = len(string)
    cycle = length // 5
    mod = length % 5
    for i in range(1,cycle+1):
        print(string[5*(i-1):5*i])
    if mod != 0:
        print(string[cycle*5:])

print_5xn("아이엠어보이유알어걸Tlqkadsfasdfasdfasdfasdfasdfaft")

#227, ==> 틀림
def printmxn(string, n):
    length = len(string)
    cycle = len(string) // n
    mod = len(string) % n
    for i in range(cycle):
        print(string[5*(i-1):i*5])
    if mod != 0:
        print(string[-mod::])

printmxn("아이엠어보이유알어걸", 3)

# 정답
# def print_mxn(line, num):
#     chunk_num = int(len(line) / num)
#     for x in range(chunk_num + 1) :
#         print(line[x * num: x * num + num])


#228.12월나누고 1원 미만 버림 계산만 하면 됨
def calc_monthly_salary(salary):
    monthly_pay = int(salary/12)
    return monthly_pay
calc_monthly_salary(12000000)

#229. 바인딩을 명시적으로 표현하기
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)


#230. 바인딩 되어있기때문에 순서상관없다.
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)
