##함수

def findMinIndex(ary):
    minIdx=0
    for i in range(1,len(ary)): #내가 비교하려는 배열[0,1,2,3...]>배열[1,2,3,4....]
        if (ary[minIdx]>ary[i]): #값을비교해서 자리를바꿀지말지 결정
            minIdx=i
    return minIdx

##변수
testAry=[55,88,99,11]

##메인
minPos=findMinIndex(testAry)
print('최솟값=>',testAry[minPos])

