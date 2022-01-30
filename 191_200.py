#191.
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for row in data:
    for col in row:
        print(col*1.00014)

#192.
for line in data:
    for column in line:
        print(column * 1.00014)
    print('-'*5)

#193.
result = []
for line in data:
    for column in line:
        result.append(column*1.00014)
print(result)

#194. 2차원 배열로 저장
result = []

for line in data:
    temp = []
    for column in line:
        temp.append(column*1.00014)
    result.append(temp)
print(result)

#195. close에 해당하는 값 뽑기
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for row in ohlc[1:]:
    print(row[3])

#196.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for row in ohlc[1:]:
    if row[3] > 150:
        print(row[3])

#197.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
print()
for row in ohlc[1:]:
    if row[3] >= row[0]:
        print(row[3])

#198.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
result = []
for row in ohlc[1:]:
    result.append(row[1] - row[2])
print(result)

#199.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# 1) 종가가 시가보다 높
# 2) 고가 - 저가

for row in ohlc[1:]:
    if row[3] > row[0]:
        print(row[1]-row[2])

#200. 시가에서 종가에 매도했을 때 수익금
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

result = 0
for row in ohlc[1:]:
    result += -row[0] + row[3]
print(result)