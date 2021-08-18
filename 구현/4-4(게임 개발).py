# N,M=map(int,input().split())
# A,B,d=map(int,input().split())

# game_map=[]
# for i in range(N):
#     line=list(map(int,input().split()))
#     game_map.append(line)    
# print(game_map)

# count=0 # 확인한 뱡향이 몇개냐, 4가 되면 사방 확인한 것이므로 move3으로 이동
# visited=[(A,B)]  # 방문한 좌표 기록

# def move1():
#     global d
#     d-=1
#     if d==-1:d=3    # 북 -> 서

# count=0
# def move2():
#     global count, A, B, d
#     # count가 4인지 확인, 4라면 move3실행
#     if count==4:
#         move3(A,B,d)

#     # 따져야할 조건: d, 맵 벗어나지 않기, 바다냐, 이미 방문했나
#     # 북쪽
#     if d==0 and A!=1 and game_map[A-1][B]==0 and visited.find((A-1,B))==-1:
#         A-=1
#         visited.append((A,B))
    
#     # 동쪽
#     elif d==1 and B!=M and game_map[A][B+1]==0 and visited.find((A,B+1))==-1:
#         B+=1
#         visited.append((A,B))
    
#     # 남쪽
#     elif d==2 and A!=N and game_map[A+1][B]==0 and visited.find((A+1,B))==-1:
#         A+=1
#         visited.append((A,B))
    
#     # 서쪽
#     elif d==3 and B!=1 and game_map[A][B-1]==0 and visited.find((A,B-1)):
#         B-=1
#         visited.append((A,B))   

#     else:
#         count+=1
#         move1(A,B,d)    # 다시 move1로 돌아가서 왼쪽으로 회전하려구 


# def move3():
#     global count,A,B,d
#     count=0
#     # 따져야할 조건: d, 맵 벗어나지 않기, 바다냐
#     # 북쪽
#     if d==0 and A!=N and game_map[A+1][B]==0:
#         A+=1    # d유지한 채로 뒤로 한칸 움직이기

# 방향을 설정해서 이동하는 문제일 때 dx, dy 정의하기!!
# 해설지
# N, M을 공백으로 구분하여 입력받기
N, M= map(int,input().split())

# 방문한 위치를 저장하기 위한 맵을 생성, 0으로 초기화
d=[[0]*M for _ in range(N)]

# 현재 캐릭터의 x좌표, y좌표, 방향을 입력 받기
x, y, direction=map(int,input().split())
d[x][y]=1   # 방문 처리

# 전체 맵 정보를 입력 받기
array=[]
for i in range(N):
    array.append(list(map(int,input().split())))    # array에 list를 행으로 집어넣기

# 북(0), 동(1), 남(2), 서(3)
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

# 왼쪽으로 회전 함수 정의
def turn_left():
    global direction
    direction-=1
    if direction==-1:   # 서
        direction=3

# 시뮬레이션 시작
count=1 # 결과 (내가 밟은 땅 수)
turn_time=0 # 내가 이 땅에서 회전한 수

while True:
    # 왼쪽으로 회전
    turn_left()
    # 회전 후 한칸 전진 (nx, ny : next x,y)
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny]==0: # 아직 방문x and 육지임
        d[nx][ny]=1     # 방문했으니깐 1로 바꿔줌
        # 이동
        x=nx
        y=ny
        count+=1    # 새 땅 밟음
        turn_time=0 # 새 땅이니깐 회전수 0으로 바꿔줌
        continue

    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time+=1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time==4:    # 사방을 모두 돌아봤는데 갈 곳 x
        # 현 위치에서 뒤로 한칸 이동
        nx=x-dx[direction]
        ny=y-dy[direction]
        # 뒤로 갈 수 있다면, 뒤로 가기
        if array[nx][ny]==0:
            x=nx
            y=ny
        # 뒤가 바다 
        else:
            break   # 끝!
        turn_time=0

print(count)