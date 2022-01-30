#201. 202
def print_coin():
    print("bitcoin")
print_coin()

#203.
for _ in range(10):
    print_coin()

#204.
print("-" *100)
def print_coin2():
    for _ in range(10):
        print("bitcoin")
print_coin2()

#205. 정의되기 전에 함수 호출하면 에러 뜬다.

#206.
def message() :
    print("A")
    print("B")

message()
print("C")
message()

#207. -- 이따구로 작성하면 알아보기 힘들다
print("A")

def message() :
    print("B")

print("C")

#208, -- 이따구로 작성하면 알아보기 힘들다
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

#209.
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

#210.
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()