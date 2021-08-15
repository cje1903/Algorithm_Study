# 내 답
# def solution(food_times, k):
#     answer = 0
    
#     t=0
#     i=0 #food번호 (0번~len(food_times)-1번)
    
#     while t<=k:
#         while food_times[i]==0: #남은 food 찾기
#             i+=1
#             if i==len(food_times):
#                 i=0
#         t+=1
#         i+=1
#         if i==len(food_times):
#             i=0
    
#     answer=i+1
#     if answer==len(food_times):
#         answer=1

#     return answer

# print(solution([3,1,2],5))

# 해설지
# 우선 순위 큐 사용!!!!


import heapq

def solution(food_times,k):
    #  전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <=k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q=[]    #우선순위 큐
    for i in range(len(food_times)):
        # (먹는데 걸리는 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q,(food_times[i],i+1))

    sum_value=0 # 먹기 위해 사용한 시간
    previous=0  # 직전에 다 먹은 음식 시간
    length=len(food_times)  # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value+((q[0][0]-previous)*length)<=k:
        now=heapq.heappop(q)[0]
        sum_value+=(now-previous)*length
        length-=1   # 다 먹은 음식은 제외시키기
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result=sorted(q,key=lambda x:x[1])  # 음식의 번호 기준으로 정렬
    return result[(k-sum_value)%length][1]

# ex) 1번-8초, 2번-6초, 3번-4초, k=15
# 최소 힙
#       [4초, 3번]
#       /         \
# [6초, 2번]    [8초, 1번]

# while문 한바퀴
# sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 <=k ???
# 0 + (4초-0초) * 3개 =12 <=15
# now=heapq.heappop(q)[0] 이므로, [4초, 3번]은 pop
# sum_value+=(now-previous)*length=0+(4-0)*3=12
# 총 음식 3개 중 1개 다 먹었으므로, length=2
# previous=now  -> previous=4

# sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 <=k ???
# 12 + (6초-4초) * 2개 =16 <=15     x
# result=sorted(q, key=lambda x:x[1])   x[1]: 음식 번호를 기준으로 정렬한다는 것을 의미, 왜냐면 이젠 음식 번호 순으로 세볼 거니깐
# result[]=[(1번음식, 8초), (2번음식, 6초)]
# result[(k-sum_value)%length][1]
# result[(15-12)%2  =   1][1]
# result의 1번째 인덱스에 있는 것: 2번음식!! 정답은 2번 음식~~~