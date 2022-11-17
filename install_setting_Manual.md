# 가상머신 하둡,스파크설치

1.업데이트&기본설치

sudo apt update

sudo apt upgrade -y

sudo apt install vim -y

**ssh서버 설치**

sudo apt install openssh-server -y
sudo apt install ssh-askpass -y

**공개키암호화(암복호화다른거).암호안묻고 로그인하는설정**

ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.shh/id_rsa.pub >> ~/.ssh/authorized_keys


2.아마존 corretto=java 설치(11버전설치할것임. 버전은자유)

wegt [tar xvzf amazon-corretto-11-x64-linux-jdk.tar.gz](https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.tar.gz)

- 코레토의 위치가 루트에있으면 편함 
- 루트가아닐경우 mv [이동대상] [이동할경로] (여러대상을 한번게 옮기기가능)
- mv *[이동할경로] :현재위치의 모든파일 이동

**설치 후 압축해제** 

tar -xvzf amazon-corretto-11-x64-linux-jdk.tar.gz

사용하기 쉽게 심볼릭링크(바로가기) 생성

ln -s amazon-corretto-11.0.17.8.1-linux-x64/ java

amazon[tab]-11.[tab] 누르면 / 까지 자동완성 java는  심볼릭 링크 이름

  
```python
~/.bashrc 설정

sudo vim ~/.bashrc 

맨끝에 입력

# java
export JAVA_HOME=/home/계정명/java
export PATH=$PATH:$JAVA_HOME/bin

vim에서 저장하고 
터미널에서 source ~/.bashrc 입력(적용)

```

3.python 설치 & 설정

sudo apt install python3-pip -y

```python
sudo vim ~/.bashrc

# python
alias python=python3
```

4.아파치 hadoop 설치 & 설정

스파크에 하둡이 같이들어있는 패키지가있는데,
이것은 하둡실행을 위한 **라이브러리** 이므로 하둡을 데이터저장용도로 사용하고싶으면,
하둡을 따로 설치하는것을 권장.



다운로드(hadoop3.3.4버전을 설치할것임)

**source말고 binary를 이용하자** 

홈페이지 -> 다운로드 -> 3.3.4 바이너리 클릭-> .tar링크복사 -> 터미널에 아래코드입력

wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz

ls로 다운로드가 잘되어있는지 확인 후 

**압축해제 /심볼릭 링크 생성**

tar -xvzf hadoop-3.3.4.tar.gz 

ln -s hadoop-3.3.4 hadoop
->hadoop으로 심볼릭 링크생성

