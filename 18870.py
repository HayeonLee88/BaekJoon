# 18870번: 좌표 압축
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))
sorted_data = sorted(set(data)) # 같은 값은 같은 인덱스를 가지도록 set으로 변환하여 오름차순 정렬
dict_zip_data = {key: value for value, key in enumerate(sorted_data)} # 데이터가 key, 데이터의 인덱스가 value

print(' '.join(str(dict_zip_data[x]) for x in data))