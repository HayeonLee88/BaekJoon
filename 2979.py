# 2979번: 트럭주차
a, b, c = map(int, input().split())
data = [0] * 100
for _ in range(3):
  arrival, departure = map(int, input().split())
  for time in range(arrival, departure):
    data[time] += 1
print(data.count(1)*1*a+data.count(2)*2*b+data.count(3)*3*c)