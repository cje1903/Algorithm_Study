N, M, K, X = map(int,input().split())
# N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시
# 도로는 단방향

graph=[[] for _ in range(N+1)]  # 1 ~ N번 도시가 어느 도시와 연결되어 있는지 (단방향)

for i in range(M):
    a, b=map(int,input().split())
    graph[a].append(b)

for i in range(N+1):    # 오름차순으로 출력하기 위하여
    graph[i].sort()

print(graph)