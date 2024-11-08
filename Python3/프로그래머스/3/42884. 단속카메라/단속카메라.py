def solution(routes):
    answer = 0
    temp = -30001
    routes.sort(key = lambda x : x[1])
    # print(routes)
    for route in routes :
        if route[0] <= temp <= route[1] :
            continue
        else :
            temp = route[1]
            answer += 1
    return answer