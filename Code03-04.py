##함수
def add_data(data):
    katok.append(None)
    Klen=len(katok)
    katok[Klen-1]=data #배열의 마지막자리에 넣는다


def insert_data(position,data):
    katok.append(None)
    Klen=len(katok) #카톡이라는 배열의 전체길이를 klen으로선언
    
    for i in range(Klen-1,position,-1): #klen의 전체-1의길이의 자리에 postion위치에넣음
        katok[i] = katok[i-1]
        katok[i-1]=None #이러면 지정한자리까지 지우고 당기고를반복
    katok[position]=data


def delete_data(position):
    katok[position]=None #정연삭제
    Klen=len(katok)
    for i in range(position+1,Klen,1):#솔라의자리가 position임
        katok[i-1]=katok[i]
        katok[i]=None
    del(katok[Klen-1])


##전역

katok=[]

##메인

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

# print(katok)

#insert_data(2,'솔라')
# print(katok)

delete_data(1)
print(katok)