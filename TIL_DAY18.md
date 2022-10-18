# TIL DAY18(22_10_18)

## matplot 이용해서 (plt) 여러 그래프를 그려보자.

- matplotlib?
    분석한데이터를 그래프로 그려주는라이브러리. 여러 그래프를 사용할수있다
    import matplotlib.pyplot as plt
    주로 plt.~로 많이쓰인다.

figure():도화지 개념.보통 fig라는 변수에 담아서 씀

- seaborn?
    {name}으로 원하는 데이터를 가져와서 쓸 수 있다.(타이타닉,아이리스,펭귄 기타등등..) seaborn에서 깃헙에 올려놓은 데이터를 df(데이터프레임)끌고온다.
    깃헙에 들어가보면 데이터의 출처와 어떤데이터들이 올라 와 있는지 알 수 있다.

<details>
<summary>matplotlib 연습코드(주석)</summary>

## 그래프를 그리고 알아보자!

```python
1.
import matplotlib.pyplot as plt

#figure 생성 ->피규어 생성 =도화지생성
fig =plt.figure()

#subplot 배치 -> 서브플롯 배치 = 도화지나누기

ax = fig.subplots()

#그래프 그리기
ax.plot([1,2,3,4,5])

#그래프 출력
plt.show()

2.
import matplotlib.pyplot as plt #그래프필수

#피규어,서브플롯 한번에
#fig =plt.figure()
#   +
#ax = fig.subplots()

fig,ax=plt.subplots()

#그래프 그리기
x=[1,2,3,4,5]
y01=list(map(lambda x: x**2,x))
y02=list(map(lambda x: x**3,x))

ax.plot(x, y01,color='red',label='pow2')#plot =그냥 선
ax.plot(x, y02,color='blue',label='pow3')

#범례표시
plt.legend()

#그래프에 보여주자
plt.show()

3.

import matplotlib.pyplot as plt

#figsize:도화지크기

fig=plt.figure(figsize=(10,5))
#add_subplot(행,열,위치)
ax01= fig.add_subplot(1,2,1)
ax02=fig.add_subplot(1,2,2)

#x축을 선한개로그림
x=[1,2,3,4,5]
y01=list(map(lambda x: x**2,x))
y02=list(map(lambda x: x**3,x))


ax01.plot(x,y01,color='r' ,label="pow2") #라벨 범례제목
ax02.plot(x,y02,color='g' ,label="pow3")

ax01.legend() #범례표시여부.범례표시할 네모칸생성 t/f인데 컬러에 영향안줌
ax02.legend()


ax01.set_title('x**2')
ax02.set_title('x**3')

plt.show()

4.
import matplotlib.pyplot as plt
import random


# fig=plt.figure() #서브플롯과 한번에씀
#
# #각그래프들이 그려질 위치 (행,열) 몇번째인지,
# ax01 =fig.add_subplot(2,2,1)
# ax02 =fig.add_subplot(2,2,2)
# ax03 =fig.add_subplot(2,2,3)
# ax04 =fig.add_subplot(2,2,4)

fig,ax =plt.subplots(2,2) #도화지가 네개 하나의 도화지를 + 모양으로나눔

x=list(range(50))

y01=list(random.randint(0,50) for i in range(50))
y02=list(random.randint(0,50) for i in range(50))
y03=list(random.randint(0,50) for i in range(50))
y04=list(random.randint(0,50) for i in range(50))

#산점도 그래프 =scatter. x와y의 상관관계 분포도.
ax[0,0].scatter(x,y01, color='red')
ax[0,1].scatter(x,y02, color='green')
ax[1,0].scatter(x,y03, color='blue')
ax[1,1].scatter(x,y04, color='yellow')

fig.tight_layout()
plt.show()

5.
import matplotlib.pyplot as plt
from random import randint

fig,ax =plt.subplots()

x=list(randint(0,10)for i in range(100))

ax.hist(x,bins=10)

plt.xticks(list(range(0,11)))
plt.yticks(list(range(0,101,5)))

plt.xlim(0,10) #x의 최대치 0-10
plt.ylim(0,100) #y의최대치 100

plt.show()

6.
import matplotlib.pyplot as plt
from random import randint

fig,ax = plt.subplots()

x = list(randint(0,10) for i in range(100)) #누적 데이터  100개! 개수임.

#cumulative :누적. 주황색데이터는 누적false라서 y로안올라가고 파란색은 누적이라올라감
ax.hist(x,bins=10, cumulative=True)
ax.hist(x,bins=10, cumulative=False)

plt.xticks(list(range(1,11)))
plt.yticks(list(range(0,101,5)))

plt.xlim(0,10)
plt.ylim(0,100)

plt.show()

7.
import matplotlib.pyplot as plt
from random import randint
import numpy as np


#matplotlib설치할때 numpy가 자동으로 설치되서,따로 numpy를 설치안해도된다.
#박스 플롯 (Box plot) 또는 박스-위스커 플롯 (Box-Whisker plot)은 수치 데이터를 표현하는 하나의 방식입니다.

fig,ax=plt.subplots()

x=list(randint(0,1000) for i in range(10))
print(x)
print(np.mean(x)) #매개변수의 평균갑 구하기 mean=평균값.
print(np.median(x))

ax.boxplot(x)

plt.show()

8.
import matplotlib.pyplot as plt
from random import randint

fig,ax=plt.subplots() #도화지생성과 도화지나누기 같이

#100명의 사람이이있다고 가정
ages=list(randint(1,100) for i in range(100))

child=list(x for x in ages  if x <19)
young=list(x for x in ages  if 19 <= x < 40)
middle=list(x for x in ages  if 40<= x <60)
old=list(x for x in ages  if 60 <= x)

# print(child)
# print(young)
# print(middle)
# print(old)

labels=['child','young','middle','old']
count=[len(child),len(young),len(middle),len(old)]

#파이차트의 라벨(이름표)는 라벨의값 차일드,영.. counterclock=False는 시계방향으로 라벨링함. startangle=90 90도방향
ax.pie(count,labels=labels,counterclock=False,startangle=90)
ax.legend(loc=(1,0.8)) #1자리가 가로 0.5는 도화지의(fig)50%. 0.8자리가 세로.도화지의 80프로 즉 오른쪽상단에 범례가위치가헤됨
#오른쪽하단으로하로싶으면 'lower right' top right는없다 ㅋㅋ
plt.show()

9.

import matplotlib.pyplot as plt
from random import randint

fig=plt.figure()
ax01=fig.add_subplot(1,2,1)
ax02=fig.add_subplot(1,2,2)

x=[1,2,3,4,5]
y=list(randint(1,100)for i in range(5))

ax01.bar(x,y, color='r')
ax02.barh(x,y, color='b')

plt.show()
```
</details>

