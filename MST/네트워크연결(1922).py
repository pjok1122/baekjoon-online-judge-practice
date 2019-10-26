import sys
import heapq
n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
selected_nodes = []
for i in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    arr[s].append((e, c))
    arr[e].append((s, c))


def MST_prim():
    h = []
    selected_nodes.append(1)
    result = 0
    for e, c in arr[1]:
        heapq.heappush(h, (c, e))

    while(len(selected_nodes) != n):
        c, e = heapq.heappop(h)
        if e in selected_nodes:
            continue

        selected_nodes.append(e)
        result += c
        for e, c in arr[e]:
            heapq.heappush(h, (c, e))

    return result


print(MST_prim())
