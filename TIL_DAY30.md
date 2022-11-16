# TIL_DAY(2022-11-15)

### ★lambda x,y :x + y ->익명함수식인데 def dd(x,y):x+y return dd 와 같다. 재활용이냐 재활용안되느냐의 차이
-----

## Spark2

실습 데이터
```python
member = ['CaptainAmerica', 'Thor', 'Hulk', 'IronMan', 'BlackWidow', 'Hawkeye', 'Hulk']
avengers = sc.parallelize(member, 2)
avengers.collect()

nums = sc.parallelize([1, 4, 2, 3, 7, 6, 5], 1)
nums.collect()
```

## action연산을써보자

|이름|설명|
|:---:|:---:|
|max()|최대|
|min()|최소|
|mean()|평균|
|variance()|분산|
|stdev()|표준편차|
|stats()|개수,평균,표준편차,최소,최대값 같이나옴|
|take(n)|n개가져와주세요|
|takeOrdered(n)|n개를 정렬해서 앞에서부터가져온다.(오름차순)|
|top(n)|정렬해서 뒤에서부터 3개가져온다. 내림차순 == sortby(lambda x:x).collect</br>()|
|countByValue| 각 값의 갯수를 세어준다. ※메모리에 저장(올려서)숫자를 세기때문에</br>데이터가 큰 경우는 위험하다. 따로 갯수를세는 함수를만들어서 사용하는게편함 변수.|
|reduce(계산식)|계산식대로 계산한다.파티션단위로 병렬연산해서 다시 합치는방식이다.|
|rdd.fold(0,max)|기본값(시작값),max(구할값) 파티션별로 가장큰값을구하고,구한 파티션별</br>큰값중에서 다시 제일큰값을찾아서 반환한다. 즉 파티션별로 계산이일어남 |
|.aggreagte|파티션별로 값을구해서 식으로 '집계'한다.파티션별 집계함수|


```python
ex)rdd01.aggreagte(0,max lambda x,y : x+y) 

ex2).reduce를사용하여 avengers에서 가장 긴 단어, 짧은단어를찾자

2-1. 가장 긴 단어

def longvengers(x,y):
	if len(x) > len(y):
		return x
	else:
		return y

longest=avengers.reduce(longvengers)
longest

2-2. 가장 짧은단어(lambda사용)

shortest=avengers.reduce(lambda x,y : y if len(x) > len(y) else x)
shortest

```
### 하둡에 파일을 저장하고 확인해보자

**saveAsTextFile('경로')**
->avengers.saveAsTextFile('/avengers')

hdfs dfs -ls /~: 터미널 하둡에서 확인. ls뒤에 찾을파일의 경로를넣으면된다. -cat같이사용가능
localhost:9870 : 9870포트에서 확인

★현재 작업환경에서는 마스터가 yarn이다.
어제 master를 yarn으로 잡았기때문에,하둡으로 올라가고 기본은 master가 local이다.

**즉 하둡에 올리려면 설정에서 master를 yarn으로해줘야한다.**

**textFile('파일') : 하둡에올라와있는 텍스트파일을 가져온다.**

↓↓↓↓↓

    result = sc.textFile('/avengers/part-*')

    확인작업
    result

    result.collect()

    ※df.write은 베이직 액션에 속한다

    하둡의 anengers의 part(파티션)을다가져온다.



**rdd의 파티션 갯수변경 방법**

|이름|설명|예시|
|:---:|:---:|:---:|
|repartition()|파티션 늘리기/줄이기 둘다가능 셔플o|RDD.repartition</br>(numPartitions: int) ->지정한 파티션갯수를가진 새로운 rdd반환한다.</br>coalesce를기반으로 작동한다.|
|coalesce()|파티션 줄이기만가능 셔플x(기본값이 셔플을하지않음.</br> 늘리려면 셔플을true로바꿔줘야함)|rdd.coalesce (numPartitions: Int, shuffle: Boolean = false)->새로운rdd반환.기본값 셔플false|
|셔플|컴퓨터가 알아서 내부에서 정렬하는작업.</br> 정렬된값을가지고 우리가지정한 동작을수행| reduce,Bykey등등|

