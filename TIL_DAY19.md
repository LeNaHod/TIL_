# TIL_DAY 19(22_10_19)

## Mysql

- Mysql이 오라클에 들어가면서 원래 개발하시던분이 나와서 만든게 Mariadb.
- 
- mysql은 오토 인크리먼트가 존재한다.(기본키 설정하는것과 같은곳에 지정)
오토 인크리먼트는 시퀀스(자동으로 +1씩 증가)와 같다.

- mysql은 fullouter join이없다. 안쪽 오른쪽 왼쪽만 지원해줌


## django를 알아보자
장고는 웹프레임워크이다.
사용하기가 플라스크보다 쉽다.

- 장고 = 너가 뭘 쓸지 몰라서 다 가져와봤어
- 플라스크 = 너가 뭘 쓸지 몰라서 최소한만 가져와봤어.

## django들어 가기전에
가상환경 생성하는법과 조작하는 법을 간단하게 알아보자
보통 가상환경은 env로(아니면 venv) 되어있다.

(아나콘다 가상환경이라고 가정)
conda create -n python=버전 가상환경 생성
conda deactivate 가상환경 종료
conda activate 가상환경이름  가상환경 접속
conda env list  가상환경 리스트를 경로와 함께 보여줌 

**웹 서버와 웹 어플리케이션 서버의 차이를 알고가자**

클라이언트가 서버에게 '정적'(js,css,img,mp3...안변하는애들.게시판은 '동적')인것을 요청함 -> 웹 서버에서 정적인애들을 응답해줌
'동적'인것을 요청함->서버가 웹어플리케이션을 실행시켜서 웹 어플리케이션이 클라이언트에게 응답함 =이게 줄여서 와스(was)!

    웹어플리케이션서버=와스=동적처리
    웹서버=정적처리

    싱크=동기
    어싱크=비동기

    리퀘스트=요청
    리스판스=응답

## django의 구조

디렉터리

    -manage.py(아래 파일들을 전체적으로 관리해주는친구.)
        -asgi.py
        -★settings.py
        -★urls.py
        -wsgi.py
        -★view(생성해야함.기본x)
    asig~wsig까지 APP이라고 부른다.
    
    manage:주요명령어가 startapp/ ★runserver(실행)/makemigrations / migrate
    wsig:Web Server Gateway Interface의 약자. wsgi->asig로 대체가능. WAS의 통신지원.
    asig:Asynchronous Server Gateway Interface. WAS의 동기/비동기 통신지원!(단,3.0버전이상)
    settings.py:project환경설정 부분. 기본urls경로와 디렉터리 경로(dir)를 지정해줄수있다. 잘 활용하면 찾아가지않고 바로 보여줄수있다.
    ALLOW_HOST/ INSTALLED_APPS / ★TEMPLATE(탬프릿(실질적으로 그려주는친구)설정)/DATABASES / ★STAITC_URL

    urls: ★url과 views안의 함수를 매핑해주는친구★.요청에 맞는 작업을 호출해준다.
    예를들면 https://naver.com/ <endpoint 가 들어왔을시, /뒤에는 아무것도 없어보이지만
    사실 ""이 붙어있어서  path("","함수이름"), <(뒤에 아무것도 안올거여도 ','반드시붙여야함!) 이렇게 매핑시켜줘야한다. 그럼 views.py파일 안에 def index(request){endpoint까지만 들어왔을때 실행시킬 조건~ return HttpResponse("출력할것") } 을 찾아 실행시킨다. ★★이건 정말 중요!!!★★

그렇다면 django는 어떻게 작동할까? MVT 구조로 만들어져있다. 각 모델,뷰,탬플릿의 약자이다.

먼저, 요청이들어오면! 아래와 같은 작업을 거친다.

모델 : 데이터베이스 연동(ORM). DB에서 데이터를가져오고 넣고하는걸 도와준다.db에서가져와서 뷰로넘어감.

★뷰: 데이터 구성 (Business Logic).실질적으로 데이터를 처리(가공)을 담당한다.
뷰에서 데이터를 가공하고 처리해서 탬플릿에 넘겨서 출력하거나, urls.py와 연결한다(path이용).

탬플릿:view에서 처리된 데이터를가지고 페이지에 그려서 출력한다. 그렇게 요청한 클라이언트에게 Response(응답)해준다. 주로 *(파일명).html

![웹구조](./webmodel.png)


## 문법

```python
아래는
반드시 딕트타입(키:밸류)로 들어와야한다!

def greetings(request, name):
 return render(request, ‘greeting.html’, {“name”: name})

Request를 받아 화면을 구성하여 Response
def hello(request):
 return HttpResponse(“<h1>Hello, World! /h1>”)

data를 template에 전달하여 화면을 구성 (rendering)
<h1>{{ name }} /h1>

{{ 변수명 }}   : <h1>Hello, {{ name }}! /h1>
{{ iterable.index }} : <p>{{ lst.0 }} /p>
{{ object.key }} : <p>{{ dct.class }} /p>
{{ value|filter }} : <p>{{ subject|upper }} /p>

```

