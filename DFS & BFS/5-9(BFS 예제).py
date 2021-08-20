# BFS 과정
# BFS는 큐!! (FIFO)
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

from collections import deque

# BFS 메서드 정의
def bfs(graph,start,visited):
    # queue 구현
    Q=deque([start])

    # 현재 노드를 방문 처리
    visited[start]=True

    # 큐가 빌 때까지 반복
    while Q:
        # 큐에서 front 원소를 뽑아 출력
        v=Q.popleft()
        print(v,end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                Q.append(i)
                visited[i]=True     # 큐에 넣으면 방문처리 (그래야 다른 원소와 연결된 원소 삽입할 때 중복이 안 됨)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited=[False]*9

# bfs 호출
bfs(graph,1,visited)