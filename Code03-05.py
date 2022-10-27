# ##함수
# def add_data(data):
#     katok.append(None)
#     Klen=len(katok)
#     katok[Klen-1]=data #배열의 마지막자리에 넣는다


# def insert_data(pos,data):
#     katok.append(None)
#     Klen=len(katok) #카톡이라는 배열의 전체길이를 klen으로선언
    
#     for i in range(Klen-1,pos,-1): #klen의 전체-1의길이의 자리에 postion위치에넣음
#         katok[i] = katok[i-1]
#         katok[i-1]=None #이러면 지정한자리까지 지우고 당기고를반복
#     katok[pos]=data


# def delete_data(pos):
#     katok[pos]=None #정연삭제
#     Klen=len(katok)
#     for i in range(pos+1,Klen,1):#솔라의자리가 position임
#         katok[i-1]=katok[i]
#         katok[i]=None
#     del(katok[Klen-1])
# ##전역
# katok=[]
# select =-1

# ##메인

# while(select !=4):
#     select = int(input('선택하세요(1:추가,2:삽입,3:삭제,4:종료)--->'))
    
#     if(select ==1):
#         data=input('추가할 데이터-->')
#         add_data(data)
#         print(katok)
#     elif(select ==2):
#         pos=int(input('삽입할 위치-->'))
#         data = input('추가할데이터-->')
#         insert_data(pos,data)
#         print(katok)
#     elif(select==3):
#         pos=int(input('삭제할 위치-->'))
#         delete_data(pos)
#         print(katok)
#     elif (select == 4):
#         print(katok)
#         exit
#     else:
#         print('1~4중 하나를 입력하세요')
#         continue


