##함수

class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

##전역

memory=[]
root=None #아무것도없는 이진탐색트리
current =None #현재작업중인노드
nameAry=['블랙핑크','레드벨벳','트와이스','걸스데이','마마무','에이핑크']

##메인
node=TreeNode()
node.data=nameAry[0] #root가되는데이터
root=node
memory.append(node)

for name in nameAry[1:]: #네임어레이의 1번째 데이터부터 name에 넣음
    node=TreeNode()
    node.data=name
    
    current = root #무조건 root부터!

    #왼/오? ->root보다 작은건 왼쪽 큰건 오른쪽
    while True: #몇번까지 실행될지 몰라서 무한반복을시키고 예외처리,종료문(브레이크 등)을쓴다.
        if name < current.data: #언제까지?=자리를잡을때까지 무한반복
            if current.left==None: #current는 계속 바뀐다 root가currnet엿다가 그아래 노드가 current엿다가..
                current.left=node
                break #여기까지가 자리잡는곳
            current =current.left
        else :
            if current.right ==None :
                current.right=node
                break
            current = current.right
    memory.append(node)
print('이진탐색트리완성!') #이진탐색트리는 log n이라서 찾는속도가매우빠름
print(node.data) #맨끝에있는거 출력

findName='마마무'
current=root
while True:
    if(findName == current.data):
        print(findName,'뮤비가나옵니다.')
        break
    if (findName<current.data):
        if (current.left ==None): #왼쪽으로내려가고싶은데 없음
            print(findName,'없다')
            break
        current=current.left
    else :
        if(current.right ==None):
            print(findName,'없음')
            break
        current=current.right


