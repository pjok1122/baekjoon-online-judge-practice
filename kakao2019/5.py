#기둥과 보를 놓을 수 있는가?
#기둥과 보를 삭제해도 되는가?

def isAvailable(build_frame):
    x,y, type, install = build_frame

    if type==0: #기둥은 밑이 '보' 이거나 '기둥'인 경우에 설치가능.  보 ==1, 기둥==2
        if install:
            if y==0:
                return 1
            if Map[x][y-1] == 2:
                return 1
            if Map[x-1][y] == 1:
                return 1
            if x-1>0 and Map[x-1][y] == 1:
                return 1
            if y<n and Map[x][y-1]:
                pass
        

def build(build_frame):
    x,y,type,build = build_frame
    if type==0:
        if install:
            Map[x][y] = 2

def solution(n, build_frames):
    answer = [[]]

    for build_frame in bulid_frames:
        


    return answer