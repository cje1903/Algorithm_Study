# 내 답.. (틀림ㅠ.ㅠ) (백준 1439)
# S=input()

# res=0

# x=S[0]
# i=1
# count=0
# while i<len(S):
#     if x!=S[i]:
#         count+=1
#         x=S[i]
#     i+=1

# res=count-1

# if res==0:
#     res=1

# print(res)

# 해설지
S=input()

count0=0    # 모두 0으로 바꿀 때 필요 횟수
count1=0    # 모두 1로 바꿀 때 필요 횟수

if S[0]=='0':
    count1+=1
else: count0+=1

for i in range(len(S)-1):
    if S[i]!=S[i+1]:    #이번 것과 다음 것이 다를 경우
        if S[i+1]=='1':
            count0+=1
        else: count1+=1

res=min(count0,count1)
print(res)