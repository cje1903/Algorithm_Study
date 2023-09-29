n, m = map(int, input().split()) # n: 격자 크기, m: 리브로스를 키우는 년 수
trees = [[0] for i in range(n) ]
for i in range(0,n):
    trees[i] = list(map(int, input().split()))
moves = []
for i in range(m):
    d, p = map(int, input().split()) # d: 이동 방향, p: 이동 칸 수
    moves.append((d, p))

# 좌표: (y, x) - y: 세로, x: 가로
# 좌표 범위: 0 ~ n-1
# → ↗ ↑ ↖ ← ↙ ↓ ↘
dxy = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

# 영양제 초기 위치
nutrients = [(n-1, 0), (n-2, 0), (n-1, 1), (n-2, 1)]

### m년 동안 리브로 재배 ###
for year in range(m):
    ### move ###
    d, p = moves[year]
    move_y, move_x = dxy[d-1]
    # p번 이동
    for i in range(p):
        cnt_nutrients = len(nutrients)
        for j in range(cnt_nutrients):
            nutrient_y, nutrient_x = nutrients[j]
            nutrient_y += move_y; nutrient_x += move_x
            # 끝에 도달했을 경우 반대로 보내기
            if nutrient_y==n:
                nutrient_y = 0
            elif nutrient_y==-1:
                nutrient_y = n-1
            if nutrient_x==n:
                nutrient_x = 0
            elif nutrient_x==-1:
                nutrient_x = n-1

            nutrients[j] = (nutrient_y, nutrient_x)

    ### 성장 ###
    for nutrient in nutrients:
        nutrient_y, nutrient_x = nutrient
        trees[nutrient_y][nutrient_x] += 1

    past_nutrients = []
    while nutrients:
        nutrient = nutrients.pop()
        nutrient_y, nutrient_x = nutrient
        past_nutrients.append(nutrient)

        # 대각선 나무의 높이에 따라 추가 성장
        cnt = 0
        if 0 <= nutrient_y+1 <= n-1 and 0 <= nutrient_x+1 <= n-1:
            if trees[nutrient_y+1][nutrient_x+1] >= 1: cnt += 1
        if 0 <= nutrient_y+1 <= n-1 and 0 <= nutrient_x-1 <= n-1:
            if trees[nutrient_y+1][nutrient_x-1] >= 1: cnt += 1
        if 0 <= nutrient_y-1 <= n-1 and 0 <= nutrient_x+1 <= n-1:
            if trees[nutrient_y-1][nutrient_x+1] >= 1: cnt += 1
        if 0 <= nutrient_y-1 <= n-1 and 0 <= nutrient_x-1 <= n-1:
            if trees[nutrient_y-1][nutrient_x-1] >= 1: cnt += 1
        trees[nutrient_y][nutrient_x] += cnt

    ### new_nutrients ###
    for i in range(0, n): # y
        for j in range(0, n): # x
            if (i, j) not in past_nutrients:
                if trees[i][j] >= 2:
                    trees[i][j] -= 2
                    nutrients.append((i, j))

### 정답 출력 ###
ans = 0
for i in range(n):
    ans += sum(trees[i])
print(ans)
