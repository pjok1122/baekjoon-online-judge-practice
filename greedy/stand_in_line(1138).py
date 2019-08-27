'''
1. Permutation을 이용해도 Pass 할 확률이 높다. 제한시간이 2초기 때문. 다만, 메모리 제한이 128MB 이기 때문에, 모든 Permutation을 저장해두고 사용하는 방식은 바람직하지 못함.
2. Permutation은 무식하게 해결하는 방법이므로 Greedy한 접근이라고 볼 수 없음.
3. 이 문제의 핵심 아이디어는 작은 숫자부터 나열할 경우 어디에 나열해야 하는지 위치를 바로 결정할 수 있다는 것!
4. 작은 숫자부터 나열할 경우, 왼쪽 빈 자리의 갯수 == 나보다 큰 숫자의 갯수 라는 규칙이 성립함.
5. 이유를 잘 생각해보면 다음과 같음. 작은 숫자부터 나열하기 때문에, 현재 숫자를 나열할 때에는 반드시 자신보다 작은 숫자만 존재함.
6. 또한 그 이후에 나열되는 모든 숫자는 자신보다 큰 숫자임이 분명함.
7. 이정도로도 수학적으로 충분히 증명이 가능하다.
8. 시간복잡도 : O(1)
'''
N = int(input())
data = [-1] + list(map(int,input().split()))
result = [-1]*N
index = list(range(N))
for i in range(1,N+1):
    result[index.pop(data[i])] = i

print(' '.join(str(e) for e in result))