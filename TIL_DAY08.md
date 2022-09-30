TIL DAY 08 (22_09_30)


## 파이썬에서 csv를 읽어와보자
파일안의 문자들이

    abcd->.csv   
    a,b,c,d ->구분자 에러
    'a','b','c','d',**e** -> 라인단위로 분철,''을 없앤상태로 **재저장**
이런구조로 파일을 읽어오기때문에 꼭 **type을 통해 type확인**을 해야한다. (화면에 보이는게 전부가아님)
또 str->int 등으로 형식을 변환하는 작업도 필요하다.

## 정규분포를 알아보자

여러가지 자연현상을 표현할수있다.
도수분포 곡선이 평균값을 중앙으로하여 좌우대칭을 '종'모양을 이루는 분포이다.
=표준 정규분포: 평균이0이고 표준편차가 1인 정규분포.
ex)처음보는 학생의 키를 구한다던가, 처음보는 학생의 모의고사 점수 추측 등.
## merge와 db join

select ename,deptno,dname from emp join dept using(deptno) 

and

on(emp.deptno=deptno.deptno02)

★위의 코드를 merge로 바꿔보자

merge(dg01,df02,how='outer',on='A'). how조인종류 기본이 inner.

- outer = df1 과 df2에 공통적으로 존재하는 교집합일 경우에만 추출.
- right = right outer join 오른쪽df전부, 왼쪽은 조건에 일치하는것만
- left  = 왼쪽에있는애들 다, 오른쪽은 일치하는것만.
- inner = 디폴트값임 inner조인과같음
- cross = cross조인과같다

```python
#)df03,04를 머지해보자.
#중복되는 컬럼은 megr에 명시한 왼쪽df를기준으로_x가붙고,오른쪽이_y
#중복되지않는 컬럼은 _x,y가붙지않는다.
#하지만 조인 기준이된 컬럼은 한번만 출력한다.
df03 = pd.read_csv('A:\ds_work\data\emp.csv')
df04 = pd.read_csv('A:\ds_work\data\emp01.csv')
res_m=pd.merge(df03,df04,how='outer',on='empno')
res_m
```

