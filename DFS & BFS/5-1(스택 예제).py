# 파이썬에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요가 없다
stack=[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop()

stack.append(1)
stack.append(4)

stack.pop()

print(stack)        # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소부터 출력

# 최종 stack
# 1
# 3
# 2
# 5