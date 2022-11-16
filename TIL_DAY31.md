# TIL DAY 31(2022-11-16)

## Window함수란?

분석함수중에서 윈도우절(WINDOW절)을 사용할수 있는 함수.(=윈도우 함수라고부름.)

**분석함수중에서 일부만 윈도우절을 사용**할수 있다는것이다.

PARTITION BY 절에 의해 명시된 그룹을 다시 그룹핑할수 있다

- 종류 : AVG, COUNT, FIRST_VALUE, LAST_VALUE, MAX, MIN, STDDEV, SUM...

        문법 EX)↓
        AVG(컬럼명) OVER(

        PARTITION BY 컬럼1,컬럼2....

        ORDER BY 컬럼 ASC(생략가능,기본값) / DESC

        ROWS / RANGE

        BETWEEN UNBOUNDED PRECEDING / PRECEDING / CURRENT ROW
                AND UNBOUNDED FOLLOWING / CURRENT ROW

                )

|함수명|설명|
|:---:|:---:|
|UNBOUNDED PRECEDING|윈도우의 **시작위치가 첫번째 행**|
|UNBOUNDED FOLLOWING|윈도우의 **마지막위치가 마지막 행**|
|CURRENT ROW|윈도우의 시작위치가 **현재 행**|
|ROW|윈도우의 크기를 **물리**적인 단위로 행 집합 지정|
|RANGE|**논리적인 주소**로 행 집합 지정|

## SPARK3

|이름|설명|추가설명|
|:---:|:---:|:---:|
|모집단|표본을 뽑으려는 그룹전체|-|
|표본|모집단에서 일정수량 데이터를 뽑아온것(10%,30%...)|-|
|편차|평균에서 얼만큼 떨어져있느냐의 수치|ex)학급평균 키 170이고 내가 160이면</br>나의 편차는 -10|
|분산|데이터들이 어떻게 분산되어있느냐|-|
|표준편차|구하려는 편차의 단위,모집단등이 다르기때문에 그걸 표준화시키도록 가공한것</br>평균이 1이되도록 가공한것이다.|-|
|var_pop|모집단 분산|-|
|stddev_pop|모집단 표준편차|-|
|var_samp|표본분산|-|
|stddev_samp|표준편차|-|
|covar_pop|모집단 공분산|-|
|covar_samp|표본 공분산|-|
|corr|피어슨 상관관계|-|

**모집단의 규모가 일정수를 넘으면 표본을 적게뽑아도 데이터에 신뢰성이생긴다.**


### df.count() / df.select(count("*")) 차이점 

- df.count: 값으로반환한다. Transformation
- df.select(count("*")) : 데이터 프레임으로 반환한다. action. 
- ★count / select내부 count는 같은조건으로 실행시 row개수의 차이는없다.


### Temp View에대하여

**SQL의 VIEW가 아님!**

Spark내에서 데이터 분석작업을 할 때 DataFrameAPI말고,SQL표현식을 써서 데이터를 조작한다.

(SparkSession.sql()메서드를 이용함), 즉 sql표현식으로 조작하고싶은 데이터는 아래 코드로 TempView를생성해줘야한다.

- spark(df).createOrReplaceTempView 

- 여러가지 종류가있지만 가장 보편적으로쓰는게 createOrReplaceTempView

