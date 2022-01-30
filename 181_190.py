#181.
apart = [[101,102],[201,202],[301,302]]

#182.
stock = [["시가", 100, 200, 300], ["종가 ",80, 210, 330]]

#183.
# stock = {"시가":"종가", 100:80, 200:210,300:330}
stock = {"시가": [100, 200, 300], "종가": [80, 210, 330] } # 이런식으로하면댐
print(stock)

#184.
stock = {"10/10":[80, 110, 70, 90], "10/11":[210, 230, 190, 200]}

#185. => 틀림
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in range(len(apart)):
    print(apart[i][0], "호")
    print(apart[i][1], "호")

for row in apart:
    for col in row:
        print(col)

#186.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in range(len(apart)):
    for col in apart[len(apart)-i-1]:
        print(col, '호')
# 정답
# for row in apart[::-1]:
#     for col in row:
#         print(col, "호")

#187.
for row in apart[::-1]:
    for col in row[::-1]:
        print(col, '호')

#188.
for row in apart:
    for col in row:
        print(f'{col}호')
        print('-------')

#189.
for row in apart:
    for col in row:
        print(col,'호')
    print('------')

#190.
for row in apart:
    for col in row:
        print(col,'호')
print('------')