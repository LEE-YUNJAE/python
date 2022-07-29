def solution(lottos, win_nums):
    
    answer = []
    count = 0
    zeros = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    zeros = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            count += 1
        
    answer = rank[count + zeros], rank[count]       
    return answer

def solution2(lottos, win_nums):
    
    answer = []
    zeros = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    zeros = lottos.count(0)
    W    = set(win_nums)
    mine = set(lottos)
    common = len(W & mine)
    
    answer = rank[common + zeros], rank[common]       
    return answer

lottos   = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution2(lottos, win_nums)
print(answer)