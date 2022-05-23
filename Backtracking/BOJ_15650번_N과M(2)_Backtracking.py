N, M = map(int, input().split())

def Backtrack(num, ans, visited):
    
    # 방문 처리
    ans.append(num+1)
    visited[num] = True

    # 정답의 길이가 M인 경우 -> 출력하고 그만두기.
    if len(ans) == M:
        ans_string = ""
        for a in ans:
            ans_string += str(a) + " "
        print(ans_string)
        return

    for i in range(num+1, N):   # 현재 수 ~ N-1
        if visited[i] == False:
            Backtrack(i, ans, visited)
            # 후에 i의 흔적 지우기
            ans.remove(i+1)
            visited[i] = False


visited = [False] * N   # 0 ~ N-1 방문기록
for n in range(N):
    Backtrack(n, [], visited)
    visited = [False] * N   # 방문 기록 초기화