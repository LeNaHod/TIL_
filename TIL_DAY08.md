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