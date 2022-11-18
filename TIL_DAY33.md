TIL DAY 33(2022-11-18)


## Mong Db 설치


★AWS는 오늘날짜기준으로 18버전이므로, 18버전으로 오피셜,리스트파일 을 받아줘야한다.

```python

1.몽고디비 오피셜 설치
[몽고디비리눅스다운링크](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

Install MongoDB Community Edition이부분 가서 wget링크복사!

-> wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

2. 몽고디비 리스트 설치

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

3.apt 업데이트 & 업그레이드


sudo apt update 
-> ==  # sudo apt-get update 같은거!

업그레이드할게있으면

sudo apt upgrade

4.몽고디비 패키지 설치

패키지도 여러버전이있는데 지금은 최신버전을 설치할것이다.

특정버전 패키지를 설치할수도있다. 특정 버전패키지 설치 시, 호환되는버전을 찾으면된다. 

sudo apt-get install -y mongodb-org
-> == #sudo apt-get install -y mongodb-org

5. systemd vs system v int(service)

systemd  = service보다 권한이 조금 더 많다는 차이가있는데 큰차이는없음 

service = 도커사용시 이용

sercive로 시작해보자

sudo service mongod start


6.확인

sudo serviece mongdod status

monogd = 몽고디비데몬이다. 데몬이니 백그라운드로 실행되고있다.


7.자동실행 등록

sudo systemctl enable mongod

->도커나 systemctl을 사용하지못하는 환경에서는 어쩔수없이 사용할수없다.


8. 몽고디비 실행

mongosh

입력 후 셸이뜨면 성공!
test>  이런식으로 나와야함

9.test데이터 생성

db.test.insertOne({"id":"5","name":"mongo"})

db.test.find() ->확인



10. 하둡과 몽고디비 연결

start-all.sh 이후 아래 경로로 이동해준다.

cd $SPARK_HOME/conf

경로이동 후, 아래 파일을 열어서 

vim spark-defaults.conf

아래 코드를 하단에 추가

spark.jars.packages 		org.mongodb.spark:mongo-spark-connector_2.12:3.0.1

spark.mongodb.input.uri			mongodb://localhost/test
spark.mongodb.output.uri		mongodb://localhost/test



11.pyspark를 실행시켜보자

제대로 연결되었으면 pyspark 실행시 중간에

	---------------------------------------------------------------------
	|                  |            modules            ||   artifacts   |
	|       conf       | number| search|dwnlded|evicted|| number|dwnlded|
	---------------------------------------------------------------------
	|      default     |   4   |   4   |   4   |   0   ||   4   |   4   |
	---------------------------------------------------------------------
이런게 뜨는데 처음에만 jar파일을 설치하는거기때문에 값이뜨고 다음부턴 0000이 뜰것이다.


12.pyspark에서 몽고디비를 사용해보자

test = spark.read.format("mongo").option("database","test").option("collection","test").load()
->아까 몽고에서 만들어놓은 test데이터를 가져옴

test.show() 

↓↓↓

+--------------------+---+-----+
|                 _id| id| name|
+--------------------+---+-----+
|{6376d289b4d8b4f0...|  5|mongo|
+--------------------+---+-----+

넣은 테스트 데이터에따라 상세값이 다르겠지만, 크게 틀은 위와같이 나온다.

★추가해보자

insertDf = spark.createDataFrame([("6","mongo-spark")],["id","name"])

insertDf.show()

★저장해보자

insertDf.write.format("mongo").option("database","test").option("collection","test").mode("append").save()


```

## 재플린 노트북에서 mysql,mongodb가져와서 하나로붙여보자!

```python

zeppelin-daemon.sh start


#mysql에서 test database 가져와서 출력해보자

%pyspark

mytest=spark.read.format("jdbc").options(user="계정명",password="비밀번호",url="jdbc:mysql://localhost:3306/mysql",driver="com.mysql.cj.jdbc.Driver",dbtable="test").load()

mytest.show()

#mongodb에서 test collection 가져와보자

mongoDf=spark.read.format("mongo").option("database","test").option("collection","test").load()
mongoDf.show()

#두개의 dataframe을 하나로 합쳐서 출력해보자

unionDf=mytest.union(mongoDf.select("id","name")) ->몽고쪽에 id,name밖에없어서!
unionDf.show()

```
## 에어플로우란?

