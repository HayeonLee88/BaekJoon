# 2116번: 주사위 쌓기 (구현, BruteForce)
'''
서로 붙어 있는 두 개의 주사위에서 아래에 있는 주사위의 윗면에 적혀있는 숫자는 위에 있는 주사위의 아랫면에 적혀있는 숫자와 같아야 한다

problem: 한 옆면의 숫자의 합의 최댓값을 구하는 프로그램을 작성하시오.

How?
    dic: 주사위 위/아래 딕셔너리 {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
    1. 시작 주사위를 1~6까지 아래로 가도록 쌓는다.
    2. 1~n번째 주사위는 아래의 주사위 윗면과 일치한 숫자와 그 숫자의 반대면을 제외하여 최대 숫자를 구한다.
    3. 시작 주사위의 아랫면에 따라 옆면의 최대합을 구해 합이 가장 큰 수가 정답.
'''
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
dic = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

answer = 0 # 정답 변수 초기화
for i in range(6):
    tmp = [] # 첫 주사위의 rotation에 따라 변하는 옆면의 최대값 리스트
    nums = [1, 2, 3, 4, 5, 6]
    bottom = dices[0][i] # 아랫면 숫자
    next = dices[0][dic[i]]  # 아랫면이 i번째일 때 윗면의 값
    nums.remove(bottom) # 첫 주사위의 아랫면 제거
    nums.remove(next) # 첫주사위 윗면 & 다음 주사위 아랫면 제거
    tmp.append(max(nums))
    for dice in dices[1:]:
        nums = [1, 2, 3, 4, 5, 6]
        nums.remove(next) # 주사위 아랫면 제거
        next = dice[dic[dice.index(next)]]  # 윗면(다음 주사위의 아랫면)
        nums.remove(next) # 주사위 윗면 제거
        tmp.append(max(nums)) # 옆면 최대값 저장
    hap =  sum(tmp)
    answer = max(answer, hap)

print(answer)



