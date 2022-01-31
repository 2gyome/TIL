#281 클래스 정의

class 차:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
    def get_info(self):
        print(f"바퀴 {self.wheel}")
        print(f"가격 {self.price}")

car = 차(2, 1000)
print(car.wheel)
print(car.price)


#282. #283 차 클래스를 상속받은 자전거 클래스 정의
class 자전차(차):
    def __init__(self, wheel, price, 구동계):
        super().__init__(wheel, price)
        self.구동계 = 구동계
    def get_info(self):
        super().get_info()
        print(f"구동계 {self.구동계}")

# bicycle = 자전차(2, 100)
# print(bicycle.wheel)

#284.클래스 상속
# bicycle = 자전차(2, 100, "시마노")
# print(bicycle.구동계)

#285. 정보 얻는 매소드 추가
# car = 차(4,1000)
# car.get_info()

#286. 부모클래스 생성자 호출 #287. 부모클래스 매서드 호출
bicycle = 자전차(2, 100, "시마노")
bicycle.get_info()

#288.매서드 오버라이팅
class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")

나 = 자식()
나.호출()# 자식호출
나 = 부모()
나.호출() # 부모호출

#289.
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
나 = 자식() # 자식생성
나 = 부모() # 부모생성


#290.
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식() # 자식생성 부모생성
나 = 부모() # 부모생성
