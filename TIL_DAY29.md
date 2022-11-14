# TIL DAY (2022-11-14)

# HADOOP

- 여러대의 서버에 데이터를 분산저장한다.
- java기반
- 대용량 데이터(빅데이터) 분산 저장 및 처리할 수 있는 오픈소스 프레임워크

**우리는?**
하둡 (데이터 저장) -> 스파크 (데이터 처리) -> DB에 저장 -> 이 DB를 사용해서 Django시각화 흐름으로 진행할것이다.

### HDFS는 뭔데?

- 대용량 데이터 분산 파일 시스템의 약자이다. 구글 파일 시스템을 기반으로 분산/저장 처리.
- **Namenode와 Datanode를가지고 있다.**

### MapReduce,Yarn

- MapReduce:데이터셋 **병렬처리**하는 역할.다만 느려서 스파크(처리집중)를많이씀
- Yarn: 작업 예약 및 리소스 **관리** . 작업관리자라고생각하면 편함(nodemanager,resourcemanager가 관리를 도맡음)


## 하둡PATH설정

```python

sudo vim ~/.bashrc

#hadoop
export HADOOP_HOME=/home/big/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

source ~/.bashrc  ->소스 명령은 껏다켜야 적용되는걸 바로적용하기위한 명령어.
    
.bashrc파일은 켜면 한번실행되는 파일이다. 고로 source로 적용시켜주면 편함!

- vim hadoop-env.sh를 열어서 PATH설정을해줘야한다.

# export HADOOP_PID_DIR=/tmp 가상머신에서는 안잡힌다(AWS에서는 상관x)
->export HADOOP_PID_DIR=$HADOOP_HOME/pids 가상환경에서는 이렇게 바꿔줘야한다.

core-site.xml파일 여기에작성한 갯수만큼 Live datanode갯수가 나옴
<configuration>
	<property>
		<name>fs.defaultFS</name> # '클라이언트의 기본파일시스템' 지정 URL. hdfs://hostname:port 의 구조를 가지고있다.★ 데이터노드들이 아래 지정된 url로 하트비트를보낸다!! 필수지정
		<value>hdfs://localhost:9000</value> #file:// 가 기본형태. aws하면 local이변경되겟
	</property>
</configuration>


hdfs-site.xml


<property>
	<name>dfs.replication</name>  #기본블록을 복제하는것.파일 생성시, 복제 수 지정가능.복제내용 작성시간이 없을시 기본값 적용
	<value>1</value> #복제할수. 현재 실습환경에서는 물리적한계로 1로 설정
</property>
<property>
	<name>dfs.namenode.name.dir</name> #namenode의 hdfs파일시스템 메타데이터 저장 경로의 목록.공백x 각 경로는 ','구분. '기본값'말고 별도의 경로를 설정해주는게 좋다.(아래 기본hadoop.tmp.dir가 휘발성 디렉터리로 껏다키면 삭제됨.)
	<value>/home/big/hadoop/namenode_dir</value> #	file://${hadoop.tmp.dir}/dfs/name 가 기본형태.
</property>
<property>
	<name>dfs.namenode.secondary.http-address</name> #세컨노드를 value값의 http주소로설정
	<value>localhost:9868</value> # ip와 포트
</property>
<property>
	<name>dfs.datanode.data.dir</name> #datanode의 HDFS블록을 저장하는경로 설정. 위의 네임노드.네임.dir와 비슷한데, 단 HDFS자체에서 데이터노드끼리 복제를하기때문에, 분산저장하게된다.
	<value>/home/big/hadoop/datanode_dir</value> # file://${hadoop.tmp.dir}/dfs/data 가 기본형태이다.
</property> 



mapred-site.xml

<property>
	<name>mapreduce.framework.name</name> #vlaue값에 맵리듀스를 어떤 모드로 실행할지 설정한다. 두가지 모드가 있다 yarn/local local모드는 JVM 1개. 디버깅이나 테스트용도에 적합하고, yarn은 그냥 yarn으로 실행
	<value>yarn</value>
</property>


(command)_(subcommand)_USER
->HDFS_DATANODE_USER=root datanode를 사용할수있는 유저는 root이다. 사용자지정해주는명령어


~/.bashrc설정

# hadoop user

export HDFS_NAMENODE_USER=big  
export HDFS_DATANODE_USER=big  
export HDFS_SECONDARYNAMENODE_USER=big
export YARN_RESOURCEMANAGER_USER=big
export YARN_NODEMANAGER_USER=big #big유저는namenode,datanode,secondarynamenode,nodemananger를
사용할수있다.

	cd <현재위치변경임. 나의 위치가 루트라면 따로x
	hdfs namenode -format
	hdfs datanode -format


	WARNING: /home/big/hadoop/pids does not exist. Creating.
	WARNING: /home/big/hadoop/logs does not exist. Creating.

위와같이 하면 WARNING이 뜨는데,오류가아니라 위의 폴더들이 없으니까 만들겠다는 의미이므로
정상작동이다.

```
### Namenode란?

