from collections import deque

M, N, H = map(int, input().split()) # M: 가로, N: 세로, H: 높이
tomatos = [[0] for _ in range(N*H)]
# tomatos[t]일 때, 같은 높이: t//H, 위아래: |위-아래|/H=0, M도 같아야 함
for i in range(N*H):
    tomatos[i] = list(map(int, input().split()))
    # 1: 익은 토마토, 0: 안 익은 토마토, -1: 토마토 X
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

Q = deque() # bfs에서 쓰일 큐
# check 함수에서 할 것
# 1) 토마토가 모두 익지 못하는 상황인지 체크 => 나중에 확인하기
# 2) 모든 토마토가 이미 익어있는 상황인지 체크
# 3) 이미 익어있는 토마토 Q에 넣기
def check(Q, tomatos):
    tomato0 = 0
    for i in range(0, N * H):
        for j in range(0, M):
            # 큐에 익은 토마토 담기
            if tomatos[i][j]==1:
                Q.append((i,j,0))
            elif tomatos[i][j]==0:
                tomato0 += 1
    # 모든 토마토가 이미 익어있는지 체크
    if tomato0==0: # 익지 않은 토마토 개수 == 0
        return 0
    return Q

### 토마토 익히기 시작 ###
def BFS(Q, cnt, tomatos):
    visited = [[False] * M for _ in range(N * H)]
    # cnt = 0
    while Q: # BFS
        q = Q.popleft() # 익힌 토마토 하나 큐에서 꺼내기
        q_i, q_j, cnt_new = q
        # 날짜 카운트 +1
        if cnt < cnt_new:
            cnt = cnt_new

        h = q_i//N  # 몇 층인지
        visited[q_i][q_j] = True
        # 주변 토마토 익히기 -> 좌우
        if 0 <= q_j - 1:  # 좌
            if tomatos[q_i][q_j - 1] == 0:
                tomatos[q_i][q_j - 1] = 1  # 익히기
                Q.append((q_i, q_j-1, cnt+1))
        if q_j + 1 <= M - 1:  # 우
            if tomatos[q_i][q_j + 1] == 0:
                tomatos[q_i][q_j + 1] = 1  # 익히기
                Q.append((q_i, q_j+1, cnt+1))
        # 주변 토마토 익히기 -> 상하 (같은 층)
        if (q_i-1)//N == h:  # 위
            if tomatos[q_i - 1][q_j] == 0:
                tomatos[q_i - 1][q_j] = 1  # 익히기
                Q.append((q_i-1, q_j, cnt+1))
        if (q_i + 1)//N == h:  # 아래
            if tomatos[q_i + 1][q_j] == 0:
                tomatos[q_i + 1][q_j] = 1  # 익히기
                Q.append((q_i+1, q_j, cnt+1))
        # 주변 토마토 익히기 -> 위아래층
        if 0 <= q_i - N:  # 아래층
            if tomatos[q_i - N][q_j] == 0:
                tomatos[q_i - N][q_j] = 1  # 익히기
                Q.append((q_i-N, q_j, cnt+1))
        if q_i + N <= N * H - 1:
            if tomatos[q_i + N][q_j] == 0:
                tomatos[q_i + N][q_j] = 1  # 익히기
                Q.append((q_i+N, q_j, cnt+1))

    return cnt


### main ###
result = check(Q, tomatos)
if result == 0:
    print(0)
else:
    # 토마토 익히기 시작
    cnt = BFS(result, 0, tomatos)
    flag = 0
    for i in range(N*H):
        if 0 in tomatos[i]:
            flag = 1
            break
    if flag==1:
        print(-1)
    else:
        print(cnt)
