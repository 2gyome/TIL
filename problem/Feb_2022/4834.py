import sys
sys.stdin = open("./input/4834.txt")
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cards = input()
    max_num = 0
    max_time = 0

    number = [0 for _ in range(10)] # 0 ~ 9 까지 배열

    for card in cards: # 카드 개수 저장
        number[int(card)] += 1

    for i in range(1,10):
        if number[i] >= max_time:
            max_num = i
            max_time = number[i]
    print(f'#{tc} {max_num} {max_time}')