<details>
<summary>seaborn을 이용해보자!</summary>

## seaborn에서 여러데이터

```python

#conda install seaborn 와 pip insall~ pip는 최신버전으로 설치해주고 conda는 호환성이 높고 c관련해서 이것저것 많이 설치해줌
#시본이뭔데?  타이타닉,아이리스 등  시본을 통해서 데이터를 가져올수있다. 시본은 캐글이등에서 가져와서 가공한 데이터를 깃헙에올려놓고 깃헙에서
#sns.load_dataset('name')으로 원하는걸 가져올수잇다.
import seaborn as sns
import matplotlib.pyplot as plt

'''

total : 전체 사고 건수
speeding : 과속 비율
alcohol : 음주 비율
not_distracted : 주의산만하지 않은(?) -> 딴데 정신팔린?
no_previous : 이전에 사고가 없었던 운전자 비율
ins_premium : 자동차 보험료
ins_losses : 운전자 1인당 충돌사고로 보험사가 입은 손해
abbrev : 미국 주 약자

barplot:지정한 변수의 평균을 계산하여 그림.데이터의 개수가 아닌 평균을 계산한다.


sns.barplot(x, y, data, .., )
-data : 데이터프레임
- x, y : 컬럼 참조


막대그래프 위에 덧그려진 검은 선은 95%의 신뢰구간.
'''

1.
car_crashes =sns.load_dataset('car_crashes')
print(car_crashes)

plt.figure()
sns.barplot(data=car_crashes, x='abbrev',y='total') #abbrev=미국주별 total=전체사고건수  == 즉 주별 사고건수
plt.show()

2.
import matplotlib.pyplot as plt
import seaborn as sns
'''
바플롯 다시설명!
barplot:지정한 변수의 평균을 계산하여 그림.데이터의 개수가 아닌 평균을 계산한다.


sns.barplot(x, y, data, .., )
-data : 데이터프레임
- x, y : 컬럼 참조


막대그래프 위에 덧그려진 검은 선은 95%의 신뢰구간. =엣징?
'''

car_crashes=sns.load_dataset('car_crashes')
car_crashes.sort_values('total',ascending=False, inplace=True) #inplace=변경사항(삭제이런거.삭제는저장해야 반영됨) 저장여부. true=저장 false저장안함

plt.figure()

sns.barplot(data=car_crashes, x='abbrev', y='total', facecolor='w', edgecolor="black")

sns.lineplot(data=car_crashes, x='abbrev', y='speeding', linewidth=3, color='r',label='speeding' )
sns.lineplot(data=car_crashes, x='abbrev', y='alcohol', linewidth=3, color='g',label='alcohol' )
sns.lineplot(data=car_crashes, x='abbrev', y='no_previous', linewidth=3, color='b',label='no_previous' )
plt.xlim(-1,51)
plt.show()

3.
import matplotlib.pyplot as plt
import seaborn as sns

car_crashes=sns.load_dataset('car_crashes')
car_crashes.sort_values('total',ascending=False, inplace=True)

plt.figure()
sns.barplot(data=car_crashes, x='abbrev', y='total', facecolor='w', edgecolor="black")

sns.lineplot(data=car_crashes, x='abbrev', y='no_previous', alpha=0.3, color='b',label='no_previous' )
sns.lineplot(data=car_crashes, x='abbrev', y='speeding', alpha=0.3, color='r',label='speeding' )
sns.lineplot(data=car_crashes, x='abbrev', y='alcohol', alpha=0.3, color='g',label='alcohol' )

plt.xlim(-1,51)
plt.show()

4.

import matplotlib.pyplot as plt
import seaborn as sns

'''
species : 종
island : 서식지
bill_length_mm : 부리의 길이
bill_depth_mm : 부리의 깊이
flipper_length_mm : 날개의 길이
body_mass_g : 체질량
sex : 성별

'''

penguins=sns.load_dataset('penguins')
# print(penguins)
#ver sns.histplot(penguins['body_mass_g']) body_mass_g하나만 가져옴
#sns.histplot(data=penguins,x='body_mass_g')
#sns.histplot(data=penguins,y='body_mass_g') 값 세로출력

sns.histplot(data=penguins, x='body_mass_g', hue='species', multiple='fill', fill=False) #fill=false는 색이사라짐
#multiple 배경색같은거

plt.show()

5.
import matplotlib.pyplot as plt
import seaborn as sns

penguins=sns.load_dataset('penguins')

#sns.swarmplot(data=penguins,x='body_mass_g')
sns.swarmplot(data=penguins,x='body_mass_g',y='species', color='black', alpha=0.5) #종별로 나눔
sns.boxplot(data=penguins,x='body_mass_g',y='species',hue='sex') #hue가무엇이냐? 범례제목.
plt.show()

6.
import matplotlib.pyplot as plt
import seaborn as sns

penguins=sns.load_dataset('penguins')

# sns.boxplot(data=penguins, x='body_mass_g')
# sns.boxplot(data=penguins, y='bill_length_mm')
sns.boxplot(data=penguins,x='species', y='bill_depth_mm',hue='sex')
plt.show()


7.
import matplotlib.pyplot as plt
import seaborn as sns


penguins=sns.load_dataset('penguins')
markers={"Male":"P", "Female":"o"} #아이콘바꾸기
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm',hue='species',style='sex',markers=markers) #hue를쓰면 레전드(범례생성)도 알아서 잡아줌

plt.show()

8.
import matplotlib.pyplot as plt
import seaborn as sns


penguins=sns.load_dataset('penguins')
#성별별로 바이올렛 플롯으로 species와 body_mass_g출력 split=True (아래위로)반으로나눔
sns.violinplot(data=penguins, x='body_mass_g', y='species',hue='sex',split=True)

plt.show()

9.
import matplotlib.pyplot as plt
import seaborn as sns

penguins=sns.load_dataset('penguins')
#regplot:scatter+추세선. 스케터에추세선을 추가해주는 친구
sns.regplot(data=penguins,x='bill_length_mm', y='bill_depth_mm')

plt.show()

10.

import matplotlib.pyplot as plt
import seaborn as sns

penguins=sns.load_dataset('penguins')
#ecdf:경험적 누적분포함수.(반복된 시행을 통해 확률변수가 일정 값을 넘지 않을 확률을 유추)
sns.ecdfplot(data=penguins, x='body_mass_g')

plt.show()

13.(11-12x)
import matplotlib.pyplot as plt
import seaborn as sns


penguins=sns.load_dataset('penguins')

fig=plt.figure()
ax01=fig.add_subplot(1,2,1)
ax02=fig.add_subplot(2,2,2)
ax03=fig.add_subplot(2,2,4)


sns.histplot(data=penguins,x='body_mass_g',ax=ax01) #his=걍 막대그래프
sns.scatterplot(data=penguins, x='bill_length_mm',y='bill_depth_mm', ax=ax02) #스케터 분포도
#중요! fillna=결측값 채우기. 결측값을 펭귄 body_mass_g의 평균값으로 채운다.
sns.boxplot(penguins['body_mass_g'].fillna(penguins['body_mass_g'].mean())) #박스플롯 박스로 정도측정같은거

plt.tight_layout()
plt.show()


```
</details>