```python
#card데이터를 다 가져와서 조작해보자!

cardAll=spark.read.format('csv').option('header','true').option('inferSchema','true').load("card_data/csv/*csv")
->하둡에올라간 card_data/csv/ 경로안에있는 모든 csv를 다가져온다.

cardAll.count() ->특정컬럼,혹은 전체를 'Row갯수'를 검색한다.(action아님)
cardAll.createOrReplaceTempView("cardall")

spark.sql("""
select * from cardall
""").show()

from pyspark.sql.functions import count

cardAll.select(count("*")).show() -> 데이터 프레임으로 타입으로 반환한다.


spark.sql("""
select count("*")
from cardall
""").show()


from pyspark.sql.functions import col,countDistinct

cardAll.select(countDistinct(col("이용일"))).show()


spark.sql("""
select count(distinct(`이용일`)) 
from cardall
""").show()

->spark.sql에서는 countDistinct라는 함수는없지만,  count(distinct(컬럼명))으로 같은 결과를 낼수있다.



#fist(컬럼 데이터) last(컬럼 데이터)
#DataFrame의 첫, 마지막 값을 찾는 데 사용, 값이 아닌 Row를 기반으로 동작

from pyspark.sql.functions import first,last

cardAll.orderBy(col("이용일")).select(first(col("이용일")),last(col("이용일"))).show()
-> select를 먼저하면 정렬할게없어져서, order By를 먼저쓰고 select로 가져와야한다. sql과 순서가 반대


spark.sql("""
select first(`이용일`),last(`이용일`)
from cardall
""").show()

# max,min을 사용해보자

from pyspark.sql.functions import min,max

cardAll.select(min("`금액`"),max(col("금액"))).show() -> min에 ``준이유는 col객체를 쓰지않았기때문에,  컬럼임을명시

spark.sql("select min(`금액`),max(`금액`)from cardall").show()

from pyspark.sql.functions import sum

cardAll.select(sum(col("금액"))).show()

spark.sql("select sum(`금액`) from cardall").show()


# avg,mean / 둘은 같음.

from pyspark.sql.functions import avg,mean

cardAll.select(count(col("금액")),sum(col("금액")),avg(col("금액")),mean(col("금액"))).show()

spark.sql("""
select count(`금액`),sum(`금액`),avg(`금액`),mean(`금액`)
from cardall
""").show()

# 모집단,표본

from pyspark.sql.functions import var_pop,var_samp,stddev_pop,stddev_samp

cardAll.select(var_pop(col("금액")).alias("var_pop"),var_samp(col("금액")).alias("var_samp"),
stddev_pop(col("금액")).alias("stddev_pop"),stddev_samp(col("금액")).alias("stddev_samp")).show()

↓↓↓↓↓

spark.sql("""
select var_pop(`금액`),var_samp(`금액`),stddev_pop(`금액`),stddev_samp(`금액`)
from cardall
""").show()

# 공분산과 상관관계

from pyspark.sql.functions import covar_pop,covar_samp,corr

cardAll.select(covar_pop(col("이용일"),col("금액")),covar_samp(col("이용일"),col("금액")),corr(col("이용일"),col("금액"))).show()

->상관관계가 0.005..이렇게나오는걸로봐서 이용일과 금액은 아무런관계가없다. 

cardAll.groupBy(col("대분류"),col("중분류")).count().show()

spark.sql("""
select `대분류`, `중분류`,count(*)
from cardall
group by `대분류`,`중분류`
""").show()

# Window함수를 사용해보자

from pyspark.sql.functions import to_date

dateDf = cardAll.withColumn('date',to_date(col("이용일").cast("string"),"yyyyMMdd"))
dateDf.show()

dateDf.createOrReplaceTempView("datetable") #datetable생성 이용일이 yyyy-mm-dd형식인 date컬럼을추가해서

from pyspark.sql.window import Window ->functions 아님!
from pyspark.sql.functions import desc

windowFuntion = Window.partitionBy(col("대분류"),col("date")).orderBy(desc(col("금액"))).rowsBetween(Window.unboundedPreceding,Window.currentRow)

->rowsBetween(시작값,끝값): 윈도우에 포함될 행의 범위를 지정해준다. 숫자값으로 직접 범위를 적용해줄수있다. ★현재 행을 기준★으로, 음수이면 이전, 양수이면 다음 행(row)를 범위로 정한다.

ex)rowsBetween(-5,5):현재 행을 기준으로 5개 이전, 5개 이후까지 범위로잡는다.

★직접값을 정해주는것보다 unboundedPreceding/currentRow 를 사용하는것이 좋다.

unboundedPreceding : 윈도우의 시작 위치가 첫번째 ROW
currentRow : 윈도우의 시작 위치가 현재 ROW
maxPay = max(col("금액")).over(windowFuntion)

from pyspark.sql.functions import dense_rank,rank

winDenseRank = dense_rank().over(windowFuntion)
winRank=rank().over(windowFuntion)

dateDf.orderBy(col("대분류")).select(col("대분류"), col("date"), col("금액"), winRank.alias("rank"), winDenseRank.alias("densrank"), maxPay.alias("maxpay")).show()


spark.sql("""
select `대분류`,date,`금액`, rank() over(partition by `대분류`,date order by `금액` desc) as rank,dense_rank() over(partition by `대분류`,date order by `금액` desc) as denserank,max(`금액`) over(partition by `대분류`,date order by `금액` desc) as maxPay
from datetable
"""
).show()

->spark문에서 정렬을 대분류로하고 maxpay를내야하는데, maxpay 대분류와 date기준으로 금액의 max값을 구하고있음. 그래서 max(`금액`) over (patition by `대분류`,date)

spark.sql("""
select `대분류`, date,`금액`,rank() over(partition by `대분류` order by date)as rank,dense_rank() over(partition by `대분류` order by date) as dense_rank
from datetable
order by `대분류`
""").show()


★partition : 분석함수를쓸때사용한다. dense_rank/rank는 분석함수 
★partition by `대분류` order by date -> 랭크낼건데 대분류를 date기준으로.그룹바이 역할을한다.

#rollup

rollupDf=cardAll.rollup(col("이용일"),col("대분류")).agg(avg(col("금액")).alias("avgpay")).selectExpr("`이용일`","`대분류`","`avgpay`").orderBy(col("이용일"))

rollupDf.show()

★스파크 agg : 집계함수(avg,sum,max...)를 사용하기위해 추가해준것
★rollup:지정한 컬럼별로 집계하고 전체집계별 합,컬럼별 합도 보여준다(sum으로 했을시 합이지 평균이면 평균 최대치면 최대치)

rollupDf.createOrReplaceTempView('rolluptable')

spark.sql("""
select `이용일`,`대분류`,avg(`금액`) as avgpay
from cardAll
group by ROLLUP(`이용일`,`대분류`)
order by `이용일`
""").show()

```
## DATAFRAME 2

