'''
9:01~
나가는 화살표: 팀장
모든 팀에서 각 한 명씩 워크숍 참석 -> 매출 손실 최소화 되도록
1: CEO
각 팀에서 가장 작은 매출을 선택 -> 팀이 겹치는 경우 고려
'''
from collections import defaultdict
def solution(sales, links):
    num = len(sales)
    dp = [[0, 0] for _ in range(num + 1)]
    answer = 0
    teams = defaultdict(list)
    # 팀원들 저장
    for a, b in links:
        teams[a].append(b)
    
    def DFS(i):
        if i not in teams:
            dp[i][0] = 0
            dp[i][1] = sales[i - 1]
            return
        
        total_sum = 0
        attend_flag = False # 팀원 중 한명이라도 참석하는지 확인
        min_diff = 1e9
        
        for b in teams[i]:
            DFS(b)
            # 팀원이 참석 하는 것과 아닌 것 중 더 저렴한 것 선택
            if dp[b][0] < dp[b][1]:
                total_sum += dp[b][0]
                # 나중에 참석 필요시 최소 비용 차이 계산
                min_diff = min(min_diff, dp[b][1] - dp[b][0])
            else:
                total_sum += dp[b][1]
                attend_flag = True
        # 팀장이 참석하는 경우
        dp[i][1] = sales[i-1] + sum(min(dp[b][1], dp[b][0]) for b in teams[i])
        
        # 팀장이 참석하지 않는 경우
        if attend_flag:
            dp[i][0] = total_sum
        else:
            # 아무도 참석하지 않은 경우 가장 손해 안보는 팀원을 참석
            dp[i][0] = total_sum + min_diff
            
    DFS(1)
    return min(dp[1][0], dp[1][1])