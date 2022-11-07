##함수

#그래프생성

class Graph():
    def __init__(self,size): #정점에따라 달라지기때문에 size에 정점의 개수를넣는다.
        self.SIZE=size
        self.graph=[[0 for _ in range(size) for _ in range(size)]]
##전역
G =None
gSize=4 #정점 개수 :A,B,C,D
A,B,C,D=0,1,2,3
#메인
G=Graph(gSize)
G.graph[A][B]=1 #인접행렬의 선을 뜻함
G.graph[A][C]=1
G.graph[A][D]=1
G.graph[B][A]=1; G.graph[B][C]=1
G.graph[C][A]=1; G.graph[B][D]=1
G.graph[D][A]=1; G.graph[D][B]=1



for i in range(gSize):
    for k in range(gSize):
        print(G.graph[i][k], end=' ')
    print()

