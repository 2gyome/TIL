import sys
sys.stdin = open('../input/4836.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    box = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0 # 보라색 칸의 수
    for n in range(N):
        x1,y1,x2,y2, color = map(int,input().split())

        for col in range(y1, y2+1):
            for row in range(x1, x2+1):
                if box[row][col] == 0: #빈칸인경우
                    box[row][col] = color
                else:
                    if box[row][col] == color: # 동일색상인경우
                        continue # continue 다시 확인하기
                    elif 0 < box[row][col]: # 다른색인경우 및 보라색 아닌경우
                        box[row][col] = -1 # -1이 보라색
                        cnt += 1
    print(f'#{tc} {cnt}')


