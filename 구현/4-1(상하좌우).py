# 내 답
# N=int(input())  # N x N
# data=list(map(str, input().split()))     # 여행 계획서

# # (X, Y) 초기값
# X=1
# Y=1

# for i in data:
#     print(i)
#     if i=="R":
#         if Y<N:
#             Y+=1
#     elif i=="L":
#         if Y>1:
#             Y-=1
#     elif i=="U":
#         if X>1:
#             X-=1
#     elif i=="D":
#         if X<N:
#             X+=1
    
# print(X, Y)

# 해설지
# N을 입력받기
N=int(input())
X, Y=1,1
plans=input().split()

# L, R, U, D에 따른 이동방향
dx=[0,0,-1,1]   # x축으로 U는 -1,   D는 +1
dy=[-1,1,0,0]   # y축으로 L은 -1,   R은 +1
move_types=["L", "R", "U", "D"]

for plan in plans:
    for j in range(len(move_types)):
        if plan==move_types[j]:
            nx=X+dx[j]
            ny=Y+dy[j]
        
    if nx>N or nx<1 or ny>N or ny<1:
        continue
    else:
        X=nx
        Y=ny

print(X, Y)