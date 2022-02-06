#291. txt 파일 만들고 자료 적기
f = open("./291_300/매수종목.txt", mode="wt", encoding="utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420")
f.close()

#292. 파일 쓰기
f = open("./291_300/매수종목2.txt", mode="wt", encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")
f.close()

#293. csv 파일 만들고 데이터 넣기
import csv
f = open("./291_300/매수종목.csv", mode="wt", encoding="cp949", newline="")
writer = csv.writer(f)
writer.writerow(["종목명", "종목코드", "PER"])
writer.writerow(["삼성전자", "005930", 15.59])
writer.writerow(["NAVER", "035420", 55.82])
f.close()

#294. 파일 읽기
f = open("./291_300/매수종목.txt", encoding="utf-8")
lines = f.readlines()   # 머지
for line in lines:
    code = line.strip()  #'\n'
    print(code)
f.close()

#295. 파일 읽은 후 딕셔너리 저장
f = open("./291_300/매수종목2.txt", encoding="utf-8")
lines = f.readlines()
dict = {}
for line in lines:
    code, name = line.strip().split() # \n 없애기
    dict[code] = name
print(dict)

#296 예외처리 에러 발생할 경우 0 처리하는법
per = ["10.31", "", "8.00"]

for i in per:
    try:
       print(float(i))
    except:
        print("0")


#297. 예외처리 및 리스트에 저장
per = ["10.31", "", "8.00"]
new = []
for i in per:
    try:
        new.append(float(i))
        print(float(i))
    except:
        new.append(0)
        print("0")
print(new)

#298. 특정 예외만 처리하기
#  try ~ except로 모든 에러에 대해 예외처리하지 말고 ZeroDivisionError 에러만 예외처리
try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누면 안됨")

#299.예외 메시지 출력 가능
# try:
#     실행코드
# except 예외 as 변수:
#     예외처리코드

data = [1, 2, 3]
for i in range(5):
    try:
        print(data[i])
    except IndexError as tlqkf:
        print(tlqkf)

#300. try except else finally 구조
# try:
#     실행 코드
# except:
#     예외가 발생했을 때 수행할 코드
# else:
#     예외가 발생하지 않았을 때 수행할 코드
# finally:
#     예외 발생 여부와 상관없이 항상 수행할 코드

#else finallty 적당한 문구 출력
per = ["10.31", "", "8.00"]
new_per = []
for i in per:
    try:
        print(float(i))
    except ValueError as A:
        print(A)
    else:
        new_per.append(float(i))
    finally:
        print(new_per)