웹서버 / 스케줄러로 나누어져있고 저 두개가 사용자는 웹서버를 통해 사용할수있다.

웹서버:사용자가 쓸수있는애. 포트로접속해서 보여주는 화면을 그려주고 사용자랑 통신함

스케줄러 : 웹서버가 보내는 작업을 실제로 처리해주는친구이다. 이 데이터를 메타스토어(메타데이터베이스)에서 가져온다.excurot/ 스케줄러로 나눠져있다.

흐름 : 사실상 '실행'은 excutor가 하고 스케줄러가 관리(언제,어디서 어떻게실행할것인가)해서 웹서버에 다시 보내주는흐름이다. 즉, 우리가 py파일등으로 작업을 해놓고 그걸 excutor가실행, 스케줄러가 처리해서  웹서버에 보내주고,사용자가 응답받음


## 에어플로우 설치

>Successful installation requires a Python 3 environment.
>Only pip installation is currently officially supported.

->python 3에서만 동작하고 pip만 공식이다.

 
```python
(사전작업 / 켜져있는거 다끄기)

zeppelin-daemon.sh stop
stop-all.sh

[에어플로우링크](https://airflow.apache.org/docs/apache-airflow/stable/start.html)


1. ~/.bashrc 에 에어플로우추가

sudo vim ~/.bashrc 에 추가 

# airflow
export PATH=$PATH:/home/계정명/.local/bin

source ~/.bashrc 로 적용!

2. pip로 에어플로우를 설치해보자

pip install apache-airflow
->동작해서 버전이안맞으면 빨간줄로 오류가 발생. 대부분 업그레이드 오류이므로 잘 읽어보고 해당 라이브러리를 업그레이드하면됨

pip install -U requests
->설치도중 requests 업데이트 오류가나면, 이거 실행하고 에어플로우를 pip로 재설치

##(export AIRFLOW_HOME=~/airflow ->보류)##

3. 기본DB를 MYSQL로바꾸자

sudo apt install libmysqlclient-dev -y

pip install apache-airflow-providers-mysql

mysql -u 계정명 -p -> 위의 인스톨이끝난 후 mysql접속


2. ★계정생성과 권한설정!

create database airflow character set utf8mb4 collate utf8mb4_unicode_ci;
->utf8로되어있는 데이터베이스를 하나 생성 / 로컬에서만 사용가능

create user '계정명'@'%' identified by '비밀번호'; ->어디서든 사용가능한 계정


grant all privileges on airflow.* to 'airflow'@'localhost';
grant all privileges on airflow.* to 'airflow'@'%';


flush privileges;

airflow db init

ls

cd airflow

mkdir dags

vim airflow.cfg

#18번째

default_timezone = utc
->default_timezone = Asia/Seoul

#24번째
executor = LocalExecutor

#52번째

load_examples = True
->에어플로우가 만들어놓은 예제 노출여부 안볼거니 load_examples = False


#206번째

sql_alchemy_conn = sqlite:////home/리눅스계정명/airflow/airflow.db
->sql_alchemy_conn = mysql://airflow:비밀번호@localhost:3306/airflow 
mysql의 접속 정보이다. airflow는 sql 데이터베이스명, localhost:3306은 접속경로
접속하려는 db정보가 다른경우 airflow부분 대체가능


#428번째

endpoint_url = http://localhost:8080
-> http기본경로가 8080이기때문에 바꿔준다. 끝을 8988로

#525번째
base_url = http://localhost:8080
->base_url = http://localhost:8988

#531번째
default_ui_timezone = UTC
->default_ui_timezone=Asia/Seoul

#537번째
web_server_port = 8080
->web_server_port = 8988

#963번째

dag_dir_list_interval = 300
->dag라는 파일의 새로고침 시간 기본값 5분씩. 연습할때는 자주 새로고침해놓고, 프로젝트땐 길게잡아놔도된다.

-> dag_dir_list_interval = 60 으로 변경해주자

airflow db init
->위에서 설정한것을 재저장한다. 아까 위에서는 안바꿨기때문에 spllie3(기본값)이고 지금은 mysql로바꿨기때문에 새로 저장해줘야함


★airflow 계정추가

airflow users create \
--role Admin \	->권한
--username 아이디 \
--password 비밀번호 \
--firstname min \
--lastname ad \
--email admin@admin.com

★실행확인

새로운 터미널 두개를 켜서, 각각

airflow scheduler

airflow webserver

따로 실행시켜준다.

!중요!
실행시켜놓은 상태에서 -> 파이어폭스 loccalhost:8988 ->admin 계정정보입력->접속성공

★하나의 터미널로 airflow실행하기

nohup airflow scheduler &   ->53892(실행할때마다 할당되는 프로세스가다름)

nohup airflow webserver &   ->54079

↑한줄씩 따로 실행한후에 에어플로우 웹 브라우저에 접속O

## 에어플로우 프로세스 끄기

ps -ef|grep airflow ->airflow프로세스 확인

아까 nohup으로 실행시키면 뜨는 프로세스를 보고 kill해주면된다

kill 53892
kill 54079

이후 웹브라우저에 접속해 접속이 끊긴걸 확인할 수 있다.

```
## ubunto에서 vscode 설치하기!

