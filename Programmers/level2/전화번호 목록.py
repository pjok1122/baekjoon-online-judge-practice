'''
문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
입출력 예제
phone_book	return
[119, 97674223, 1195524421]	false
[123,456,789]	true
[12,123,1235,567,88]	false
입출력 예 설명
입출력 예 #1
앞에서 설명한 예와 같습니다.

입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

[문제 풀이]

정렬과 startswith()를 이용해서 문제를 해결할 수도 있다. 하지만, 어떤 문자열이 접두어인지 확인하는 가장 빠른 방법은 Trie 자료구조를 사용하는 것이다.

Trie 자료구조의 insert를 주어진 조건에 맞게 구현하면 문제는 끝. 쉬운 문제에 속한다.
'''


class Node:
    def __init__(self, key, string=None):
        self.key = key
        self.string = string
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        exist_prefix = True
        for char in string:
            if cur_node.string != None:
                return False
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
                exist_prefix = False
            cur_node = cur_node.children[char]
        if exist_prefix == True:
            return False
        cur_node.string = string
        return True


def solution(phone_book):
    trie = Trie()
    for phone in phone_book:
        result_of_insert = trie.insert(phone)
        if result_of_insert == False:
            return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
