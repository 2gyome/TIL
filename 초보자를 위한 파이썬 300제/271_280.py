#271.Account 클래스 구현
#272. 생성 갯수
#273. 클래스 변수 출력
#274. 입금 매서드
#275. 출금 매서드
#276. 정보 출력 메서드
#277. 이자 지급하기
#278. 여러 객체 생및 생성된 인스턴스를 리스트에 저장
import random

class Account:
    #class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0,999999)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1
    def get_account_num(cls): #여기에 cls가 왜 있는거지..
        print(cls.account_count)   # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance *= 1.01
            self.deposit_log.append(amount)

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            self.withdraw_log.append(amount)
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance) # 아니 이거 끝에서 3 번째 , 찍는거 안찍어놓고선 나보곤 찍으라그러네;

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)

p = Account("파이썬", 10000)
p.display_info()
# print("#272")
# kim = Account("김민수", 100)
# print(Account.account_count)
# lee = Account("이민수", 100)
# print(Account.account_count)

# print("#273")
# kim = Account("김민수", 100)
# lee = Account("이민수", 100)
# kim.get_account_num()
#
# print("#274")
# k = Account("kim", 100)
# k.deposit(100)
# k.withdraw(90)
# print(k.balance)

print("#278.")
data = []
k = Account("KIM", 10000000)
l = Account("LEE", 10000)
p = Account("PARK", 10000)

data.append(k)
data.append(l)
data.append(p)

print(data)

print("#279.")
for i in data:
    if i.balance >= 1000000:
        Account.display_info(i) #클래스 내 정의되어있는 매서드에 출력 있음으로 따로 Print 없어도 됨

print("#280.")
k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()

