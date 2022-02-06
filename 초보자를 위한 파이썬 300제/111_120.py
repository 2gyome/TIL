#111. 사용자로부터 입력받은 문자열 두 번 출력하기
#T = input()
# print(2 * T)

#112. 입력받은 숫자에 10 더해 출력하기
# print("숫자를 입력하세요:", end=" ")
# T = int(input())
# print(T + 10)

#113. 짝수 홀수 판별하기
# T = int(input())
# if T % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

#114. 받은 값에 20 더한 값 출력하기. 255 초과시 255 출력
# print("입력값 : ", end=" ")
# T = int(input())
# add_T = T + 20
# if add_T > 255:
#     print(255)
# else:
#     print(add_T)

#115. 입력 받은 후 20 뺀 값 출력. 0 보다 작으면 0 출력 255보다 크면 255 출력
# print("입력값 :", end=" ")
# user = int(input())
# num = user - 20
# if num < 0:
#     print(0)
# elif num > 255:
#     print(255)
# else:
#     print(num)

#116. 정각인지 판별하기
# print("현재시간:", end="")
# user =  input()
# if user[-2:] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")

#117. 특정 문자가 포함되어있는지 확인하기
# fruit = ["사과", "포도", "홍시"]
# print("what is your favourtie fruit?", end=" ")
# user = input()
# if user in fruit:
#     print("correct")
# else :
#     print("wrong")

#118.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# user = input("종목망: ")
# if user in warn_investment_list:
#     print("yes")
# else :
#     print("no")

#119.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("제가좋아하는계절은: ")
# if user in fruit:
#     print("yes")
# else:
#     print("no")

#120.
user = input("좋아하는과일은: ")
if user in fruit.values():
    print("yes")
else:
    print("no")