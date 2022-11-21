TIL DAY34(2022-11-21)

2022-11-21


REST 란?

REST:REpresentational State Transfer ->자원(Resource)중심으로 요청/응답

[REST참고홈페이지](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods)

REST에 대해 자세히 알고싶으면 ↑위의 홈페이지로 가보면 알수있다.


REST의 가장 기본구성요소. 뭔가를 REST하게만들고싶으면 아래 요소를 충족해야한다. 

- GET:자원요청(read)
- POST;자원저장(create)
- PUT:자원(전체)수정(update)
- PATCH:자원(일부)수정(update)
- DELETE:자원삭제

★https://jsonplaceholder.typicode.com/posts/1 <서버안에 posts안에 리소스1번을찾아라, 우리는 저런구조로 클라이언트가 응답받을수있게 만들어야한다

EX)파이프라인구축(수집->적제->가공) ->시각화 할때 파이프라인구축,시각화 중간에 가공된데이터를 사용하는 API를 구현하고싶다. 이럴때 REST의 개념을 알아야 만들수있다.(API는 보통 GET방식 통신)

curl이란?

[curl메뉴얼](https://curl.se/)

cURL은 다양한 통신 프로토콜을 이용하여 데이터를 전송하기 위한 라이브러리와 명령 줄 도구를 제공하는 sw프로젝트. 다만 사용하기다 많이불편하다

jsonplaceholder?

[jsonplaceholder](https://jsonplaceholder.typicode.com/)
curl이랑 비슷한데 좀 더사용하기 수월함.

사용법:curl 옵션 서버/리소스/아이디 구조이다.

jsonplaceholder을통해 get방식으로 통신해보자

GET방식으로 요청하기

curl https://jsonplaceholder.typicode.com/posts
->jsonplaceholder.typicode.com 라는서버에서 posts라는것을 다 가져옴


curl https://jsonplaceholder.typicode.com/posts/1
->posts에서 해당아이디 1개만받기. 서버가 이렇게사용할수있도록 만들어놨기때문에, 저렇게 만들어놓는게 보편적이다.

 
curl https://jsonplaceholder.typicode.com/posts/100
->아이디가100인 리소스 한개 

#-X:method명시
명시하지않으면 post방식
curl -X GET https://jsonplaceholder.typicode.com/posts/100

#-i:header + body 
헤더와 바디를 같이가져온다(기본은 바디만나옴)

curl -i https://jsonplaceholder.typicode.com/posts/100

#POST(데이터를 생성,insert)
curl https://jsonplaceholder.typicode.com/posts/101
->POST방식은 다 추가/생성으로 들어가게된다. 

★101번이 나오는이유

100번까지 서버에 데이터가있기때문에, 이 서버에서 POST방식으로 작업을하게되면 자동으로 마지막데이터 ID 다음으로 할당되게된다. 이 서버는 지금 없는데이터(101)을 요청하면 그냥 {} <이런식으로 반환되게 설계해놓은거고, 우리가 만들때 {}대신 넣고싶은것(404에러나 기타등등)을 넣으면된다.


#-d옵션:data 사용
curl -d "title=test&body=insert" https://jsonplaceholder.typicode.com/posts/
->비어있는 101번에 title은 test, body는 insert가 넣어져서 나옴.이것도 서버가 id(101)을 할당되게만들어놨다. 

★단, insert되었다고 나오지만 실제 서버에는 저장되지않았다(test서버라서)

#-H:header 변경

#Content-Type : application/json ->json형태로 보낼거야 라는의미

- 일반적인Json:{key:value} / 데이터많이보낼때 {list:[{k:v},{k:v}]}
- curl 에서의 json : "{\"key\":\"value"}" ->원래 저런모양이라 정규식\로 key와 value가 문자열임을 명시해주는 형태가되었다.

curl -H "Content-Type: application/json" -d "{\"title\": \"test\", \"body\": \"insert\"}"  https://jsonplaceholder.typicode.com/posts/

★Content-Type: application/json ->이건 예약어라서 대소문자 구분해야한다.

#PUT

있는데이터를 update하는친구.

curl -X PUT -d "title=test&body=update" https://jsonplaceholder.typicode.com/posts/1
->'있는데이터' 를 업데이트한다. 기존1번 데이터의 title을 test로 body를 update로 바꿈

#DELETE
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
->ID 1번 내용 삭제

## axios
[axios](https://axios-http.com/kr/docs/intro)

axiso는 callbackhell을 해결하기위해 나왔다.

- 서버가 Rest하게 만들어져있으면 사용할수있는 라이브러리이다.

설치는 여러가지가있는데 그 중 CDN을 사용할것이다.(window)

CDN?
Content Delivery Network(컨텐츠 전송 네트워크)의 약자이다.
아주 먼곳에있는 데이터를 중간중간 기지국같은곳에 저장해놓은거라고 생각하면된다.
 ex) 서울-미국까지 택배받는데 대전에 같은물건이있어서 대전에서 물건이오는거랑 같음


### CDN을사용해보자

위의 홈페이지에서 아래 내용 복사해서 이용한다.

jsDelivr CDN 사용하기:
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

```http
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        button{
            width: 100px;
        }
    </style> <!--↓라이브러리이니까 이렇게 가져옴-->
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script> 
    <script>
        onload=()=>{//onload:function(){}이랑 같음
            target_url="https://jsonplaceholder.typicode.com/posts"; //주소를 변수로선언해서 사용
            btns=document.querySelectorAll("button");
            btns[0].addEventListener('click',()=>{
                axios({
                    method:"get",
                    url:target_url
                }).then(function(resp){ //이부분은 => 사용x
                    alert(JSON.stringify(resp)); //응답된객체를 문자열로 바꿔서 출력할것
                }) //0번째 버튼을 누르면,지정한 url의 데이터를 get방식으로 가져와 문자열로 바꿔출력한다. 
                    //지금은 url이 전체내용을가져오는 주소여서 모든 데이터를가져온다.

            });
            btns[1].addEventListener('click',()=>{ //기본적으로 axios는 헤더와 바디를같이보여주는구조
                axios({
                    method:"get",
                    url:target_url+"/1"
                }).then(function(resp){ 
                    alert(JSON.stringify(resp)); 
                })
                    

            });

            btns[2].addEventListener('click',()=>{
                axios({
                    method:"post", 
                    url:target_url,
                    data:{"title":"test","body":"insert"} //data를쓰는이유는 post방식이 insert,create이기때문에 데이터를 같이보내줘야한다.
                }).then(function(resp){ 
                    alert(JSON.stringify(resp)); 
                })
                  //data를안쓰면 그냥 비어있는상태를 반환함(서버가그렇게반환하게만들어놨음 서버 바이 서버. 404에러뜨는곳도있음)  

            }); 
        
            btns[3].addEventListener('click',()=>{
                axios({
                    method:"put", 
                    url:target_url+"/1", //put은 '있는데이터'만 '수정/갱신'이가능하기때문에 특정 리소스지정
                    data:{"title":"test","body":"update"} 
                }).then(function(resp){ 
                    alert(JSON.stringify(resp)); 
                })
                    //사용할수있는 method는 버튼의 종류와같다.
            });     //get all(url만지정), get 1(ulr+리소스), post(생성,추가. url+data:{추가할데이터:딕셔너리형태})
                    //put(update),delete(삭제)
            btns[4].addEventListener('click',()=>{
            axios({
                    method:"delete", 
                    url:target_url+"/1", 
                    data:{"title":"test","body":"update"} 
                }).then(function(resp){ 
                    alert(JSON.stringify(resp)); 
                }) //삭제버튼을 눌러보면 상태 200 뜨고 {} < 잘 비어있는것을 확인할수있다.
                    
            });    
                    
        }    
        
    </script>
</head>
<body>
    <button>GET ALL</button>
    <br>
    <button>GET 1</button>
    <br>
    <button>POST</button>
    <br>
    <button>PUT</button>
    <br>
    <button>DELETE</button>
</body>
</html>
```
## django로 REST를 사용해보자

[장고레스트홈페이지](https://www.django-rest-framework.org/)

우선 djangorestframework를 설치하자

pip install djangorestframework

```python
django-admin startproject 폴더명 :프로젝트생성
(선택사항)

django-admin startproject restdjango생성

#settings.py

INSTALLED_APPS = [
    ..
    ..
    ..
'restdjango']

↑ restdjango폴더 안의 settings.py파일을 열어서 installed_apps안에 restdjango추가


#models.py생성

from django.db import models
from django.utils.timezone import now
class MyBoard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=1000)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField(default=now) #타임존은 utils.timezone안에있다.

#serializers.py
from rest_framework import serializers
from .models import MyBoard <아까만들었던 models.py를 import해온다


class MyBoardSerializer(serializers.ModelSerializer):serializer클래스를 상속받을것임
    class Meta: 메타클래스는 클래스안에있어야한다.
        model = MyBoard
        fields=('id','myname','mytitle','mycontent','mydate')

serializer를 상속받아서 그 안의 요소들을 가져다쓸수있다. 그래서 meta클래스를 하나 선언하고 가져와서
그안에 myboard의 내용을 넣어준다. serializers.ModelSerializer안의 my보더시리얼라이저로 import해서쓸수있다.

★serializer?
쉽게말하면 view와 models사이에서 변환시켜주는역할을 한다고 생각하면된다.


#models.py(db랑통신)

from django.db import models
from django.utils.timezone import now
class MyBoard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=1000)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField(default=now)

orm:데이터베이스의 관계와 파이썬의 오브젝트를 연결해준다. models.py가

#vuews.py(응답)

from rest_framework import viewsets
from .serializers import MyBoardSerializer
from.models import MyBoard


class MyBoardView(viewsets.ModelViewSet):
    queryset = MyBoard.objects.all()
    serializer_class = MyBoardSerializer

    def perform_create(self, serializer):
        serializer.save

#urls.py(요청)

from django.contrib import admin
from django.urls import path
from .views import MyBoardView


myboard_url=MyBoardView.as_view({'post':'create','get':'list'})
myboard_resource = MyBoardView.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update', #post
    'delete':'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myboard/',myboard_url,name='myboard_url'),
    path('myboard/<int:pk>',myboard_resource,name='myboard_resource'),
]


#터미널
마이그레이션적용

cd restdjango 로 실행하려는 manage.py가있는곳으로 이동

migrate적용

python manage.py makemigrations restdjango(<폴더이름)
python manage.py migrate

★장고 동작

urls(요청이들어옴) <-> view(urls를 통해들어온 요청에대한 처리)<->models(db에서데이터를가져와줌)<->DB
(view와 model사이에 시리얼라이즈)

#CMD창에서 제대로 응답하는지 확인
curl -X GET "http://127.0.0.1:8000/myboard/" 얘는 get방식통신(가져오는거)
curl -X POST -d "myname=django&mytitle=rest&mycontent=resful" "http://127.0.0.1:8000/myboard/"(post방식 추가하는거)

curl -X PUT -d "myname=test&mytitle=update&mycontent=test" "http://127.0.0.1:8000/myboard/1"

curl -X GET "http://127.0.0.1:8000/myboard/1"(확인용)

curl -X DELETE "http://127.0.0.1:8000/myboard/1"

```
# Elasticsearch7(elk7) 설치

Elasticsearch를 DE부분에서 어떻게사용할까?

LOG를쌓아서 LOG를KEYBANA 분석할것이다.

[Elasticsearch](https://www.elastic.co/kr/downloads/elasticsearch)

위의 링크에가서 각 os에맞는버전을 설치함
(현재는 리눅스 -> 7.17.7 버전설치)

```bash

1.설치

wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.17.7-linux-x86_64.tar.gz


tar xvzf elasticsearch-7.17.7-linux-x86_64.tar.gz
(압축해제)

ln -s elasticsearch-7.17.7 elastic
(심볼릭 링크생성)

2.키바나 설치

https://www.elastic.co/kr/downloads/past-releases#kibana

버전은 위의 일레스틱서치와 같아야한다.

위의 링크에서 원하는버전을 누르고,다운로드누르고 링크를복사해온다.

wget https://artifacts.elastic.co/downloads/kibana/kibana-7.17.7-linux-x86_64.tar.gz


tar xvzf kibana-7.17.7-linux-x86_64.tar.gz
(압축해제)

ln -s kibana-7.17.7-linux-x86_64 kibana
(심볼릭 링크생성)

3.logstash설치

https://www.elastic.co/kr/downloads/past-releases#logstash

키바나와 같은방법으로 설치진행

wget https://artifacts.elastic.co/downloads/logstash/logstash-7.17.7-linux-x86_64.tar.gz

tar xvzf logstash-7.17.7-linux-x86_64.tar.gz
(압축해제)

ln -s logstash-7.17.7 logstash
(심볼릭 링크생성)

4.sudo vim ~/.bashrc 설정

# elk

export ELASTIC_HOME=/home/계정명/elastic
export LOGSTASH_HOME=/home/계정명/logstash
export KIBANA_HOME=/home/계정명/kibana

export PATH=$PATH:$ELASTIC_HOME/bin:$LOGSTASH_HOME/bin:$KIBANA_HOME/bin

source ~/.bashrc

5.sudo vim /etc/security/limits.conf

end of file안에 아래내용 입력


#~~~~

계정명              -       nofile         655535

#end of file


6.sudo vim /etc/sysctl.conf 파일열기

#kernel.sy~

vm.max_map_count=262144

↑파일 제일 하단에 vm~만 입력 

```

## mysql에서 데이터를 가져와보자

```bash

1.logstash랑 mysql연결

logstash-plugin install logstash-integration-jdbc

2. vim ~/logstash/test.conf


input {
    jdbc {
      jdbc_driver_library => "/usr/share/java/mysql-connector-j-8.0.31.jar"
      jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
      jdbc_connection_string => "jdbc:mysql://localhost:3306/mysql"
      jdbc_user => "root"
      jdbc_password => "1234"
      statement => "SELECT * from test"
      schedule => "* * * * *"
    }
}

filter {

}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "test"
    document_id => "%{id}"
  }
}

↑test.conf 안에 위의 내용 붙여넣기!


3.

★터미널 3개켜서 진행

3-1.기존터미널

elasticsearch 

->elasticsearch 실행 
정상실행되면[2022-11-21T14:36:45,688][INFO ][o.e.c.m.MetadataMappingService] [ubuntu] [.kibana_7.17.7_001/eQaBG~~(생략)] update_mapping [_doc] 이런식으로뜬다.


3-2.logstash -f ~/logstash/test.conf

->1분에 한번씩 select * from test가 출력된다.

3-3.kibana

-> 위의 세개 다 입력후에 아래 localhost에 접속해서 확인

★터미널 한개로 켜기(airflow와 동일한방법)

elasticsearch -d (데몬으로실행, 백그라운드로 돌아간다)

nohup kibana &

nohup logstash -f ~/logstash/test.conf &

각 아래 로컬호스트에가서 정상작동되는지  확인

```

### elasticsearch : localhost:9200

![elasticasearch](/9200.PNG)

#### kibana : localhost:5601
![kibana](/5601.PNG)

### localhost:9200/test/_search
![logstash](/9200_test.PNG)


# elk8

```bash

#elk8버전 설치

1.elastic

wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.5.1-linux-x86_64.tar.gz

tar xvzf elasticsearch-8.5.1-linux-x86_64.tar.gz


ln -s elasticsearch-8.5.1 elastic


2.logstash

wget https://artifacts.elastic.co/downloads/logstash/logstash-8.5.1-linux-x86_64.tar.gz

tar xvzf logstash-8.5.1-linux-x86_64.tar.gz 

ln -s logstash-8.5.1 logstash

3.kibana

wget https://artifacts.elastic.co/downloads/kibana/kibana-8.5.1-linux-x86_64.tar.gz

tar xvzf kibana-8.5.1-linux-x86_64.tar.gz

ln -s kibana-8.5.1 kibana


4.sudo vim ~/.bashrc 설정

# elk

export ELASTIC_HOME=/home/계정명/elastic
export LOGSTASH_HOME=/home/계정명/logstash
export KIBANA_HOME=/home/계정명/kibana

export PATH=$PATH:$ELASTIC_HOME/bin:$LOGSTASH_HOME/bin:$KIBANA_HOME/bin

저장하고 ↓ 적용

source ~/.bashrc

5.kibana 입력으로 실행

eyJ2ZXIiOiI4LjUuMSIsImFkciI6WyIxOTIuMTY4LjEyNi4xMzE6OTIwMCJdLCJmZ3IiOiJjNDA1NWYzOWRiOGRlNmQxYWU3ZGE3MmFjZjU5OWEyNGU2Zjk3ODU4NjIzYzY5ZDZmZjIzZjgxZTIxMjUxYzJjIiwia2V5IjoiWDZNSm1ZUUJkazM1VGdfanFQaTQ6YVNrQzVLNThSNGFEaFYtT3FlX1ZjQSJ9 (토큰값)

->토큰값 30분제한있고, 키바나 깔고 최초1회 설정해줘야한다. 두번째부터는 localhost:5601로 키바나 접속가능


★5.키바나 최초접속 key값 ★(제한시간30분)

※주의:새로운 터미널에서작업!

elasticsearch-reset-password -i -u 아이디

->y 누르고 -> 비밀번호입력/ u다음에오는값이 아이디, y다음으로 입력하는값이 비밀번호

6. localhost:5601

키바나에 접속하여, 토큰값 넣어주고 아까 생성한 유저와 비밀번호로 로그인하기


elk8 kibana : localhost:5601

elk8 kibans : https://localhost:9200  
->7버전에비하여 "https://"가 앞에붙는다. 이거 안붙이면 접속안됨


7.mysql와 연결

logstash-plugin install logstash-integration-jdbc
(7버전과 동일하다), 입력 후 test.conf파일 오픈


vim ~/logstash/test.conf
↓ 아래내용 입력


input {
    jdbc {
      jdbc_driver_library => "/usr/share/java/mysql-connector-java-8.0.29.jar"
      jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
      jdbc_connection_string => "jdbc:mysql://localhost:3306/mysql"
      jdbc_user => "root"
      jdbc_password => "1234"
      statement => "SELECT * from test"
      schedule => "* * * * *"
    }
}

filter {

}

output {
  elasticsearch {
    index => "test"
    hosts => ["https://127.0.0.1:9200"]
    cacert => '/home/big/elastic/config/certs/http_ca.crt'
    ssl_certificate_verification => false
    user => "elastic"
    password => "123456"
    ilm_enabled => false
    document_id => "%{id}"
  }
}

8.접속확인

https://localhost:9200/
go말고 옆에 흰색버튼 -> 하단의 흰버튼

elastic 로그인 창 활성화 ->로그인 ->성공!

```
