[리눅스용vs](https://code.visualstudio.com/docs/setup/linux)

```python

위의 링크에서 두번째 박스에있는 내용을 하나하나 따라하면 된다. 

sudo apt-get install wget gpg

wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg

sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg

sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'

rm -f packages.microsoft.gpg


sudo apt install apt-transport-https

sudo apt update

sudo apt install code # or code-insiders


sudo apt update

sudo apt upgrade -y

sudo apt install code

위의 설치가 정상적으로 된다면, 터미널에서 code 라고 입력하면, vscode가 실행된다.

```
## vscord로 dag를 만들어 실행해보자

```python
폴더열기 -> airflow안의 dags폴더 오픈 -> air01.py생성

★dag란?
비순환 방향 그래프이다. task(작업)을 가지고있고 각 task들의 배치 스케줄을관리한다.
쉽게 작업 실행순서와 실행현황 등을 그래프로 보고 관리할수있다고 생각하면된다.
dag안에 task들을 작성하는것으로 하나의 작업그래프를 그릴 수 있다.
dag를 선언하는 방법은 여러가지가있는데, 맨밑에서 자세하게 다룸

DAG_ID(
    TASK1
    TAKS2
    TASK3.....
)
↑ 위와 같은 구조이다

# air01.py(기본, 파일올리고 내리고)

from airflow import DAG
from pendulum import yesterday
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id='air01',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')

)

def hello():
    print('hi')

task01 =PythonOperator(
    task_id='hello',
    python_callable=hello,
    dag=dag
)
실행하면 airflow에 올라간다.

# air02(echo, 배쉬셸사용)

from airflow import DAG
from pendulum import yesterday
from airflow.operators.bash import BashOperator

dag=DAG(

dag_id='air02',
schedule_interval=None,
start_date=yesterday('Asia/Seoul')
)

task01=BashOperator(

task_id='hello',
bash_command='echo Hello, Airflow',
dag=dag

)

아웃풋이 hello, airflow로나옴
왜냐면 echo명령어가 내가입력한걸 그대로 출력해주는애라서, echo를 떼고 hello,airflow만 출력되게 되는것이다!

= 에어플로우는 python도되고, 배쉬셸도 사용할수있다는걸 알수있다.


# air03(작업순서)

from airflow import DAG
from pendulum import yesterday
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


dag=DAG(
    dag_id='air03',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')
)

def hello():
    print('Hellow,python Oerater')

task01=PythonOperator(
    task_id='hello_python',
    python_callable=hello,
    dag=dag
)

task02=BashOperator(
    task_id='hello_bash',
    bash_command='echo hleeo,bash',
    dag=dag
)

task01 >> task02

#A>>B:A는 B의 upstream / B는 A의 downstream -> 작업순서지정하려고. 안하면 병렬실행됨. 순환되면 큰일나니까 순환되지않게

upstream:위에있는작업, 먼저실행할작업
downstream:아래에있는작업, 후에실행할작업


★에어플로우 웹서버에서 py파일클릭해서 그래프를 눌러보면, 작업순서를 그래프로 볼수있다! 여기서 작업을 클릭하면 해당작업의 log도 확인할수있다.

★log:하단의 러닝 command (입력부분인듯) output부분을 잘 보면된다.

# air04(시간)

from airflow import DAG
from pendulum import yesterday,tomorrow
from datetime import timedelta
from airflow.operators.python import PythonOperator


dag=DAG(
    dag_id='air04',
    #schedule_interval='*/1 * * * *',
    #schedule_interval=timedelta(hours=1),
    schedule_interval='@hourly'
    start_date=yesterday('Asia/Seoul'),
    end_date=tomorrow()

)

def hello():
    print('time')

task01=PythonOperator(
    task_id='schedule_test',
    python_callable=hello,
    dag=dag
)


schedule_interval : 실행간격.

interval안에올수있는게

- cron
- timedelta
- cron presets (분 시 일 월 주)
	- @once : (한번이라 따로x)
	- @hourly : 0 * * * *
	- @daily : 0 0 * * *
	- @weekly : 0 0 * * 0 or sun
	- @monthly : 0 0 1 * *
	- @quarterly : 0 0 1 */3 *
	- @yearly : 0 0 1 1 *

start_date: 스케줄 시작날짜

end_date : 스케줄 끝낼날짜

↓↓↓↓↓↓

만약 내가 오늘 13시에 어제부터 오늘24시까지 실행해줘,라고했으면 오늘13시까지 작업을 쭉~하고 내가 설정한 간격대로 오늘24시까지 실행함


timedelta :두 , 또는 인스턴스 간의 차이를 마이크로초 단위로 표현하는 date기간 시간이다 .datetime


# air05

from airflow import DAG
from pendulum import yesterday
from airflow.operators.python import PythonOperator

dag=DAG(
    dag_id='air05',
    start_date=yesterday('Asia/Seoul'),
    schedule_interval='*/1 * * * *',
    catchup=False

)

def hello():
    print('backfill')

task01=PythonOperator(
    task_id='backfill_test',
    python_callable=hello,
    dag=dag

)

catchup : 기본=False. '과거' 작업관련 인수. 과거에 실행하다가 중단된경우 / start_date가 현재보다 과거부터 시작할경우 '과거스케줄 실행여부'설정이라고 생각하면된다.(빈 dag run부분 채우기라고 볼수도있다).False로하면 과거 dag run을 실행하지않는다. True면 실행. 

※True로 설정시 과거 dag run을 한번에 실행하기때문에 과부화에 주의해야한다.

catchup 옵션

    1.max_active_runs : DAG수준에서 설정 되며(dagid='..',start_dat='..', max_active_runs=n 이런식), 
    Catch up 중에 DAGrun이 얼마나 실행 될 수있는지를 설정 한다.

    2.depends_on_past : 작업 수준에 설정 되며, 가장 최근에 DAG에서 동일한
    작업이 수행 되었을 때 작업이 수행 될 수 있도록 제약을 걸 수 있다.

    3.wait_for_downstream : DAG 수준에서 설정되며 다음 DAG를 실행 하려면 전체 task들이 수행 되어야 실행 되도록 한다.

    4.catchup_by_default : config파일에서 설정이 가능하며 DAG를 만들 때 기본 값 True, False를 정할 수 있다.

backfill : dag의 시작날짜(start_date)이전의 데이터를 처리할때 사용한다.
지정기간 동안 dag 재시작/ 전체 재시작 / 지정기간, 지정상태 동안 전체 재시작 ..등 지정기간/ 과거날짜를 명시하며 실행할수도있다. 

※하지만 보통 일정기간동안 실패한 task에 대해 재실행하는데 사용함.back-fill안에 들어갈수있는 인수들이 많다. 자세한것은 아래 표에서 다룸

    airflow dags backfill 
    [-h] [-c CONF] [--delay-on-limit DELAY_ON_LIMIT] [-x]
    [-n] [-e END_DATE] [-i] [-I] [-l] [-m] [--pool POOL]
    [--rerun-failed-tasks] [--reset-dagruns] [-B]
    [-s START_DATE] [-S SUBDIR] [-t TASK_REGEX] [-v] [-y]
    dag_id

    ex)
    1.
    airflow dags backfill --start-date {date} --end-date {date} dag_id

    2.
    airflow dags backfill --start-date {date} --end--date {date} --rerun-failed-tasks

#air06

from airflow import DAG
from pendulum import yesterday
from airflow.operators.python import PythonOperator

dag=DAG(
    dag_id='air06',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul'),
    catchup=False
)

def hello(ds):  ->오늘날짜찍힘
    print(ds)

def print_context01(**kwargs): ->실행내역이 딕셔너리형태로찍힘
    print(kwargs)

def print_context02(ds, **kwargs): ->오늘날짜+딕셔너리형태의 실행내역
    print(ds)
    print(kwargs)

task01 = PythonOperator(
    task_id='hello',
    python_callable=hello,
    dag=dag
)

task02 = PythonOperator(

    task_id='print_context01',
    python_callable=print_context01,
    dag=dag

)

task03 = PythonOperator(

    task_id='print_context02',
    python_callable=print_context02,
    dag=dag

)

task01 >> task02 >> task03

```
```python
# air07

from airflow import DAG
from pendulum import yesterday
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator


dag = DAG(
    dag_id='air07',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')

)

task01 = EmptyOperator(task_id='task01', dag=dag)
task02 = EmptyOperator(task_id='task02', dag=dag)
task03 = EmptyOperator(task_id='task03', dag=dag)
task04 = EmptyOperator(task_id='task04', dag=dag)
task05 = EmptyOperator(task_id='task05', dag=dag)
task06 = EmptyOperator(task_id='task06', dag=dag)
task07 = EmptyOperator(task_id='task07', dag=dag)
task08 = EmptyOperator(task_id='task08', dag=dag)


# fan-in(n:1)
task01 >> [task02,task03]

#fan-out(1:n)
[task02,task03]>>task04
task04 >> task05 >> task06
task03 >> task07
[task06,task07]>>task08


★EmptyOperator:더미 오퍼레이터. 내용x 그냥 껍데기만
fan-in:여러개가 들어오는것
fan-out:여러개가 나가는것
```

![fan-in,out이미지](/airflow_fan_in_out.PNG))

