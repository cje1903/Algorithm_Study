from collections import deque

N, M=map(int,input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,input().split())))

# [y축][x축]
# 상 하 좌 우
dx=[0,0,-1,1]   # x축
dy=[-1,1,0,0]   # y축

def bfs(n,m):
    
    # Queue 구현
    Q=deque()
    Q.append((n,m))

    # 큐가 빌 때까지 반복
    while Q:
        # 큐에서 front 원소를 뽑아 출력
        n,m=Q.popleft()
        # v와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in range(4):
            nextN=n+dy[i]
            nextM=m+dx[i]
            # 범위 벗어나지 않는지 확인
            if nextN<0 or nextM<0 or nextN>=N or nextM>=M:
                continue
            # 괴물이 있는지 확인
            if graph[nextN][nextM]==0:
                continue
            # 해당 노드를 처음 방문하는 경우만
            if graph[nextN][nextM]==1:
                graph[nextN][nextM]=graph[n][m]+1
                Q.append((nextN,nextM))
    
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[N-1][M-1]

print(bfs(0,0))