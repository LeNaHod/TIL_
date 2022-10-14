# TIL DAY16(22_10_14)

가상환경
python venv ->파이썬이지원하는 가상환경 

## python 가상환경

1.python venv
cd /

2.mkdir myenv 
dir로확인가능

3.cd myenv

4.python -m venv crawling  >dir  >cd crawling >dir 

5.cd Scripts >dir 해서 activate.bat이있는지확인

6..\activate.bat 입력 (해제는 .\deactivate.bat)

## 아나콘다 가상환경(아나콘다 기본제공 conda)

cmd에서 conda가안될시,

1.아나콘다가 설치되어있는 경로로가서 확인

2.경로를복사

3.내 pc 고급설정> 시스템 환경변수 >Path 편집 

4.환경변수 추가 A:\Anaconda3\condabin 추가

5.터미널 재실행

6.콘다 가상환경 만들기 

6-1.conda create -n mycrawling python=3.9(버전명)

y

conda activate mycrawling(<이름)
conda deactivate

## 파이참 단축키와 프로젝트생성

- interpreter 경로가 터미널 conda env list에 만들어둔 경로와 일치하게한다.(가상환경 여러개만들때)
가상환경을 바꾸고싶을땐, 오른쪽하단의 python3.9(3.9는가상환경버전)(가상환경이름)을 클릭해 원하는것으로 변경

- 단축키
- 파이참:alt+1. 해당메뉴로 바로가기 
- 윈도우4:실행창 바로가기
- alt+insert=바로만들기 
- alt+1 -> alt+ins하면 바로만들기 가능

## 공공데이터 활용법과 스크래핑/크롤링
스크래핑와 크롤링은 서로 다른것인데 요즘은 크게 구분하지않는 추세라 정보를 가져오는작업을 크롤링이라고 하기도한다.

- 스크래핑: 웹페이지에서 원하는 정보만 가져오는것
- 크롤링 : 웹페이지 전체를 다 가져오는것

**공공데이터 포털에서 오픈 AIP를 활용해보자!**
endpoint와 서비스 URL 요청메세지 명세의 필수 조건 이렇게 세가지를 조합하여 사용한다.
완성된 주소를 웹에보내고 데이터가 제대로 불러지는지 확인 후 파이썬에서 활용한다.

>EX) ~~rest/Covid19/~getCovid19~?erviceKey=m~ 이런식인데 
서비스URL+요청메세지명세1&요청메세지명세2&...

주소의'?'뒷부분은 키:밸류형식(GET방식)으로 querystring이라고 부른다.

## 코드를 통해 크롤링해보자!

