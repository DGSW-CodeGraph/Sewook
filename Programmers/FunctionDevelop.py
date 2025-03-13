def getDeploy(p, s):
    if (100 - p) % s != 0:
        return (100 - p) // s + 1
    return (100 - p) // s


def solution(progresses, speeds):
    answer = []
    temp = []
    t = 0
    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]
        deploy = getDeploy(p, s)
        temp.append(deploy)
    for i in temp:
        if len(answer) != 0:
            print(t, i)
            if t >= i:
                answer.append(answer.pop() + 1)
            else:
                t = i
                answer.append(1)
        else:
            t = i
            answer.append(1)

    return answer