**하둡에 파일을 올릴때 중복된 디렉터리에는 업로드X. 덮어쓰기도 안된다. 새로운 디렉터리에 욜려야함. (파티션 갯수를변경해서 같은 디렉터리에 올리는것도X)**

```python
ex)

avengers=avengers.coalesce(1)

avengers.saveAsTextFile('/avengers_u')

->위에서 파티션을2개설정했고 그걸 coalesce로 줄였다.늘리지않을거니까 셔플false값 기본유지


rdd.getNumPartitions() : rdd개수확인
```
### 하둡 권한변경

hdfs dfs -chmod 777or744.. /디렉터리or사용자명
->만약 /avengers 안의 파티션을 삭제하고싶다. 그러면, hdfs dfs -chmod 777 /avengers (777추천x)

hdfs dfs -chmod 777or766.. /
->/ 권한변경

## key,value조작

**keyBy**

키를만들어준다.
keyVal = avengers.keyBy(lambda x:x[0]) : 


키를 따로 만들어서 아래처럼 키와 밸류로 나눠서 가져올수잇다.

keyVal.keys().collect()
keyVal.values().collect()


**mapValues**

keyVal.mapValues(lambda x: list(x)).collect()

람다식으로 밸류값을 다 분해한다.

**flatMapValues**

keyVal.flatMapValues(lambda x:list(x)).collect()

[(키1:키1의분할된값1),(키2:키1의분할된값2),....] 이런식으로나온다.


**groupByKey**

keyVal.groupByKey().mapValues(list).collect()
->그룹으로 다시묶은다음,리스트로 가져와라.


keyVal.groupByKey().mapValues(lambda x:list(x)).collect()

**redueceByKey 를 이용하여 [...('키','값1,값2,값3')...]의형태로 출력하자

keyVal.reduceByKey(lambda x,y : x+ ','+'y').collect()

->keyVal의 키끼리 묶고, 람다로 '키', '값 +','+'y'형태로만들어줬다.

**.countByKey()**

각 키의 갯수(ex: c:1 h:3...)


## shakespeare.txt를 가지고 실습해보자

