TIL DAY 07(22 09 29)


**numpy에서는**
- universal functions(ufunc) / array objects 이쪽 도움말을 많이보기
## 포트번호 피해야하는것
- 0~65535
  - 1. 2로 시작하는 포트 
  - 2. 8로 출발하는포트
  - 3. 0으로출발하는포트(히든포트)

## 기본 기능 조금정리

> ★상관계수:
 변수들 또는 데이터 서로 독립적인지 아니면 영향을 주고 있는지를 알아내는방법(상관분석),두변수의 (관계의 강도)를 상관계수라고한다. 

  |상관계수의 값| 의미|
  |:---------:|:----:|
  |0.0 ~ 0.2| 거의없다|
  |0.2 ~ 0.4| 약한 상관관계|
  |0.4 ~ 0.6| 상관 관계|
  |0.6 ~ 0.8| 강한 상관 관계|
  |0.8 ~ 1.0| 매우 강한 상관 관계|
1에가까울수록 상관관계가 높다.

- ★범주형 데이터란? 
   관측 결과가 몇개의 범주 또는 항목의 형태로 나타나는 자료
   
   ex)성별(남,여), 선호도(좋다, 보통, 싫다), 혈액형(A,B,O,AB) 등

- 구간을 왜 나눠야하는가? 
    그래프 그런거 만들때 구분이없어져버림 나이,성별로나누고싶은데 안나눴다->걍 통 데이터나옴

- 데이터프레임에 value_counts() 함수 사용:
  
    행을 하나의 value로 설정하고 동일한 행이 몇번 나타났는지 반환
    주로 컬럼별 값의 분포를 확인할때 사용한다.

    행의 경우가 인덱스로 개수된 값이 value로 표시되는 Series 반환
 

- Serires.loc : 데이터 프레임의 행이나 컬럼의 순서를 라벨이라 조건표현으로 선택함. 인덱스가 라벨링되어있을때 주로 사용
- Serires.iloc  :위와 같은 기능이지만, 정수로 표현하는방법(컴퓨터가 접근하기쉽게) 인덱스가 라벨링 되어있지않고, 0,1,   2..등으로되어있을때.

  ★ 머지류는 세개↓
- Series.append(to_append[, ignore_index, ...]) : 두개이상의 시리즈를 연결

- Series.compare(other[, align_axis, ...]) :다른시리즈와 비교한다.차이점도 보여줌

- Series.update(other) : 시리즈를 수정한다.
- 시리즈에서 갯수세기
 
    ```python
        s = pd.Series(range(10))
        s[3] = np.nan   #NaN값을 입력
        s
        count()를 이용해보자.
        s.count()  9개출력. # nan은 제외하고 count는 null값을 제외한다.
    ```
- .shape : 행렬의 차원을 말한다.ex) (891,15) 이런식으로
        
        1 1 1 1 1   
        2 2 2 2 2 
        ↑ 1차원(->방향)에 4개, 2차원에 (↓방향)에 2개이므로 = (4,2)/(1차원,2차원,3차원...)

- .reshape : 배열 차원변경 .axis 순서대로(가로 -> 세로 축 방향) 값들을
  변환되는 shape으로 재배정하는 원리이며,**재배정이 불가능한 shape인 경우 ValueError가 발생**
  즉,(4,2,4) / array=([1,2,3,4,5])등의 형식을 아래처럼 바꿔주고, 그 반대의 경우도 실행해준다 가로->세로 /세로->가로 
  1 2
                                                                    
  3 4    *이런식인데 실제론이렇게안나옴 *               

- 사용법 : a.reshape(변환 shape) 혹은 np.reshape(a, 변환 shape)
- 응용 : -1을 넣을수도있다. b.reshape(-1, 2) = b.reshape(4,2)
- ex)8개의 사이즈에서 reshape(2, -1)로 넣으면,(2, 4)로 자동 변환.
  **단, 2개 이상의 axis 자리에 -1이 포함되는 것은 불가능**
