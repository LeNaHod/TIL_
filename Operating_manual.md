# Spark 기본 조작 매뉴얼(우분투)

## Rdd를 하나 생성하여 하둡에 파일을 올려보자

★하둡에서 명렁어 사용시, hdfs '-'명령어 옵션 이다. 앞에 '-'를 붙이면 대부분 O

EX)하둡에 올라가있는 특정 디렉터리삭제 :  hdfs dfs -rm [옵션] 삭제할폴더경로

```python

1.pyspark
test=[1,2,3,"Abc,Def",'Gh'] 테스트 데이터 생성
rdd01=sc.parallelize(test,3) parallelize를 통해 rdd로 변환. 파티션은3개
rdd01.collect() rdd 확인.

rdd01.saveAsTextFile('/rddtest01') 하둡에 올리기 rddtest01이라는 디렉터리안에(없으면 생성)

2.하둡에 파일 저장(올리기)

1.로컬 터미널에서 파일저장
hdfs dfs -put 원본파일명 하둡에서부를파일명

2.pyspark에서 저장

csv write(저장, 포맷은 여러가지이지만 대표적인게 csv)

card2010=spark.read.option('header','true').csv('card_data/csv/202010.csv')

card2010.write.format('csv').mode('overwrite').save('/temp/csv')

↓↓
json을 저장하고싶으면 포맷을 바꿔주면된다.

jsonDf.write.format('json').mode('overwrite').save('/tmp/json')
->다만 일반적인 {kye:value, key:{value,value...}}의 형태가아니라 {} {} {}..형태이다.

3.하둡 디렉터리권한 변경

hdfs dfs -chmod 부여할권한 /경로
EX) hdfs dfs -chmod 444 /test 

```
## 하둡에서 파일을내려받기

```python

1.헤더옵션없이 그냥가져오기

card2010 =spark.read.csv('card_data/csv/202010.csv')
-> 컬럼명이 _c0 _c1...이렇게출력

2.헤더옵션을줘서 컬럼명도 출력되게

card2010=spark.read.format('csv').option('header','true').load('card_data/csv/202010.csv')
-> 컬럼명이 생겨서 이용일, 결제일,금액...으로나옴

3.원하는구조의 데이터프레임에 넣어서 가져오기

EX)한글csv->영어로 가져와보자

from pyspark.sql.types import *

engColumns = StructType([
	StructField('postdate', IntegerType(), True),
	StructField('transdate', IntegerType(), True),
	StructField('amount', IntegerType(), True),
	StructField('pointree', IntegerType(), True),
	StructField('maincategory', StringType(), True),
	StructField('subcategory', StringType(), True),
	StructField('store', StringType(), True)
])

StructType: 구조체유형(구조체x).row이다. StructFiedl와 한묶음이라고 생각
StructField: StructType과 한묶음. ()안에 각  컬럼명,컬럼유형(string,integer..),T/F
add : 위와같이 StructType([StructField(내용),StructField(내용)..]) 한번에 넣을수도있지만, StructType().add(컬럼명1,타입,T/F).add(컬럼명2,타입,T/F)로할수도있다.

engColumns = StructType([
	StructField('postdate', IntegerType(), True),
	StructField('transdate', IntegerType(), True))]
	↓↓↓↓
engColumns = StructType().add('postdate',IntegerType(),True).add('transdate',IntegerType(),True)

두개의 결과는같다.

card2010=spark.read.format('csv').option('header','true').schema(engColumns).load('card_data/csv/202010.csv')
->card2010을 아까 위에서 만든 engColumns틀에 넣는다.

4.json파일을 불러오기

json2010 =spark.read.format('json').load('card_data/json/202010.json')
-> #json2010=spark.read.json('card_data/json/202010.json')
```