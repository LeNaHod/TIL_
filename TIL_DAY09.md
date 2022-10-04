TIL DAY 09 (22_09_30)

한달 커리큘럼
html/css
javascript/jQuery
크롤링
django

-----------
# HTML에 대해 알아보자
HyperText Mark-up Language의 약자이다. 팀 버스너리경이 문서의 형태가 다양하기때문에 만들게되었다.
그외에도 WWW,URL,HTML등을 설계했다. 클라이언트가 리퀘스트(요청)하면, 서버가 만들어놓은 문서(HTML)를 Response(응답)한다.
온라인 상의 문서를 만들기 위해 **데이터를 구조화 시키는 언어**이다.

css: 구조화시킨언어(html)을 예쁘게 꾸미는것


- 간단한 작동방식을 보자 
http://127.0.0.1:5501/hello.html 
127.0.0.1:5501 이친구가 hello.html을 클라이언트가 요청하면 반환하는것이다.(ALT+L,O누르면 바로 켜진다)

## HTML의 구조

```

<!DOCTYPE html>
<html lang="en">
    <head> 주로 설정값이나 타이틀 설정을한다
        <title>hello</title>  타이틀과 값
    </head>
    <body>
      <p style="color:red;"> 속성
        hello,world 해당 요소의 내용
      </p>  
    </body>
</html>5

- 헤드안에 들어갈 수 있는것
<meta>: 문서의 기본 정보 등
<title>: 문서의 제목
<script>: javascript 등
<style>: css 등
<link>: 외부 문서 연결

```
-------

```
<body>
    <h1>block/linline</h1>
     <h2>블록요소</h2> 
     <p>줄바꿈</p>
     <div>
        블록 요소 안에 텍스트,<strong>인라인요소</strong>포함가능
        <p>블록요소안에 블록요소 포함가능</p>
     </div>  
     <h2>인라인 요소</h2>
     <a>줄바꿈 x</a>
     <q style="background-color: yellow;">인라인 요소안에 텍스트와  <b>인라인 요소</b>포함가능</q>
     <br>
     <span>인라인 요소 안에 <p>블록요소</p>포함불가</span>
      바로위의 내용은 사용은 가능하나 지양해야함
</body>

```
-----

```
</head>
<body>
    <h1>제목</h1>
    <h2>글자</h2>
    <h3>크기</h3>
    <h4>지정</h4>
    <h5>하는</h5>
    <h6>태그</h6> 
<hr>
     <div style="background-color:red;">영역을 정의</div>
     <div style="background-color: black; color:white;">
        <p>paragraph1</p>
        <p style="background-color: skyblue;">paragraph2</p>
    </div>
</body>
</html>

<hr>=수평선
<hn>류는 2,3, 4,5,6점점갈수록 작아진다. 6이 최대

```
----
```
<body>
    <h1>text</h1>
    <p>
        <b>진하게(b)</b>
        <br>
        <strong>강하게(strong)</strong>
        <br>
        <i>기울임(i)</i>
        <br>
        <em>강조하여(em)</em>
        <br>
        <samll>작은 텍스트, 코멘트(small)</samll>
        <br>
        위<sup>첨자</sup>(sup)
        <br>
        아래<sub>첨자</sub>
        <br>
        <ins>내용추가(ins)</ins>
        <br>
        <del>내용 삭제(del)</del>
    </p>
</body>

```