- 마스터역할로,hdfs에있는 (위에서 설정한거) 데이터를 datanode에 분산시키고,관리하는기능을담당
- datanode의 이상유무를 체크하는일도 처리한다. 블록관리= 클라이언트 요청 접수를한다.
- 대신, Main Namenode가 죽어버리면 클라이언트가 메인네임노드를 못쓰니까 안에 저장되어있는 데이터들을 사용할수없다!

### Secondary NameNode

- 위의 메인노드가 죽는경우를위해서, 세컨드네임노드를 설정한다. 
- 메인노드가 죽었을시 세컨드 네임노드가 메인 네임노드의 역할을 대신한다. 장애복구가 편하다.

### Datanode란?

자신에게 할당된 데이터 블록을처리(저장하고 등등)하는 역할!

**localhost:9870** ->우리는 위에서 데이터노드를 localhost:9000로 지정했기때문에 localhost:9000 active라고 나와야 정상.

저 9870으로 접속되는곳이 namenode인데 브라우저형식인것일뿐이라서
경로 /에서 우리가 원하는데이터를 요청하면 namenode가 알아서 datanode를 가져와줌

(내부동작은 안보여줌 그냥 사람보기편하라고 /~ 이런식으로 경로로잡아놓음)


**localhost:8088** ->Yarn

두개다 사이트가 동작되어야함! 9870은 하둡 8088은 yarn


    start-all.sh -> start-dfs.sh + start-yarn.sh 를 한번에실행하겠다.

    최종 동작확인 : hdfs dfsadmin -report 실행하면
    LIVE datanode(n)<연결되어있는 데이터노트갯수만큼 나오고 동작정보가나온다.

### 파일을 올려보자

(경로는 루트)

1.hdfs dfs -mkdir /test/

2.hdfs dfs -put /home/big/test.txt /test/

3.hdfs dfs -ls /test/

- Utillties ->browse directory에 들어가보면 아까만든 test.txt를 확인할수있다.
- test.txt를 눌러서 hard/tail the file 32 를 누르면 위/아래에서 각각 32바이트만큼 내용을 불러온다.

**hdfs(하둡)에서 기존명령어를 사용할때 '-'를 앞에 붙여주면 거의 다 동작함**

EX) hdfs -cat /tset/test.txt 이런식으로해도 동작 O


|파일명|내용| 
|:---:|:---:|
|hadoop-env.sh|하둡실행 시 쉘 스크립트 파일에서 필요한 환경변수설정|
|masters|보조 네임노드(Secondary NameNode)실행 서버설정파일|
|slaves|데이터 노드를 설정할 서버 설정|
|core-site.xml|**HDFS와 맵리듀스에서 공통적**으로 사용할 환경정보'설정.</br>기본값을 **hadoop-common-core-default.xml에서 오버로드**(가져온다)한다.</br>(기본값설정 안했을시 저 파일의 기본값을 따른다는것)|
|hdfs-site.xml|HDFS에서 사용할 **환경정보**설정. 얘도 hadoop-hdfs/hdfs-default.xml에서</br>기본값을 오버로드해온다.|
|mapred-site.xml|맵리듀스에서 사용할 환경정보를 설정한다.</br>hadoop-mapreduce-client-core/mapred-default.xml에서 오버로드해옴|
|yarn-site.xml|YARN에서 사용할 환경정보를 설정한다.</br>hadoop-yarn-common/yarn-default.xml에서 기본값 오버로드|