```python

1. vim ~/.bashrc 

# hadoop 
export HADOOP_HOME=/home/계정명/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin



★중요! hadoop-env.sh를 설정하러 경로를 변경해줘야함↓

2. cd $HADOOP_CONF_DIR(위에서 설정했던)

계정명@우분투:~/hadoop/etc/hadoop$ vim hadoop-env.sh

#exmport hadoop_home  ->원래주석으로 되어있던부분 
->export hadoop_home=/home/계정명/hadoop  으로 설정

#export hadoop_pid_dir=/temp ->원래주석으로 되어있던부분 
->export hadoop_pid_dir=$HADOOP_HOME/pids



#export JAVA_HOME=
->export JAVA_HOME=/home/계정명/java
# export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop 주석되어있다면 해제
# export HADOOP_OS_TYPE=${HADOOP_OS_TYPE:-$(uname -s)} 주석되어있다면 해제

3. core-site.xml 설정
vim core-site.xml (hadoop-env.sh 편집했을때랑 같은 위치)


<configuration>
	<property>
		<name>fs.defaultFS</name> 
		<value>hdfs://localhost:9000</value>
	</property>
</configuration>


4. hdfs-site.xml 설정

vim hdfs-site.xml (여기도 core-site와 위치같고, configuration태그안에 작성)

<property>
	<name>dfs.replication</name>  
	<value>1</value> 
</property>
<property>
	<name>dfs.namenode.name.dir</name>  
	<value>/home/계정명/hadoop/namenode_dir</value>
</property>
<property>
	<name>dfs.namenode.secondary.http-address</name>
	<value>localhost:9868</value>  
</property>
<property>
	<name>dfs.datanode.data.dir</name> 
	<value>/home/계정명/hadoop/datanode_dir</value>
</property> 

5. mapred-site.xml

vim mapred-site.xml (configuration태그 안에 작성)

<property>
	<name>mapreduce.framework.name</name> 
	<value>yarn</value>
</property>

6. bashrc에 HadoopUser를 추가해주자

sudo vim ~/.bashrc

# hadoopuser

export HDFS_NAMENODE_USER=계정명 
export HDFS_DATANODE_USER=계정명  
export HDFS_SECONDARYNAMENODE_USER=계정명
export YARN_RESOURCEMANAGER_USER=계정명
export YARN_NODEMANAGER_USER=계정명


저장 후, source ~/.bashrc 로 적용!

7. 네임노드 / 데이터노트 포맷과 실행

hdfs namenode -format
hdfs datanode -format
문제없이 실행되면 (common오류 대부분 오타!)

start-all.sh  실행
(start-dfs.sh + start-yarn.sh 합친것)

jps로 확인

namenode, datanode, naodemanager , secondaryNameNode, ResourceManager 가 최소


```


5.Spark 설치 & 설정

**스파크 3.2.2를 다운로드받자**

wget https://dlcdn.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-without-hadoop.tgz

**압축해제&심볼릭 링크생성**

tar -xvzf 
ln -s spark

hadoop설치떄와 비슷한 방식으로 진행한다.

```python
sudo vim ~/.bashrc 아래내용 추가 후 source ~/.bashrc

# spark
export SPARK_HOME=/home/na/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

1.cd $SPARK_HOME/conf 
1-1 계정명@ubuntu:~/spark/conf$ 경로에서 작업

2.cp workers.template workers >이부분은 hadoop과다름!

3.cp spark-env.sh.template spark-env.sh

4.vim spark-env.sh 

제일 하단에 아래내용 작성

export YARN_CONF_DIR=/home/계정명/hadoop/etc/hadoop
export HADOOP_CONF_DIR=/home/계정명/hadoop/etc/hadoop
export SPARK_DIST_CLASSPATH=$(/home/계정명/hadoop/bin/hadoop classpath)
export JAVA_HOME=/home/계정명/java

export PYSPARK_PYTHON=/usr/bin/python3
export PYSPARK_DRIVER_PYTHON=/usr/bin/python3

5.spark-defaults.conf

★cp spark-defaults.conf.template spark-defaults.conf 를 실행하여

spark-defaults.conf 을 생성해주자.

vim spark-defaults.conf
↓

# Example: ~~ 제일하단부분에 주석없이 아래 내용추가

spark.master                              yarn

6.pyspark 실행

start-all.sh -> pyspark -> spark로고 확인 / master:yarn확인
```

6.Rdd를 하나 생성하여 하둡에 파일을 올려보자

test=[1,2,3,"Abc,Def",'Gh'] 테스트 데이터 생성
rdd01=sc.parallelize(test,3) parallelize를 통해 rdd로 변환. 파티션은3개
rdd01.collect() rdd 확인.

rdd01.saveAsTextFile('/rddtest01') 하둡에 올리기 rddtest01이라는 디렉터리안에(없으면 생성)
================================
2022-11-15 - 2022-11-16 설치오류:
jps시 
ResourceManager만 나옴

↓↓↓↓↓↓

2022-11-17 
오류해결!

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorize_keys
↓↓↓↓↓↓
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 바꿔서 재실행

authorized_keys 에 d가빠져서 오타가되어서,제대로 ssh에 문제가생김.

>error=localhost: 계정명@localhost: Permission denied (publickey,password).
================================




