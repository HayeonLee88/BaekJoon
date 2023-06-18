# 10825번: 국영수
'''
1. 국어 점수 내림차순
2. 국어 같 영어 점수 오름차순
3. 국어& 영어 같 수학 내림차순
4. 모든 점수 같 이름 사전 오름차순
N 1이상 100,000이하
4번부터 1번 순으로 정렬하기
'''
import sys

data = []
n = int(input())
for i in range(n):
    name, kor, eng, math = sys.stdin.readline().rstrip().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    data.append([name, kor, eng, math])
data.sort(key=lambda x: x[0])
data.sort(reverse=True, key=lambda x: x[3])
data.sort(key=lambda x: x[2])
data.sort(reverse=True, key=lambda x: x[1])

for i in range(n):
    print(data[i][0])
