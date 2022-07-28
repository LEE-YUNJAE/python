def solution(left, right):
    answer = 0
    ## 1. 약수의 개수가 홀수 인지 짝수인지 구분 가능
    for num in range (left, right+1):
        
        divisor = 0
        for num2 in range (1,num+1):
            if num%num2==0:divisor+=1

        if divisor%2==0:
            answer+=num
        else:
            answer-=num
             
            
    return answer

left = 13
right = 17
c = solution(left, right)
print(c)