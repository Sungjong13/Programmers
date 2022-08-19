queue1=[3, 2, 7, 2]
queue2=[4, 6, 5, 1]

def solution(queue1, queue2):
    #check if the queues are equally distributable.
    if len(queue1+queue2)%2==1:
        return -1
    else:
        list1=[]
        list2=[]
        for i in sorted(queue1+queue2,reverse=True):
            if sum(list1)>=sum(list2):
                list2.append(i)
            else:
                list1.append(i)
        if sum(list1)!=sum(list2):
            return -1
    #distribute queues with counter(answer).
    # answer = 0
    # print('initially',queue1,queue2)
    # while sum(queue1)!=sum(queue2):
    #     print(queue1,queue2)
    #     print(sum(queue1),sum(queue2))
    #     if sum(queue1)<sum(queue2):
    #         queue1.append(queue2.pop(0))
    #         answer+=1
    #     else:
    #         queue2.append(queue1.pop(0))
    #         answer+=1
            
    return answer

# print(solution(queue1,queue2))
# print(sum(queue2))

# print([1,2,3,4,5,6,7,8,9,0][0:3])

my_list=[1,2,3,4,5,6,7,8,9,0]

print((my_list+[1,2,3,4])[:])