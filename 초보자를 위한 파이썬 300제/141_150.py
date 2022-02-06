#141.
리스트 = [100, 200, 300]
for i in 리스트:
    print(i + 20)

#142.
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print("오늘의 메뉴는:{}".format(i))

#143.
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for 종목 in 리스트:
    print(len(종목))

#144.
리스트 = ['dog', 'cat', 'parrot']
for animal in 리스트:
    print("{} {}".format(animal, len(animal)) )

#145.
for animal in 리스트:
    print(animal[0])

#146.
number = [1, 2, 3]
for n in number:
    print("3 x {}".format(n))

#147.
for n in number:
    print("3 x {} = {}".format(n, n*3))

#148.
리스트 = ["가", "나", "다", "라"]
for 한글 in 리스트[1:]:
    print(한글)

#149.
for 한글 in 리스트[::2]:
    print(한글)

#150
for 한글 in 리스트[::-1]:
    print(한글)
