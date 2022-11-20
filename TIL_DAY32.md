TIL DAY 32(2022-11-17)

# 파일불러오기
cardAll= spark.read.format("csv").option("header","true").option("inferSchema","true").load("card_data/csv/*csv")
cardAll.show()
cardAll.createOrReplaceTempView("cardall")

```python
#ROLLUP
from pyspark.sql.functions import *

rollupDf=cardAll.rollup(col("이용일"),col("대분류")).agg(avg(col("금액")).alias("avgpay")).selectExpr("이용일","대분류","avgpay").orderBy(col("이용일"))


spark.sql("""
select `이용일`,`대분류`,avg(`금액`) as avgpay
from cardAll
group by ROLLUP(`이용일`,`대분류`)
order by `이용일`
""").show()

#substring을이용해서 원하는 날짜만 출력

rollupDf=cardAll.rollup(col("이용일"),col("대분류")).agg(avg(col("금액")).alias("avgpay")).selectExpr("이용일","대분류","avgpay").filter(substring(col("이용일"),1,6)=="2019-01").orderBy(col("이용일")

rollupDf.show()

#cube

cubeDf=cardAll.cube(col("이용일"),col("대분류")).agg(avg(col("금액")).alias("avgpay")).select(col("이용일"),col("대분류"),col("avgpay")).orderBy(col("이용일"))

->rollup이랑 사용방법은 동일.결과만 다름


spark.sql("""
select `이용일`,`대분류`,avg(`금액`)as avgpay
from cardall
group by cube(`이용일`,`대분류`)
order by `이용일`
""").show()


cubeDf.show()


# Join을 해보자!

heroes  = spark.createDataFrame([
    (1, 'iron man', 1, [1]),
  	(2, 'batman', 3, [1]),
  	(3, 'captain america', 1, [1]),
  	(4, 'deadpool', 2, [1, 2]),
    (5, 'superman', 3, [1]),
    (6, 'harley quinn', 4, [2]),
    (7, 'dooly', 0, [0])
]).toDF('id', 'name', 'team', 'job')

teams = spark.createDataFrame([
    (1, 'avengers', 'marvel'),
    (2, 'x-force', 'marvel'),
    (3, 'justice league', 'dc'),
    (4, 'suicide squad', 'dc'),
    (5, 'guardians of galaxy', 'marvel')
]).toDF('id', 'team', 'comics')

jobs = spark.createDataFrame([
    (1, 'hero'),
    (2, 'villain')
]).toDF('id', 'job')

heroes.show()
teams.show()
jobs.show()

heroes.createOrReplaceTempView("heroes")
teams.createOrReplaceTempView("teams")
jobs.createOrReplaceTempView("jobs")

joinCondition = heroes["team"] == teams["id"]
-> # joincondition = herose.team == teams.id 로도 쓸수있다, 둘이같은것

heroes.join(teams,joinCondition).show()
->조인만해놨기때문에 위와같이 따로 조회해야한다.

★join시 기본값 innerjoin!


spark.sql("""
select *
from heroes join teams on(heroes.team = teams.id)
""").show()


heroes.join(teams,joinCondition,'inner').show()
->특정 조인으로 조인하고싶을땐 뒤에 명시해준다.

spark.sql("""
select * from heroes inner join teams on (heroes.team = teams.id)""").show()

# outer join

heroes.join(teams,joinCondition,'outer').show()
->위에서 join을 이미 만들어놨기때문에 조인유형만 바꿔주면된다. 단, ★여기서말하는 outer=fullouter join이다!


spark.sql("""
select *
from heroes full outer join teams on(heroes.team = teams.id)
""").show()

->그래서 sql문에서도 full outer join이라고 명시해줘야한다.


#left outer

heroes.join(teams,joinCondition,'left').show()

heroes.join(teams,joinCondition,'left_outer').show()

->left조인으로쓰나 leftouter조인으로쓰나 결과는같음

저자리에 어떤종류가올수있을까??

기본조인외에도 cross,(left)semi, anti 등등이 올 수있다. ★right semi,anti는 구현안되어있다!

|종류|설명|예시|
|:---:|:---:|:---:|
|left semi|inner join이후 결과에서 오른쪽과 일치하는 왼쪽데이터만가져온다!|</br>heroes.join(teams,joinCondition,'left_semi').show()|
|left anti join|오른쪽과 일치하지않는 왼쪽의 데이터만(차집합)|</br>heroes.join(teams,joinCondition,'left_anti').show()|


(left semi)
spark.sql("""
select *
from heroes left semi join teams on (heroes.team = teams.id)
""").show()

(left anti)
spark.sql("""
select * from heroes left anti join teams on(heroes.team=teams.id)
""").show()


(left outer)
spark.sql("""
select*
from heroes left outer join teams on(heroes.team = teams.id)
""").show()

(cross join)

spark.sql("""
select * from heroes join teams
""").show()

heroes.join(teams,joinCondition,'cross').show()

heroes.join(teams,how='cross').show()
-># heroes.join(teams).show() 결과동일!

# 배열데이터로 조인을하자

array_contains(배열안에 해당값이 있는지 없는지 확인후 t/f로 반환하는친구)를 이용하자

heroes.show()
jobs.show()



tt = array_contains(heroes["job"],jobs["id"])
heroes.join(jobs,tt).show()

->이렇게 따로 선언해서 쓸수도있고

heroes.join(jobs,array_contains(heroes["job"],jobs["id"])).show()
->바로 식에 넣어도된다.


★
spark.sql("""
select 
from
""")
->select *
from emp join salgrade on (emp.sal between salgrade.losal and salgrade.hisal) 의 on부분과 비슷하다!
따지자면 non-eque join축에 속하지않을까


# right outer
heroes.join(teams,joinCondition,'right').show()

spark.sql("""
select*
from heroes right outer join teams on(heroes.team = teams.id)
""").show()

->left에서 right로만 바꿔주면된다!


# RDD를 만드는방법 정리

1.rdd.toDF(schema)
2.createDataFrame(list(Row()),schema)
3.createDataFrame(list(tuple()),schema)

(2)
df = spark.createDataFrame([(1,2,"simple,fast,scalable,unified")],'test1 int, test2 string, test3 string')
df.show()

->to_pandas로도 변환할수있다. 번외로 pandas를 가져와서 pandas에서 데이터프레임을 생성해서 가져오는 방법도있다.



# lit를 표현하는 방법들

lit은 일단 improt 해와야한다.

from pyspark.sql.functions import lit

spark.sql("""
select 3 as three
""").show()

df.select(lit(3).alias("three")).show()

# cast(변환)

df.select(col("test2"),col("test2").cast("int")+1, col("test2")+1).show()

->cast안에는 ★변환할 타입★ 이온다.

df.select(col("test2"),col("test2").cast("int")+1 , col("test2")+1).summary
->summary로 구조를 자세하게 확인할수있다. cast로 명시적으로 형변환해주면 명시해준 타입으로, 묵시적(명시x)이면
가장 큰 타입으로 자동으로 변환된다. (test2 +1 은 위와같은경우 double로 잡힘)


# 문자열 함수

#  lower,upper,initcap

from pyspark.sql.functions import lower,upper,initcap

df.select(lit('spark'),lower(lit('spark')),upper(lit('spark')),initcap(lit('spark'))).show()

->lower: 모두소문자로, upper : 모두대문자로, initcap:첫글자만 대문자로

# ltrim,rtrim,trim / lpad, rpad

df.select(ltrim(lit('   spark   ')).alias('ltrim'),rtrim(lit('   spark   ')).alias('rtrim'),trim(lit('   spark   ')).alias('trim'),lpad(lit('spark'),10,'*').alias('lpad'),rpad(lit('spark'),10,'*').alias('rpad')).show()

->pad류 : 정렬하고, 남은공간 지정문자로 채우기


# 파일불러오기 상세

# 한글csv->영어로 가져와보자

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
->card데이터를 저장할 schema구조! 구조체가x. 그냥 이 스키마가 StructType인것임, 즉 스키마를 생성했다고 생각하면될것같음

card2010=spark.read.format('csv').option('header','true').schema(engColumns).load('card_data/csv/202010.csv')
->schema(engColumns) = 이 데이터(card)를 저장할 스키마를 engColumns로 지정해줬다.
card2010.show()

# csv write(저장)

card2010=spark.read.option('header','true').csv('card_data/csv/202010.csv')

card2010.write.format('csv').mode('overwrite').save('/temp/csv')

(파이어폭스/확인용)
localhost:9870 

#json

json2010 =spark.read.format('json').load('card_data/json/202010.json')
-> #json2010=spark.read.json('card_data/json/202010.json')

json2010.show()
json2010.printSchema()


json2010.select(explode(col('list'))).show()
->list컬럼안에 값들이있어서

tempDf=json2010.select(explode(col('list')).alias('temp'))
tempDf.show()
tempDf.printSchema()

tempDf.select('temp.*').show()



jsonDf=tempDf.select('temp.*')
jsonDf.show()
jsonDf.printSchema()


스트럭트구조라서 쪼개서쪼개서 분해도 이렇게했다.list에서 temp


# json저장하기!

jsonDf.write.format('json').mode('overwrite').save('/tmp/json')

hdfs dfs -cat /tmp/json/*.json

# 일반적인 json 구조 : {k : {}, {} ...}
# 스파크의 json 구조 : {} {} {} {}... 

->★그래서 스파크에서 json으로 저장하는거보단 다른형태로 저장하는게 좋다!

# 그 외 저장형식

parauet:spark 컬럼 기반 데이터 저장형식
orc : hadoop컬럼 기반 데이터 저장형식
db : 하이브,오라클,마이에스큐엘,몽고,카산드라
text : text


# 어플리케이션 생성/ 버전 & install

cd spark
-> /spark $ cat RELELASE 현재 스파크버전 확인

=============매우중요=============
★pyspark의 버전과 스파크의 버전이 일치해야한다
그래서 

★pip install pyspark == 스파크버전

(현재 작업환경은 spark 3.2.2버전을 쓰고있어서 pip install pyspark==3.2.2)

==================================

sc = rdd/ 콘텍스트
spark = df / 세션

어플리케이션을 만든다 : == 파이썬 파일을 만든다.

1. vim spark_app.py 해서 파일을 연다.

아래내용 입력

from pyspark.sql import SparkSession

if __name__=="__main__":
    spark = SparkSession.builder.master("local").appName("myCount").getOrCreate()
    print(spark.range(1,1001).selectExpr("sum(id)").collect())


2. 실행해보자

spark-submit spark_app.py

->python spark_app.py 
->이렇게해도 실행되는이유는 아까 pip install pyspark==3.2.2를 위에서 설치했기때문! 그렇다면 pyspark 3.2.2를 설치가안되어있으면 버전이 맞지않아서 실행X

# Zeppelin 노트북을 설치해보자

1.[재플린다운로드링크](https://zeppelin.apache.org/download.html)

다운로드링크에서 netinst버전 클릭 -> 다운로드링크 복사 -> 

wget https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-netinst.tgz 입력


2. 심볼릭링크 생성

ln -s zeppelin-0.10.1-bin-netinst zeppelin


3. ~/.bashrc 에서 zeppelin추가

export ZEPPELIN_HOME=/home/계정명/zeppelin
export PATH=$PATH:$ZEPPELIN_HOME/bin

저장하고,

source ~/.bashrc 


4. zeppelin-env.sh 설정


cd $ZEPPELIN_HOME/conf 로 이동!

~/zeppelin/conf$ < 이경로에서 파일있는지 확인하고, 여기서 작업!


cp zeppelin-env.sh.template zeppelin-env.sh
->cp로 zeppelin-env.sh.template -> zeppelin-env.sh로 카피

(vim으로 파일오픈)
vim zeppelin-env.sh

19번째줄
export JAVA_HOME=/home/계정명/java

79번째줄
export SPARK_HOME=/home/계정명/spark

89번째줄
export HADOOP_CONF_DIR=/home/계정명/hadoop/etc/hadoop 


5. zeppelin-site.xml 설정

cp zeppelin-site.xml.template zeppelin-site.xml

vim zeppelin-site.xml

# 포트밸류값 변경!

<value>127.0.0.1 -> 0.0.0.0</vaule>

<value>8080 -> 8987</vaule>


6.zeppelin-daemon.sh 실행 확인

cd 입력해서 최상위로 이동 후

zeppelin-daemon.sh start

localhost:8987 
->파이어폭스에 localhost:8987 입력하면 welcome to zeppelin 하면서 재플린 비행선페이지가나옴.


7. Interpreters 설정
8987에서 어노니먼스 ->  Interpreter ->spark 검색 ->edit클릭

edit모드가되면

spark.master local[*] -> yarn으로 바꿔줌

spark.submit.deployMode ->client (우리는 지금 싱글노드이기때문에)

그리고 맨밑에 save버튼클릭해서 저장.

8.노트북을 사용해보자

★시프트+스페이스: 한/영전환

상단의 노트북버튼클릭해서 create new note해서 추가, 사용하면된다

#test 디렉터리를 하나 만들어보자

(하얀부분이 셸)

%pyspark ->인터프리터를 pyspark

cardAll = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("card_data/csv/*.csv")
cardAll.show()


#조작

%pyspark

cardAll.createOrReplaceTempView("cardAll")

%sql

select * from cardall
->에러남!

터미널에가서 cd spark/jars로 이동 , 

#터미널에서 특정 단어를 가지고있는것을 찾기

ls |grep lang ( |<or의 파이프라인. lang을 포함하는것들을 찾아라! 라는의미)

commons-lang3-3.12.0.jar ->얘때문에 오류남 java버전이안맞아서 나는 오류이므로, 다운로드받아줘야한다.

# commons-lang3 다운로드작업

https://commons.apache.org/proper/commons-lang/ 접속 ->좌측에 다운로드클릭->
commons-lang-2.6-bin.tar.gz 다운로드 링크복사

cd 최상위로와서

wget https://dlcdn.apache.org//commons/lang/binaries/commons-lang-2.6-bin.tar.gz

(압축해제)
tar xvzf commons-lang-2.6-bin.tar.gz 

cd commons-lang-2.6/
-> ~/commons-lang-2.6$  경로이동.

#카피작업

cp commons-lang-2.6.jar $SPARK_HOME/jars/

(이동해서 확인)
cd $SPARK_HOME/jars

ls |grep lang
-> commons-lang-2.6.jar이 있는지 확인


#재플린 재시작

cd 루트로이동

zeppelin-daemon.sh stop

zeppelin-daemon.sh start

#재플린의 장점!

각종그래프를 알아서 그려주고 컬럼별로도 계산해준다.

그래프옆에 setting-> 컬럼별, 집계별로 그래프를 그릴수있다.

그래프 사이즈조절도 가능해서, 하나에 두개 그래프도 볼수있다. 코드숨기기는 디폴트말고 레포트 등 여러모드로바꾸면 안보임!


# mysql을 설치해보자!

(사전작업)

재플린노트북이 켜져있다면끄고 여러가지 다른것도 종료

zeppelin-daemon.sh stop / stop-all.sh


1.mysql을 다운로드받자

sudo apt install mysql-server -y

(확인해보자)

sudo service mysql start ->시작

sudo service mysql status 
->q누르면 종료됨, 작업관리자의 서비스부분을 상세하게 확인할수있다.


2.재부팅해도 서비스가 자동실행되게 설정

sudo systemctl enable mysql ->서비스돌아가는 상태에서! 코드실행 후 status에 enable이라고 뜨면 성공.

3.원하는계정으로 접속해서 비밀번호를 변경해주고,자동로그인하자
==============================================================
★쓰고싶은 계정명을 넣으면된다 패스워드부분도 쓰고싶은걸로

sudo mysql -u 계정명
->mysql을 입력한 계정명으로 시작

alter user '계정명'@'localhost' identified with mysql_native_password by 비밀번호입력

create user '계정명'@'%' identified by 비밀번호입력

#권한주기

grant all privileges on *.* to '계정명'@'localhost' with grant option;

grant all privileges on *.* to '계정명'@'%' with grant option;

flush privileges;

=================================================================
'계정명'@'localhost' ->로컬호스트가 사용하는 계정이라는 의미

'계정명'@'%' ->어디서든(외부) 접근가능한 계정이라는 의미이다.

# test테이블을 만들어보자. 

(사전작업)
use mysql; ->use 선택할데이터베이스이름

create table test(id int, name varchar(30));
insert into test values(1, 'hadoop');
insert into test values(2, 'spark');

exit : mysql종료


# mysql-connector-java 설치

mysql-connector-java : mysql 과 java를 연결시켜주는 친구.

#설치

[다운로드링크](https://dev.mysql.com/downloads/) -> Connector/J ->우분투 리눅스 -> 각자맞는 os버전선택 ->다운로드버튼클릭 -> 하단의 No thanks, just start my download 링크 카피 

wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-j_8.0.31-1ubuntu20.04_all.deb


sudo dpkg -i mysql-connector-j_8.0.31-1ubuntu20.04_all.deb 

cd /usr/share/java
->libintl.jar  mysql-connector-j-8.0.31.jar 파일있는지 확인


# spark-defaults.conf 설정(스파크에 mysql을 연결하는것임)

해놓으면 재플린, 스파크 어디에서든 쓸수있다.

/usr/share/java/mysql-connector-j-8.0.31.jar ->
우선 경로를 복사해놓자

cd $SPARK_HOME/conf ->경로로 이동 후

vim spark-defaults.conf ->입력

spark-defaults.conf 내용 하단에 

spark.jars 	/usr/share/java/mysql-connector-j-8.0.31.jar 입력



# spark와 데이터베이스연결

(아래는 로컬 데이터베이스로 접속)
user="계정명"
password="비밀번호"
★url="jdbc:mysql://localhost:포트번호/mysql" ->mysql접속경로
driver="com.mysql.cj.jdbc.Driver"
dbtable="베이스테이블이름"


# mysql(mysql데이터베이스)에 저장해놨던 테이블을 스파크에서 불러와보자
 
testDf=spark.read.format("jdbc").option("user",user).option("password",password).option("url",url).option("driver",driver).option("dbtable",dbtable).load() ->jdbc라는포맷, 어떤계정에 어떤드라이버,어떤페스워드, 어떤데이터테이블을쓸건지를 가져옴. 로드가 셀렉트역할

↓
(한줄로넣기 option->options 로 바뀜)
spark.read.format("jdbc").options(user=user, password=password, url=url, driver=driver, dbtable=dbtable).load()

testDf.show()


#★spark에서 만든 테이블->mysql로 저장

(예제 데이터 생성)
testinsert = [(3,"mysql"),(4,"zeppelin")]
insertDf = sc.parallelize(testinsert).toDF(["id","name"])

inserDf.show()

insertDf.write.jdbc(url,dbtable,"append",properties={"driver":driver, "user":user,"password":password})
->inserDf를 jdbc포맷으로 저장할것이다. 옵션이 append니까 추가해서 저장한다.프로퍼티스에 딕셔너리형태로 계정 접속정보가 들어가있다.

testDf.show()

->그래서 기존에있던 testDf내용에 inserDf의 내용이 추가되서 출력된다!.
```

