N, M=map(int,input().split())

ice_map=[]
for i in range(N):
    ice_map.append(list(map(int,input().split())))

visited=[[False]*M for _ in range(N)]   # N x M

# [y축][x축]    총: [N][M]
d=[(1,0),(-1,0),(0,1),(0,-1)]   # 북, 남, 동, 서

def dfs(ice_map,v,visited): # 현위치 v=(n,m)의 tuple형태, v[0],v[1] 형태로 추출하자
    # 현재 노드 방문처리하기
    visited[v[0]][v[1]]=True
    print(v)
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in d:
        n=v[0]+i[0]
        m=v[1]+i[1]
        if n<0 or m<0 or n>=N or m>=M:
            continue
        # 따져야할 조건: 아직 방문 x + 구멍 뚫려 있는 부분인지
        if not visited[n][m] and ice_map[n][m]==0:
            dfs(ice_map,(n,m),visited)

result=0
# dfs 함수 호출
for i in range(N):
    for j in range(M):
        if ice_map[i][j]==0 and visited[i][j]==False:
            result+=1
            dfs(ice_map,(i,j),visited)


#dfs(ice_map,(0,0),visited)
print(visited)
print(result)