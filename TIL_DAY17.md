# TIL DAY 17(22_10_17)

## TIP

### 크롤링 전 알아야할것!

웹페이지/robots.txt 를쳐서 allow(크롤링 가능한거) disallow(크롤링하면안되는거) 를 구분해서
가져오자.

★개발자 도구 열어놓은상태에서 새로고침 오른쪽클릭하면 캐시비우기가있다.★

### 페이지값을 받는 URL을 만들어보자

     - EX)
       공공데이터포털에서 url을 가져와서 
        ?키=밸류&키=밸류 로만 구분하고 밸류값이없는친구들은 다 삭제후, 필요한것만 남김(아래는필요한것도첨삭함)
        완성형:
            https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=교육&currentPage=2 


### Ajax ->jQuery

- 스타벅스 홈페이지에서 매장데이터(지역/구군 별 매장위치와 이름 등 데이터)를 가져오는 코드를분석
 
        -jQuery :
            = $.ajax{
	                url:./store~
	                ?:{}
                    async:true ->비동기로 작동, false면 동기로 작동
                    json=dataType. json타입으로 받는다.
                    post=mothod:post
                    성공시 function(_response)..실행}
        -원본코드 :
            __ajaxCall("/store/getSidoList.do", {}, true, "json", "post",
					    function (_response) {}~
        
- 그래서 우리가 가져올건 : **endpoint 부분 +url**이니까
  
                (endpoint)+url
        https://www.starbucks.co.kr/store/getSidoList.do 

- 지역 매장데이터 이름과 도로명주소를가져올때, 필요없는 데이터를지우고, 최소 데이터만 남길 수 있다.
     
    EX)

        in_biz_cds=0&in_scodes=0&ins_lat=37.4494699&ins_lng=126.9057288&search_text=&p_sido_cd=01&p_gugun_cd=0101&in_distance=0&in_biz_cd=&isError=true&iend=100&searchType=C&set_date=&all_store=0&T03=0&T01=0&T27=0&T12=0&T09=0&T30=0&T05=0&T22=0&T21=0&T10=0&T36=0&T43=0&T48=0&P10=0&P50=0&P20=0&P60=0&P30=0&P70=0&P40=0&P80=0&whcroad_yn=0&P90=0&new_bool=0&rndCod=F7H1GNLCI4
        
        ↓↓↓↓↓

        ins_lat=37.4494699
        ins_lng=126.9057288
        p_sido_cd=01
        p_gugun_cd=0101
        in_biz_cd=
        set_date=

        이 최소한의 데이터를가지고, request.post/get(url,data={"키":밸류 | "밸류"})형식으로 넣어서 원하는 데이터를 추출할수있다.
        __ajaxCall( storeInterfaceUrl ,$search, true, "json", "post", 의  $search가 저 최소데이터이기도함


## 실습 코드와 주석풀이

```python

01.페이지 단위로 가져오고 싶은 태그만 추출해보자. 리스트로도 해보고 그냥도 해보고.

#1에서 마지막페이지 번호를 가져와서 끝페이지까지 가져올수도있다

import requests
from bs4 import BeautifulSoup #객체화모듈

url="https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode="
resp=requests.get(url)
soup=BeautifulSoup(resp.text,"html.parser") #지금의 url데이터는 txt이므로,객체화작업
paging=soup.find("nav",class_="pagination")

#ver1
# paingnum=paging.find_all("a")[2:11]
# onepage = paging.find("strong", class_="active").text #find_all은 .text X
# print(onepage)
# for i in paingnum:
#     print(f'pagenum:{i.text}')


#ver2

#여러줄로 코딩
# nums=list() #nums를 빈 list로만듦 그리고 그안에 paging을 넣을거임
# for page in paging:   #반복할거다
#     if page.text.isdigit(): #text를(=<a>12</a>면 12만가져와짐)가져와서 숫자인지 판단
#         nums.append(page.text) #숫자면 nums에추가한다
# print(nums)

#.text 와 .string  
#ex) <a>aaa</a>
#    <p></p>
#    <b><p>ddd</p></b>
#    <td>abc<b>defg</b></td> 

#.text: 하위 자식태그의 텍스트까지 문자열로 반환. 결과값:aaa ddd acbdefg
#.string:.string 태그 하위에 문자열을 객체화. 문자열이 없으면 None 을 반환. 결과값:aaa None ddd None.

#한줄로 바꾸기
nums= list(filter(None,map(lambda x: x.text if x.text.isdigit() else None, paging)))
# print(nums)

#내가원하는페이지(i)의 내용들만 가져오기 (기본)
# for i in nums:
#     sub_url=f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=교육&currentPage={i}"
#     print(sub_url)

#★내가원하는페이지(현재1-10)까지의 제목만 가져오기★
for i in nums:
    sub_url=f"https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=교육&currentPage={i}"
    sub_soup = BeautifulSoup(requests.get(sub_url).text, "html.parser")
    titles = sub_soup.select("span[class=title]")#select()선택한태그들을 모두선택.find보다 오차가 좀 높음. 클래스네임이 title인 span태그를 선택해서 내용가져옴
    for title in titles:
        print(title.text.strip())

#특정문자를 제거하기. 문자열 생략시 ★공백제거★
#strip(문자열[생략가능]) :인자로 전달된 문자를 string의 양쪽에서 제거. 
#lstrip(문자열[생략가능]):인자로 전달된 문자를 string의 왼쪽에서 제거.
#rstrip(문자열[생략가능]):인자로 전달된 문자를 string의 오른쪽에서 제거.


#extract()와 decompose()
#decompose():태그를 트리에서 제거하고, 내용물 완전없앰.그래서 결과를 리턴할때 지정한태그는 추출X.None를 리턴함
#extract():실행시에만 1회성으로 태그를 제거하고 결과를 리턴. 제거된 태그를 리턴함. 라스트의.pop와 비슷하다.
#자식태그를 제외하고 부모태그만 사용하고싶을때 주로 사용.
#즉 for문을돌렸을시 똑같은 단어가  11라인과 12라인에 출력된다면, decompose()이친구는 영영안나오고 extract()다음에나옴

02.인스타 이미지를 추출

import requests
from bs4 import BeautifulSoup

#셀레니움=웹자동화해주는친구. 근데 봇은 못뚫음

#ver1
# url="https://www.instagram.com/explore/tags/python/"
# resp=requests.get(url)
# soup = BeautifulSoup(resp.text,"html.parser")
# imgs=soup.find("div",class_="_aagv")
# print(imgs)

#ver2
tag=input("search tags :")  #input태그로 tag를 입력받음 그럼 url태그자리에 내가입력한게들어감 =내가 찾고싶은게시물을 찾을수잇음 ex)python,food등
url=f'https://www.instagram.com/explore/tags{tag}' #붕어빵으로치면,팥=데이터,밀가루=틀. 그래서 url만가져오면 밀가루빵만가져오는거고
                                            #팥은 클라이언트(지금의 우리)가 넣고싶은만큼,원하는종류(원하는데이터를 원하는만큼)넣는다.
#이부분이 팥넣는과정                                         
resp=requests.get(url)
soup = BeautifulSoup(resp.text,"html.parser")
divs=soup.find("div",class_="_aagv")['img']
print(divs)

03.셀레니움을 이용해서 인스타에서 이미지 src를 추출해보자.

#셀레니움을 사용해보자. Hard Coded Location
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

tag=input("search tags :")
url=f"https://www.instagram.com/explore/tags/{tag}"

driver.get(url)

sleep(3) #창이 로딩이된다음에 코드를 실행해야하므로, 로딩후 3초후에 실행

soup=BeautifulSoup(driver.page_source,"html.parser")
divs=soup.find_all("div",class_="_aagv")

for img in divs:
    print(img.find('img')['src'])  #img태그의 src를 가져와서 실행창에뜬다.

driver.close()

04.아이디,비밀번호창을 선택해서 값을 자동으로 입력하게해보자

#로그인하는 매크로. 선택에 의의를 두는거니까 페이지내에서 링크를 클릭해 다른곳을 넘어갈 수 있다.

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

input_id=input('id 입력:')
input_pwd=input('pwd 입력:')

service=Service('./chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get("https://www.instagram.com/")

sleep(3) #sleep주는이유는 화면이 그려진다음에 입력해야하는데 컴퓨터가 느려서 그려지기까지의 시간이걸리기때문에 이후에 입력하라고 3초지연시간줌
id=driver.find_element(By.NAME,'username') #이름이 유저네임인 객체하나를가져온다. by사용시 위에처럼 import필수
id.send_keys(input_id) #input_id의값을 진짜로 입력해줌

pw=driver.find_element(By.NAME,"password") #이름이 password인 객체를 가져온다.
pw.send_keys(input_pwd)

sleep(3)
#ver1
# driver.find_element(By.CSS_SELECTOR,"#loginForm > div > div:nth-child(3)").click()

#ver2
driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click() 
            #파일의 위치 경로복사같은것 = ↑↑↑XPATH 


```