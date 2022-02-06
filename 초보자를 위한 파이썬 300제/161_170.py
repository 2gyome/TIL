#161.
for i in range(100):
    print(i)

#162.
for i in range(2002,2051,4):
    print(i)

#163.
for i in range(0,31,3):
    print(i)

#164.
for i in range(90,-1,-1):
    print(i, end=" ")

for i in range(100):
    print(99 - i)

#165.
for i in range(0,10):
    print(f'0.{i}')

for num in range(10):
    print(num / 10)

#166. 구구단 3단
for i in range(10):
    print(f'3x{i} = {i*3}')

#167.
for i in range(1,10,2):
    print(f'3x{i} = {i*3}')

#168. 다 더하는 프로그램
total = 0
for i in range(1,11):
    total += i
print(total)

#169. 홀수 합 더하기
total = 0
for i in range(1,10,2):
    total += i
print(total)

#170. 곱한 값
total = 1
for i in range(1,11):
    total *= i
print(total)