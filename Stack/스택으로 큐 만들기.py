'''
데이터를 스택에 순서대로 넣은 뒤, 스택에 있는 내용을 전부 새로운 스택으로 옮기면 된다.
'''


class Queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def push(self, item):
        self.inbox.append(item)

    def pop(self):
        if len(self.outbox) == 0:
            while self.inbox:
                self.outbox.append(self.inbox.pop(-1))

        return self.outbox.pop(-1)


if __name__ == "__main__":
    q = Queue()
    q.push("A")
    q.push("B")
    print(q.pop())
    q.push("C")
    print(q.pop())
    print(q.pop())
