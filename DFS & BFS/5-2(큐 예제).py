# 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용하자!
# deque는 스택과 큐의 장점을 모두 채택한 것인데, 데이터를 넣고 빼는 속도가 리스트 자료형에 비해서 효율적이며, queue 라이브러리를 이용하는 것보다 더 간단하다
# 더불어 대부분의 코딩테스트에서 collections 모듈과 같은 기본 라이브러리 사용을 허용하므로 안심하고 사용해도 괜찮다.

from collections import deque

queue=deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.popleft() # 5 삭제

queue.append(1)
queue.append(4)

queue.popleft() # 2 삭제

queue=list(queue)   # list로 변환 가능

print(queue)    # 먼저 들어온 순서로
queue.reverse() # 역순
print(queue)    # 늦게 들어온 순서로