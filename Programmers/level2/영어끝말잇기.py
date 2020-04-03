
# tank - kick - kit - tank   , 4명

def solution(n, words):
    dic ={}
    next = words[0][0]
    for i,word in enumerate(words):
        if word in dic.keys() or not word.startswith(next):
            return [i%n +1, i//n + 1]
        
        dic[word] = True
        next = word[-1]

    return [0,0]
        

