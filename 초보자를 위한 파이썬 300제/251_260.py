#251. 클래스, 객체, 인스턴스
# 1. 클래스 : 틀, 객체를 만들기위한 변수와 메서드의 집합
# 2. 매서드 : 클래스 안에서 구현되는 함수
# 3. 인스턴스 : 클래스의 객체가 소프트웨어에서 실체화 되면
# 먼말이지..

#252. 빈 클래스 생성
# class Human:
#     pass

#253. 클래스의 인스턴스 생성 후 변수에 바인딩
# class Human:
#     pass
# areum = Human()

#254. class 내 출력문 추가
# 만약 함수로 한다면 print("응애응애")
# 클래스는 기본적으로 아래와 같이 이용한다
# 클래스 내에 정의된 함수들을 메소드라고 한다.
# __init__은 반드시 첫 번째 인수로 self를 지정해야함
# class Human:
#     def __init__(self):
#         print("응애응애")
# areum = Human()

#255. class에 생성자 추가하기
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
# areum = Human("정재현",25,"남")
# print(areum.name)
# print(areum.age) - 256. 인스턴스 속성에 접근

#257. 이름 성별 출력하는 who() 메소드 추가
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def who(self):
#         print(self.name, self.age, self.sex)
#
# areum = Human("이민형", 23, "남")
# areum.who() # Human.who(areum)과 같은표현이다.

#258. 받는 setinfo 메소드 추가
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def who(self):
#         print(self.name, self.age, self.sex)
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# areum = Human("모름", 26, "모름")
# Human.who(areum)
#
# areum.setInfo("민지", 27, "여자") # 이게뭐지..
# Human.who(areum)

#259. class 소멸 될 때
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def who(self):
#         print(self.name, self.age, self.sex)
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def __del__(self):
#         print("나의 죽음을 적에게 알리지 마라")
#
# areum = Human("아름이", 26, "여자")
# del(areum)

#260
class OMG :
    def print() :
        print("Oh my god")

mystock = OMG()
OMG.print()
#파라미터 없이 호출해야대는데 파라미터 있이? 했다던데 아니 어디에있다는거지;
#  아마 print에 self가 없어서 mystock.print()가 안되는듯 OMG.print(mystock)과 같으니