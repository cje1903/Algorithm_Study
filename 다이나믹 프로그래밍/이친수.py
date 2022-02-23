# 백준 2193번

# top - down
dp = [0]*91 # dp[n]: n-1자리 이친수의 개수 (1<=n<=90)

def d(n):
    if dp[n]!=0: return dp[n]
    dp[n] = d(n-1) + d(n-2)     # n번째 자리가 1 -> dp[n-2]이고, 01 이어야 함 / n번째 자리가 0 -> dp[n-1] (바로 앞에 아무거나 상관x)
    return dp[n]
    
def solution():
    dp[0]=1 # 1
    dp[1]=1 # 10
    # 앞 2자리가 10인건 고정

    n = int(input())
    d(n-1)
    res = dp[n-1]
    print(res)

solution()