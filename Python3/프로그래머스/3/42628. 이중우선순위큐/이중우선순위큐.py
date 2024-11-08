import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    entry_count = {}
    
    for operation in operations:
        op_list = operation.split()
        if op_list[0] == 'I':
            num = int(op_list[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry_count[num] = entry_count.get(num, 0) + 1
        elif op_list[0] == 'D':
            if not entry_count:
                continue  # 힙이 비어있으면 다음 명령으로 넘어갑니다.
            if op_list[1] == '1':
                # 최댓값 삭제
                while max_heap:
                    num = -heapq.heappop(max_heap)
                    if entry_count.get(num, 0) > 0:
                        entry_count[num] -= 1
                        if entry_count[num] == 0:
                            del entry_count[num]
                        break
            elif op_list[1] == '-1':
                # 최솟값 삭제
                while min_heap:
                    num = heapq.heappop(min_heap)
                    if entry_count.get(num, 0) > 0:
                        entry_count[num] -= 1
                        if entry_count[num] == 0:
                            del entry_count[num]
                        break
    if not entry_count:
        return [0, 0]
    else:
        # 최댓값 찾기
        while max_heap:
            num = -max_heap[0]
            if entry_count.get(num, 0) > 0:
                max_num = num
                break
            else:
                heapq.heappop(max_heap)
        # 최솟값 찾기
        while min_heap:
            num = min_heap[0]
            if entry_count.get(num, 0) > 0:
                min_num = num
                break
            else:
                heapq.heappop(min_heap)
        return [max_num, min_num]
