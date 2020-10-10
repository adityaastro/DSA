class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, *newNode):
        nodes = []
        self.size += len(newNode)
        for entry in newNode:
            nodes.append(Node(entry))
        newNode = nodes
        if self.head is None:
            self.head = newNode[0]
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        for node in newNode:
            lastNode.next = node
            lastNode = node

    def insert(self, node, pos):
        self.size += 1
        node = Node(node)
        if not pos:
            headnode = node
            headnode.next = self.head
            self.head = headnode
        else:
            currNode = self.head
            i = 0
            while currNode:
                if i == pos - 1:
                    break
                currNode = currNode.next
                i += 1
            node.next = currNode.next
            currNode.next = node

    def __getitem__(self, pos):
        currNode = self.head
        i = 0
        while currNode:
            if i == pos:
                return currNode.data
            i += 1
            currNode = currNode.next
        raise ValueError('Index out of range')

    def __len__(self):
        return self.size

    def delete(self, element):
        i = 0
        self.size -= 1
        curNode = self.head
        prevNode = Node()
        while True:
            if curNode.data == element:
                break
            prevNode = curNode
            curNode = curNode.next
        prevNode.next = curNode.next
        if element == self.head.data:
            prevNode = self.head.next
            self.head = prevNode
        del curNode

    def __repr__(self):
        p = ""
        if self.head is None:
            return "[]"
        curNode = self.head
        while curNode:
            p += ", " + str(curNode)
            curNode = curNode.next
        return "[{}]".format(p[2:])


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, entry):
        self.stack.insert(entry, 0)

    def pop(self):
        self.last = self.stack.head.data
        self.stack.delete(self.last)
        return self.last

    def __len__(self):
        return self.stack.size

    def peek(self):
        return self.last

    def empty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return self.stack.__repr__()


def brackets(s):
    c = 0
    Brackets = Stack()
    for i in s:
        c += 1
        if i in ('(', '[', '{'):
            Brackets.push((i,c))
        elif i in (')', ']', '}'):
            if Brackets.empty():
                return c
            Top = Brackets.pop()[0]
            if (i == ')' and Top != '(') or (i == ']' and Top != '[') or (i == '}' and Top != '{'):
                return c
    if Brackets.empty():
        return 'Success'
    else:
        while not Brackets.empty():
            last = Brackets.pop()
        return last[1]


print(brackets(str(input())))