--------------------------------------------
- df.sort_values() : 특정열 값 기준 정렬
데이터프레임은 2차원 배열과 동일하기 때문에
정렬시 기준열을 줘야 한다. by 인수 사용 : 생략 불가
**by = '기준열', by=['기준열1','기준열2']**
오름차순/내림차순 : ascending = True/False (생략하면 오름차순)

- df.sort_index() : DF의 INDEX 기준 정렬
오름차순/내림차순 : ascending = True/False (생략하면 오름차순)

↓↓↓↓↓↓결국 이런이야기임.

- sort_index() : 인덱스를 기준으로 정렬 value와 앞의 매개인자가 거의동일
- sort_value() : 데이터 값(기준컬럼)을 기준으로 정렬매개인자는 이거외에도많음.특정값 기준 정렬.
-  .ascending =true면 오름 ,false면 내림 

------------------
- groupin : df.groupby(level=0).mean() ->level=0이라는부분이 엑셀의 부분합같은거. 
- df(데이터프레임명).describe() :평균,표준,최대,최소,중간값 리턴
- df.info() : 기본 정보 조회 클래스 유형,인덱스 구성,열이름,종류,개수,행이름,종류,메모리할당
- df.drop('행/열 이름'axis=0/1)  : 행삭제는 axis 0, 기본값도 0 이다. 열삭제를 하고싶으면 axis1에 열이름**원본데이터에 바로 적용되는게아니라서 저장을해줘야 적용이된다!**
- 데이터셋 읽어오기 : 패키지명.load_dataset("data명") ex) sns.load_dataset('titanic')

- df의 기본함수
- mean(axis=0/1)
- min(axis=0/1)
- max(axis=0/1)
- 열의 합계 중간값 최소값 

        df2.loc['max_mean']=df2.mean(axis=0) 객체.mean,min,mas(axis 0/1)
        df2.loc['max_min']=df2.min(axis=0)
        df2.loc['max_max']=df2.max(axis=0)

- 행/열 삭제 - drop() 사용 예제
    df.drop('행이름',0) : 행삭제
    행삭제 후 df로 결과를 반환
    df.drop('행이름',1) : 열 삭제
    행삭제 후 df로 결과를 반환
    원본에 반영되지 않으므로 원본수정하려면 저장 해야 함


**열 또는 행에 동일한 연산 반복 적용할 때 : apply() 함수**
apply() 함수는 DataFrame의 행이나 열에 복잡한 연산을 vectorizing할 수 있게 해주는 함수로 매우 많이 활용되는 함수임

동일한 연산을 모든열에 혹은 모든 행에 반복 적용하고자 할때 사용

**apply(반복적용할 함수, axis=0/1)**

0 : 열마다 반복
1 : 행마다 반복
생략시 기본값 : 0

```python
#예제 df 생성
df3 = pd.DataFrame({
    'a':[1,3,4,3,4],
    'b':[2,3,1,4,5],
    'c':[1,5,2,4,4]
})
df3

# np.sum() 함수는 전달된 첫번째 인수 데이터를 합친 결과를 반환하는 함수
np.sum([1,2,3])

df3.apply(np.sum, 0) #sum을 열마다반복

df3.apply(np.sum, 1)#sum을 행마다반복

# + seaborn 패키지의 titanic 데이터셋을 load 하시오
import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.head() # 처음 5행 출력
titanic.tail() # 마지막 5행 출력
itanic.head(2) # 처음 2행 출력   주석할것

# titanic df의 alive, sex, class 열에 대해서 value_counts() 함수를 적용하여 결과를 
# 확인하시오. apply()  함수 사용할 것

titanic[['alive', 'sex', 'class']].apply(pd.value_counts, 0)

```
### 타입과 속성
object:문자열타입과 흡사.
category:문자열이지만, 카테고리화 시킬수있는 컬럼을 의미한다.
describe() : 각 컬럼에 대한 요약 통계를 제공하는데, 수치형 컬럼의 통계를 기본으로 보여줌
T: EX)df.T  =index와 column 축을 바꿔준다.
.astype(): 타입을 바꿔준다. ex) df['컬럼'].astype('타입').head() ※(head는 값을안주면 기본으로5개를보여줌)

