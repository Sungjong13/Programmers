import re

# string="aabbaccc"
string="ababcdcdababcdcd"
# string="abcabcdede"
# string="abcabcabcabcdededededede"
# string="xababcdcdababcdcd"


def solution(string):
    final_string_len=1001
    for mult in range(1,int(len(string)/2+1)):
        processedstring=string
        for startindex,endindex in zip(range(0,len(string)+1,mult)[:-1],range(0,len(string)+1,mult)[1:]):
            matches=re.finditer((string[startindex:endindex]),string)
            regexcounter=1
            lastend=''
            print('new pattern start',string[startindex:endindex])
            for match in matches:
                if lastend==match.start():
                    regexcounter+=1
                else:
                    if regexcounter>1:
                        processedstring=re.sub(f'({string[startindex:endindex]}){{2,}}',f'{str(regexcounter)}{string[startindex:endindex]}',processedstring,1)
                        print('string processed to',processedstring)
                        regexcounter=1
                lastend=match.end()
            if regexcounter>1:
                processedstring=re.sub(f'({string[startindex:endindex]}){{2,}}',f'{str(regexcounter)}{string[startindex:endindex]}',processedstring,1)
                print('string processed to',processedstring)
                regexcounter=1
        if len(processedstring)<final_string_len:
            final_string_len=len(processedstring)
            print('shortest len updated',processedstring)
    return final_string_len

print(solution(string))

#84점. 