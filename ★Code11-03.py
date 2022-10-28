##함수
import random


def selectionSort(ary):
    n=len(ary)
    for i in range(0,n-1): #만약n이4라면 0~3까지 즉 세번사이클이돌음
        minIdx=i #다른걸 바꿔야하니까 for돌때마다 바뀌는값으로
        for k in range(i+1,n): #0빼고 1부터 4까지
            if(ary[minIdx]>ary[k]):
                minIdx=k
        ary[i],ary[minIdx]=ary[minIdx],ary[i] #두개의 위치가 바뀌어짐. 파이썬만가능


    return ary

##변수
dataAry=[random.randint(50,200) for _ in range(8)]

##메인

print('정렬전=>',dataAry) #방을 하나쓸거니까

dataAry=selectionSort(dataAry)

print('정렬후=>',dataAry)