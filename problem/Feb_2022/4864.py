import sys
sys.stdin = open('../input/4864.txt')
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    flag = 0
    for i in range(0, len(str2)-len(str1)+1):
        if str1 == str2[i:i+len(str1)]:
            flag = 1
            break

    print(f'#{tc} {flag}')