```
<body>
    <h1>&nbsp;&nbsp;&nbsp;&nbsp; &lt;a&gt;</h1>
    <a href="https://lc.multicampus.com/k-digital/#/feed">mlp</a>

    <a href="#a">1번으로</a>
    <br>
    <a href="#b">2번으로</a>
    <br>
    <a href="#c">3번으로</a>


    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <p id="a">1번</p>
    
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <p id="b">2번</p>

    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <p id="c">3번</p>

    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>

    
</body>
</html>

<!--&nbsp 공백-->
```
<details>
<summary>이하 코드 숨김</summary>

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>LIST</h1>
    <h2>순차적 목록</h2>
    <!--ordered list-->
    <ol>
            학원 오기까지의 순서
            <li>눈을 뜬다.</li>
            <li>옷을입고 운동한다.</li>
            <li>씻는다
                <ol>
                    <li>머리감고</li>
                    <li>샤워하고</li>
                    <li>양치하고</li>
                </ol>
            </li>    
            <li>옷입는다.</li>
            <li>출발한다.</li>
    </ol>
    <h2>비 순차적 목록</h2>
    <ul>
        점심메뉴 고르기
        <li>굶는다.</li>
        <li>계란</li>
        <li>커피</li>
        <li>편의점
            <ul>
                <li>삼각김밥</li>
                <li>샌드위치</li>
            </ul>
        </li>
        <li>음식점
            <ul>
                <li>한식</li>
                <li>중식</li>
                <li>양식</li>
            </ul>

        </li>

    </ul>
    <dl>
        <dt>
            학원 커리큘럼
        </dt>
        <dd>python</dd>
        <dd>database</dd>
        <dd>html cas js jq</dd>
        <dd>crawling</dd>
        <dd>django</dd>
        <dd>
            <dl>
                <dt>DS</dt>
                <dd>ml</dd>
                <dd>dl</dd>
            </dl>
            <dl>
                <dt>DE</dt>
                <dd>hadoop spark</dd>
            </dl>
        </dd>
    </dl>
</body>
</html>

<!--리스트목록을 생성함. ol type:"A"으로 abc가능 대문자여야함
ul을쓰면 비순차적으로 만들수있다. 그냥 li만써도 비순차적이되기도함
dl:d태그들의 블록같은느낌
dt:제목
dd:내용
-->

<body>
    <h1>table</h1>   <!--div사용권장-->

    <h2>기본 테이블</h2>

    <table border="1">
        <tr>
            <th>컬럼1</th>
            <th>컬럼2</th>
        </tr>
        <tr>
            <td>데이터1</td>
            <td>데이터2</td>
        </tr>
        <tr>
            <td>데이터3</td>
            <td>데이터4</td>
        </tr>
    </table>
    <h2>추가 태그</h2>
    <table border="1">
        <caption>테이블 제목</caption>
        <colgroup>
            <col width="100px">
            <col wirdth="200px">
            <col wirdth="300px">
        </colgroup>
        <thead>
            <tr>
                <th>컬럼1</th>
                <th>컬럼2</th>
                <th>컬럼3</th>
            </tr>
        </thead>

        <tfoot>
            <tr>
                <td>발1</td>
                <td>발2</td>
                <td>발3</td>
            </tr>
        </tfoot>
        <tbody>
            <tr>
                <td>1</td>
                <td>2</td>
                <td>3</td>
            </tr>
            <tr>
                <td>4</td>
                <td>5</td>
                <td>6</td>
            </tr>
            <tr>
                <td>7</td>
                <td>8</td>
                <td>9</td>
            </tr>
    </tbody>

    <h2>셀 병합</h2>
    <table border="1">
        <col wirdth="200px">
        <col wirdth="200px">
        <col wirdth="200px">
        <col wirdth="200px">
        
        <thad style ="background-color: white;">
            <tr>
                <th>컬럼1</th>
                <th>컬럼2</th>
                <th>컬럼3</th>
                <th>컬럼4</th>
            </tr>
        </thad>
        <tbody>
            <tr>
                <td rowspan="2">1(열 합치기)</td>
                <td>2</td>
                <td>3</td>
                <td>4</td>
            </tr>
            <tr>
                <td>6</td>
                <td colspan="2">7(행 합치기)</td>
            </tr>
            <tr>
                <td>9</td>
                <td>10</td>
                <td>11</td>
                <td>12</td>
            </tr>
            <tfoot> <!--foot써도되고 안써도되고-->
                <tr> 
                    <td colspan="4">13 행합치기</td>
                </tr>
            </tfoot>
            <tr>
                <td rowspan="2">14<br>열합치기</td>
            </tr>
        </tbody> 
    </table>
</body>
</html>

