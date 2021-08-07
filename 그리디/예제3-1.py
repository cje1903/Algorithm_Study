N=int(input("거슬러 줘야 할 돈:"))

# total=0 #줘야할 동전의 갯수

# if N>=500:
#     total+=N//500
#     N-=N//500*500

# if N>=100:
#     total+=N//100
#     N-=N//100*100

# if N>=50:
#     total+=N//50
#     N-=N//50*50

# if N>=10:
#     total+=N//10
#     N-=N//10*10

# print(total)

coin_type=[500,100,50,10]

count=0

for i in coin_type:
    count+=N//i
    N%=i

print(count)