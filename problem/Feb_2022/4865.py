import sys
sys.stdin = open('../input/4865.txt')
T = int(input())
for tc in range(1,T+1):
    str1 = list(set(input()))
    str2 = input()
    for i in range(0,len(str1)):
        temp_cnt = 0
        for j in str2:
            if str1[i] == j:
                temp_cnt += 1
        str1[i]=temp_cnt

    print(f'#{tc} {max(str1)}')