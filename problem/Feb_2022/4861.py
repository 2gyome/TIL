import sys
sys.stdin = open('../input/4861.txt')
T = int(input())

def isPalindrome(str):
    if str == str[::-1]:
        return str
    return 0

def FindPalindrome():
    cnt = 0
    for col in range(0,N):# 가로
        for row in range(0,N-M+1):
            str = ''
            for i in range(M):
                str += box[col][row+i]
            if isPalindrome(str):
                return str

    for col in range(0,N-M+1):
        for row in range(0,N):
            str = ''
            for i in range(M):
                str += box[col+i][row]
            if isPalindrome(str):
                return str





for tc in range(1,T+1):
    N, M = map(int, input().split())
    box = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        temp = input()
        for j in range(N):
            box[i][j] = temp[j]
    print(f'#{tc} {FindPalindrome()}')