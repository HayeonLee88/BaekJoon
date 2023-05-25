# 1427번: 소트인사이드
array = list(input())
array.sort(reverse=True)
print(''.join(a for a in array))