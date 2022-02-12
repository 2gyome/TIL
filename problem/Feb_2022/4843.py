import sys
sys.stdin = open('../input/4843.txt')
T = int(input())

def arrange(A):
    length = len(A)
    for i in range(0,length-1): # 맨 마지막 원소는 당연히 최대로 정해져 있음
        temp_min = i
        for j in range(i+1,length):
            if A[temp_min] > A[j] :
                temp_min = j
        A[i], A[temp_min] = A[temp_min], A[i] #자리 바꿔주기

    for i in range(int(length / 2)):

        result.append(A[length-i-1])
        result.append(A[i])
    if length % 2 == 1:
        result.append(A[int(length/2+1)])


for tc in range(1,T+1):
    N = int(input())
    number = list(map(int,input().split()))
    result = []
    arrange(number)
    print(f'#{tc}', end =' ')
    for i in range(9):
        print(result[i],end =' ')
    print(result[9])