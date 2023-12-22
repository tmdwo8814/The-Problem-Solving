def solution(n, works):
    answer = 0
    while n:
        works.sort()

        max_count = works.count(max(works))
        gap = max(works) - works[-(max_count + 1)]

        if max_count > n:
            for i in range(1, n+1):
                works[-i] -= 1
                n -= 1
        else:
            for i in range(gap, 1, -1):
                if gap * max_count > n:
                    continue
                elif gap * max_count <= n:
                    for j in range(1, max_count+1):
                        works[-j] -= i
                        n -= i
                    break


    return answer

   
print(solution(4, [4, 3, 3]))