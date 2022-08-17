# this whole design is impractical since c3abcab could be caaabcab or cabababcab or cabcabcabcab and so on...
import re

# string="aabbaccc"
# string="ababcdcdababcdcd"
# string="abcabcdede"
string="abcabcabcabcdededededede" #produces weird result that changes every time. probably due set(). 
    #would give consistant results if another sorted() is added, but doesn't fix some other problems(cabcabcabcab will become c3abcab)
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

pattern_duplicate=sorted(list(set(pattern_duplicate)),key=len)
print(pattern_duplicate)
final_result='a'*1001
lastend=''
while pattern_duplicate:
    string2=string
    final_string_list=[]
    print('next pattern list')
    for i in pattern_duplicate:
        repeats=1
        regex=f'(?:{i})'
        matches=re.finditer(regex,string2)
        for match in matches:
            if lastend==match.start():
                repeats+=1
            else:
                if repeats>1:
                    string2=re.sub(f'(?:{i}){{2,}}',f'{str(repeats)}{i}',string2,1)
                    repeats=1
                    print(string2)

            lastend=match.end()
        if repeats>1:
            string2=re.sub(f'(?:{i}){{2,}}',f'{str(repeats)}{i}',string2,1)
            repeats=1
            print(string2)
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