★from pyspark.sql import SparkSession or * : spark.sql(~)를사용하기위해


```python
card2010=spark.read.format('csv').option('header','true').option('inferSchema','true').load('card_data/csv/202010.csv')

card2010.show()

Schema = card2010.schema

Schema ->위에서만든 스키마보기 

# 새로운row를만들어서 데이터프레임 생성

from pyspark.sql import Row

newRows=[Row(2022116,None,100000,None,'유흥','술',None),Row(2022116,None,5000,None,'생활','편의점','CU')]

★card2211=spark.createDataFrame(newRows,Schema) : 생성/ spark.createDataFrame(생성대상)

cards=card2010.union(card2211) #합집합
cards.show(cards.count())

★card2010.createOrReplaceTempView('card') 복사/createOrReplaceTempView(복제대상)

#정렬

그냥정렬

card2010.sort('금액').show() #기본값 오름
card2010.sort('금액',ascending=False).show() # 내림

컬럼 객체로 정렬

from pyspark.sql.functions import col

card2010.orderBy(col('금액')).show() # 컬럼객체로가져옴
card2010.orderBy(col('금액').asc()).show() #asc=오름
card2010.orderBy(col('금액').desc()).show()

col객체의 asc/desc는 파이썬내장함수가아니라 스파크내장함수이다.


asc,desc 를 import해서 orderBy asc,desc사용 

from pyspark.sql.functions import asc,desc

card2010.orderBy(asc('금액')).show()
card2010.orderBy(desc('금액')).show()


spark.sql("""
select *
from card
order by `금액` desc
""").show()

# 한번에 여러개 정렬

card2010.orderBy(asc('이용일'),desc('금액')).show() 

spark.sql("""
select *
from card
order by `이용일` , `금액` desc
""").show()

card2010.orderBy(['이용일','금액']),asecding=[1,0].show()
card2010.orderBy(col('이용일').asc(),col('금액').desc()).show
card2010.sort(['이용일','금액'],ascending=[1,0].show()
card2010.sort(col('이용일').asc(),clo('금액').desc()).show()

# instr을 써보자

instr:찾으려는 문자의인덱스위치 반환

from pyspark.sql.functions import instr

storeFilter=instr(col('소분류'),'마트') >=1
payFilter = col('금액') <= 10000


filter = where 같은거라서 filter <> where 대체가능

card2010.filter(storeFilter & payFilter).filter(col('이용일')>=20201010).filter(col('이용일')<= 20201031).show()

spark.sql("""
select *
from card
where `이용일` >= 20201010 and `이용일` <= 20201031 and instr(`소분류`,"마트")>=1 and `금액` < 10000 

""").show

★↑한글 컬럼은 ``로 묶어야하고 찾을 한글문자는 "" 로 구분해줘야한다.


# 금액이 30000초과 미만을 나누고 비쌈컬럼을 붙이고 true인값만 출력
expensiveFilter = col('금액') > 30000

card2010.withColumn('비쌈',expensiveFilter).filter(col('비쌈')).show()

card2010.withColumn('비쌈',expensiveFilter) ->금액이 30000초과 미만인애들을 t/f로 나눠서 비쌈컬럼 추가

filter(col('비쌈') -> 비쌈이 트루인값만


# round 사용

from pyspark.sql.functions import round

payFilter =col('금액')/1000
card2010.select(payFilter,round(payFilter)).show()


spark.sql("""
select `금액`/1000, round(`금액`/1000)
from card
""").show()

#dsecribe를써보자

dsecrib: summary(요약)출력. count,mean,stddev_pop,min,max 등이 출력된다.

card2010.describe().show()

# monotonically_increasing_id

monotonically_increasing_id : sql의 시퀀스와같다.

from pyspark.sql.functions import monotonically_increasing_id

card2010.select(monotonically_increasing_id(),"*").show() 
(모노토리컬리_id, 적용대상)


#문자열치환

from pyspark.sql.functions import regexp_replace

chain = "파머스빈|빽다방|바나프레소|카페7그램|스타벅스"

card2010.select(col("소분류"),regexp_replace(col("소분류"),chain,"커피체인점").alias("치환")).where(col("중분류")=="카페").show()

->체인에 들어있는 목록 중 하나에 부합하다면 커피체인점으로 바꿔라, 바꾸고 컬럼이름을 치환

regexp_replace: 주어진 문자역에서 특정 패턴을 찾아서 주어진 다른 모양으로 치환하는 함수이다.

(source_char(찾아올곳,원본데이터,컬럼명,문자열), 
pattern(바꿀조건), replace_string(치환할문자),
position (검색위치 지정), 
occurrence(패턴일치횟수. 0은 모든값대체, n은 n번발생한 애들에대하 지정문자열대입,
match_parameter(기본값으로 검색되는 옵션을 바꿀수 있다.

c : 대소문자를 구분해서 검색,

i : 대소푼자를 구분하지 않고 검색,

m : 검색 조건을 여러 줄로 줄 수 있음,

c와 i가 중복으로 설정되면 마지막에 설정된 값을 사용 ex) ic가 중복으로 절정되면  c 옵션 적용)
)



spark.sql("""
select `소분류`,regexp_replace(`소분류`,"파머스빈|빽다방|바나프레소|카페7그램|스타벅스","커피체인점") as `치환`
from card
where `중분류`='카페'
""").show()

from pyspark.sql.functions import translate 

card2010.select(col('소분류'),translate(col('소분류'),'스벅그프다','12345').alias('치환')).where(col('중분류')=='카페').show()

translate:특정문자를바꾸기 
translate(바꿀컬럼or데이터, 조건, 바꿀값)

spark.sql("""
select `소분류`,translate(`소분류`,"스벅그프다","12345")as `치환`
from card
where `중분류`=='카페'
""").show()


★ regexp_replace vs translate 

REPLACE는 전체 문자열 하나를 다른 문자열로 변경하고, REGEXP_REPLACE는 문자열에서 정규 표현식 패턴을 검색하는 반면 TRANSLATE는 단일 문자를 여러 차례 변경

#regexp_extract

from pyspark.sql.functions import regexp_extract

extractStr = "카페|다방"
card2010.select(regexp_extract(col("소분류"),extractStr,0).alias("치환"),col("소분류")).where(col("중분류")=="카페").show()

regexp_extract: 해당컬럼에서 조건을찾아 변환시켜주는데, 조건을 그룹으로 여러개 사용할수있다. 단, 정규식!표현으로 조건을줘야한다. 

regexp_extract(컬럼 or 원본데이터, 조건1 or (조건1),(조건2),(조건3)...,n(조건중에n번째쓸거다))

# 카페,다방이라는 값이 있는지 없는지 확인해보자

cafefilter = instr(col('소분류'),'카페') >=1
cafefilter2 = instr(col('소분류'),'다방') >=1

card2010.withColumn('카페다방포함',cafefilter | cafefilter2).select('카페다방포함','소분류').where(col('중분류')=='카페').show()

★ withColumn()뒤에 .select가 올수있다! 조회가 뒤에올수잇음!

# date(날짜)를 다뤄보자

from pyspark.sql.function import cureent_date,current_timestamp

dateDf = spark.range(1).withColumn('mydate',current_date()).withColumn('mytimestamp',current_timestamp())
dateDf.show()
dateDf.show(1,False) -> 너무길어서 ...생략 해제

★타임스탬프는 년월일'시,분,초' 다나오고, cureent_date는 년월일

↓↓↓↓↓↓↓↓↓

cureent_date,current_timestamp를 import 해와서 dateDf안에 mydate와 mytimestamp로 바꿔저


dateDf.createOrReplaceTempView('datetable')

from pyspark.sql.functions import date_add, date_sub

dateDf.select(date_sub(col('mydate'),5),date_add(col('mydate'),5)).show()

date_sub : 날짜를 뺀다

date_add : 날짜를 더한다

spark.sql("""
select date_sub(mydate,5), date_add(mydate,5)
from datetable

""").show()

↓↓↓↓↓↓↓↓↓

그 데이터를가지고 date_add,date_sub로 날짜 더하고 빼보고 / sql문으로 표현하기위해 createOrReplaceTempView('datetable')로 탬프뷰 생성. (datetable 이라는 이름으로)


from pyspark.sql.functions import datediff,months_between,to_date

dateDf.withColumn('week_ago',date_sub(col('mydate'),7)).select(datediff(col('week_ago'),col('mydate'))).show()

->오늘로부터 지정한날짜의 경과일

dateDf.select(to_date(lit('2022-11-16')).alias('today'),to_date(lit('2023-01-27')).alias('end')).select(months_between(col('today'),col('end'))).show()

->오늘부터 23-01-27까지 몇개월이 남았는지를 알려주고있다. 
★lit:리터럴의 약자. 말그대로 값임. lit('2022-11-16')이면 2022-11-16이라는 값을 하나 생성한것임.


spark.sql("""
select datediff(date_sub(mydate,7),mydate) as datediff,  ->스파크내부sql에서는 as 하고 별칭명에아무것도안씀.근데 가끔안될때, ``로감싸주면된다.
months_between('2022-11-16','2023-01-27') as months_between  
from datetable
""").show()

# 날짜로바꿀수 없는값을 날짜로 치환해보자

dateDf.select(to_date(lit('2022-12-32'))).show()
->12월32일이라는 일은 없기때문에 치환x ,null값리턴

dateFormat='yyyy-MM-dd' # 년월일 / HH:mm:SS (소문자m이여야 분)

formatDf=spark.range(1).select(to_date(lit('2022-12-25'),dateFormat).alias('fomat01'),to_date(lit('2022-25-12'),'yyyy-dd-MM').alias('format02'))

formatDf.show()

formatDf.createOrReplaceTempView('formattable')

form pyspark.sql.functions import to_timestamp

formatDf.select(to_timestamp(col('fomat01'),dateFormat)).show()
->timesteamp이기때문에 시분초까지 나옴

spark.sql("""
select to_timestamp(fomat01,'yyyy-MM-dd')
from formattable
""").show()

formatDf.select(to_date(col('fomat01'),'yyyy-MM-dd HH:mm:ss').alias('to_date'),to_timestamp(col('fomat01'),'yyyy-MM-dd HH:mm:ss').alias('to_timestamp')).show()


spark.sql("""
select to_date(fomat01,'yyyy-MM-dd HH:mm:ss'),to_timestamp(fomat01,'yyyy-MM-dd HH:mm:ss')
from formattable
""").show()

★import * ->스파크는 메모리에 다 올려놓고 사용하기때문에 다가져오면 필요없는것까지 가져오기때문에 리소스를많이잡아먹음
추천X

card2010.select(to_date(col('이용일').cast('string'),'yyyyMMdd')).show()
->cast:타입을 변환한다. 위는 이용일이 넘버(int)이여서 넘버(int)<>스트링(str,문자)<>데이트(날짜) 이니까 문자로 먼저바꾼것이다. 대신 스파크는 cast를 지원하는것


#★ 문자열로바꾸고 나아가 날짜로도바꿔보자

spark.sql("""
select to_char(`이용일`,yyyy-MM-dd)
from card
""").show() 



#

nullDf=sc.parallelize([
Row(name='You',phone='010-0000-0000', address='Seoul'),
Row(name='Shin',phone='010-1111-1111',address=None),
Row(name='Kang',phone=None, adress=None)
]).toDF()

nullDf.show()

nullDf.createOrReplaceTempView('nulltable')

from pyspark.sql.functions import coalesce

nullDf.select(coalesce(col("address"), col("phone")).alias("coalesce")).show()

-> 어드레스에서 한줄(가로)로 null이아닌 항목을 반환, 어드레스가 null이면 phone에서 null이아닌값을 반환한다.
어드레스,폰 둘다 null이면 null반환. row의 갯수만큼나오게된다. null이아닌 제일먼저 찾는값을 반환하니까.


spark.sql("""

select ifnull(null,'value'),nullif('same','same'),nvl('notnull','value1'),nvl(null,'value1'),nvl2('notnull','value1','value2'),nvl2(null,'value1','value2')

""").show()

#↓Null값 관련 함수(sql에서만 사용가능)

ifnull:첫번째값이null이면 두번째 값 리턴
nullif : 두값이 같으면 null
nvl:첫번째값이 null이면 두번째 값
nvl2:첫번째값이 null이면 두번째값, 아니면 마지막값


스파크에서 null처리

na: DataFrameNaFunction 지원
DataFrameNaFunction : drop, fill,replace 

-> na.drop/ na.fill/ na.replace ....으로 쓸수있다.

nullDf.show() 	#  데이터확인
nullDf.na.drop().show()

nullDf.na.drop('all',subset=['phone']).show()
nullDf.na.drop('any',subset=['phone']).show()


nullDf.na.drop('all',subset=['phone','address']).show()
nullDf.na.drop('any',subset=['phone','address']).show()


all:해당컬럼 중 모두 null이면 drop
any:해당컬럼 중 '하나라도' null 이면 drop


nullDf.na.fill("n/a").show()

nullDf.na.fill("n/a",subset=["phone"]).show()
nullDf.na.fill("n/a",subset=["phone","address"]).show()

dfaultValue = {"phone":"010-9999-9999","address":"street"}
nullDf.na.fill(dfaultValue).show()

fill:null값 대체

nullDf.na.replace(["Seoul"],["서울"],"address").show()

# ★구조체

★구조체:데이터 프레임안의 데이터프레임이고 struct타입 | struct라고 부른다.

card2010.selectExpr("(`이용일`,`금액`)as complex", "*").show()

->complex:{이용일값, 금액} 이런식으로 나오는데, 사실상 컬럼두개가 complex컬럼하나로 묶여져있는것과같다.
{이용일:값 ,  금액: 값} 의 형태라고 이해하면 편하다.

from pyspark.sql.functions import struct

complexDf=card2010.select(struct('이용일','금액').alias('complex'))
->이용일과 금액컬럼을 struct(구조체)로 만들겠다라는 의미! 그리고 묶은 구조체 별칭은 complex

complexDf.show()

complexDf.createOrReplaceTempView('complextable')

complexDf.select('complex.이용일').show()

complexDf.select('complex.금액').show()

complexDf.select('complex.*').show()

complexDf.printSchema() -> 타입이 struct라고 잡히고 struct안에 이용일/금액컬럼이 나눠져있다.

↓↓↓↓↓

spark.sql("""
select complex.`이용일`
from complextable
""").show()


# 배열

from pyspark.sql.functions import split

card2010.select(split(col("중분류")," ")).filter(col("대분류")=="교통").show()
->값1 " " 값2 [] ★배열형식★으로 나온다.


spark.sql("""
select split(`중분류`,' ')
from card
where `대분류`='교통'
""").show()


# arrycolumn의 택시,버스만 출력하자

card2010.select(split(col("중분류")," ").alias("arraycolumn")).selectExpr("arraycolumn[0]").filter(col("대분류")=="교통").show()
-> 배열로 반환하고있기때문에 스플릿 후 0번째 자리의 내용만 반환하겠다.

spark.sql("""
select split(`중분류`,'')[0] as arraycolumn from card where `대분류`='교통'
""").show()


※size출력도 가능하다!

# arry_contains

from pyspark.sql.functions import arry_contains

card2010.select(array_contains(split(col("중분류")," "),"버스")).where(col("대분류") == "교통").show()
->contains:배열안에 해당값이있는지 없는지 확인 후 T/F로 반환한다. 근데 일단 중분류에서 공백으로 나눈 후 버스가있는지확인하는 순서라서 split을 씀


spark.sql("""
select array_contains(split(`중분류`,' '),'버스')
from card
where `대분류`='교통'

""").show()


# explode

from pyspark.sql.functions import explode

card2010.withColumn("splitted",split(col("중분류")," ")).select("중분류","splitted").filter(col("대분류")=="교통").show()

->스플릿 이전 중분류 :택시 버스 17 버스 26 이렇게들어가있고, 스플릿 후 중분류: [택시] [버스, 17] [버스, 26] 공백을 기준으로 나눠져있고 값을 배열로 반환하고있다.

# ★★★ exploded
card2010.withColumn("splitted",split(col("중분류")," ")).withColumn("exploded",explode(col("splitted"))).select("중분류","splitted","exploded").filter(col("대분류")=="교통").show()

->위의 코드에서 exploded한 새 컬럼 추가. explode: 값을 쪼개서 새로운 row로만든다. 버스 17이면 버스한줄 17한줄. 단순컬럼에는 안된다! 구조체나 배열로 나눠져있는컬럼에만 적용되는것같음.

# map, 키를통해 값에 접근하자

card2010.select(create_map(col("이용일"),col("금액")).alias("complexmap")).show()
-> create_map:키를통해 값에 접근하게 해주는 역할을한다.

spark.sql("""

select map(`이용일`,`금액`)as complexmap
from card

""").show()


card2010.select(create_map(col("이용일"),col("금액")).alias("complexmap")).selectExpr("complexmap['20201005']").show()
->단순 이용일이라는 컬럼에 where조건을 적용한것과같다. 일단 이용일과 금액을 묶고, 이용일이 키가되어있으니까 거기에 20201005이라는 조건을 줘서 이용일이 저 값인애들을 찾아와서 값이있으면 그대로, 없으면 null


# explod+map 을 같이사용해보자

card2010.select(explode(create_map(col('이용일'),col('금액')))).show()

spark.sql("""
select explode(map(`이용일`,`금액`))
from card
""").show()

-> map이 키,밸류로 묶어놨는데 explode가 키,밸류를 다시 풀어서 각각으로 나눠버림.

```