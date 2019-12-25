import time

# i가 소수임을 확인하기 위해, 2부터 i//2+1 까지 나눠보는 방식.
# 시간복잡도 : O(n^2)


def solution1(n):
    answer = []
    for i in range(2, n+1, 1):
        prime = i
        for j in range(2, i//2+1, 1):
            if i % j == 0:
                prime = 0
                break
        if prime != 0:
            answer.append(prime)
    return len(answer)


# i가 소수임을 확인하기 위해 i보다 작은 소수들로 나눠보는 방식.
# 시간복잡도 : O(nlogn) (n보다 작은 소수의 개수를 대략 logn으로 가정)
def solution2(n):
    primes = [2]
    for i in range(2, n+1):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return len(primes)


# arr[i]=0인 경우에는 소수가 아닌 것으로 판단하며, arr[i]!=0인 경우에는 소수이므로 그 수의 배수를 모두 제거한다. (에라토스테네스의 체 효율성 높은 버전)
# 시간복잡도 : O(n)
def solution3(n):
    arr = list(range(0, n+1))
    result = []
    for i in range(2, len(arr)):
        if arr[i] == 0:  # 소수가 아닌 경우
            continue
        else:  # 소수인 경우
            result.append(arr[i])
            for j in range(arr[i], n+1, arr[i]):
                arr[j] = 0
    return len(result)


# 알고리즘 1 시간측정  (24초)
s_time = time.time()
solution1(100000)
e_time = time.time()
print("알고리즘 1 : ", e_time-s_time)

# 알고리즘2 시간측정 (4.7초)
s_time = time.time()
solution2(100000)
e_time = time.time()
print("알고리즘 2: ", e_time-s_time)

# 알고리즘3 시간측정 (0.02초)
s_time = time.time()
solution3(100000)
e_time = time.time()
print("알고리즘 3: ", e_time-s_time)
