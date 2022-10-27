##함수
class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNodes(start): #자동출력문
    current=start
    print(current.data,end='')
    while(current.link !=Node):
        current=current.link
        print(current.data,end='')
    print()

def insertNode(findData,insertData):
    global memory, head, current, pre
    # Case1 : 머리 앞에 삽입 (다현, 화사) 
    if (findData == head.data) : #finddata가 head이면 실행
        node = Node()
        node.data = insertData
        node.link = head #헤드에 아까 위에서 생성한 노드를 넣음
        head = node
        memory.append(node)
        return

    # Case2 : 중간 노드에 삽입 (사나, 솔라)
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == findData) : #찾으려는 데이터와 현재(current)데이터가 일치하면
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node #pre가 있어야 원래잡고있던 링크를 놓치지않는다.
            memory.append(node)
            return

    # Case3 : 찾는 데이터가 없다== 마지막에 삽입(재남,문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData) :
    global memory, head, current, pre
    # Case1 : 하필 첫 노드를 삭제(다현)
    if(deleteData == head.data) :
        current = head
        head = head.link
        del(current)
        return
    # Case 2 : 중간 노드를 삭제(쯔위)
    current = head
    while (current.link != None) : #현재링크가 none이아닐때 실행 즉 다음노드가잇을때 실행됨
        pre = current
        current = current.link
        if (current.data == deleteData) : #넘아가다 deleteData를만나면 삭제실행
            pre.link = current.link
            del (current)
            return
    # Case 3 : 없는 노드를 삭제 (재남)
    return


#연결리스트 코딩 권장방법:헤드랑 섞어서 x 헤드따로 몸통따로
#아래는 찾는함수 구현
def findNode(findData):
    global memory,head,current, pre
    
    current = head  
    if(findData==current.data):
        return current
    while(current.link != Node):
        current =current.link
        if(findData==current.data):
            return current
    return Node()

## 전역
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연','쯔위', '사나', '지효']

## 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] : # ['정연','쯔위', ...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

# insertNode('다현', '화사')
# printNodes(head)
# insertNode('사나', '솔라')
# printNodes(head)
# insertNode('재남', '문별') #없는데이터(재남)을 찾아서 문별을 넣어라.
# printNodes(head)

# deleteNode('다현')
# printNodes(head)
deleteNode('쯔위')
printNodes(head)
deleteNode('재남')
printNodes(head)

