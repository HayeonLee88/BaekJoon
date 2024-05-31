import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))
sorted_data = sorted(set(data))
dict_zip_data = {key:value for value, key in enumerate(sorted_data)}

print(' '.join(str(dict_zip_data[x]) for x in data))