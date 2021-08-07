N,K=map(int,input().split())

count=0

while N!=1:
    count+=1
    if N%K!=0:  # 나누어 떨어지지 x
        N-=1
    else:
        N/=K

print(count)

# 최대한 많이 나누기!!!
# K가 2이상이기만 하면, K로 나누는 것이 1빼는 것보다 항상 빠르다!!!