```python
#air08.py

from airflow import DAG
from pendulum import today
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id='air08',
    schedule_interval=None,
    start_date=today('Asia/Seoul')

)


def send_function(task_instance):
    msg='xcom_test'
    task_instance.xcom_push(key='msg', value=msg) ->키이름이 msg, 값은 xcom_test


def receive_function(**kwargs): ->**kwargs ->ds내용이담겨있다. 설정정보, 실행정보 등등등
    print(f"receive:{kwargs['task_instance'].xcom_pull(task_ids='task01',key='msg')}") ->리시브에서 send_funtion의 값이나오도록 설계


task01 = PythonOperator(

    task_id='task01',
    python_callable=send_function,
    dag=dag
)

task02=PythonOperator(
    task_id='task02',
    python_callable=receive_function,
    dag=dag

)


task01 >> task02

★xcom:task간 데이터 공유를 위한 객체. task01->task02 로 데이터를 보내고싶을때 사용하는것


# air09



from airflow import DAG
from pendulum import yesterday
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from pprint import pprint




dag = DAG(
    dag_id='air09',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')

)


def print_context(**kwargs):
    pprint(kwargs)
    result=str(kwargs)
    return result

task01 = PythonOperator(
    task_id='print_context',
    python_callable=print_context,
    dag=dag
)

task02=BashOperator(

    task_id='save_context',
    bash_command='echo "{{task_instance.xcom_pull(task_ids="print_context")}}" >> ~/context.json'


)

task01 >> task02



air09는 xcom_push 대신 reurn한것임. 그리고 context.json으로 저장했으니, 열어보면 deg(혹은 작업중인곳)의 설정,실행정보들이 들어있다.(**kwargs<얘가 저런정보 다가져와주는 친구) 

>> ~/context.json 앞에서 나온 결과를 뒤에있는곳에 전달 ,저장해라

ex)A >> B  : A의 내용,결과를 B에 전달(저장)해라



# ★air10 (json파일로 저장, 크롤링)

from airflow import DAG
from pendulum import yesterday
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
import json


dag =DAG(

    dag_id='air10',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')
)

def python_task():		->크롤링처리해주는 부분 크롤링하고,파일저장까지
    dummy = {'key':'value'}
    return json.dumps(dummy)

crawling =  PythonOperator(
    task_id='crawling',
    python_callable=python_task,
    dag=dag
)

make_file = BashOperator(
    task_id='make_file',
    bash_command='echo "{{ task_instance.xcom_pull(task_ids="crawling")}}">> /home/big/dummy.json',
    dag=dag
)

exists =FileSensor(	->filesensor:파일에관련된 작업만하는 오퍼레이터. 센서:하나의 작업만하는친구

    task_id='exists',
    filepath='/home/big/dummy.json',   ->이녀석이 있어야만 다음작업으로 넘어감. 즉 얘가 만들어질때가지 동작x기다림.
    poke_interval=30,		->하지만 30초마다 저파일이있는지 확인한다.
    dag=dag
)

upload = BashOperator(

    task_id='upload',
    bash_command='hdfs dfs -put /home/big/dummy.json /dummy',
    dag=dag
)

prn = BashOperator(
    task_id='prn',
    bash_command='echo "success make & upload"',
    dag=dag
)


crawling >> [make_file, exists] >> upload >> prn

크롤링했다고치고, 파일이있으면 exists하고 upload(하둡에), prn하는것까지 해준다


## using spark.py에 작업

(사전작업, 터미널에서 진행)
pip install apache-airflow-providers-apache-spark

from pyspark.sql import SparkSession


spark = SparkSession.builder.master("yarn").appName("airflowUsingSpark").getOrCreate()

mysqlDf = spark.read.format("jdbc").options(user="계정명", password="비밀번호", url="jdbc:mysql://localhost:3306/mysql",
driver="com.mysql.cj.jdbc.Driver", dbtable="test").load()
mysqlDf.show()

mongoDf = spark.read.format("mongo").option("database", "test").option("collection", "test").load()
mongoDf.show()

unionDf = mysqlDf.union(mongoDf.select("id", "name"))
unionDf.show()

unionDf.write.format("json").mode("overwrite").save("/using")

## air11

[Providers링크](https://airflow.apache.org/docs/)
↑Providers packages : 에어플로우와 연결해서 사용할수있는 패키지의 목록


from airflow import DAG
from pendulum import yesterday
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


dag = DAG(

    dag_id='air11',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')

)

spark_submin_task=SparkSubmitOperator(
    task_id='spark_submin_task',
    application='/home/big/airflow/dags/using_spark.py',
    conn_id='spark_default',
    dag=dag
)


# air12(하둡과 에어플로우 연결하기 )

(사전작업)
pip install apache-airflow-providers-apache-hdfs
-> kbr5, pands 관련 오류가난다면, 아래코드 입력

kbr5 : sudo apt install libkrb5-dev -y
pands : pip install -U python-dateutil


from airflow import DAG
from pendulum import yesterday
from airflow.providers.apache.hdfs.sensors.hdfs import HdfsSensor
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.bash import BashOperator



dag =DAG(
    dag_id='air12',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')

)


spark_submin_task=SparkSubmitOperator(
    task_id='spark_submint_task',
    application='/home/big/airflow/dags/using_spark.py',
    conn_id='spark_default',
    dag=dag
)

hadoop_sensor_task=HdfsSensor(
    task_id='hadoop_sensor_task',
    filepath='/using/_SUCCESS',
    hdfs_conn_id='hdfs_default',
    dag=dag

)


print_task=BashOperator(
    task_id='prn',
    bash_command='echo "success pyspark hadoop process"',  ->성공하면 에어플로우에뜬다.
    dag=dag
)


spark_submin_task >> hadoop_sensor_task >> print_task


에어플로우 웹에서 ->상단의 admin->connection에 hadoop추가(좌측상단 파란+버튼 클릭)

connection id : hdfs_default
host : localhost
port : 9000

하단의 세이브버튼 클릭 / HDFS가서 using디렉터리 생성확인




# dags01

air시리즈와 같은기능을 하지만, 코드 형태만 다르게 생성해보자



from airflow import DAG
from pendulum import yesterday
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id='dags01',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')
)as dag : 
    task01 = EmptyOperator(task_id='task01')
    task02 = EmptyOperator(task_id='task02')
task01 >> task02

★dags01방법이 깔끔하고 편함 air방법은 dag객체 생성하고 task에서 dag=dag라고 하나하나잡아줘야하는 불편이있음

#dags02(air,dags1와 다른 데코레이터(@)를 사용하는방법)

단, decorator 사용은 pytgonOperator만 가능! 다른 오퍼레이터에서 쓰고싶다면 그냥 만들어놓은걸 연결해주는방법밖엔..


from airflow.decorators import dag,task
from pendulum import yesterday
from airflow.operators.empty import EmptyOperator


@dag(
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')


)

def dags02():
    @task
    def task01():
        pass
    @task
    def task02():
        pass
    task01 = task01()
    task02=task02()

    task01 >> task02 >> task03


task03 = EmptyOperator(task_id='task03')

dags02=dags02()

```
```python
# dependency01

from airflow import DAG
from pendulum import yesterday
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id='dependency01', ->웹브라우저에서 보일 아이디
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')
)as dag:
    task01 = EmptyOperator(task_id='task01')
    task02 = EmptyOperator(task_id='task02')
    task03 = EmptyOperator(task_id='task03')
    task04 = EmptyOperator(task_id='task04')
    task05 = EmptyOperator(task_id='task05')


#set.dowunstream : >>

task01.set_downstream(task03)
task01.set_downstream(task04)

task02.set_downstream(task03)
task02.set_downstream(task04)

#set.upstream : <<
task05.set_upstream(task03)
task05.set_upstream(task04)
```

