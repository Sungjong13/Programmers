# queue1=[3, 2, 7, 2]
# queue2=[4, 6, 5, 1]
# queue1=[1, 2, 1, 2]
# queue2=	[1, 10, 1, 2]
queue1=[-4]
queue2=	[4]

def solution(queue1, queue2):
    #check if the queues are equally distributable.
    total_list=queue1+queue2
    if len(total_list)%2==1:
        return -1
    else:
        indicator=0
        for i in sorted(total_list,reverse=True):
            if indicator<=0:
                indicator+=i
            else:
                indicator-=i
        if indicator!=0:
            return -1
    #add everything from beginning, sub target value, add or sum one by one.
    indicator2=sum(queue1)-int(sum(total_list)/2)
    answer=0
    total_list=(total_list+queue1)[::-1]
    total_list2=(queue2+queue1+queue2)[::-1]
    while indicator2!=0:
        if indicator2>0:
            indicator2-=total_list.pop()
        else:
            indicator2+=total_list2.pop()
        answer+=1
    return answer

print(solution(queue1,queue2))