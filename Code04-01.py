##단순연결 리스트의 간단구현!

class Node():
    def __init__(self):
        self.data=None
        self.link=None


node1=Node()
node1.data='다현'

node2=Node()
node2.data='정연'

node1.link=node2

node3=Node()
node3.data='쯔위'

node2.link=node3

node4=Node()
node4.data='사나'
node3.link=node4

node5=Node()
node5.data='지효'
node4.link=node5

#헤드만잡아주면 나머지요소들은 link로들어감 node1의 링크된거의 링크된거의 링크된거의...(갯수만큼)
print(node1.data, end='  ')
print(node1.link.data, end='  ')
print(node1.link.link.data, end='  ')
print(node1.link.link.link.data, end='  ')
print(node1.link.link.link.link.data, end='  ')


#연결리스트 삽입
newNode=Node()
newNode.data='재남'
newNode.link=node2.link #재남과 node2를 링크한다
node2.link=newNode 

#연결리스트 삭제

node2.link=node3.link #노드2를 노드3에링크하고
del(node3)#기존노드3은삭제

#current =변수. 현재작업중인 것

current=node1
print(current.data, end='')

while(current.link != None): #노드의 끝까지 출력하는문. 비어있는지 아닌지를 판단해서
    current=current.link
    print(current.data,end='')
print()
