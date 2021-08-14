# 내 답
# N=int(input())

# data=list(map(int,input().split()))
# data.sort()

# res=0
# count=0
# i=0
# while i<N:
#     count+=1    #나 자신 카운트
    
#     if count==data[i]:  #끝
#         res+=1
#         count=0

#     i+=1    #다음 원소로 넘어가기

# print(res)

#해설지
n=int(input())
data=list(map(int,input().split()))
data.sort()

result=0    # 총 그룹 수
count=0     # 현재 그룹에 포함된 모험가의 수

for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
    count+=1    # 현재 그룹에 해당 모험가를 포함시키기
    if count>=i:    # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성!
        result+=1   # 총 그룹의 수 증가시키기
        count=0     # 현재 그룹에 포함된 모험가의 수 초기화

print(result)   # 총 그룹의 수 출력