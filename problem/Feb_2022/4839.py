import sys

sys.stdin = open('../input/4839.txt')
T = int(input())

def binarySearch(A,K):
    start = 1 # 1페이지
    end = A # 마지막페이지
    cnt = 0
    while start <= end:
        cnt += 1
        middle = int((start + end) / 2)
        if K == middle:
            return cnt # 찾음
        elif K < middle:
            end = middle # 예시 기준 참고
        else:
            start = middle
    return -1 # 실패했을경우

for tc in range(1,T+1):
    P, PA, PB = map(int, input().split())
    A = binarySearch(P, PA)
    B = binarySearch(P, PB)

    if A == B:
        result = 0
    elif A > B:
        result = 'B'
    else:
        result = 'A'

    print(f'#{tc} {result}')