<!---
th:표의 제목.헤드의 약자(컬럼)
td:실제 안에 들어갈값
tr:셀을 만들어주는역할(왼쪽정렬)
thead :테이블머리
tbody:몸통부분
tfoot :밑에 놓음
다만, foot,head는 한번씩만와야하고 body는 여러번. 또, foot->head순서바뀌어도 알아서 정렬이된다.
rowspan:세로합치기
colspan:가로합치기
-->

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        *{
            padding :0px;
            margin : 0px;
        }
        div{
            border : 1px dashed blue;
            margin : 10px;
        }
        #body { height: 400px;} 
        #left{ width:48%; height: 90%;float:left;}
        #right{width:48%; height: 90%;float:right;}
    </style>
<!---바디라는 큰 네모안에 오른쪽,왼쪽 또 나눔--->
</head>
<body>
   <div id="header">
        <h1>제목</h1>
        <div>
            <span><a href="#">메뉴1</a></span>
            <span><a href="#">메뉴2</a></span>
            <span><a href="#">메뉴3</a></span>
            <span><a href="#">메뉴4</a></span>
        </div>
   </div>
   <div id="body">
        <div id="left">
            <p>내용1</p>
        </div>
        <div id="right">
            <p>내용2</p>
        </div>
   </div>

   <div id="footer">
        <address>copyright &copy; all rights re..</address>
   </div>
</body>


<!DOCTYPE html>
<html lang="en">
    <header class="html5">
        <h1>제목</h1>
        <nav class="html5">
            <span><a href="#">메뉴1</a></span>
            <span><a href="#">메뉴2</a></span>
            <span><a href="#">메뉴3</a></span>
            <span><a href="#">메뉴4</a></span>
        </nav>

        <style>
            .html5{    
                border : 1px dotted red;
                margin : 10px;
            }
            #left{ width:48%; height: 90%;float:left;}
            #right{width:48%; height: 90%;float:right;}
            section{height : 400px;}
        </style>
    <!--.*{} ->html5 / body -> section-->
    </header>
    <section class="html5">
        <article class="html5" id="left">
            <p>내용1</p>
        </article>
        <article class="html5" id="right">
            <p>내용2</p>
        </article>
    </section>
    <footer class="html5">
        <address>copyright &copy;all rights re...</address>
    </footer>
<body>

</body>
    
</html>

<!--
sementic =div랑 똑같이나옴. 어떤태그들이있냐면 아래와같다.
위에서쓸때 :haeder
nav:다른 페이지 또는 현재 페이지의 다른 부분과 연결되는 
네비게이션 링크(navigation links)들의 집합을 정의한다.
<nav> 요소를 사용하는 일반적인 예로는 메뉴, 목차, 인덱스 등, 메뉴류
<a href="" 이부분이 nav
바디:section
밑에:footer
쓰는이유는 가독성이 더 좋고 편리하기때문이다.
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script>
        onload=function(){alert(location.search);}
    </script>
</head>
<body>
    <form action="html-form-res.html" method="get">
        <fieldset>
            <legend>회원가입</legend>
            <p>ID: <input type="text" name="id"></p>
            <p>PW: <input type="password" name="pw"></p>
            <p>email 수신여부 <br>
                <lable for="yesb"></lable>
                <input type="radio" name="rdo" value="y" id="yesb">yes<br>
                <input type="radio" name="rdo" value="n">no
            </p>
            <p>관심분야<br>
                <input type="checkbox" name="python" value="python">PYTHON<br>
                <input type="checkbox" name="web" value="web">WEB<br>
                <input type="checkbox" name="database" value="database">DATABASE 
            </p> 
            <p>
                하고싶은 말<br>
                <textarea name="etc" col="30" rows="10"></textarea>
            </p>
            <p>
                <input type="button" value="그냥버튼">
                <input type="reset" value="리셋버튼">
                <input type="submit" value="전송버튼">
            </p>
            
        </fieldset>

    </form>