기본값 파일 생략 경로:

- core : share/doc/hadoop/hadoop-project-dist/
- hdfs : share/doc/hadoop/hadoop-project-dist/
- mapred: share/doc/hadoop/hadoop-mapreduce-client/
- yarn : share/doc/hadoop/hadoop-yarn/


## SPARK설치,경로

```python
sudo vim ~/.bashrc

# spark

export SPARK_HOME=/home/big/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
export SPARK_DIST_DLASSPATH=$($HADDOP_HOME/bin/hadoop calsspath)

### CONF로 이동하여 이름을줄여서 카피
cd $SPARK_HOME/conf
big@ubuntu:~/spark/conf$ cp workers.template workers
big@ubuntu:~/spark/conf$ cp spark-env.sh.template spark-env.sh

spark-env.sh설정

vim spark_env.sh

export JAVA_HOME=/home/big/java
export HADOOP_CONF_DIR=/home/big/hadoop/etc/hadoop
export YARN_CONF_DIR=/home/big/hadoop/etc/hadoop
export SPARK_DIST_CLASSPATH=$(/home/bin/hadoop/bin/hadoop classpath)

★export PYSPARK_PYTHON=/usr/bin/python3
export PYSPARK_DRIVER_PYTHON=/usr/bing/python3★

가상환경에서 파이스파크를 쓰고싶으면 위의 두줄을 꼭 써줘야한다. 내컴에맞게 경로설정

cp spark-defaults.conf.template spark-defaults.conf

vim spark-defaults.conf

spark.master                            yarn    (들여쓰기는 그냥 위에가그렇게되어있어서)


실행을해보자

start-all.sh
jps

pyspark

이렇게 세개를 실행하는동안 어떤 오류가 발생하지않으며 spark가 뜨고 >>가 떠야 정상
```

### 스파크 폴더안을 확인해보자

cd spark

|폴더명|내용|
|:---:|:---:|
|bin|실행폴더|
|pyspark|파이썬으로 스파크실행|
|conf|환경설정파일|
|data|기본적으로 샘플데이터가들어있다.|
|examples|예제코드|
|jars|java아카이브들이들어있다. jar파일들이있는데 이건 자바 라이브러리 파일|
|k8s|쿠버네티스파일들이 들어있다. 도커(쿠버네티스)로 배포.|
|python|pysaprk, 말그대로 python을 스파크로 사용할때 필요한것들이 들어있다.|
|R|R로 시작하기위한것들|
|SBIN|하둡이나, 메소스,YARN 등 분산으로 되어있는것을 실행시키는 파일들이 들어있다.|


### 쿠버네티스란?

- 배포하는것을 관리하고 자동화시키는것
- 쿠버네티스는 컨테이너화된 워크로드와 서비스를 관리하기 위한 이식성이 있고, 확장가능한 오픈소스 플랫폼이다

### 스파크에서 사용할수있는 언어

- PYTHON으로 사용할수있다
- SCALA로도 사용할수있다. 근데 스칼라가 JVM(자바가상머신)기반이기때문에 JAVA기반이다.
- 스파크는 JAVA,PYTHON,스칼라,R 모두사용가능.

### 구조
- RDD =판다스의 시리즈와 매우 흡사하다.(내결함성 분산 데이터셋 = 결함성에 강하다. 하둡처럼 분산저장이라 장애복구 등 결함성에강함)
- DataFrame =판다스의 데이터프레임(df)와 흡사하다.비타입형 api - 런타임 시 데이터의 타입을 확인
- DataSet  = 타입형 api 컴파일 시 데이터의 타입을 확인. ex)int a = 10 / str a= '10'이렇게씀

