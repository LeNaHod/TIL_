##함수
import random

#이진검색알고리즘 
def binSearch(ary,fData):
    pos=-1
    start = 0
    end = len(ary)-1
    while (start <= end):
        mid=(start+end)//2 #//=소수점까지버려버림
        if (ary[mid] == fData):
            pos=mid
            break
        elif(ary[mid] < fData): #시작을 중앙의 오른쪽으로
            start =mid +1 #start를 중앙의 오른쪽으로(오른쪽버릴거니까)=버릴값쪽으로 보내버림
        else:
            end = mid -1 #end를 중앙의 왼쪽으로(왼쪽버릴거니까)=버릴값쪽으로 보내버림
    return pos

##변수
dataAry=[random.randint(50,200) for _ in range(10)]
dataAry.sort() #정렬이 시간이 조금걸림
findData=random.choice(dataAry)

##메인

print('배열=>',dataAry)

position=binSearch(dataAry,findData) 

if(position == -1):
    print(findData,'는 배열에 없어욥')
else:
    print(findData,'는',position,'번째에 있어욥')