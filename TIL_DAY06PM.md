TIL_DAY06PM(220928 오후 수업내용)

# 판다스

- 판다스 설명(pandas)
- series, DataFrame등의 자료구조를 활용한 데이터분석 기능을 제공해주는 라이브러리
- 라이브러리 구성
    - 여러종류의 클래스와 다양한 함수로 구성
    - 시리즈와 데이터 프레임의 자료 구조 제공
    - 시리즈(**1차원** 배열) 데이터프레임(**2차원** 행열 구조)
    - 
판다스의 목적
- 서로 다른 유형의 데이터를 공통된 포맷으로 정리하는 것
- 행과 열로 이루어진 2차원 데이터프레임을 처리 할 수 있는 함수제공 목적
- 실무 사용 형태 : 데이터 프레임

Series 
- pandas의 기본 객체 중 하나
- numpy의 ndarray를 기반으로 인덱싱을 기능을 추가하여 1차원 배열을 나타냄
- index를 지정하지 않을 시, 기본적으로 ndarray와 같이 0-based 인덱스 생성, 지정할 경우 명시적으로 지정된 index를 사용

==>txt등 파일 ->dataFralme -> Series. 데이터프레임은 시리즈가 모인것

1. 자료구조 : 순차1차원 배열, 인덱싱 :데이터,dict형식의 키:밸류
2. 시리즈의 인덱싱 : 레이블추가, 데이터 관리[리스트]
3. 시리즈 생성 : Series()를 통해서 데이터를 나열 지정 ->리스트 ->튜플->딕셔너리(xml,json) 

## 왜 판다스와 넘파이를 같이써야할까?

- 넘파이는 사람이 계산할수없는 고차원(5차원이상)의 계산을 하기위해 쓴다. (넘파이는 4차원이상부터도 씀)
  그래서 차원이 올라가고 복잡해질수록 판다스와 넘파이를 같이쓴다.

## Jupyter를 이용한 numpy,pandas 실습

<details>
<summary>실습</summary>

