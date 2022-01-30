#261. stock 클래스 생성
#262. 종목명, 종목코드 받도록 생성자 정의
#263. 종목명 입력할 수 있는 매서드 추가
#264. 종목코드 입력할 수 있는 매서드 추가
#265 종목명과 종목코드를 리턴하는 get_name, get_code 메서드 추가
#266. 개체 속성 값 업데이트
#267. 객체 생성
#268.객체 속성 수정
#269.객체 속성 수정
#270. 여러 종류 객체 생성
class Stock:
    def __init__(self, name, code, PER, PBR, 배당수익률):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.배당수익률 = 배당수익률
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def set_per(self,PER):
        self.PER = PER
    def set_PBR(self, PBR):
        self.PBR = PBR
    def set_dividend(self, dividend):
        self.배당수익률 = dividend


# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name, 삼성.code)
# a = Stock(None, None)
# a.set_name("삼성전자") # Stock.set_name(a,"삼성전자) 와 동일
# print(a.name, a.code)
#
# a.set_code("005930")
# print(a.name, a.code)
# Stock.set_code(a,"0058930")
# print(a.name, a.code)
#
# print("#265")
# print(삼성.get_name(), 삼성.get_code())
# print(Stock.get_name(삼성), Stock.get_code(삼성))

print("#266")
삼성 = Stock("삼성전자","005930",15.79, 1.33, 2.83)
print(삼성.name, 삼성.code, 삼성.PER, 삼성.PBR, 삼성.배당수익률)

print("#269")
삼성.set_per(12.75)
print(삼성.PER)
s
print("#270")
종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)