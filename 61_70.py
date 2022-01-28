#61. 슬라이싱
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#62.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#63.
print(nums[1::2])

#64.리스트 역방향 출력
print(nums[::-1])

#65. 리스트 바인딩
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

#66. join
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest))

#67.
print('\n'.join(interest))

#68.
print(' '.join(interest))

#69.
string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)

#70. 리스트 오름차준 정렬
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)