![dependency01업다운스트림](/airflow_dependecny01.PNG)

```python
#dependency02

from airflow import DAG
from pendulum import yesterday
from airflow.operators.empty import EmptyOperator
from airflow.models.baseoperator import cross_downstream


with DAG(
    dag_id='dependency02',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')
)as dag:
    task01 = EmptyOperator(task_id='task01')
    task02 = EmptyOperator(task_id='task02')
    task03 = EmptyOperator(task_id='task03')
    task04 = EmptyOperator(task_id='task04')
    task05 = EmptyOperator(task_id='task05')

cross_downstream([task01,task02],[task03,task04])
cross_downstream([task03,task04],task05)


★cross_downstram에 마우스호버링하면 예시를보여준다(내 작업예시아님).


#dependency03


from airflow import DAG
from pendulum import yesterday
from airflow.operators.empty import EmptyOperator
from airflow.models.baseoperator import chain


with DAG(
    dag_id='dependency03',
    schedule_interval=None,
    start_date=yesterday('Asia/Seoul')
)as dag:
    task01 = EmptyOperator(task_id='task01')
    task02 = EmptyOperator(task_id='task02')
    task03 = EmptyOperator(task_id='task03')
    task04 = EmptyOperator(task_id='task04')
    task05 = EmptyOperator(task_id='task05')

    chain([task01,task02],[task03,task04],task05)

#task01 >> task03 >> task05
#task02 >> task04 >> task05
```
![dependency03_chain](/airflow_dependency03.PNG)

## Backfill 인수 상세

|인수명|설명|
|:---:|:---:|
|-c CONF|CONF속성을 피클한다.|
|-delay-on-limit|재시작 전 최대활성dag실행 제한에 도달했을때 대기시간|
|-e end-date|end_date를 yyyy-mm-dd로 정의|
|-i|업스트림 작업 생략, 정규표현식과 일치하는 작업만 실행|
|-I|dependencies_on_past 무시|
|-l|로컬 익스큐터(스케줄러안의 실제작업처리해주는친구)로 실행|
|-m|작업실행x, 성공한것으로 표시한다.|
|--pool|사용할 리소스풀|
|--verbose|상세 로깅출력 만들기|
|-s|시작날짜를 yyyy-mm-dd로 정의|
|-rest-dagruns|이게설정되어있으면 ,기존 backfill dag실행 삭제, dag새로시작|
|-rerun-failed-tasks|백필 날짜범위에 대해 실패한 모든작업 자동재시작(단 예외 thow)|
|-continue-on-failure|설정되어있으면, 일부 작업이 실패해도 백필계속진행|
