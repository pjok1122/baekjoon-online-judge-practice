# 캐시 사이즈가 작음.

# 사이즈가 작아 큰 영향은 없지만 앞 제거 뒤 삽입이 많으므로 큐를 이용하는게 더적합했던 것 같음. 

def solution(cacheSize, cities):
    cache = []
    answer = 0

    if(cacheSize==0):
        return len(cities)*5

    for city in cities:
        city = city.upper()
        print(cache, answer)
        if city not in cache:
            answer+=5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
        else:
            index = cache.index(city)
            cache.pop(index)
            cache.append(city)
            answer+=1

    return answer

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))