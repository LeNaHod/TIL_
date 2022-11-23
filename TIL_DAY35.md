# TIL DAY 35(2022-11-22~)

## PROJECT2 TEST 
(비정기업데이트)

BeautifulSoup 를 사용하는이유

크롤링, 스크래핑 등에 필요하다. request.txt를 통해 가져온데이터는 **텍스트형태의 html**이기때문에
html태그를 조작하기어렵다. 그 조작을 하기위해 수프객체로 바꿔사용한다.

```python
import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint
import json

#===서비스 key, url 모음======
#url+'?'+serviceKey&numOfRows(출력행갯수)=n&pageNo(페이지갯수)=n
#curl -X GET http://api.kcisa.kr/openapi/service/rest/meta4/getKCPG0506?serviceKey=yourkey&numOfRows=n&pageNo=n -H accept:application/json
#============================
key='yourservicekey'
ROWS=1
#PAGE=2
book_list=list()
#url = f'http://api.kcisa.kr/openapi/service/rest/meta4/getKCPG0506?serviceKey={key}&numOfRows={ROWS}&pageNo={PAGE}'
for books in range(120):
    PAGE=1
    if books <= 200:
        PAGE=PAGE+books
        url = f'http://api.kcisa.kr/openapi/service/rest/meta4/getKCPG0506?serviceKey={key}&numOfRows={books}&pageNo={PAGE}'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser").title #타이틀 태그만 뽑아진다. .body면 바디태그만 뽑아진다.  원하는 html태그를 쉽게 추출할수있다.
        book_list=soup

    print(PAGE)
print(type(soup)) #뷰티풀수프 객체를 반환한다. 수프객체는 html을 수프로만들어주고 각 태그조작을 쉽게해줌


# 기본사용법

1.request와 BeautifulSoup import

2. url 생성에 필요한 변수,값들 설정하고  url생성

mykey=servicekey
row=1
page=1

url = 'http://aaaaabbbdd/dda/?servicekey=mykey~~'

3. request로 데이터 받아오기

#resp는 respans의 약자
resp=request.get(url)  #GET 방식: .get() ,POST 방식: .post(),PUT 방식:.put(),DELETE 방식: .delete

print(resp.status_code) #응답 상태코드를 출력한다.

resp.text #텍스트 형태의 html로 반환한다.(utf-8인코딩)
resp.content #바이너리 원문을 반환한다.
★resp.json() #응답데이터가 json포맷이면 .json()으로 딕트객체반환.

보통 soup의 parser와 한번에씀.

4.수프객체로반환하고 파싱하기
soup=BeautifulSoup(resp.json()|.content | .text, 'html.parser |xml.parser')
->resp에서 반환한걸 html구조로 탐색,분석한다. 즉 html구조에서 파싱하기위해 사용.
=>맨끝에.태그 를붙이면 BeautifulSoup 객체에서 명시한 태그만 추출해서 가져오게되는 구조이다.

parsing =분석or탐색 / html을 분석한다, xml탐색한다


#자바스크립트로도 가져올수있다.
   <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script> 
    <script>
        onload=()=>{
            key='yourkey';
            ROWS=1;
            PAGE=10;
            target_url='http://api.kcisa.kr/openapi/service/rest/meta4/getKCPG0506?serviceKey='+key+'&numOfRows='+ROWS+'&pageNo='+PAGE;
            btns=document.querySelectorAll("button");
            btns[0].addEventListener('click',()=>{
                axios({
                    method:"get",
                    url:target_url
                }).then(function(resp){ 
                    alert(JSON.stringify(resp));
```