## 실습코드
```python

#시리즈의 값이 정수,문자열 등 '카테고리' 값인 경우에
#시리즈.value_counts()메서드를 사용해 각각의 값이 나온 횟수를 셀 수 있음

np.random.seed(1) #항상 같은 값이 나오게 설정
s2=pd.Series(np.random.randint(6,size=100))
s2.tail() # 시리즈의 뒷부분 데이터 5개를 추출
s2.head() # 시리즈의 앞부분 데이터 5개를 추출
s2.head(10) # 해당 개수 만큼의 데이터를 추출
len(s2)

s2.value_counts() #카테고리가 각 몇번나왔는지 세줌
s2.value_counts(normalize=True) # 각 카테고리가 100%의 기준에서 몇%를 차지하는지 보여준다.

#범주형 데이터에 value_counts() 함수 적용
titanic.value_counts()
titanic.value_counts(Normalize=Ture) #범주형데이터에서 각 비율을 내준다.


# df의 첫번째 시리즈를 리턴받아 res01로 출력
res01 =df.loc[:, ['num_legs']] #df['num_legs']  #iloc는 :, 0이나 1 등등 정수. [[]]=데이터프레임으로. []면 데이터프레임 x 데이터프레임을 추출할땐 [][]로해야한다.
                              # 또 기본적으로 .loc가 loc[행,열]이기때문에 열만가져오고싶으면 :,해서 넘겨야한다.
res01
#df의 두번째 시리즈를 리턴받아 res02로 출력
res02 = df.loc[:, 'num_wings'] #df['num_wings']/ df.loc['컬럼명']=df['컬럼명']의 결과는같지만,값을 대입하고싶다면
res02                           #df.loc['컬럼명']이 이슈가나지않는다.
#res01+02결과를 출력
res01 + res02
#loc에 조건을 써보자.
condition2 = (df['who'] == 'woman') =t/f출력.
#데이터프레임으로 나오게하고싶으면
df[df['컬럼']=='조건']. [['출력할열1','2','3'...]]
df.loc[ (df['num_legs']==조건) & (df['num_wings'])==조건] 
#df의 인덱스를 abcd로 출력
df.index=['a','b','c','d']  #df의 인덱스 라벨링 작업
df
#res01 시리즈의 인덱스를 AA BB CC DD로 출력
res01.index=['AA','BB','CC','DD']
res01

---------------
행/열 합계
df.sum() 함수 사용
행과 열의 합계를 구할때는 sum(axis=0/1) - axis는 0이 기본
각 열의 합계를 구할때는 sum(axis=0)  열이니까 0
각 행의 합계를 구할때는 sum(axis=1)  행잉니까 1

# 예제 DF 생성
#4행 8열의 데이터프레임 작성, 난수를 발생시키고
#0-9범위에서 매번 같은 난수 발생되어 반환되도록 설정
np.random.seed(1)
df2=pd.DataFrame(np.random.randint(10,size=(4,8)))
df2
df2.sum(axis=0)
df2.sum(axis=1)
r=np.random.randint(10,size=(4,2,2))#4개의면 2 *2,(면,행,열)
r.shape #전체 면 ,행,열 을 튜플로리턴. 
r.ndim #차원을 리턴 데이터 프레임은 2가출력된다(2차원이니까).
r=np.random.randint(10,size=(4,8,2))#4개의면 2 *2,(면,행,열)
r.shape 
r.ndim 

#r을 2,4,2로 변경해보자
r02=np.reshape(r,(2,4,2))  #shape/reshape을 만들땐 '튜플'이기때문에 ()O![]x
r02,type(r02)

#r02를 출력
r02
np.reshape(r02,16) #r02에는 원래 16개가들어있다. 16개이상,이하면오류
#np.reshape(r02) 아규먼트 2개이상이여야함
np.reshape(r02,r02.size) #r02의 사이즈만큼 배열차원을바꿈.갯수가많을땐 .size로주는게 좋을거같다 몇개인지 모르니까

#1)csv파일을 df로 읽어오자. df=read_csv() 
df=pd.read_csv('C:\ds_work\data\movies_train.csv') # .read_csv(경로) 로 csv를불러올수있다.
df

#2)데이터 프레임의 사이즈를 확인해보자
df.size #총 몇개인지데이터가 7200
df.shape #1차원에 600개 2차원에 12개 (600,12)

#3)기본정보를 확인 해보자
df.info() #클래스 유형,인덱스 구성,열이름,종류,개수,행이름,종류,메모리할당

#결측처리를해보자(nan데이터처리)1

df.isnull  = df.isna  #nan값을 출력한다. isnull()과 isna()은 같은결과다. 편한거쓰면됨

#결측처리를해보자(nan데이터처리)2
titanic['deck'].value_counts() #일단갯수확인
titanic['deck'].value_counts(dropna=False) #nan갯수 가져오기

#.sum()을써서 nan 갯수를 합쳐보자
df.isnull().sum() = df.isna().sum() #nan값을 더해서 열별로 보여준다. sum()을 한번 더 사용하면 총계를볼수있다.

#결측치가 아닌 데이터
df.notnull()  #결측치가 아닌 데이터를 출력한다.
titanic['deck'].value_counts(dropna=Ture) #nan제외하고가져오기
#결측 데이터 채우기

age_mean=titanic['age'].mean() #age의 중앙값
age_mean
titanic['age'].fillna(age_mean,inplace=False) #inplace=저장유무,age의 결측값을 중앙값으로 채운다.
titanic

#결측데이터 삭제하기

df.dropna()/df.dropna(how='any'or'all') #결측데이터를삭제한다. 옵션은 기본 how='any'
                                        #any: 1개 라도 NaN값이 존재시 drop
                                        #all: 모두 NaN값이 존재시 drop


#4-1)최빈 최대 평균등 통계값은 자주이용한다.

titanic['embarked'].value_counts(dropna=False)
e_idxmax=titanic['embarked'].value_counts(dropna=False).idxmax() #idxmax=데이터프레임내의 최댓값출력
#최대값을 구하자
titanic['embarked'].fillna(e_idxmax,inplace=True)

#4-2)embark_town으로 구해보자
e_idxmin=titanic['embark_town'].value_counts(dropna=False).idxmin() #idxmin=데이터프레임내의 최소값출력
titanic['embark_town'].fillna(e_idxmin,inplace=True)
#확인을해보자
titanic.isnull().sum()


#상관계수를 구해보자(기본형)

df.corr(method='pearson', min_periods=1)
method : {pearson / kendall / spearman} 상관계수 방식 택1
min_periods : 유효한 결과를 얻기위한 최소값의 수 (피어슨, 스피어먼만 사용가능)

#행열간의 상관계수(기본형)
DataFrame.corrwith(other, axis=0, drop=False, method='pearson')
other : 동일한 이름의 행/열을 비교할 다른 객체
axis : 0:인덱스 1:컬럼. 기본적으로 0으로 인덱스끼리 비교
drop : 동일한 이름의 행/열이 없을경우 NaN을 출력하는데, NaN출력 여부
method : {pearson / kendall / spearman} 위와같은 상관계수 구할 방식.

#5)객체['컬럼'].corr(method = ''), survived 와 adult_male의 상관관계
titanic.corr(method='pearson')
#-0.55555가나오므로, 상관 전혀없음. 즉corr=상관관계 수치구하기
titanic['survived'].corr(titanic['adult_male'],method='pearson')

#6)성별로 상관관계(상관 관계 계수)를 구해보자.
#★문자->숫자로 바꾼다 .map를 이용해서! map({'컬1':값,'컬2',값..})

#titanic['sex']=titanic['sex'].map({'male':10,'female':20}) #컬럼의갯수가두개니까 map(이 안에도 갯수를맞춰서 두개를줘야함.) 두번실행하면 NaN을반환하니 주석처리.
titanic['survived'].corr(titanic['sex'],method='pearson')


#7)aplly()를 이용해서 특정열/모든 열값을 변경해 보자.
#객체.apply.map or 객체.apply(lamba x: ~ or if~) 응용이있다.
#df['열이름'].apply(사용자 정의함수)/df.apply(사용자 정의함수,axis = 0)
#applymap(func[,na_action])

def r_age(age):
    res=int(age//10)*10   #소수를 정수로바꾸겠다.10대20대30대
    return res            #29.11231같은게 들어와도 20대가됨

titanic['r_age'] = titanic['age'].apply(r_age) #r_age라는컬럼생성후, #apply에 r_age넣어 해당함수를age컬럼에서 반복한다.
titanic.head()


#8)데이터 프레임 구간 나누기 cut(데이터,구간개수,레이블명)
#★구간개수는 레이블갯수를넘을수없음
titanic['r_cut']=pd.cut(titanic['age'],3,labels=['child','young','old'])
titanic['r_cut'].value_counts()
#x 축 age, hue구간=범례(위에서 세개로나눴으니 3개로나뉨),element=요소
sns.histplot(data=titanic, x="age",hue="r_cut",element="step") 

#sec03:판다스를 이용한 그룹연산

#01. 그룹함수를 이용한 연산

#1) 특정열을 기준으로 데이터프레임 분할(그룹핑) 객체.groupby('열이름')
#screening_rat 컬럼을 그룹핑하자!
df.groupby('screening_rat')
df.groupby('screening_rat').size
#그룹의 개수를 리턴받자
df_g=df.groupby('screening_rat')
df_g.ngroups #그룹개수가나온다.(ex job의 종류가 5개면5출력)

#2)그룹핑 상태에서 특정열을 기준으로 객체가 키값을 리턴받자.
df_g.groups.keys() #분할 한 그룹의 키값을 리턴 groups.keys()가 셋트.그룹했어도붙여야함

#3)특정한 그룹핑한 키값의 밸류를 리턴받아보자
df_g.get_group('15세 관람가')  #.get_gorup이 특정 그룹핑한 키값의 밸류

#4) 그룹핑한 후 집계함수를 써보자.
df_g['title'].count()  #타이틀열별로 카운팅
df_g['box_off_num'].max()  #box_off_num를 이용한 최댓값

#5)groupby.add(func,*args,**kwargs)를 이용해서 연산을 해보자
#df_g['titile'].count()df_g['box_off_num'].max()
df_g.agg({'time':max, 'box_off_num' : max})  #시간을 가장 많이사용한

#5-1 각 열의 맥스,민값을 출력해보자(위에는 맥스 한개만)
#두개주려면 밸류값부분에 []를넣고 두개를넣으면됨    
df_g.agg({'time':[max,min],'box_off_num': [max,min]})
df[df['box_off_num']==1]

#6)groupby.agg(fun,*args,**kwargs)
#사용자 정의 함수 time컬럼의 데이터들 중에서 가장 시간이 긴 시간-가장 짧은시간

def my_fun(x):
    diff = x.max() - x.min()
    return diff

df_g['time'].agg(my_fun)

#02. 시계열 데이터 처리

#7)시계열데이터를 사용해보자.df의 컬럼을 시계열 객체로 변환하자
df['my_date'] = pd.to_datetime(df['release_time']) #my_date라는컬럼명시
df.head()
df.info()
#object->datetime64[ns]로 타입변환되었다. 이제 year,mon,day,h,m,s등으로 다 자를수있다.

#8)my_date 의 컬럼을 이용한 년 월 일 로 분철해서 각각의 컬럼을 추가
df['my_year']=df['my_date'].dt.year  #dt.year(데이트타입으로my_date에서 년도를추출하겟다)
df['my_month']=df['my_date'].dt.month
df['day']=df['my_date'].dt.day
df['my_w']=df['my_date'].dt.weekday
w=['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
df['요일']=df.apply(lambda x: w[x['my_w']],axis=1)
#df['my_w']=df['my_date'].dt.weekday.name #영어로요일출력
df.head()

```

