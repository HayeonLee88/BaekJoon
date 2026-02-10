'''
max(앞단어, 뒷단어 겹치는 단어) + 1
'''
def solution(words):
    answer = 0
    def count_same_word(w1, w2):
        cnt = 0
        for s1, s2 in zip(w1, w2):
            if s1 == s2:
                cnt += 1
            else:
                break
        return cnt
    words.sort()
    for i in range(len(words)):
        prev = 0
        nxt = 0
        if i > 0:
            prev = count_same_word(words[i - 1], words[i])
        if i < len(words) - 1:
            nxt = count_same_word(words[i], words[i + 1])
        needed = max(prev, nxt) + 1
        answer += min(len(words[i]), needed)
    return answer