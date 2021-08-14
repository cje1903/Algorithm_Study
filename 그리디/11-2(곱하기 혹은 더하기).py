# 내 답
# S=input()

# res=int(S[0])
# print(type(res))
# i=1
# while i<len(S):
#     if res==0:
#         print("더했음"+str(res)+str(S[i]))
#         res+=int(S[i])
#     elif (S[i]==0 or S[i]==1):
#         print("더했음"+str(res)+str(S[i]))
#         res+=int(S[i])
#     else:
#         print("곱했음"+str(res)+str(S[i]))
#         res*=int(S[i])
#     i+=1

# print(res)

# 해설지
data=input()

# 첫 번째 문자를 숫자로 변경하여 대입
result=int(data[0])

for i in range(1,len(data)):
    #두 수 중에서 하나라도 0 혹은 1인 경우, 더하기 수행
    num=int(data[i])
    if num<=1 or result<=1:
        result+=num
    else: result*=num

print(result)