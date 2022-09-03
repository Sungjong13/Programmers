

def solution(N, stages):
    clear_dic = {x:0 for x in range(1,N+2)}
    notclear_dic = {x:0 for x in range(1,N+2)}
    for stage in stages:
        notclear_dic[stage]+=1
        for j in range(1,stage+1):
            clear_dic[j]+=1
    failrate_dic = {}
    for i in range(1,N+1):
        if clear_dic[i]!=0:
            failrate_dic[i]=notclear_dic[i]/clear_dic[i]
        else:
            failrate_dic[i]=0
    # failrate_dic={i:notclear_dic[i]/clear_dic[i] for i in range(1,N+1) if clear_dic[i]!=0 else i:501}
    return [x[0] for x in sorted(failrate_dic.items(), key=lambda x:(-x[1],x[0]))]

N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]	
result =[3,4,2,1,5]
# N=4
# stages=	[4,4,4,4,4]
# result = [4,1,2,3]


print(solution(N,stages))


