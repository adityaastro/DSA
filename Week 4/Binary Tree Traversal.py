# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
#
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def build(self, In):
#         tup = In[0]
#         self.root = Node(tup[0])
#         self.add_node(self.root, tup[1], tup[2], In)
#
#     def add_node(self, node, left, right, In):
#         if node and left != -1:
#             tupl = In[left]
#             node.left = Node(tupl[0])
#             self.add_node(node.left, tupl[1], tupl[2], In)
#
#         if node and right != -1:
#             tupr = In[right]
#             node.right = Node(tupr[0])
#             self.add_node(node.right, tupr[1], tupr[2], In)
#
#     def inorder(self, node):
#         if node:
#             self.inorder(node.left)
#             print(node.data,end=' ')
#             self.inorder(node.right)
#
#     def preorder(self, node):
#         if node:
#             print(node.data,end=' ')
#             self.preorder(node.left)
#             self.preorder(node.right)
#
#     def postorder(self, node):
#         if node:
#             self.postorder(node.left)
#             self.postorder(node.right)
#             print(node.data,end=' ')
#
# In = tuple(tuple(map(int, input().split())) for i in range(int(input())))
# T = BST()
# T.build(In)
# T.inorder(T.root)
# print()
# T.preorder(T.root)
# print()
# T.postorder(T.root)
import sys
import threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(input())
        self.key = [0] * self.n
        self.left = [0] * self.n
        self.right = [0] * self.n
        for i in range(self.n):
            a, b, c = map(int, input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def p(self):
        a = []
        b = []
        c = []
        def P(node):
            if node != -1:
                b.append(self.key[node])
                P(self.left[node])
                a.append(self.key[node])
                P(self.right[node])
                c.append(self.key[node])
        P(0)
        print(*a)
        print(*b)
        print(*c)


def main():
    tree = TreeOrders()
    tree.read()
    tree.p()


threading.Thread(target=main).start()