```python

01.영화이름과 평점가져오기

import urllib.request
from bs4 import BeautifulSoup

#urllib.request  =는 크롤링할 url를 요청하고받기위한 모듈
#★기본문법★
#1.BeautifulSoup(markup, "html.parser" |"lxml" |"lxml-xml" |"xml"|"html5lib" 등을쓸수있다.)
#2.url="url주소" 꼭 url주소를 ""로해줘야한다. url을바로써도되지만, url이라는 변수를 두면 나중에 코드 복잡해졌을때 편함
#3.url을 오픈시켜주는 변수하나(아래는 resp)선언하고, requset.urlopen(url주소 |url이들어있는 변수)
#urllib는 파이썬 내장함수.
#4.find_all()을사용해서 url에서 원하는 태그를가져오자.
#4-1. soup.find_all("title") || soup.find_all("p", "title") || soup.find_all(id="link2") || soup.find(string=re.compile("sisters"))
#4-2. soup.find_all("a", class_="sister") <클래스로가져오는것.

url="https://movie.naver.com/movie/running/current.naver"
resp=urllib.request.urlopen(url);
soup=BeautifulSoup(resp,"html.parser")
movies = soup.find_all("dl", class_="lst_dsc") # class를쓸때 class= X class_ = O.

for movie in movies:
    title = movie.find("a").get_text()
    star = movie.find("span",class_="num").text
    print(f'title:{title}/star : {star}')

02.웹툰이름과 평점 가져오기

import requests
from bs4 import BeautifulSoup
import json

#★requests는 뭔가를 요청해서 주고받고할때 ★매우매우★ 편함!
#requests쓰는법 ↓
#r = requests.get('https://api.github.com/user', auth=('user', 'pass')) ->만약 post방식으로 요청하려면 .post하면끝
# ↓아래는 대강 사용법
#--------------------------------------------------------
# r.status_code
# 200
# r.headers['content-type']
# 'application/json; charset=utf8'
# r.encoding
# 'utf-8'
# r.text
# '{"type":"User"...'
# r.json()
# {'private_gists': 419, 'total_private_repos': 77, ...}
#----------------------------------------------------------
#.find는 결과값을 하나만 반환한다. 그래서 all로써야지 여러개반환.
#pase =분석 .화이트스페이스=공백. 그렇지만 제이슨객체로간주
#오브젝트{공백만나고(""), 문자열을만났다:밸류, 문자열:밸류 또 ,만나면? 다시 문자열로돌아가서 ,없을때까지 돌다가 없으면 빠져나옴}
#밸류는 공백 문자열 공백 | 공백 숫자 공백 | 공백("") 오브젝트 "" | ""트루""|""펄스""
#즉 {"":{:}} | {"":[{:...}]}이런식도가능 ex ){"name":"asndans","age":100} 키:밸류 근데 밸류가 문자열이니까 ""
#↑대한 표는 하단 json 그림을 참조.
#API는 정의 및 프로토콜 집합을 사용하여 두 소프트웨어 구성 요소가 서로 통신할 수 있게 하는 메커니즘이다. 즉 두 소프트웨어간에 대화형식으로 데이터를 주고받는것.
#API는 Application Programming Interface(애플리케이션 프로그램 인터페이스)의 줄임말.
#AIP는 여러서비스 방식이있는데 REST방식은 웹에 존재하는 모든자원(이미지 동영상 DB자원 등)에 고유한 URI를 부여해 활용하는것. EX)	rest/covid19~이런식으로되어있는거
#---------------------------------------------------------
url="https://comic.naver.com/webtoon/weekdayList?week=fri"
resp=requests.get(url)
soup = BeautifulSoup(resp.text,"html.parser")

webtoon = soup.find("div", {"class":"list_area daily_img"}) #all 써도 첫번째를찾기때문에 div 반복문이 한번만 돌음(왜냐면 이페이지의 div가 한 덩어리고 내가가져오고싶은 데이터는 div안의 dl에있으니까)
webtoons=webtoon.select("dl") #그래서, 저 div 안에서 또 dl태그를찾음. 이건 find,find_all 이랑 "div"말고 "ul"을써도 결국 dl로찾아줘야함
#---------------------------------------------------------
#방법2.webtoon=soup.find_all("div",class_="list_area daily_img") <이런형식으로 쓰는 방법도있다.
#webtoon = soup.find("ul",class_="img_list") 이런것도 가능
#----------------------------------------------------------
webtoon_list=list() #webtoon_list라는 list하나 생성
for webtoonss in webtoons:
    title = webtoonss.find("a")["title"]  #title속성을가져오기때문에 .text,.string이안먹힌다.
    star = webtoonss.find("strong").text
   # print(f'{title} {star}')

    tmp=dict()
    tmp['title']=title
    tmp['star']=star
    webtoon_list.append(tmp)
    #결과값이 리스트니까 []가 제일 겉에있고, 딕셔너리로 넣어서 []안에 {}.
    #그리고 tmp['title']->키값부분에 문자열 title출력 tmp['star'] ->밸류부분에 star출력
    #'title': '외모지상주의', 'star': '9.47' 이런식을 나오는것

#print(webtoon_list)
res=dict()
res['webtoons']=webtoon_list #'webtoons':'title': '외모지상주의', 'star': '9.47'
#print(res)

res_json=json.dumps(res,ensure_ascii=False)       #★★★★★★★★★★dump 안됨!!!! dsumps!!!꼭 s!!!
# print(res_json) 이렇게하면 위 결과들의 '' 가 ""로바뀜  ''->""

#마지막단계! 제이슨파일로 저장하여 생성하자 with open("파일이름.json","파일방식(w,r,..)",인코딩방식)as 변수이름인데 보통 f:변수이름.write(넣을제이슨데이터)
with open("webtoons.json","w",encoding="utf-8") as f:
    f.write(res_json)


```
### json dict타입 그림 (키:밸류)

![dict](https://www.json.org/img/object.png)


### json arry
![arry](https://www.json.org/img/array.png)
    

### json value
![value](https://www.json.org/img/value.png)

