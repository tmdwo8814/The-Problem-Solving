def solution(n, works):
    answer = 0
    while n:
        works.sort()

        max_count = works.count(max(works))
        if max(works) == min(works):
            gap = 0
        else:
            gap = max(works) - works[-(max_count + 1)]

        if sum(works) <= n:
            return 0
        
        elif max_count > n:
            for i in range(1, n+1):
                works[-i] -= 1
                n -= 1

        elif min(works) == max(works):
                if max_count * max(works) > n:
                    minus = n // max_count
                    for i in range(1, max_count):
                        works[-i] -= minus
                        n -= minus

            
        else:
            for i in range(gap, 1, -1):
                if gap * max_count > n:
                    continue
                elif gap * max_count <= n:
                    for j in range(1, max_count):
                        works[-j] -= i
                        n -= i
                    break

    
    for i in works:
        answer += i*i

    return answer

   
print(solution(4, [4, 3, 3]))