# 내 답
# N=input()   # ex) a1
# x=N[0]
# alp=['a','b','c','d','e','f','g','h']
# x=alp.index(x)+1
# print(x)
# y=int(N[1])
# print(y)

# # 총 8가지 경우
# # 수평 2칸, 수직 1칸 경우   -   4가지 경우
# count_1=4
# if x<3 or x>6:
#     count_1-=2
#     if y==1 or y==8:
#         count_1-=1

# # 수직 2칸, 수평 1칸 경우   -   4가지 경우
# count_2=4
# if y<3 or y>6:
#     count_2-=2
#     if x==1 or x==8:
#         count_2-=1

# res=count_1+count_2
# print(res)

# 해설지
input_data=input()
row=int(input_data[1])  # 행
col=int(ord(input_data[0]))-int(ord('a'))+1 # 열

# 나이트가 이동할 수 있는 8가지 경우 정의
steps=[(-2,1), (-2,-1), (2,-1), (2,1), (1,2), (1,-2), (-1,2), (-1,-2)]

# 8가지 step으로 이동 가능한지 확인
res=0
for step in steps:
    next_col=col+step[1]
    next_row=row+step[0]
    if next_col>=1 and next_col<=8 and next_row>=1 and next_row<=8:
        res+=1
print(res)
