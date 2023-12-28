# 내가 짠 코드
# 73.3 / 100.0

# def solution(n, works):
#     answer = 0
#     while n:
#         works.sort()

#         max_count = works.count(max(works))
#         if max(works) == min(works):
#             gap = 0
#         else:
#             gap = max(works) - works[-(max_count + 1)]

#         if sum(works) <= n:
#             return 0
        
#         elif max_count > n:
#             for i in range(1, n+1):
#                 works[-i] -= 1
#                 n -= 1

#         elif min(works) == max(works):
#                 if max_count * max(works) > n:
#                     minus = n // max_count
#                     for i in range(1, max_count+1):
#                         works[-i] -= minus
#                         n -= minus

            
#         else:
#             for i in range(gap, 0, -1):
#                 if gap * max_count > n:
#                     continue
#                 elif gap * max_count <= n:
#                     for j in range(1, max_count+1):
#                         works[-j] -= i
#                         n -= i
#                     break

    
#     for i in works:
#         answer += i*i

#     return answer

# 정답코드
# 우선순위 큐 - heap 이용

import heapq

def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    
    works = [-i for i in works]
    
    heapq.heapify(works)
    
    while n:
        popped = heapq.heappop(works)
        heapq.heappush(works, popped + 1)
        
        n -= 1
        
    for i in works:
        answer += i**2
    return answer