[예제데이터](https://github.com/brunoklein99/deep-learning-notes/shakespeare.txt)


```python

# 로컬에서 shakespeare.txt를 하둡에올려보자

※로컬에 shakespeare.txt가있고, 다른터미널에서 스파크가 실행중인 가정하에

hdfs dfs -put shakespeare.txt shakespeare.txt
-> 하둡에 shakespeare.txt라는 이름으로 shakespeare.txt가 올라간다.

파일이 올라가있는 경로가,(localhost:9870에접속해서) user->계정이름->shakespeare.txt 에있다.

/user/계정명/ 이렇게찾아가도된다.

# 파일을가져와서 10개만 출력하자

inputFile='shakespeare.txt'(파일명) #인풋파일이라는안에 셰익스피어.txt를넣고
wordcount=sc.textFile(inputFile) #가져와서 wordcount에넣는다
wordcount.take(10) #그중10개만


# 공백 데이터 제거
wordcount=wordcount.filter(lambda x: len(x) >0)
->람다함수로 x(문자)가 길이가 0보다 큰것(공백은 포함안됨)을 만족하는 애들만 필터링한다.
wordcount.collect() or wordcount.take(5)

# 문자가 아닌 것으로 자르기(re.split('\W+',x) ->대문자로하면 문자가아닌것,소문자로하면 문자인것으로해서 공백만나옴

import re
wordcount = wordcount.flatMap(lambda x: re.split('\W+',x))
wordcount.take(20)

# 공백 데이터 제거

wordcount=wordcount.filter(lambda x:len(x)>0)
wordcount.take(20)

# (단어, 1) 형태로 변경

wordcount=wordcount.map(lambda x:(x,lower(),1))
wordcount.take(5)

# 같은 키 값 기준으로 뒤의 숫자 더하기

키를기준으로 '집계연산'=reduceByKey

wordcount=wordcount.reduceByKey(lambda x,y : x+y)
wordcount.take(10)

각 단어가 몇번나왔는지나옴(키를기준으로 나온횟수를더햇다 람다로)그래서 단어의갯수가나온것

# (단어, 숫자) -> (숫자, 단어) 형태로 변환

wordcount=wordcount.map(lambda x:(x[1],x[0]))
wordcount.take(10)

# 내림차순으로 정렬

wordcount=wordcount.sortByKey(ascending=False) # sortByKey(ascending=T/F)T:오름,F:내림 OR 람다식
wordcount.take(10)


```

## dataframe 사용해보자

실습데이터(card이용내역 csv,json파일)

hdfs dfs -put card_data card_data
->하둡에 카드데이터.zip을 올림


```python

mynums=spark.range(1000).toDF('nums') # 카드는아니고 연습용 데이터프레임을하나 생성

printSchema()() : 지정한파일의 스키마가나옴

head(n)/tail(n) : 앞에서/뒤에서 n개

.show() : 표로나온다. 기본적으로 20개씩나옴

ex)

myEvens =myNums.where('nums %  2 = 0') #.where():조건
myEvens.show()

->짝수만 출력

# 하둡에올린 카드데이터를 가져와서써보자.

card2010 =spark.read.csv('card_data/csv/202010.csv')
card2010.printSchema()
card2010.show()

# 위에서 가져온데이터프레임의 컬럼명도같이가져오자!

card2010=spark.read.format('csv').option('header','true').load('card_data/csv/202010.csv')
->option'header','true'가 컬럼명가져올지안가져올지 여부

card2010.printSchema() #여기서부터 컬럼명:내용 이렇게나온다.
card2010.show()

# 실행계획 excution plan :sql작동순서

card2010.sort('이용일').explain() ->읽을때 정보를 아래에서 위로 읽어야한다.대략 ~를 어디에있는파일이 어떤거고, 어디에있는걸 어떻게가져올거야 하고, sort가 마지막으로 동작

card2010.sort('이용일').show()

card2010.show(3)

card2010.show(card2010.count()) ->기본이20개만가져오는건데 이렇게쓰면 다가져옴


#inferSchema

card2010=spark.read.format('csv').option('header','true').option('inferSchema','true').load('card_cata/csv/202010.csv')

card2010.printSchema()
->inferSchema true : 타입추론(정확성은 높아지지만,가지고오는 속도가 느려질수있다.)

#table생성해서 sql구문으로가져오기

card2010.createOrReplaceTempView('card')
spark.sql('select * from card').show

->sql구문으로 가져올수있다. 테이블을 생성했기때문에

# ★한글을쓸때 ``(~옆에있는)을 사용해야한다.★

spark.sql("""
select `이용일`,`결제일`,`금액`,`포인트금액`,`대분류`,`중분류`,`소분류` 
from card
""").show()


sc.~ =rdd조작
spark.~ = dataframe조작 

->sc붙으면 타입이 rdd이고 spark.~타입이 데이터프레임

# explain으로 두 데이터프레임을 비교해보자. 튜닝작업 중 하나.

튜닝:최고의성능을뽑아내기위해서 쿼리를 최적화하는작업

df01 = card2010.groupby("이용일").count()
df01.show()

df02 = spark.sql("""
select `이용일`,count(*)
from card
group by `이용일`
""")
df02.show()

df01.explain()
df02.explain()

->01,02은 plan_id말고 다른게없다! = 그래서 함수를쓰거나,sql로쓰거나 다를게없다!


#이용금액이 max인 값을 가져오자

from pyspark.sql.functions import max
card2010.select(max('금액')).show()

↓↓ 

spark.sql("""
select max(`금액`)
from card
""").show()

-> 위의 select 와 sql문의 select는 같은것

ex2)

spark.sql("""
select `대분류`,`중분류`,`금액`
from card
""").show()

card2010.select('대분류','중분류','금액').show()

#expr

from pyspark.sql.functions import expr,col

card2010.select(expr("`대분류`as category"),col("`금액`")).show()
->expr: 안에 sql표현식을 넣을수있도록 도와주는친구.주로 alias주는방법을까먹었을때 사용.
★그외에도 산술연산,타입변환,조건문 자리에서 expr조건문을줘서 처리할수도있다.★
반환값은 컬럼객체

column = col 


↓↓↓↓↓↓

card2010.select(expr("`대분류`").alias("category"),col("`금액`")).show()

↓↓↓↓↓↓

spark.sql("""
select `대분류` as category, `금액`
from card
"""
).show()

세개 다 같은것.

#selectExpr (select+expr)

card2010.selectExpr("`대분류` as category","`금액`").show()

card2010.selectExpr("*","`금액` >40000").show()

※따옴표주의! 금액과 비교할조건이 같은""안에들어가있어야한다.


spark.sql("""
select * , `금액` > 40000
from card
""")

# 금액의 평균을 출력하자

spark.sql("""
select avg(`금액`)
from card
""").show()

↓↓↓↓ 알아서 평균을내줌

card2010.selectExpr("avg(`금액`)").show()

# withColumn

card2010.withColumn("up4",expr("`금액`>40000")).show()

->withColumn은 이름을 바꿔서 저장하겠다라는 의미이다. expr의결과를 up4라는이름으로바꾼다는의미.withColumn("컬럼명", 조건), 지금은 바로 .show()로 보여주고있기때문에 실제 card2010에
저장되지는않는다. 저장하려면 card2010 = ~ 로 넣어야함

↓↓↓ 같은 의미이다. 

spark.sql("""
select * ,`금액`>40000 as up4
from card
""").show()


#withColumnRenamed

card2010.withColumnRenamed("대분류","category").show()


spark.sql("""
select `이용일`,`결제일`,`금액`,`포인트리금액`,`대분류`as category,`중분류`,`소분류`
from card
""").show()

withColumnRenamed:반환 타입이 데이터프레임이고, withColumnRenamed(컬럼이름,바뀔컬럼이름)
※'존재하는열만' 바꿔준다. 기존에있는 컬럼만 가능한거고
※withColumn(컬럼이름,col객체) : col객체를 내가원하는 조건대로할수도있다. 즉 얘는 기존에있는것만 바꿔주는게아니라 일종의 생성도 가능하다는것.


#drop

card2010.drop("결제일").show()
card2010.drop("결제일","포인트리금액").show()

#col조건

card2010.filter(col("금액")<10000).show()
card2010.where(col("금액")<10000).show()

↓↓↓

spark.sql("""
select * from card where `금액` < 10000""").show()

※where = filter 같은거다.

card2010.where("금액"<10000).show() : 오류나는이유는 where가 sql표현식이여서.
->card2010.where(expr("`금액` < 10000")).show()


card2010.where(col('금액')<10000).where(col('금액')>5000).show()

↓↓↓

spark.sql("""
select *
from card
where `금액` <10000 and `금액`>5000
""").show()

spark.sql("""
select *
from card
where `금액` between 5000 and 9999
""").show()

※동시에 모든 조건수행시 특정상황에서 잘못나올수있다.

# distincet를 사용해보자

card2010.select("대분류").distinct().show()

↓↓↓

spark.sql("""
select distinct(`대분류`)
from card
""").show()

#
card2010.select("대분류","중분류").distinct().show()
->대분류와 중분류가 중복되지않게 나옴 식사:카페 1개 식사:한식1개 나오면 식사:한식 이 더이상안나오는거지

↓↓↓

spark.sql("""select distinct(`대분류`,`중분류`)from card""").show() ->구조체로나온다.

↓↓↓

spark.sql("""
select `대분류`,`중분류`
from card
group by `대분류`,`중분류`
""").show()


```

