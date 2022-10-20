# TIL DAY20(22_10_20)

## Django를 통해 게시판을 만들자(DB이용)
class를 Model로만들어 DB에 추가하거나 삭제 수정 등을 할 수 있고
매니저를 이용해 Model과 DB사이에서 통신할수있다.
DB는 Mysql, Oracle, sqlilte3 등등 여러가지 사용가능.
(APP 생성문(터미널):django-admin startapp app이름)

**DB를 사용하려면 settings.py안의 DB를잡아주는 부분에가서 먼저 기본설정을 해 줘야한다.**

    1. 'ENGINE': 'django.db.backends.mysql', 사용할 기본 db지정.mysqldb서버와장고서버를연결해줍니다.(그게model레이어)

    mysql의 서버정보

            'HOST': 'localhost(호스트명)',
            'PORT': '포트번호(DB포트번호)'

    사용할 프로그램이름과(name)
    유저이름과 패스워드

            'NAME': '사용할 프로그램 명',
            'USER': '계정이름',
            'PASSWORD': '비밀번호',

    settings.py의 Installs App[]안에서 생성한 App폴더이름을 추가 해 줘야 실질적으로
    사용할 수 있다.
    ex)만약 DataTest1 App폴더를 생성하고, 그안에 Models라는 py파일을 생성 후,
    settings.py안에가서 Installs Apps[~]를 찾아 []안에 'DataTest1' 을 추가.

    2. Model파일은 아래처럼 생성하는데
    class 클래스명(models.Model):
        생성할컬럼명 = models.타입(타입크기 (max_length=100 ...)

    def __str__(self): <리턴값으로 내용물의 출력내용을 재정의 할것임.
        내용물 
        return  값 

    3.터미널에서 아래와 같이 입력해서 생성해준다.

    python manage.py makemigrations dbtest2 <깃헙의 add임. dbtest2는 app폴더명. 그래서 여튼 add인상태라고 생각하면 된다. '반영'은안되어있는 상태

    python manage.py migrate <데이터를 넣는다.  migrate 은 위에설명했듯이 셋팅의 intalls apps안의 내용을 데이터베이스로 만들어준다(만들거있을 때). 깃헙의 commit과같음! 

    makemigrates 앱폴더명 : add 
    migrate : commit

    4.index생성(보통 html파일)
    5.views의 함수생성(def aaa(request)|(request,id(테이블의 프라이머리 키 지정안했을시 자동생성되는 프라이머리 키값을 의미하는 id.)).단 model에서 데이터 가져올시 import필수. from .models import 생성한 클래스명<이런식으로
    6.urls연결. (path('경로','호출될html'or views.호출될 함수명,name='지정할이름'))
        (단 views 사용시 import views필수/ include('넘길urls')사용시 기본 path import옆에 ,include추가) 
        name같은경우는 경로의 이름이라고 생각하면된다. 저 path의(경로)의 이름.
        이름이있으면, 다른곳에서 불러오기 수월하다 아래에서 조금 더 자세하게 알아보자
    (4,5,6번은 만드는것에따라 달라지기때문에 생략)

데이터베이스 간단한 조작은(아래는 터미널에서 실행) 

아래는 조회문. add하면 생기는 파일과 비슷한것임 
python manage.py sqlmigrate dbtest 0001  <0001은 바뀔수있음

추가문

from dbtest.models import MyBorde < MyBorde를 불러옴
from django.utils import timezone < mydate에 시간을 추가해 주기 위해 사용.

test=MyBorde(myname='testuser',mytitle="test-title",mycontent="test 1234 abcd 뭐래", mydate=timezone.now()) 각 컬럼안에 testuer, test-title tset12134 abcd등이 추가된다.

**수정하려면**
```python
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=100)),
                ('mytitle', models.CharField(max_length=500)),
                ('mycontent', models.CharField(max_length=2000)),
                ('mydate', models.DateTimeField()),
            ],
        ),
    ]
```
위는 makemigrations 하면 생성되는 0001.py파일이다. 
만약 내용을 수정하고싶다면 models.py안의 수정하려는 class내용을 고치고,
다시 makemigrations하면! 

아래와같이 

```python
class Migration(migrations.Migration):

    dependencies = [
        ('dbtest2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myboard',
            name='mytitle',
            field=models.CharField(max_length=300),
        ),
    ]

```
0002.alter_~.py파일이 생성되고, 수정된 내용이나온다.
그리고 반영하려면, 꼭 migrate를 해줘야한다.


## url리팩토링과 url 분리(path(~~name='test'))

path(~~name='test') 이렇게 경로에 이름을 부여해 1:1로 매핑하는방법.
name속성이라고하는데 알아보자.

왜사용하는가?

- url의 구조가 빈번하게 바뀌니까 수월하게 바꾸기위해서 사용.
- 실제주소대신 1:1로 매칭된 네임으로 관리하면 리팩토링하기가 수월하다. as 별칭 같은개념.
이렇게 별칭을 주면 여러곳에서 호출해서 사용하기 편하다. 

예를들어
urls.py에 아래와 같은 코드가 작성되어있다고 가정
```python
path('<int:question_id>/', views.detail, name='detail')
```
차례대로

<int:question_id> 이건뭐야?

 ->루트주소/question_id/와 같은구조의 url을받는데 question_id의 값을 int타입으로 받겠다는 의미입니다.(id니까 숫자만 들어옴 고로, 완성되는 주소는 루트주소/question_id)
 가 된다.

views.detail
->루트주소/question_id 주소가 요청되었을때 view.py안의 detail이라는 함수를 매핑해준다.(저 함수를 실행하게됨.)

- 경로가 찾기가 힘들기때문에 특별한 경우가아니면 앞뒤로 /경로/ 슬래시를주자. 적어도 뒤에는 주는게 좋다. 앞에 /붙이는 이유는 위에서 말한것 처럼 경로찾기가 힘드니까 상위경로까지 잡아버리는것.

- **URL을 분리해서 관리해보자**
  
분리를 왜 하죠?
 기본URL과 프로젝트 URL을 나눠서 관리하고싶을 때 자주 이용하는 방법이다.
 기본 URL에 계속 추가해주는게 번거롭고 지저분해지니까 프로젝트성격을 띄는곳의 APP의 URLS와
 기본경로의 URLS(INDEX페이지)을 따로둬서 기본경로로 요청되는 것 들은 기본경로 URLS.PY만 관리하게 만들어준다

    기본 = basic 프로젝트 = tset1 
 
    tset1은
    form .import views를 쓸 필요없이 
    
        from django.contrib import admin
        from django.urls import path

        urlpatterns = [
         path('admin/', admin.site.urls),
         path('basic/',include('basic.urls')),
    ]

    이러면 'basic/ 으로시작하는 친구들은 다 basic.urls에서 처리하게된다.
    기본에 대한 관리는 basic파일에만 관리하면 되니까 보기  편해짐.

 
## static 처리
2가지 방법이있다.

**첫번째, 프로젝트 폴더하위에서 사용하기**

파이썬에서 static도 가능하다.(정적 처리. 보통 static폴더를(디렉터리임.app아님!) **StaticApp 폴더아래**에, 생성하여 **js**/**css**/**img** 등 **정적요소**를 관리한다. )

 처리하는 방법은 일단, settings.py파일안의 STATIC_URL을 설정해준다

STATIC_URL = /static/ <기본으로 설정되어있는 경로.

여기 아래에 **STATICFILES_DIRS**를 생성 해 줘야한다!

    STATICFILES_DIRS=[BASE_DIR / 'static',] ->너가 html파일에서 호출해올 폴더의 경로를 지정해줘. 라는의미 그럼 static 폴더가 css,img,js 등을 호출해와서 씀.
    html은 static폴더를 로드해서 사용하는거고

    ★ 단,폴더이름을 static이라고 해줘야지 장고가 인식함으로 주의!★

이렇게 설정해줬으면 이제 사용하면된다.

html파일에서 **최상단**에 **{% load static %}** 를 써주고 static을 load해온다.

그럼 html내부에서 필요한곳에 static이 호출해오는 정적인 요소들을 사용 할 수 있게되는데

사용문법은
**{% static 'js/javascript.js' %}** 이다. static안의 js안의 javascript.js를 가져와라 라는 의미.

**{% load static %}**  가 뭔데? 
-> 현 html파일에 static을 로드해오는것. 


**두번째, 앱 폴더 하위에서 사용하기**

settings.py 파일안의 

STATICFILES_DIRS=[
    BASE_DIR / 'static',
    os.path.join(BASE_DIR,**'사용할app폴더명**,'static')
]

이라고 작성해주고,
setting.py파일 최상단에 os를 import해준다.(import os)
그러면 사용할 폴더명 아래의 static폴더를 인식한다.

os.path.join 가 뭐야?
->**두 개의 문자열**을 인자로 받아서 첫 번째 인자와 두 번째 인자를 이어 붙인 경로를 생성


![staticimage](static_처리과정.png)


위의 사진은 매우매우중요하다!
[참고사이트](https://0ver-grow.tistory.com/912)


**배포를 위한  STATIC_ROOT사용**

★Debug=True 일때는 runserver가 모아주는데(debug=false 사용도가능하다.)
배포할때는 runserver로 스태틱파일들을 모아주지않음.
그러므로, STATIC_ROOT를 사용해 모아줘야한다.

**프로젝트폴더 안의**settings.py에

STATIC_ROOT = os.path.join('스태틱파일들을 모을곳')

위와같이 작성해주면, 스태틱파일들을 내가 지정해준곳으로 모아준다.
(폴더명은 보통 **staticfiles** 라고 많이쓴다.
python manage.py collectstatic 사용하면staticfiles만들어진다고 한다.)


## setting.py의 BASE_DIR와 TEMPLATES DIRS를 알아보자

기본적으로 setting.py의 BASE_DIR부분을 보면

>BASE_DIR = Path(__file__).resolve().parent.parent

라고적혀있는데, 이게무슨 의미이냐면

Path(__file__)= 현재 파일(setting.py)의 구상 경로를 인스턴스화해서 가져온다.
.resolve()= 메서드를 통해 구상경로를 절대경로를 반환한다. 
.parent.parent = 반환한 **절대경로를 기준**으로 부모의 부모(상위의,상위)를 BASE_DIR로 설정한다. 

즉 현재파일의 구상경로-> 절대경로  변환 -> 절대경로를 기준으로 상위의 상위를 찾아 설정이므로, 현재 작업중인 **setting.py의 절대경로**

**이부분은 정말 중요!!**

그렇다면 TEMPLATES부분을 보자

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], ->비어있으면 ,
        'APP_DIRS': True, ->앱마다의 TEMPLATES폴더를 찾을것이다.(app폴더하위의)
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],}


'DIRS': [BASE_DIR / 'templates']=베이스 DIR 경로안의 templates를 읽어온다고 되어있다.
(root디렉터리 바로 아래에있는 templates를 불러오는걸로 경로를 지정해준다는 의미.)


## 절대경로 상대경로

절대경로:웹페이지/파일이 가지고있는 **고유한경로**. 어디에 존재하는지의 경로라고 생각해도된다. 현재위치와 상관x
http://www.google.com, C:\users\document\untitled.jpg  둘다 절대경로.
절대경로를 알고있으면 바로이동/바로실행이 가능하다.

상대경로:현재 위치에서 필요한 위치로가는데 필요한 '상대적인'경로.
현재위치를 기준으로하는것

  / : 루트(가장최상의 디렉터리로)
  ./ : 현재 위치
  ../ : 현재 위치의 상단 폴더(상위 디렉터리로)


※django는 탬플릿 태그({% 내용 %})를 이용하는데 몇가지 소개해보면

**{% for ~%}**
    <>순서 : {{ forloop.counter }}</>
    <>{{ item }}</>
**{% endfor %}**

1.{% for base in base_list %} = base_list를 순회하면서 순차적으로 base에 대입
2.{% forloop.counter %} = 루프내의 순서로, 1부터 표시한다
3.{% forloop.counter() %} = 루프내의 순서로 0부터 표시한다.
4.{% forloop.first %} = 루프의 첫번째 순서인 경우, **True**  첫번째가아니면?False
5.{% forloop.last %} = 루프의 마지막 순서인 경우, **True** 마지막이아니면?False
**{%if 조건문1 %}** 
    조건문1에 부하는 경우면 실행

{% elif 조건문2 %}
    조건문2에 부합하는 경우면 실행
{% else %}
    그외의 경우.

**{% endif %}**

1.{% if base_list %} = base_list가 있다면.
2.{% if not base_list %} = base_list가 없다면.


{{'객체'}} /{{객체.속성}}

1.{{data.id / data.myname / .subject 등}} 객체.속성

2.{{item / data / name}} 객체

