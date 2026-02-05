'''
연산자 조합(최대 3!), 우선순위, 절댓값(abs)
같은 연산자는 앞에 있는 것이 우선순위가 높음
앞에서부터 연산자 우선순위에 따라 계산
1. 연산자 종류를 찾기
2. 연산자 종류 우선순위 매기기
3. 연산자 우선순위에 따라 계산하기
'''
from itertools import permutations
from collections import deque, defaultdict
import copy
def solution(expression):
    def operation(x, y, o):
        if o == '+':
            return x + y
        elif o == '-':
            return x - y
        else:
            return x * y
        
        
    def modify_idx(search, target):
        result = 0
        for x in search:
            if target > x:
                result += 1
        return target - result
    
    
    answer = 0
    exp = set(expression)
    op = [x for x in ['+', '-', '*'] if x in exp]
    op_idxs = defaultdict(deque)
    nums = []
    start = 0
    
    for end, x in enumerate(expression):
        if x.isdigit():
            continue
        nums.append(int(expression[start:end]))
        op_idxs[x].append(len(nums))
        start = end + 1
    nums.append(int(expression[start:]))
    ops = list(permutations(op))
    
    for op in ops:
        deleted_op_idx = []
        tmp_idxs = copy.deepcopy(op_idxs)
        tmp_nums = copy.deepcopy(nums)
        for o in op:
            idxs = tmp_idxs[o]
            while idxs:
                idx = idxs[0]
                idx = modify_idx(deleted_op_idx, idx)
                n1, n2 = tmp_nums[idx - 1:idx + 1]
                deleted_op_idx.append(tmp_idxs[o].popleft())
                tmp_nums = tmp_nums[:idx - 1] + [operation(n1, n2, o)] + tmp_nums[idx + 1:]
        answer = max(answer, abs(tmp_nums[0]))
    return answer