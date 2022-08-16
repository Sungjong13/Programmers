import re

# string="aabbaccc"
string="ababcdcdababcdcd"
# string="abcabcdede"
# string="abcabcabcabcdededededede"
# string="xababcdcdababcdcd"


# print(re.findall('..',string))




def solution(string):
    answer=1001
    for mult in range(1,int(len(string)/2)+1):
        patterns=re.findall('.'*mult,string)
        counter=1
        processedstring=string
        last_pattern=''
        for pattern in patterns:
            print(pattern,'pattern start')
            if last_pattern==pattern:
                counter+=1
            else:
                if counter>1:
                    processedstring=re.sub(f'({pattern}){{2,}}',f'{str(counter)}{pattern}',processedstring,1)
                    print('new processed string',processedstring)
                    counter=1
            if counter>1:
                processedstring=re.sub(f'({pattern}){{2,}}',f'{str(counter)}{pattern}',processedstring,1)
                print('new processed string',processedstring)
                counter=1
            last_pattern=pattern
        if len(processedstring)<answer:
            answer=len(processedstring)
            print('answer updated',processedstring)
    return answer

print(solution(string))

#결과적으로 for문 하나 사라짐. 대신 re.findall()
#finditer도 없어졌다.
#64점.