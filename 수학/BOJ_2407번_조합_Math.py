# n C m 구하기
# 100 C 6 = 100! / 94! 6!

from math import factorial


n, m = map(int, input().split())

ans = factorial(n) // (factorial(n-m) * factorial(m))
print(ans)