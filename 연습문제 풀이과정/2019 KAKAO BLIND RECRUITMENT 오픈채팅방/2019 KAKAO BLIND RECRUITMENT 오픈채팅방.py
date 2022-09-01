def solution(record):
    uid_dic = {}
    answer = []
    
    #record의 행동, uid 반대 순서로 가져오기
    for i in record[::-1]:
        action,uid = i.split(' ')[0],i.split(' ')[1]
        
        #마지막 행동이 Leave이면 nick없으므로 스킵
        if action == 'Leave': 
            continue
        #처음 보는 uid의 nickname dictionary에 등록
        if uid not in uid_dic: 
            nick = i.split(' ')[2]
            uid_dic[uid] = nick
    
    #record의 요소들 가져오기
    for i in record:
        action,uid = i.split(' ')[0],i.split(' ')[1]
        
        #uid 참고해 입장 메시지 append
        if action == 'Enter':
            answer.append(f'{uid_dic[uid]}님이 들어왔습니다.')
        #uid 참고해 퇴장 메시지 append
        elif action == 'Leave':
            answer.append(f'{uid_dic[uid]}님이 나갔습니다.')
        
    return answer

