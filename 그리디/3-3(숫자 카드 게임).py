N,M=map(int,input().split())

max=0

for i in range(N):
    data=list(map(int,input().split()))
    data.sort()
    if max<data[0]:
        max=data[0]
print(max)

# map(int,input().split()) --> 띄어쓰기 인식, 엔터는 아예 넘어감
# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수!!!