## 코드를 통해 알아보자!

```python

#기존스타벅스 코드에 folium map을 추가했다.(마커도 기존것과다름)

전국의 스타벅스 매장을 표시 해 보자! 코드를 입력하면 맞는 지역에맞춰 출력된다.
이건 folium 을 이용한 시각화이다. folium예제.

import requests
import json
import folium


def getSiDo():

    url = 'https://www.starbucks.co.kr/store/getSidoList.do'
    resp = requests.post(url)
    sido_json = resp.json()['list']
    sido_code = list(map(lambda x: x['sido_cd'], sido_json))
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))
    sido_dict = dict(zip(sido_code, sido_name))

    return sido_dict


def getGuGun(sido_code):
    url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    resp = requests.post(url, data={'sido_cd': sido_code})

    gugun_json = resp.json()['list']
    gugun_dict = dict(zip(list(map(lambda x: x['gugun_cd'], gugun_json)), list(map(lambda x: x['gugun_nm'], gugun_json))))

    return gugun_dict


def getStore(sido_code='', gugun_code=''):
    url = 'https://www.starbucks.co.kr/store/getStore.do'

    resp = requests.post(url, data={
        'ins_lat': "37.56682",
        'ins_lng': "126.97865",
        'p_sido_cd': sido_code,
        'p_gugun_cd': gugun_code,
        'in_biz_cd': "",
        'set_date': ""})

    store_json = resp.json()['list']

    store_list = list()
    count = 0
    for store in store_json:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        store_list.append(store_dict)
        count += 1

    store_dict = dict()
    store_dict['store_list'] = store_list
    store_dict['count'] = count

    result = json.dumps(store_dict, ensure_ascii=False)

    make_map(store_dict)

    return result


def make_map(result):
    min_lat = min(list(map(lambda x: x['lat'], result['store_list'])))
    max_lat = max(list(map(lambda x: x['lat'], result['store_list'])))
    center_lat = float(max_lat) - (float(max_lat) - float(min_lat))/2 #센터를 기준으로 스토어 리스트를 출력한다.

    min_lot = min(list(map(lambda x: x['lot'], result['store_list'])))
    max_lot = max(list(map(lambda x: x['lot'], result['store_list'])))
    center_lot = float(max_lot) - (float(max_lot) - float(min_lot))/2

    m = folium.Map(location=[center_lat, center_lot], zoom_start=14)

    for data in result['store_list']:
        popup = folium.Popup(folium.Html(data['s_name']),max_width=len(data['s_name'])*30)
        folium.Marker(
            location=[data['lat'], data['lot']],
            popup=popup,
            icon=folium.Icon(color='red')
        ).add_to(m)

    m.save('result.html')


if __name__ == '__main__':
    print(getSiDo())
    sido = input('도시 코드를 입력해 주세요')
    if sido == '17':
        print(getStore(sido_code=17, gugun_code=1701))
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해 주세요')
        print(getStore(gugun_code=gugun))


워드 클라우드(글자로 특정 모양이나, 그림안을 글자로 채우는것)를 사용해보자.

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import json

with open('./webtoons.json','r',encoding='utf-8')as file:
    webtoons= json.load(file)

res = dict()
for webtoon in webtoons['webtoons']:
    res[webtoon['title']] = int(float(webtoon['star']) * 100)

masking_img= np.array(Image.open('h1.png')) #행렬 형태로바꿈 그림안에 맞춰서 넣어줄건데 숫자로하는게 편해서.테두리값만가져옴

cloud = WordCloud(font_path='./Goyang.ttf', max_font_size=40, mask=masking_img, background_color='white').fit_words(res)
cloud.to_file('result.png')

plt.imshow(cloud,interpolation='bilinear')
plt.axis('off')
plt.show()

장고예제

views.py

from django.shortcuts import render

def index(request):
    return render(request,"tags/index.html",{"name":"nana"}) #호출되면 tags안의 index.html에 그려줄거야.딕트타입의 name을.근데 네임의 속성값이 nana인.
    #"tags/index.html" >이 경로의 tags앞에경로는 아까 셋팅py안의 탬플릿의 베이스 dir에서 잡아줘서 앞에 탬플릿츠가잇다고생각해야함.안잡아주면 기본경로따라감

urls.py

from django.contrib import admin
from django.urls import path,include #inclue=다른곳으로 일거리 패스시켜주는친구
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("var/",include("var.urls")), #이부분은  var/ 가 들어오면, var디렉터리(현재 작업위치와 다른 디렉터리)var.urls에게 일을 넘겨주겠다는 의미.꼭 include를 import하고 사용해야함.
]

setting.py 수정한 부분만.

ROOT_URLCONF = 'tags.urls'#처음만나는 urls를 설정해줄수잇다. 말그대로 루트 url주소!

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"tags/templates"], #작은tags밑에 templates라는 폴더를 잡아줌. 그냥 /tmplates라고 써도됨
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
```
## 워드클라우드 출력 결과

![워드클라우드](/Figure_1.webp)