- Spark context available as 'sc' (master = yarn, app id = application_1668404995378_0001).sc는 판다스의 시리즈와 비슷하다 sc'객체'
- SparkSession available as 'spark'. = 판다스의 df와 비슷하다. spark'객체'

### transformation

- RDD의 동작방식 중 하나이다 . transformation /action 이있다.
- RDD에 뭔가를 적용해서 적용된 RDD가 나오는것을 의미한다. RDD만 나와야한다.
- 학원,학교에 다니는사람을 학생이라고 부르듯이 RDD를 넣어서 RDD가나오는 것.

### Spark RDD Transformation 연산 종류표
|이름|설명|
|:---:|:---:|
|distinct()|새RDD을 반환한다.|
|filter()|조건을 만족하는 결과만 반환.말그대로 필터링|
|map()|원하는작업을 레코드별로 적용한다(매핑작업)|
|flatMap()|map한작업을 하나로 반환|
|union()|RDD요소들을 합쳐서 새로운 RDD를생성|
|join()|DB의 JOIN과같다. 공통된값을 기준으로 결합시킨다.|
|groupByKey()|(A,B)이런식으로 있으면 키를기준(A)으로 데이터 셔플 후 RDD반환|
|reduceByKey(펑션 OR 식)|같은Key끼리 결합하여 key별로 계산한다.|
|sortBy()|()안에 원하는 정렬조건을 주고 정렬시킴|
|coalesce()|출력파티션 수 조절용.셔플x|
|repartition()|coalesce와 같은작업을 수행.셔플O|

### Partition의 종류

스파크에서 파티션은 디스크파티션과 다르게 내부적으로 나눠져있다.

test=sc.parallelize([1,2,3,4,5,6,7,8,9],3) ->이면 겉으로 보기엔 test하나로나오지만, 내부적으론 123,456,789 이렇게  나눠서 저장되어있다.

파티션의 수에 따라 각 파티션의 크기가 결정되고, 이게 곧 코어당 필요한 메모리크기를 정하는 구조이다.

적은수의 파티션 = 크기가 큰 파티션
많은수의 파티션 = 크기가 작은 파티션

3가지종류가있는데

- input Partition : 처음 파일을 읽을때 생성하는 파티션이다.
spark.sql.files.maxPartitionBytes으로, Input Partition의 크기를 설정.기본128MB이기때문에, 128MB이하면 알아서 불러오지만, 이상이면 따로 설정값을 조절해야한다.
- ouput Partition : 파일을 저장할때 생성되는 파티션이다. 이 파티션의 수가 HDFS상의 마지막 경로의 파일 수를 지정.
- ★shuffle Partition : 스파크의 성능에 가장 큰 영향을주는 파티션. JOIN,GROUPBY 등의 연산(Wide Transformation)을할때 많이사용된다. spark.sql.shuffle.partitions
< 이 설정값에따라 연산수행시 파티션,task의 수가 결정된다.


### Wide Transformation? 
- 연산처리할 데이터 클러스터 노드 여러곳에 분산되어있어 연산할때 시간이 오래걸리고,메모리량도 많아지는것.
- = 네트워크 연산처리량이 많아짐

### action

- RDD에 뭔가를 적용해서 **다른타입**으로 나오는것들
- 예를들면 RDD에 .count()를 적용하면 rdd전체의 row수가나오고, int로바뀜.이것은action

