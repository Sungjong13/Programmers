_list=[x for x in list(range(1,10))+['*',0,'#']]
keypad=[_list[i:i+3] for i in range(0,len(_list),3)]

def get_index(num):
    for i,v in enumerate(keypad):
        if num in v:
            return i,v.index(num)

def solution(numbers, hand):
    LHpos='*'
    RHpos='#'
    answer_list=[]
    for num in numbers:
        if num in [1,4,7]:
            answer_list.append('L')
            LHpos=num
        elif num in [3,6,9]:
            answer_list.append('R')
            RHpos=num
        else:
            a,b=get_index(num)
            ra,rb=get_index(RHpos)
            la,lb=get_index(LHpos)
            if abs(a-ra)+abs(b-rb)<abs(a-la)+abs(b-lb):
                answer_list.append('R')
                RHpos=num
            elif abs(a-ra)+abs(b-rb)>abs(a-la)+abs(b-lb):
                answer_list.append('L')
                LHpos=num
            else:
                if hand=='right':
                    answer_list.append('R')
                    RHpos=num
                else:
                    answer_list.append('L')
                    LHpos=num
                
    answer=''.join(answer_list)
    return answer
