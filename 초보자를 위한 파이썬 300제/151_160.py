#151.
리스트 = [3, -20, -3, 44]
for 숫자 in 리스트:
    if 숫자 < 0:
        print(숫자)

#152.
리스트 = [3, 100, 23, 44]
for 숫자 in 리스트:
    if 숫자 % 3 == 0:
        print(숫자)

#153.
리스트 = [13, 21, 12, 14, 30, 18]
for 숫자 in 리스트:
    if (숫자 < 20) and (숫자 % 3 ==0):
        print(숫자)

# 154.
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i) >= 3:
        print(i)

#155.
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.isupper():
        print(i)

#156.
for i in 리스트:
    if i.islower():
        print(i)

#157.
리스트 = ['dog', 'cat', 'parrot']
for animal in 리스트:
    print(animal.capitalize())
    print("=")
    print('{}{}'.format(animal[0].upper(), animal[1:]))
    print()

#158.
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for 파일 in 리스트:
    print(파일.split('.')[0])

#159.
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 파일 in 리스트:
    파일명, 확장자 = 파일.split('.')
    if 확장자 == "h":
        print(파일)

#160.
for 파일 in 리스트:
    파일명, 확장자 = 파일.split('.')
    if 확장자 == "h" or 확장자 == 'c':
        print(파일
