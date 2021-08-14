# 내 답
# N,M=map(int,input().split())    # N개의 볼링공, 1<= 무게 <= M

# data=list(map(int,input().split())) # 볼링공 무게, data[0]~data[N-1]
# data.sort()

# res=0
# i=0
# while i<N:
#     a=data[i]
#     j=i+1
#     while j<N:
#         b=data[j]
#         if a!=b:
#             res+=1
#         j+=1
#     i+=1

# print(res)

# 해설지
N,M=map(int,input().split())
data=list(map(int,input().split()))

# 1~10 무게를 담을 수 있는 리스트
array=[0]*11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x]+=1

result=0

# 1~m까지의 각 무게에 대해 처리
for i in range(1, M+1):
    N-=array[i]     #무게가 i인 볼링공에 대해서 처리햇으니깐 빼기 -->A
    result+=array[i] * N    # A*B

print(result)