```python
rdd = sc 객체로 사용

EX) rdd01=sc.range(0,1000,1,2) ->0부터1000까지 1씩증가할건데 파티션두개로저장
>>> rdd01
PythonRDD[1] at RDD at PythonRDD.scala:53

->무슨소리냐면, 스칼로만들어져있기때문에 **실행하면** 스칼라로실행이되고,
스칼라는 자바로되어있기때문에 내부적으로 또 자바로변해서 실행되고있다.

결국 rdd01은 스칼라로실행되고있다.라는걸 알려주는 메세지이다.

EX2)
RDD.getNumPartitions( )->파티션갯수를 반환한다.
겉으로보면 RDD01이지만 내부적으로 내가 지정해놓은 파티션갯수만큼 나눠져있다.

#파티션을 쓰는이유 

적당히 나눠져서 저장되어있으면 계산할때나 가져올때도 나눠서 계산,가져오기때문에
적당히 파티션을 나눠놓으면 빨라진다. (너무많거나 너무적으면 느려짐)


EX3)
# RDD01에서 홀수만 RDD02로저장

RDD02=RDD01.filter(lambda x: x%2)
rdd02.collenct() ->그냥 rdd02로실행하면 PythonRDD[2] at collect at <stdin>:1 이렇게나오므로 콜렉션으로 불러줘야한다.

filter : 특정조건으로 필터링하는기능

EX4)
# parallelize:rdd로 만들어주는친구. sc.paralleize(바꿀것)->rdd가된다.

member = ['CaptainAmerica', 'Thor', 'Hulk', 'IronMan', 'BlackWidow', 'Hawkeye', 'Hulk']

avengers=sc.parallelize(member,2) # paralleize에서 파티션지정은 필수가아님!
avengers.collect()

# map기능을(리스트안에 하나하나매핑)이용해서 모두 대문자로출력

avengers_upper = avengers.map(lambda x : x.upper())
avengers_upper.collect()

# map기능을 이용해서 단어 하나하나 분철

avengers_map = avengers.map(lambda x :list(x))
avengers_map.collect()

map : 리스트안에있는 값들을 하나하나 가져오고 묶음으로 가져옴.

# flatmap 을 써보자

avengers_flatmap = avengers.flatMap(lambda x: list(x))
avengers_flatmap.collect()

->map과다르게 그냥 리스트 하나로 반환한다. 위의 map은 [단어,단어,단어],인데
이건 [단어단어단어단어단어.....]
정확한 동작은 map처럼 가져와서 하나로 합쳐버린것이다.

EX05)

cnt=sc.range(1,avengers.count()+1)
avengers_cnt=cnt.zip(avengers)
avengers_cnt.collect()

-> [(1,'cpationmerica'),(2,'thor')...] 이런식으로 결과가나온다.1부터 어벤저스의 갯수+1 값을
어벤저스 리스트와 zip하는데 ★기존 파이썬에서는 zip하면 dict/ 키:값 으로 나왔지만,pysaprk에서는, ★튜플★로 묶여서 나온다.. 


EX06)

score=[('midterm',100),('final',100),('midterm',60),('midterm',78),('final',88),('final',95),('midterm',59)]

score_rdd=sc.parallelize(score,1)
score_rdd.collect() # collect를 실행할때


# reduceByKey, sort를 사용해보자

score_reduce=score_rdd.reduceByKey(lambda x,y:(x+y)/2) # 키를기준으로 밸류를 연산할건데,그 연산식을 ()안에 넣은거다.
score_reduce.collect() 

변수명.reduceByKey(펑션 or 식)

from operator import add 하면 저 식안에 add를써도된다.

※reduceByKey(lambda x,y:(x+y/2)) ->앞에두개를 계산한값을 /2 하고 또 뒤에있는 값을 더해서 /2 하는작업을 반복한다.midterm끼리묶어서,final끼리묶어서.

nums = sc.parallelize([1,4,2,3,7,6,5],1)
nums.collect()

nums.sortBy(lambda x: x[0]).collect() # 오름차순, 지금 위의 예제는 한개의형태이기때문에 
->nums.sortBy(lambda x: x).collect() # 이렇게해야 정상작동

nums.sortBy(lambda x: x[1]).collect() # 내림차순

# glom 

arr = sc.range(0,100,1,5) #[0,1,2,3,4,5,..],[20,21,22,23....]x5
arr.collect()

arr_glom=arr.glom()
arr_glom.collect()

-> 파티션별로 리스트로 묶어서 출력하는데, 파티션이 너무크거나,파티션의 갯수가많은경우 에러남.

```





