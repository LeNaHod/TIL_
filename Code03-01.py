##파이참은 삭제하면 none가 안보이지만 vs코드는 삭제해도 none가 보임
##함수 선언부

##전연 변수부
katok=['다현','정연','쯔위','사나','지효']
#메인코드부
katok.append(None)#카톡이라는 배열에 빈값=none를 넣어 빈칸생성
katok[0]='다현' #0번째자리에 다현을넣음

#(1)데이터 추가:모모추가
katok.append(None)
katok[5]='모모'

#print(katok)

#(2)데이터 삽입:미나를 3등으로

katok.append(None)
katok[6]=katok[5] #실제로는 복사
katok[5]=None #그래서 그냥 비워버림..그리고반복
katok[5]=katok[4]
katok[4]=None
katok[4]=katok[3]
katok[3]=None
katok[3]='마나'

#print(katok)

#(3)데이터 삭제:사나가 차단

katok[4]=None
katok[4]=katok[5]
katok[5]=None
katok[5]=katok[6]
katok[6]=None 
del(katok[6]) #6번자리는 필요없으니까 None으로 비워두지말고 자리자체를 삭제!
print(katok)