```python

#1.series 객체 생성 : [] 나열된 데이터 생성. ↓ 방향으로 왼쪽 인덱스 오른쪽 데이터
s = pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
print(s,s.dtype,s.index,s.array,'\n', s.values,s.shape,s.ndim,s.name)
s.index.name='test'
s

s.name='이름 컬럼'
s
결과가  Name: 이름 컬럼, dtype: int64 나오는데 ,
방법1)s = pd.Series([1,2,3,4,5],index=['A','B','C','D','E'],name='이름컬럼') 
방법2)
s = pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
s.name='이름 컬럼'

# s에서 3과 5를 추출해보자(s의인덱스의 라벨링을 가져온다)
s['C'],s['E']

#s에서 3과 5의 값을 3000과 5000으로 변경해보자
s['C']=3000
s['E']=5000
s

#1.series 객체 생성 : [] 나열된 데이터 생성
#s = pd.Series([1,[2,3],4,5])
s = pd.Series([1,[2,3],4,5],index=['A','B','C','D'])
print(s,s.dtype,s.index,s.array,'\n', s.values,s.shape,s.ndim,s.name)
s.index.name='test'

#인덱스를 문자열로 지정한 후에 숫자인덱스로 추출 확인
#s['A']
s[0]=1000 # A라는이름의 인덱스가 0번째에 있으므로, 0번째 값을 1000으로 지정
s['A'] #A라는이름의 인덱스

#인덱스 ,(콤마)로 나열해서 데이터를 추출해보자_슬라이싱으로 추출가능
s[[1,3]]        #중요! ,로 나열해서 가져오고싶으면 슬라이싱 필수!! [[,]]는 세트
s[1:3]  

#문자 인덱스 , 로 나열해서 데이터를 추출해보자,_슬라이싱으로 추출가능
s[['A','C']] #2개
#s['A':'C']  #3개

#객체.인덱스로 추출해보자
s.B ,s.A, s[0],s['A']   #[2,3],7777,7777,7777, a(인덱스0번째)에 7777이들어가있고,b에는 2,3이들어가잇다
#s.A=7777
#s.A

#exam) 문자 인덱스의 시리즈 이다. 아래와 같은 결과를 출력할 수 있도록 코드작성

#도시
#서울
#부산
#인천
#대구
#Name : 인구,dtype :int64

city = pd.Series([9904312,3448737,289045,2466052],index=['서울','부산','인천','대구'])
city.index.name='도시'
city.name='인구'
print(city)

#타입은 pandas.core.arrays.numpy_.PandasArray
r=pd.Series([1,2,3]).array  
print(type(r))

#벡터화 연산. 인덱스에 range를줄수도있고, 본 데이터에도줄수잇다
#단 인덱스가 데이터의 갯수보다 적으면 안됨!
#대신 length함수가없고 ★Len이있다!★
data=range(1,10,2)
print(len(data))
pd.Series(data,index = range(1,len(data)+1))


#벡터화 연산
pd.Series([1,2,3])+4  #원래 123이라는 데이터가있는데 123에 각4를 더해줌
r=pd.Series([1,2,3])  #위의 코드와 아래두줄의 코드의 결과는같다.
r+4,r -1, r/100000


#인구지표를 city/100000로 축소해보자
city/100000

# 비교연산을 이용해서 데이터를 추출해보자
s1 = pd.Series(range(1,20))
s1[s1>10]#대괄호가있으면 1~20까지 10이상인데이터

s1>10 #괄호가없으면 T/F로나옴
s1[(s1 % 2 ==0) | (s1 % 3 ==0)]    #or and x &, | 가능 대신()넣어줘야함 우선순위때문에

#인덱스로 연산을 수행 15보다 큰 데이터
s1[s1.index > 15] #인덱스 15보다 큰거.인덱스와,시리즈 데이터 둘다 연산가능

#시리즈 함수를 이용해서 목록을 출력해보자.
s1.items()
for index,value in s1.items():
    print(f"index :{index}, value : {value}")

# 시리즈 간의 연산
a1 = pd.Series([1,2,3,4])
b1 = pd.Series([1,2,3,4])
a1+b1

#시리즈간의 연산과 인덱스. 인덱스명이 동일한 시리즈 데이터는 연산이된다.
#인덱스가 안맞으면 NaN(None)이 나온다.
#이름을 안주면 내부적으로 연산이된다.
#인덱스가 같으면 = int64(타입이) 다르면 float64(NaN때문에, 표현을 가장큰 타입으로)
a1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
b1 = pd.Series([1,2,3,4],index=['aa','bb','c','d'])
a1-b1   # + 이면 결과가 6.0 -이면 결과가 0.0

d = {'a': 1, 'b': 2, 'c': 3}
#ser = pd.Series(data=d, index=['a', 'b', 'c'])
ser =pd.Series(data=d)
ser.index

#q1 city소스코드로 확인 해보자 ._dict로 만들어보자(dict는 순서가X)
ctiy2 ={'서울':9904312,'부산' : 3448737,'인천':289045,'대구':2466052}
r = pd.Series(data=ctiy2, index = ctiy2.keys()) #keys()를쓰면 순서가 줄어들 확률 ↓
r.서울 = 100000  #update
r

#q2 .r의 요소중 부산,인천을 삭제해보자.
del r['부산']
del r['인천']

r #부산과 인천이 사라져있다.

#일단위로 Datetime 생성 (*import time*)
pd.date_range(start='2018-10-01',end='2018-10-20',freq='d')

#초단위로 생성
pd.date_range(start='2018-10-01',end='2018-10-20',freq='s')

#요일단위로 생성
pd.date_range(start='2018-10-01',end='2018-10-20',freq='w')

#3일간격으로 일단위 생성 (n d,w,s...)
pd.date_range(start='2018-10-01',end='2018-10-20',freq='3d')

#스타트를 기준으로 2bm(2개월 간격으로 월말주기 12개 생성,periods=월말주기)
pd.date_range(start='2018-10-01',periods = 12, freq ='2BM')

#분기별로 qs
pd.date_range(start='2018-10-01',periods =4 ,freq='qs')

#q3)넘파이 np.random.randint()를 이용해서 난수10개 생성
np.random.randint(5)
np.random.randint(5,size=10)

#q4)넘파이 np.random.seed()를 찾아서 시간을 지정한수 난수10개 생성

print(time.time())
np.random.seed(int(time.time()))
np.random.randint(5,size=10)    #0~5까지범위내에서 난수를 발생하는데. 10번반복
```

</details>

## seaborn을 이용해서 데이터를 임포트하자 _그래프 패키지

```python
import seaborn as sns

titanic = sns.load_dataset('titanic') #titanic 데이터를가져오는 구문
titanic #출력

#타입확인
type(titanic)   #pandas.core.frame.DataFrame 데이터프레임 타입이다.

#.head()데이터 출력. hrad=앞에서. head(n)=앞에서n개
titanic.head(10)

#.tail()데이터 출력
titanic.tail(10)  #끝에서 10개출력

#q1)인덱스 100에서 150번까지 출력
t=titanic[100:151]  
t

#a2)survived,embarked,class 만 10개출력하자 loc[행,열]
titanic.loc[0:10,['survived','embarked','class']]

#a2-1)survived,embarked,class 만 10개출력하자 2차원
titanic[['survived', 'embarked', 'class']][0:10]

#q2-2)survived,embarked,class 만 10개출력하자 head이용
titanic[['survived', 'embarked', 'class']][0:10].head(10)

※ titanic.columns[[]] = 컬럼명 반환
```