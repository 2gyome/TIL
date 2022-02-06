#91. 딕셔너리 생성
inventory = {"메로나": (300, 20), "비비빅": (400, 3), "죠스바": (250, 100)}

#92. 딕셔너리 인덱싱
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory["메로나"][0])

#93.
print("{} 개".format(inventory["메로나"][1]))

#94. 딕셔너리 추가
inventory["월드콘"] = [500,7]
print(inventory)

#95. 딕셔너리 keys() 메서드 --> 틀림
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.keys()))

#96. values() 메서드
print(list(icecream.values()))

#97.
print(sum(list(icecream.values())))

#98. update 메서드
new_icecream = {'팥빙수':2200, '아맛나':1000}
icecream.update(new_icecream)
print(icecream)

#99. zip, dict --> 틀림
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

fruit = dict(zip(keys,vals))
print(fruit)

#100.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip())
