# 내 답 .. 몰라
# N=int(input())

# data=list(map(int,input().split()))
# data.sort()

# res=0
# i=1
# while i<=sum(data)+1:   #확실한 값:sum(data)+1
#     res+=1
#     #res값을 동전의 조합으로 만들 수 있나?
    

# # 모르겠다!!!!

#해설지
N=int(input())

data=list(map(int,input().split()))
data.sort()

# 작은 동전부터 시작해서 만들 수 없는 수 찾기
target=1
for x in data:
    #만들 수 없는 금액을 찾았을 때 반복 종료
    if target<x:
        break
    target+=x

print(target)
