#241. ==> 툴림
import datetime

now = datetime.datetime.now()
print(now)

#242.
print(type(now))

#243. date time 날ㅅ짜
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

#244. strftime 시간 형식 변경
print(now.strftime("%H:%M:%S"))

#245. striptime 일반 string을 datetime.datetime시간 값으로. 이게
day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

#246. sleep 함수 사용하여 1초에 한 번씩 현재 시간 자겨오게
import time
import datetime

# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

#247. 모듈 임포트하는 방법
# 1. import 모듈
# 2. from 모듈 import 이름
# 3. from 모듈 import 변수 / 함수 / 클래스 as 이름
# 4. from 모듈 import 변수, 함수, 클래

#248.
import os
ret = os.getcwd()
print(ret, type(ret))

#249.
import os
os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")

#250.
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)