def solution(s):
    answer = ''
    s_check = False

    for i in s:
        if s_check and ord(i) > 96:
            answer += ' ' 
            answer += chr(ord(i) - 32)
            s_check = False
        elif s_check and (ord(i) > 64 and ord(i) < 91):
            answer += ' '
            answer += i
            s_check = False

        elif len(answer) == 0 and ord(i) > 96:
            answer += chr(ord(i) - 32)  
        elif len(answer) == 0 and ord(i) == 32:
            s_check = True        
        elif (ord(i) > 47 and ord(i) < 58) or ord(i) > 96:
            answer += i
        elif (ord(i) > 64 and ord(i) < 91):
            answer += chr(ord(i) + 32)
        elif (ord(i) == 32):
            s_check = True
    return answer

print(solution(' hI MyNAMe is Sj 3pEO'))