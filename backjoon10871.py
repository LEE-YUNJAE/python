N, X = map(int, input().split())  

data = list(map(int, input().split()))
    
answer = []

for i in data:
    if i<X:
        answer.append(i)
        
print(answer)