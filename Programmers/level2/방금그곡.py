# 재생 시간이 0일 수 있음.

def solution(m, musicinfos):
    answer_running_time = 0
    answer_title =''

    m_running_time = len(m) - m.count('#')

    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(',')
        #재생 시간 계산.
        running_time = (int(end_time[0:2]) - int(start_time[0:2]))*60 + (int(end_time[3:5]) - int(start_time[3:5]))
        play_melody = []
        note_index = 0
        for i in range(running_time):
            if(note_index>=len(melody)):
                note_index %= len(melody)

            if(melody[note_index] =='#'):
                play_melody[-1] = play_melody[-1] + '#'
                play_melody.append(melody[(note_index+1)%len(melody)])
                note_index+=2
            else:
                play_melody.append(melody[note_index])
                note_index+=1
        
        for i in range(running_time - m_running_time + 1):
            if(m == ''.join(play_melody[i:i+m_running_time])):
                if answer_running_time < running_time:
                    answer_running_time = running_time
                    answer_title = title
                break
        
    return answer_title if answer_title != '' else "(None)"

# solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "23:55,00:00,WORLD,ABCDEF"]))
# print(solution('A',["12:00,12:14,HELLO,C#DEFGAB", "23:55,00:00,WORLD,ABCDEF"]))
# print(solution('A', ["12:00,12:14,HELLO,A", "12:24,12:40,WORLD,A"]))
# print(solution('ABC', ["00:00,00:00,DD,ABC"]))
print(solution("ABCDEFG", ["12:14,12:28,WORLD,CDEFGAB", "12:00,12:14,HELLO,CDEFGAB"]))
