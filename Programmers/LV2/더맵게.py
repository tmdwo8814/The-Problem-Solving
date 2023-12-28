from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            break
        
        first = heappop(scoville)
        sec = heappop(scoville)
        
        heappush(scoville, first + sec*2)
        
        answer += 1
        
    if scoville[0] < K and len(scoville) == 1:
        return -1
    
    return answer