### EMP.csv를 가져와서 실습해보자
```python
#1)csv파일을 df로 읽어오자 df=read_csv()
df=pd.read_csv('A:\ds_work\data\emp.csv')
df
#2)첫 다섯줄,끝 다섯줄 내용을 확인하자
df.head(5)
df.tail(5)
#3)객체[[,,,]]:select empno,ename,job from emp(empno enmae job을가져오자); 를 가져와보자!
df[['empno','ename','job']]

#4)사원자료에서 직업이 SALESMAN인 사원의 이름,작업,봉급을 출력하자.
df[['ename','job','sal']][df['job']=='SALESMAN']

#5)봉급이 3000 이상인 원의 이름과 봉급을 출력하자
df[['ename','sal']][df['sal']>= 3000]

#6)봉급이 1000에서 3000인 사원의 이름과 봉급을  출력하자
#두줄 다 결과 동일
df[(df['sal']>=1000) & (df['sal']<=3000)][['ename','sal']]
df[['ename','sal']][df['sal'].between(1000,3000)]

#7)봉급이 1000에서 3000이 아닌 사원의 이름과 봉급을 출력하자.
#pandas(not= ~(틸드)dlek.)
df[['ename','sal']][~df['sal'].between(1000,3000)]

#8)직업이 CLERK,SALESMAN인 사원의 이름과 직업을 출력해보자.
df[['ename','job']][df['job'].isin(['CLERK','SALESMAN'])]

#9)커미션이 null인 사원의 이름과 커미션을 출력하자 =null인 데이터 조회
df[['ename','comm']][df['comm'].isnull()]

#10)커미션이 null이 아닌 사원의 이름과 커미션을 출력하자(valu_count/index 로는 안댐)
df[['ename','comm']][~df['comm'].isnull()] #말그대로 자료를 출력

#11)사원 이름이 scott인 사번 봉급 입사일 출력해보자.
df[['empno','sal','hiredate']][df['ename']=='SCOTT']

#12)데이터 타입과 df정보를출력하자
df.info() #ename은 문자(object)타입
type(df['ename']) #이렇게 조회하면 object이지만,시리즈로반환한다.

#13 사원의 이름을 for문으로 출력해보자
for res in df['ename']:     #Series(list)는 안이 리스트타입이다.
                            #object->시리즈화(리스트)->str로반환
    print(res,type(res))    #for로 돌리면 str로 변환되서 리턴받는다. 

★#for로 str로받고 str을 인덱스로 특정문자를 추출할수있다
for res in df['ename']:
    print(res,res[0])

#14)사원의 이름을 첫글자가 s로 시작하는 사뤈의 이름과,봉급을 출력해보저.
# select ename,sal from emp where ename like('%S%');=db문

for res in df['ename']:
    if res[0] =='S':
        print(res)

#15)사원의 이름이 T자로 끝나는 사원의 이름과, 봉급을 출력해보자
for res in df['ename']:
    if res[-1] =='T':     #-1이면 맨끝자리 
        print(res)

#16 사원의 이름이 두번 째 글자가 M인 사원의 이름과,봉급출력

#ename 만 res에 넣고 if 비교,출력할때 ename,sal행을 출력,열은ename이res와동일한것만.
for res in df['ename']:
    if res[1] =='M':     
        print(df[['ename','sal']][df['ename']==res])
      
#16-1 번외 :파이썬의 연결 문자를 확인해보자
a='i love'
b='python'
a+b

#16-2)번외 :DB에서사원의 이름과 봉급을 결합해보자
select ename || sal from emp ||->연결문자

★#17)df의 객체에서 사원의 이름과 봉급을 결합해보자. zip(,)
#zip은 for를거쳐 str로 반환하지않고,원래 타입 그대로리턴한다.
#if를 쓰면 2번째글자가 m인애만.안쓰면 ename,sal의 형식으로
for m_name,m_sal in zip (df['ename'],df['sal']):
#     if m_name[1] =='M': 
        print(m_name+','+str(m_sal))

★#19)정규분포를 구해보자
avg=30
std=7
N=1000000
mogipdan = np.random.randn(N)*std+avg  #p.random.randa(N) 가우시안 정규분포. 외우기
print(len(mogipdan))
print(mogipdan)

#19-2 번외편 :위의 19-2의 모집단에서 평균을 구해봐라
#평균구하는애:mean
print(np.mean(mogipdan))

#19-3 번외편:모평균이30이고 표준편차가 7 인 모집단(1000000)에서
#표본 49개를 뽑아보자. np.choice(표본뽑을대상,표본의 개수)표본뽑기

avg=30
std=7
N=1000000
mogipdan = np.random.randn(N)*std+avg #p.random.randa(N) 가우시안 정규분포. 외우기
print(len(mogipdan))
print(mogipdan)
#print(np.random.choice(mogipdan,49))

#아래코드는 표본의 평균
res=np.random.choice(mogipdan,49) #표본값을 res에넣고
print(res)
print(np.mean(res)) #출력할때 표본값의 평균을출력

#20)emp.csv df01 df02만들어 concate을시켜보자!!
df01=pd.read_csv('A:\ds_work\data\emp.csv')
df02=pd.read_csv('A:\ds_work\data\emp01.csv')

#21)df01,df02를 concatconcat(axis=1로줘서)시켜보자
res01= pd.concat([df01,df02],axis=1) #열을합침 ->방향으로
res01   

#22)df01,df02,df03를 concat(axis=1로줘서)시켜보자(3개)
df03=pd.read_csv('A:\ds_work\data\emp.csv')
res01= pd.concat([df01,df02,df03],axis=1)
res01     
#★axis=0 을주면 ↓방향으로 행을 합침. 0이 디폴트값이다.   

```
## 쿼리로 생각하여 자료를 추출해보자

- 데이터베이스 쿼리를 먼저짜고, 데이터를 추출하는편이 이해가 빠르다!(개인차이가 있음)
  
