### 입력 받기, 초기화 ###
n = int(input())

students = [[0]*5 for _ in range(n*n)] # n0: 학생, n1,n2,n3,n4: 좋아하는 친구들
for i in range(n*n):
    students[i] = list(map(int, input().split()))

attraction = [[-1]*n for _ in range(n)] # 비어있을 경우 -1로 초기화

### 로직 ###
# 1) 인접 칸 중 좋아하는 친구가 가장 많은 위치
# 2) 인접 칸 중 비어있는 칸이 가장 많은 위치
# 3) 행 번호가 작은 위치
# 4) 열 번호가 작은 위치

# attraction[i][j]의 인접한 자리에 대한 계산
def count(i, j, attraction, friends): # i: 행, j: 열
    cnt_friend = 0; cnt_empty = 0
    ### 상
    if 0 <= i-1:
        if attraction[i-1][j]==-1: # 비어있는지
            cnt_empty += 1
        else: # 비어있지 않다면, 그 자리에 좋아하는 친구가 있는지
            if attraction[i-1][j] in friends:
                cnt_friend += 1
    ### 하
    if i+1 <= n-1:
        if attraction[i+1][j]==-1: # 비어있는지
            cnt_empty += 1
        else: # 비어있지 않다면, 그 자리에 좋아하는 친구가 있는지
            if attraction[i+1][j] in friends:
                cnt_friend += 1
    ### 좌
    if 0 <= j-1:
        if attraction[i][j-1]==-1: # 비어있는지
            cnt_empty += 1
        else: # 비어있지 않다면, 그 자리에 좋아하는 친구가 있는지
            if attraction[i][j-1] in friends:
                cnt_friend += 1
    ### 우
    if j+1 <= n-1:
        if attraction[i][j+1]==-1: # 비어있는지
            cnt_empty += 1
        else: # 비어있지 않다면, 그 자리에 좋아하는 친구가 있는지
            if attraction[i][j+1] in friends:
                cnt_friend += 1
    res = (cnt_friend, cnt_empty)
    return res

### main ###
for idx in range(n*n):
    student = students[idx][0] # 탑승할 학생
    friends = students[idx] # 좋아하는 친구들 (n1,n2,n3,n4)

    seats = [] # 후보 자리들
    cnt_friend_max = 0; cnt_empty_max = 0 # 현재까지 나온 cnt의 최대값
    ### 놀이기구 자리를 완전 탐색 ###
    for i in range(0, n):
        for j in range(0, n):
            if attraction[i][j]==-1: # (i, j) 자리가 비어있는지
                # 우선 순위 1,2에 대한 계산
                cnt_friend, cnt_empty = count(i, j, attraction, friends)
                if cnt_friend_max == cnt_friend: # 인접한 친구 수가 기존 max값과 동일
                    if cnt_empty_max == cnt_empty: # 인접한 빈자리 수까지 동일
                        seats.append((i,j))
                    elif cnt_empty_max < cnt_empty: # 빈 자리 수가 기존 max값보다 더 큼
                        seats = [(i,j)]
                        cnt_empty_max = cnt_empty

                if cnt_friend_max < cnt_friend: # 인접한 친구 수가 기존 max값보다 더 큼
                    seats = [(i,j)]
                    cnt_friend_max = cnt_friend
                    cnt_empty_max = cnt_empty

    # 우선순위 1,2가 동일한 자리가 여러개인 경우 우선순위 3,4로 판단
    seats.sort(key=lambda x: (x[0], x[1]))
    r, c = seats[0]
    attraction[r][c] = student

# 학생 목록을 학생 번호순으로 재정렬
students.sort(key=lambda x:x[0])

# 최종 점수
ans = 0

### 정답 계산 ###
for i in range(n):
    for j in range(n):
        ans_student = 0 # 이 학생이 인접하고 있는 좋아하는 친구의 수
        student = attraction[i][j] # 학생
        friends = students[student-1] # 좋아하는 친구들
        ### 상
        if 0 <= i-1:
            if attraction[i-1][j] in friends:
                ans_student += 1
        ### 하
        if i+1 <= n-1:
            if attraction[i+1][j] in friends:
                ans_student += 1
        ### 좌
        if 0 <= j-1:
            if attraction[i][j-1] in friends:
                ans_student += 1
        ### 우
        if j+1 <= n-1:
            if attraction[i][j+1] in friends:
                ans_student += 1
        ### 이 학생에 대한 점수 계산
        score = [0,1,10,100,1000]
        ans += score[ans_student]

print(ans)
