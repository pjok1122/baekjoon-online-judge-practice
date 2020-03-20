'''
heapq : 우선순위 큐 (heap을 구현한 라이브러리)

숫자가 작은 것이 우선순위가 높다. (Min-heap)
max_heap을 만들기 위해서는, item의 값에 -를 붙여서 삽입하면 된다. 

'''

import heapq

h = []
heapq.heappush(h, 1)
heapq.heappush(h, 2)
heapq.heappush(h, 4)
heapq.heappush(h, 9)

'''
1. heapq를 사용한다.
2. 현재 시간을 반드시 기억하고 있어야 한다.
3. 조심해야 할 것 : 현재 시간에 문서가 하나도 안들어와있을 떄, 현재 시간을 가장 빠른 문서 시간으로 이동시킨다.
'''
