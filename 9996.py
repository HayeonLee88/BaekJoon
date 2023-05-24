# 9996번: 한국이 그리울 땐 서버에 접속하지
# 총 N개의 줄에 걸쳐서, 입력으로 주어진 i번째 파일 이름이 패턴과 일치하면 "DA", 일치하지 않으면 "NE"를 출력한다.
import sys
input = lambda:sys.stdin.readline()

n = int(input())
start_pattern, end_pattern = input().split('*')
start_len = len(start_pattern)
end_len = len(end_pattern)

for i in range(n):
  string = input()
  if string[:start_len] == start_pattern and string[start_len:][-end_len:] == end_pattern:
    print('DA')
  else:
    print('NE')