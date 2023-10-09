# 13975번: 파일 합치기 3(최소힙, 정렬)
'''
각 장은 각각 다른 파일에 저장,  각 장이 쓰여진 파일을 합쳐서 최종적으로 한 개의 파일을 만든다.
두 개의 파일을 합쳐서 하나의 임시파일 -> 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 파일을 합쳐 한 개의 ㅡ파일을 만든다.

T: 테스트 케이스
K: 소설을 구성하는 장의 수 (3 ≤ K ≤ 1,000,000)
단, 파일의 크기를 10,000을 초과하지 않는다.

problem: 파일을 합칠 때 필요한 비용(시간 등)이 두 파일 크기의 합일 때 최종 파일을 완성할 때 필요한 비용의 총 합은?

How?
    files: 파일을 담을 최소힙
    answer: 최종 파일을 완성하는데 드는 최소 비용
    1. 처음 모든 장(파일)을 리스트에 담고, 오름차순 정렬을 한다.
    2. heappush를 두 번 해 나온 파일의 크기를 합하고, 그 값을 answer에 더한다.
    3. 2번의 합한 파일을 최소힙에 담는다. heappush
    4. 최소힙의 크기가 1이 될 때까지 2-3번을 반복한다.

'''
import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for test_case in range(T):
    answer = 0
    k = int(input())
    times = 0
    while k > 1:
        times += k // 2
        tmp = k // 2 + k % 2
        k = tmp
    files = list(map(int, input().split()))
    files.sort()
    for i in range(times):
        f1 = heapq.heappop(files)
        f2 = heapq.heappop(files)
        new_f = f1 + f2
        answer += new_f
        heapq.heappush(files, new_f)
    print(answer)