```python

#1)이름과 부서위치를 출력하시오
select e.ename,d.loc #오라클 조인문
from emp e, dept d
where e.deptno =d.deptno #or (= from emp join dept using(deptno))

↓↓↓↓↓↓↓↓↓

emp=pd.read_csv('A:\ds_work\data\emp.csv') 
dept=pd.read_csv('A:\ds_work\data\dept.csv')
result =pd.merge(emp,dept, on='deptno')
result[['ename','loc']]

#2)dallas에서 근무하는 사원의 이름과 부서의 위치를 출력 해보자.
select ename,loc
from emp join dept using(deptno)
where loc='dallas';

↓↓↓↓↓↓↓↓↓

result[['ename','loc']][result['loc']=='DALLAS'] #조건문은 객체[컬럼] 연산자 '조건']

#3봉급이 3000 이상인 사원의 이름과 봉급 부서위치 출력
select ename,sal,loc
from emp join dept using(deptno)
where sal>=3000;

↓↓↓↓↓↓↓↓↓

result[['ename','sal','loc']][result['sal']>=3000]

#4 select e.name, d.loc from emp  e,dept d where e.deptno(+)=d.deptno;
select ename, loc   #ansi쿼리 버전
from emp rigth outer join dept using(deptno) 

↓↓↓↓↓↓↓↓↓

emp=pd.read_csv('A:\ds_work\data\emp.csv')
dept=pd.read_csv('A:\ds_work\data\dept.csv')
res04=pd.merge(emp,dept, on='deptno',how='right') #오른쪽조인.하지만 여기on은 조인기준.
res04

#5)JONES월급보다 많이받는 사원을출력해보자.서브쿼리이용
select ename,sal
from emp
where sal>(select sal from emp where ename ='JONES');

↓↓↓↓↓↓↓↓↓

#5-1).존스의 월급을 찾아라 emp['sal'][emp['ename']=='JONES']+Values[0]
jsal=emp['sal'][emp['ename']=='JONES'].values[0] #0번째 값출력
jsal

#6)서브쿼리 :scott의 직업과 동일한 사원의 이름과 월급을 출력하자 scott제외
select ename,sal
from emp 
where job = (select job from emp where ename='SCOTT') and ename <> 'SCOTT';

↓↓↓↓↓↓↓↓↓

s_job=emp['job'][emp['ename']=='SCOTT'].values[0]
emp[['ename','sal']] [ (emp['job']==s_job) & (emp['ename']!='SCOTT')]

#7)sal을 이용한 집합함수
emp['sal'].max
emp['sal'].min
emp['sal'].sum
★emp['sal'].var ★ #분산값 
★emp['sal'].std ★ #표준편차 값

#8)20번 부서의 봉급의 합을 구하자
select sum(sal) from emp where deptno =20;

↓↓↓↓↓↓↓↓↓

emp['sal'][emp['deptno']==20].sum()

#9 )select job,max(sal) from emp group by job으로 바꿔보자

select job,max(sal) from emp group by job

↓↓↓↓↓↓↓↓↓

eg=emp.groupby('job')['sal'].max() #시리즈로 출력(안이쁨)
eg=emp.groupby('job')['sal'].max().reset_index()#reset_index()=df로출력
eg

★#11).astype(타입) ->타입바꾸기 중요!★
emp.groupby('deptno')['sal'].mean().reset_index().astype(int)

#12 )직업과 직업별 월급의 합을 출력하자

select job,sum(sal)
from emp
group by  job;

↓↓↓↓↓↓↓↓↓

emp.groupby('job')['sal'].sum().reset_index()

#13 )부서위치와 부서별 월급의 합을 출력하자.

select loc,sum(sal)
from emp join dept using(deptno)
group by loc;

↓↓↓↓↓↓↓↓↓

emp_m=pd.merge(emp,dept,on='deptno')
emp_m.groupby('loc')['sal'].sum().reset_index()

```

