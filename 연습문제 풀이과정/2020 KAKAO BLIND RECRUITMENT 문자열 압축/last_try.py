import re

# string="aabbaccc"
# string="ababcdcdababcdcd"
# string="abcabcdede"
# string="abcabcabcabcdededededede"
string="xababcdcdababcdcd"

def solution(string):
    answer=len(string)
    for mult in range(1,len(string)//2+1):
        string_list=[]
        for i in range(0,len(string),mult):
            start_index=i
            end_index=i+mult
            string_list.append(string[start_index:end_index])
        # print(string_list,'new list start')
        list_index=0
        while list_index<len(string_list)-1:
            # print('next while')
            if string_list[list_index]==string_list[list_index+1]:
                string_list.pop(list_index+1)
                if type(string_list[list_index-1]) is not int:
                    string_list.insert(list_index,2)
                    # print('added number',string_list)
                else:
                    string_list[list_index-1]+=1
                    list_index-=1
                    # print('updated number',string_list)
            list_index+=1
        string_list=list(map(str,string_list))
        newstring=''.join(string_list)
        if answer>len(newstring):
            answer=len(newstring)
            # print('updated answer',newstring)
    return answer

print(solution(string))