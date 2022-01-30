#121. 문자.islower 문자.isupper --> true false 반환
user = input()
if user == user.upper():
    print(user.lower())
else :
    print(user.upper())

#122.
user = int(input("score: "))
print("grade is ", end="")
if user >= 81:
    print("A")
elif user >= 61:
    print("B")
elif user >= 41:
    print("C")
elif user >= 21:
    print("D")
else:
    print("E")

#123.
currency = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
user = input("입력: ")
user_list = user.split()
print("{}원".format(float(user_list[0])*currency[user_list[1]]))

#124.
number = []
for _ in range(3):
    number.append(int(input()))
print(max(number))
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >=num1 and num2 >= num3:
    print(num2)
else:
    print(num3)

#125.
telecom = {"011":"SKT", "016":"KT", "019":"LGU", "010":"unknown"}
user = input("휴대전화 번호 입력: ")
print("당신은 {} 사용자입니다.".format(telecom[user.split("-")[0]]))

# 126, ==> 틀림
우편번호 = input("우편번호 : ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")

#127.
주민번호 = input("주민번호 :")
if 주민번호[8] in ["1","3"]:
    print("Namja")
else:
    print("yeoja")

#128.
주민번호 = input("주민번호 :")
뒷자리 = 주민번호.split("-")[1]
if int(뒷자리[1:3]) <= 8:
    print("seoul")
else:
    print("not seoul")


#129.
verification = [2, 3, 4, 5, 6, 7, 0,8, 9, 2, 3, 4, 5]
주민번호 = input("주민번호: ")
total = 0
for i in range(13):
    if i == 6:
        continue
    else:
        print(i)
        total += int(주민번호[i]) * verification[i]
if 주민번호[-1] == (11 - total % 11):
    print("유효한 주민번호")
else:
    print("거짓 주민번호")

#130. float으로 해야댐
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
print(btc)
if int(btc['max_price']) < int(btc['opening_price']) + int(btc['max_price']) - int(btc['min_price']):
    print("상승장")
else:
    print("하락장")