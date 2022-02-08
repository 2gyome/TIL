import sys

sys.stdin = open('./input/4835.txt')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    number = list(map(int,input().split()))
    min_sum = 9999999 # 정수
    max_sum = -999999 # 정수

    for i in range(0,N-M+1):
        temp_sum = 0
        for j in range(M):
            temp_sum += number[i+j]
        if temp_sum < min_sum:
            min_sum = temp_sum
        if temp_sum > max_sum:
            max_sum = temp_sum

    print(f'#{tc} {max_sum - min_sum}')