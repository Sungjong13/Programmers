# survey=["AN", "CF", "MJ", "RT", "NA"]
# choices=[5, 3, 2, 7, 5]
# survey=["TR", "RT", "TR"]
# choices=[7, 1, 3]
survey=["AN", "CF", "MJ", "RT", "NA", "CF", "MJ", "RT", "NA", "CF", "MJ", "RT", "NA", "CF", "MJ", "RT", "NA"]
choices=[5, 3, 2, 7, 5, 3, 2, 7, 5, 3, 2, 7, 5, 3, 2, 7, 5]


def solution(survey, choices):
    score_dic={'RT':0,'CF':0,'JM':0,'AN':0}
    for query,reply in zip(survey,choices):
        if query in ['RT','CF','JM','AN']:
            score_dic[query]+=reply-3
        else:
            score_dic[query[::-1]]-=reply-3
        print(score_dic)
    answer = ''
    for name,score in score_dic.items():
        if score<=0:
            answer+=name[0]
        else:
            answer+=name[1]
    return answer

print(solution(survey,choices))