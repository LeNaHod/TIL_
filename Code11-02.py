##함수
import random
def findMinIndex(ary):
    minIdx=0
    for i in range(1,len(ary)): #내가 비교하려는 배열[0,1,2,3...]>배열[1,2,3,4....]
        if (ary[minIdx]>ary[i]): #값을비교해서 자리를바꿀지말지 결정
            minIdx=i
    return minIdx

##변수

before=[random.randint(50,200) for _ in range(8)]
after=[]

##메인
print('정렬전=>',before)

#정렬할 배열의 갯수만큼 for문을돌림

for _ in range(len(before)):
    minPos=findMinIndex(before) #before에서 가장작은값을 찾는정렬을 실행하여 minpos에넣음
    after.append(before[minPos])#그리고 after에 append해줌 작은순서대로
    del(before[minPos]) #마지막으로 삭제해줌.안해주면 같은값만 여번나옴(for로돌아야하니까)

print('정렬후=>',after)