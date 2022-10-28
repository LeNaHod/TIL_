## 함수

def openBox():
    global count
    print('상자를엽니다')
    count -=1
    if(count==0):
        print('선물넣기')
        return
    openBox()
    print('상자재포장')
    return

##메인
count=10
openBox()#상자10개를열어서 선물1개넣고 10번재포장


