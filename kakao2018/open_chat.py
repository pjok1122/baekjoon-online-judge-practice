def solution(records):
    answer = []
    Id =[]
    Action = []
    Dic = {} #아이디 : 닉네임

    for record in records:
        record = record.split()
        if record[0] =='Enter':
            Id.append(record[1])
            Action.append(record[0])
            Dic[record[1]] = record[2]
        elif record[0] == 'Leave':
            Id.append(record[1])
            Action.append(record[0])
        else:
            Dic[record[1]] = record[2]
    # print(Id)
    # print(Action)
    # print(Dic)


    for i in range(len(Id)):
        if Action[i]=="Enter":
            answer.append(Dic[Id[i]]+"님이 들어왔습니다.")
        elif Action[i] =="Leave":
            answer.append(Dic[Id[i]]+"님이 나갔습니다.")

    # print(answer)
    return answer


# if __name__=="__main__":
#     records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
#     solution(records)