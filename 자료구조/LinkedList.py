'''
객체를 이용한 LinkedList 구현.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def push_last(self, data):
        new_node = Node(data)
        new_node.next = None

        if self.head == None:
            self.head = new_node
            return
        else:
            last = self.head
            while last.next != None:
                last = last.next

            last.next = new_node

    def get_all_items(self):
        pointer = self.head
        while pointer.next != None:
            print(pointer.data)
            pointer = pointer.next
        print(pointer.data)


linkedList = LinkedList()

linkedList.push(1)
linkedList.push(2)
linkedList.push(3)
linkedList.get_all_items()
print('################################')
linkedList = LinkedList()
linkedList.push_last(1)
linkedList.push_last(2)
linkedList.push_last(3)
linkedList.get_all_items()
