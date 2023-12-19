def solution(record):
    answer = []
    uid = {}
    
    for i in record:
        if i.split()[0] =='Enter':
            uid[i.split()[1]] = i.split()[2]
        elif i.split()[0] =='Change':
            uid[i.split()[1]] = i.split()[2]
    # uid에 uid : 최종닉넴 저장  
    
    for i in record:
        if i.split()[0] == 'Enter':
            answer.append(uid[i.split()[1]] + "님이 들어왔습니다.")
        elif i.split()[0] == 'Leave':
            answer.append(uid[i.split()[1]] + "님이 나갔습니다.")
    return answer