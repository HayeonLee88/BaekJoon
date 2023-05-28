# 11719번: 그대로 출력하기 2
'''
import sys
    for line in sys.stdin:
        print(line, end=' ')
'''
while True:
    try:
        print(input())
    except EOFError:
        break