#281 클래스 정의

class 차:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
car = 차(2, 1000)
print(car.wheel)
print(car.price)


#282. #283 차 클래스를 상속받은 자전거 클래스 정의
class 자전차(차):
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

bicycle = 자전차(2, 100)
print(bicycle.wheel)

#284.클래스 상속