</body>
</html>
<!--
name을 똑같이  지정해놓으면 버튼 중복선택을 막을 수 있다
input type="checkbox" name="python" value="python" =버튼이라 내가 밸류값을준거고
input type="text" name="id" 버튼이아니므로 입력받을수있으니까. 밸류값이 내가쓴값으로나옴
textarea
rows:텍스트 입력 영역 중 보이는 영역의 라인수를 명시함.
col:텍스트 입력 영역 중 보이는 영역의 너비를 명시함.
-->

```
</details>

### Form
**form은 유일한 post전송방식이다.(get도있다.)**
구조는 아래와 같다

form 
action ='경로' 
method='전송방식'
input type=‘형태’ name=‘name’ value=‘value’ 
input type=‘submit’ value=‘전송’
(input은 라디오박스 리스트박스 체크박스 기타등등에 쓸때 submit은 전송버튼(get,post))

전송방식은 두개가있는데

- GET/POST
    - GET=리퀘스트의 헤더에 데이터를 넣어보냄
    - POST=리퀘스트의 바디에 데이터를 넣어보냄

get으로받으면 주소밑에 ?뒤에
키:밸류&키:밸류&키:밸류 형식으로 정보가 붙어서나온다.

↓↓↓↓↓↓↓↓

http://127.0.0.1:5501/web01-html/html-form-res.html?id=12&pw=112&rdo=y&python=python&etc=asd

- 주용도
  - get 셀렉트 (가지고오는거)

  - post insert 추가    

  - put 업데이트

  - delte 삭제

즉 post방식은,데이터를 같이 보내고싶을때 ,get보다 보안성을 조금 더 챙기고싶을때 = post방식

- input의 속성
    - text 일반 텍스트를 입력받을 수 있습니다.
    - password 패스워드를 입력받을 수 있도록, 입력값이 화면에 보여지지 않도록 합니다.
    - submit <form> 태그 내에 입력된 데이터를 서버로 전달해 줍니다.
    - button 버튼을 생성해 줍니다.
    - checkbox 체크박스 형태의 입력을 받을 수 있습니다.
    - radio 라디오 버튼 형태의 입력을 받을 수 있습니다.
    - reset <form> 태그 안의 사용자 입력을 초기화 합니다

### style태그의 margin이해
 
![margin이해](https://dasima.xyz/wp-content/uploads/2019/12/css-box-model-box-sizing.png)


## 태그정리, 간단 이해도와 개념
br =엔터

div = 영역을 정의한다. 화면을 네모로 나눈다고 생각하면된다.

★a = 입력된 값만큼만 차지함. 하이퍼링크 관련으로 자주씀. a href="링크주소" 걍세트로외우기.

p = 문단을 정의함. 하나의문단을 만들때 사용한닥 생각하면됨. paragraph의 약자

q = 입력된 영역만큼 차지함

area download = “파일 이름”
download 속성은 사용자가 하이퍼링크를 클릭할 때 해당 대상(target)로 연결되지 않고 대신 해당 콘텐츠가 다운로드됨을 명시합니다.
이 속성은 반드시 href 속성이 설정되어야만 사용할 수 있다.
download 속성의 속성값은 다운로드되는 파일의 이름이 되며, 그 값에 특별한 제약X, 브라우저는 다운로드되는 파일의 정확한 확장자명을 확인하여, 자동으로 파일 이름 끝에 축하ㅏㄴ다. (.html, .pdf, .jpg 등)
만약 download 속성의 속성값을 생략하면 다운로드되는 파일의 원래이름을 사용한다.

coords : area 태그의 coords 속성은 이미지맵(image-map)에서 해당 area 요소의 좌표를 명시한다.
coords 속성은 해당  area 요소의 크기와 모양, 배치 등을 명시하기 위하여 shape 속성과 함께 사용되며, 이때 해당 영역의 왼쪽 위 모서리(top-left corner)의 좌표는 언제나 (0,0)이 된다.


index.html = welcome file

web접근성 :strong,em..등등

/ : 루트(제일최상위로)
./ : 현재
../ : 상위
아무것도안쓰면 ./라고 간주함