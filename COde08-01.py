##함수

from turtle import right


class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


##전역


##메인

node1 =TreeNode()
node1.data ='화사'

node2=TreeNode()
node2.data='솔라'
node1.left=node2

node3=TreeNode()
node3.data='휘인'
node2.left=node3

node4=TreeNode()
node4.data='쯔위'
node3.right=node4

node5=TreeNode()
node5.data='문별'
node1.left=node5

node6=TreeNode()
node6.data='선미'
node2.left=node6

root=node1

print(root.data)
print(root.left.data,root.right.data)
print(root.left.left.data, root.left,right.data)