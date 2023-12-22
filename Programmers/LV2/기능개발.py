def solution(progresses, speeds):
    answer = []
    while progresses:
        if (progresses[0] >= 100):
            count = 0
            while(progresses and progresses[0] >= 100):
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            answer.append(count)
        else:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

    return answer