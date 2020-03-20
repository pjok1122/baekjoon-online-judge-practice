class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __del__(self):
        self.val = None
        self.left, self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        new_node.left = None
        new_node.right = None

        root = self.root
        while(root != None):
            pre = root
            if root.val > val:
                root = root.left
            else:
                root = root.right

        if pre.val > val:
            pre.left = new_node
        else:
            pre.right = new_node

    def search(self, val):
        temp = self.root
        while(temp != None):
            if temp.val > val:
                temp = temp.left
            elif temp.val < val:
                temp = temp.right
            elif temp.val == val:
                return temp
        return -1

    def delete(self, val):
        parent = None
        target = self.root

        while(target != None):
            parent = target
            if target.val == val:
                break
            elif target.val > val:
                target = target.left
            elif target.val < val:
                target = target.right
        if target == None:
            return -1

        # 단말노드인 경우
        if target.left == target.right == None:
            del target

        # 하나의 자식만을 가지는 경우
        elif target.left == None or target.right == None:
            child = target.left if target.left != None else target.right
            if parent.left == target:
                parent.left = child
            else:
                parent.right = child
            del target

        else:
            succ_p = target
            succ = target.right

            while(succ.left != None):
                succ_p = succ
                succ = succ.left

            if succ_p.left == succ:
                succ_p.left = succ.right  # 자리를 바꿀 노드가 오른쪽 자식을 가질 수 있기 때문!
            else:  # 왼쪽 자식이 없는 경우에 해당.
                #

            # Binary Search Tree임을 확인하는 함수


def is_BST(tree, min_val=-10000000, max_val=1000000):
    if tree == None:
        return True

    if not min_val <= tree <= max_val:
        return False

    return is_BST(tree.left, min_val, tree.val) and is_BST(tree.right, tree.val, max_val)
