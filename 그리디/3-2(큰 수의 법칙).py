N=int(input("N: "))
M=int(input("M: "))
K=int(input("K: "))

list=[]
for i in range(N):
    n=int(input(""))
    list.append(n)
list.sort()
print(list)

res=0

n=M//(K+1)

res+=n*(list[N-1]*K+list[N-2])
res+=list[N-1]*(M-n*(K+1))
        
print(res)

# 반복되는 수열에 대해서 파악 { (가장 큰 수*K) + (두번째로 큰 수 *1) }