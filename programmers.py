def solution(store, customer):
    answer = []
    for want in customer:
        if want in store:
            answer.append('yes')
        else:
           answer.append('no')
           
    return answer

store = [1,2,3,7,8]
customer = [1,5,8,4,6]
answer = solution(store, customer)
print(answer)