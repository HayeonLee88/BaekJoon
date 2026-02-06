'''
9:18~
Enter: 입장
Leave: 퇴장
Change: 닉네임 변경

users = {'uid1234': 'Muzi'}
'''
def solution(record):
    answer = []
    # 사용자 정보를 담는 딕셔너리
    user_info = dict()
    for log in record:
        log = list(log.split())
        if log[0] == 'Enter':
            user_info[log[1]] = log[2]
            answer.append([log[1], "님이 들어왔습니다."])
        elif log[0] == 'Leave':
            answer.append([log[1], "님이 나갔습니다."])
        else:
            user_info[log[1]] = log[2]
    answer = [f"{user_info[uid]}" + ment for uid, ment in answer]
    return answer