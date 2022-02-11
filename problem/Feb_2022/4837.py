import sys
sys.stdin = open('../input/4837.txt')
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    result = 0 # 조건에 만족하는 부분집합의 수

    for i in range(1<<12):
        temp_cnt = 0 # 부분집합 원소 갯수
        temp_sum = 0  # 부분집합 원소
        for j in range(12):
            if i & (1<<j): # j 번째 비트가 1이면
                temp_sum += j+1 # 1 ~ 12
                temp_cnt += 1
                if temp_cnt > N or temp_sum > K:
                    break
        if temp_cnt == N and temp_sum == K:
            result += 1
    print(f'#{tc} {result}')

