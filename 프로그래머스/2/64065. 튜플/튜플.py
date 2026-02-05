'''
제일 긴 튜플 찾기
길이 순으로 정렬 -> 제일 짧은 것부터 순서가 정해짐.
'''
def solution(s):
    def func(x):
        return x[1:]
    answer = []
    s = s[1:-2]
    tuples = list(map(func, s.split('},')))
    tuples = list(list(map(int, t.split(','))) for t in tuples)
    tuples.sort(key=lambda x: len(x))
    answer.append(tuples[0][0])
    for t in tuples[1:]:
        for n in t:
            if n not in answer:
                answer.append(n)
                break
    return answer