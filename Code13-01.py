##함수

import random

def seqSearch(ary,fData):
        pos=-1 #못찾앗다고 가정하고 코딩
        
        for i in range(len(ary)):
            if(ary[i] == fData):
                pos=i #데이터를 찾으면 pos값을 i로바꿈
                break
        return pos

##변수
dataAry=[random.randint(50,200) for _ in range(8)]
findData=random.choice(dataAry)

##메인
print('배열=>',dataAry)
#데이터어레이에서 데이터찾아줘
position=seqSearch(dataAry,findData) #단 없는데이터를 찾을시 -1반환(관례적인것임)

if(position == -1):
    print(findData,'는 배열에 없어욥')
else:
    print(findData,'는',position,'번째에 있어욥')
