#2126753390
#1702766719


s = 1
e = 2126753390
target = 1702766719
firstBadVersion = e
while(s<=e):
    m = (s+e)//2

    if(m >= target):
        firstBadVersion = m
        e = m - 1
    else:
        s = m + 1

print(firstBadVersion)