## sec05:판다스를 이용한 데이터 프레임,병합,연결
    
    -01. concat()을 이용한 프레임 병합(concat([df01,df02],axis=0/1)0열1행
    -02. merge()을 이용한 연결,병합 고유값을 기준으로 두df를 합쳐준다.
                (pd.merge(df_left, df_right, how='inner', on=None))=db의join같은개념
    -pro02(데이터 병합)

## sec06:시각화

    - 데이터 수집 -> 데이터 정제 -> 데이터 분석 ->데이터 시각화
    - matplotlib:파이썬 표준 시각화 라이브러리, 2D평면을 표현 그래프
                  -라인플롯차트(꺾은선형.시간변화에씀)
                  -바 차트(비교,랭킹)
                  -파이차트(점유율)
                  -히스토그램(분표)
                  -산점도(연관성)
    
    - seaborn : 저위의 matplotlib외의 애들을 처리할때


## sec05,sec06의 예제를 풀어보자

```python
# csv로드
df=pd.read_csv('A:\ds_work\data\movies_train.csv')
df

#천만관중을 달성한 영화를 그래프로 나타내보자.
천만_df=df[df['box_off_num']>=10000000][['title','box_off_num']]
천만_df

#그래프 구현
import matplotlib.pyplot as plt  #★★★★★ import꼭하기 
dir(plt)으로 무엇을 사용할 수 있는지 확인가능

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()

#기본설정되어있는 폰트를 출력
import matplotlib.font_manager as fm #각종 폰트관리
plt.rcParams['font.family'] 
#기본폰트를 굴림으로설정
plt.rcParams["font.family"]='gulim'

#내컴퓨터에있는 폰트를 다 출력
fl = fm.findSystemFonts(fontpaths = None, fontext = 'ttf')
fl[:]


#천만관중 달성영화 리스트를 타이틀 별로 그래프생성
plt.figure(figsize=(10,6))
plt.rcParams["font.family"]='gulim'
plt.rcParams["font.size"]=12
plt.bar(천만_df['title'],천만_df['box_off_num'], color='blue')
plt.title("천만관중 달성 영화",fontsize=12)
plt.xlabel("영화제목")
plt.ylabel("관중수",fontsize=15)
plt.show()
type(fig)

#장르별 관객수 평균 그래프를 그려보자
장르별관객수 =df.groupby('genre')['box_off_num'].mean()
장르별관객수 =장르별관객수.reset_index()
장르별관객수

plt.figure(figsize=(15,6))
plt.rcParams["font.family"]='gulim'
plt.rcParams["font.size"]=12
plt.bar(장르별관객수['genre'],장르별관객수['box_off_num'], color='pink')
plt.title("장르별 관객수 평균",fontsize=20)
plt.xlabel("영화장르")
plt.ylabel("관객수",fontsize=15)
plt.show()
type(fig)

#ex1)release_time을 시계열 데이터로 변환 /년도별 최대 관객수
df['n_date']=pd.to_datetime(df['release_time'])
df.head(5)

#ex1-1)년도별 평균 관객수를추출하자
year_mean = df.groupby('year')['box_off_num'].mean()
year_mean =year_mean.reset_index()
#그래프부분
plt.ylim([5000000,15000000])
plt.plot(year_max['year'],year_max['box_off_num'],color='blue',marker='o')
plt.show()

#ex02)한 화면에 그래프 2개를 보고싶다.
#plot는 그래프의 x,y축 설정과 기타 스타일을 줄수있다.
#axis() 함수를 이용해서 축의 범위 [xmin, xmax, ymin, ymax]
plt.figure(figsize=(10,10)) #그래프 출력사이즈 figsize=(높이,너비)
plt.subplot(1,2,1)          #한줄에 두개를 주는데 첫번째 칸=subplot(행,컬럼,인덱스) 여러개의 그래프를 하나의그림에 나타낸다.
plt.ylim([100000,15000000]) #축 표시범위.ylim이니까 y축의 표시범위이다.xlim도있고, axis([x축범위],[y축범위])로 한번에지정가능.
plt.plot(year_max['year'],year_max['box_off_num'],color='green',marker='*') #plot(x축의값,y축의값.하나입력시y축의값,컬러,마커값(ㅇ표시))    #마커종류 'o'=동그라미,'^'=세모,'*'=별,'s'=사각형
plt.subplot(2,2,2)                      #2행2열2번째인덱스. 
plt.plot(year_mean['year'],year_mean['box_off_num'],color='red',marker='o')
plt.show()

# 스태프의 분포도 (hist그래프)
staff=df['num_staff']
#그래부분
plt.hist(staff,bins=10,color='green',alpha=0.3,) #hist(데이터,bin:구간,alpha,histtype= : 그래프종류 기본bar타입)
plt.title('스탭인원수에 대한 분포도')   #그래프 타이틀
plt.show()


#ex04)영화등급의 비율을 파이차트로 만들어보자.
st=df['screening_rat'].value_counts() #분기 구간나누기
st  #확인

#그래프부분
plt.pie(st,labels=st.keys(),autopct="%1.1f%%") #라벨입력은 두번째인자에 입력 가능한데,st의키값인 15세,12세,전체관람가를 반환.
plt.show()                          #autopct:부채꼴안에 입력될 값(=수치)을 각 영역에 할당해줌(ex)100이면4개에100심어줌)
                                    #autopct="%1.1f%%" or "%.1f%%"를 쓰면 각 점유율을 %로 계산해준다.

```

## 파이썬 모듈을 이용해서 csv파일을 조작해보자

```python
#파이썬 모듈을 이용한 csv파일 불러오기
import csv #import해서 써야한다.
#dir(csv)
file = csv.reader('A:\ds_work\data\emp.csv') #csv를 불러오는reader
file
type(file)

pandas 는         pd.read_csv(경로)
파이썬 모듈 csv 는 csv.reader(경로)

#3)전체 내용을 출력 하자. _파일의 내용을 한행씩 리스트객체에 담아서출력(csv는 꼭 이렇게!)\

for emp_list in file :
    print(emp_list)

#4)파일을 오픈한 객체를 csv의 reader로 읽어오자.
import csv
file = open('A:\ds_work\data\emp.csv') #file이라는애안에 emp.csv를 넣고,
emp_csv=csv.reader(file) #emp_csv라는 객체안에 emp.csv를 읽어와서 담는다.


flag = True    #별다섯개! flag는 bool타입(논리타입 t/f값밖에못가진다 1,0값 두개만있음) 특정 상황?조건을 참/거짓으로 판단할때 사용함
for res in emp_csv:       #자료가 많으니까 다 비교해야하니 for문
    if flag:              #위의 flag가 true인상태에서 if flag= if true와같다. 들어오는 데이터를 트루처리함
        print(res[0], res[5])    #res[0]과 res[5]가 각 ename과 sal(컬럼명)을 반환한다. 인덱싱안댐
        flag = False             #컬럼명들을 한줄 만나자마자, flag=false처리해버림. 
    else:                        #else -> 그외의상황,자연스럽게 false로 넘어감
        print(res[0], int(res[5]),type(int(res[5])))  #그래서 숫자형문자 데이터들(5000,300..)들은 int형으로 바꿀수있다. sal 아래값들이 int로 변해서 이제 연산할수있게되었다.

```