# import numpy as np
import re

string="ababcdcdababcdcd"
# string="abcabcdede"
# string="abcabcabcabcdededededede"
# string="xababcdcdababcdcd"

# regex='(?:ab)'

# matches=re.finditer(regex,string)
# for match in matches:
#     print(match,match.start(),match.end(),match.group(),sep='\t')


pattern_list=[]
pattern_duplicate=[]
for mltp in range(1,int(len(string)/2+1)):
    for startindex in range(mltp):
        indexrange=range(startindex,len(string)+1,mltp)
        for i in range(len(indexrange)-1):
            ptstindex,ptedindex=indexrange[i],indexrange[i+1]
            pattern=string[ptstindex:ptedindex]
            if pattern in pattern_list:
                pattern_duplicate.append(pattern)
            pattern_list.append(pattern)
# print(set(pattern_duplicate))

pattern_duplicate=list(set(pattern_duplicate))
print(pattern_duplicate)
final_result='a'*1001
lastend=''
while pattern_duplicate:
    string2=string
    for i in pattern_duplicate:
        repeats=1
        regex=f'(?:{i})'
        matches=re.finditer(regex,string2)
        for match in matches:
            # try:
            if lastend==match.start():
                repeats+=1
            else:
                if repeats>1:
                    string2=re.sub(f'(?:{i})+',f'{str(repeats)}{i}',string2)
                    repeats=1
                    print(string2)

            # except:
            #     pass
            lastend=match.end()
    if len(final_result)>len(string2):
        final_result=string2
        print('final result update:',string2)

    pattern_duplicate=pattern_duplicate[1:]

print(final_result,len(final_result))


# my_list=[1,2,3,5,6]
# while my_list:
#     print(my_list)
#     my_list=my_list[1:]
# print('end')
# print(my_list)

# for i in re.finditer('(?:ababcdcd)+',string):
#     print(i)
# print(re.sub('(?:ababcdcd)+','replaced',string))

# pattern_array=np.array(pattern_list)
# for pattern in pattern_duplicate:
#     duplicate_index_list=np.where(pattern_array==pattern)
#     for index in duplicate_index_list:
        


# print(pattern_list)
# print(len(set(pattern_duplicate)))
# print(pattern_list.index('ab'))
# pattern_array=np.array(pattern_list)
# print(np.where(pattern_array=='ab')[0])

