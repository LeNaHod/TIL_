TIL DAY 12 (22_10_07)

# 자바스크립트2일차

## 목차
    1. 날짜
    2. 배열
    3. 팝업
    4. 윈도우/팝업창과 회원가입 페이지
    5. location
   

### 개념정리

- new date() 로 타입변환도할수있고 시간을 가져올수도있다.
- option을 써도된다.이런식으로 / const options={weekday : "long",year:"numeric",month:"short",day:"numeric"}
  (weekday:short or long/month:short or long) 자세한건 코드참조.
- month를 가져올때 +1 넣을땐 -1
- ★reload->새로고침 =클라이언트가 서버에게 리퀘스트(요청)을 다시보내서 다시응답받아 브라우저가 그림을 다시그렸다.
- ★//  '\' + id + '\' = 안에들어가는 값이 변수가아니라 문자임을 알려주려고.
- sort:정렬. sort정렬은 오름 내림 등으로 정렬하려면 기준을 줘야하는데 보통 오름차순:a-b 이고 내림차순:b-a 이다.
음수값이면 오름. 양수값이면 내림 0이면 그대로. 라고 생각할 수 있는데,

```CS
function compare(a,b){
    if(a is less than b by some ordering criterion){
        return -1;
    }

    if(a is greater than b by some ordering criterion){
        return 1;
    }
   # a must be equal to b
    return 0;
}
  
```

위와 같은 구조라고 생각 할 수있다. 즉 a-b를 본다면 두개의값을 가져와서 비교하여 결과값이 음수이면 그자리 그대로냅두고 만약 양수를 반환한다면 두 숫자의 자리를 바꿔 작은쪽이 오른쪽으로가게 정렬한다. 자세한건 코드를 보자

###  코드첨부
1. 날짜
 
```HTML
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script>
        onload=function(){ //괄호안을 제일 나중에 실행해라. 밑에 동작 다하고 여기로 올라옴.
        document.getElementsByTagName("button")[0].onclick=testDate01;
        document.getElementsByTagName("button")[1].onclick=testDate02; 
        document.getElementsByTagName("button")[2].onclick=testDate03; 
        document.getElementsByTagName("button")[3].onclick=testDate04;
        document.getElementsByTagName("button")[4].onclick=testDate05; 
        }//콜백:부르면(요청)그때 대답해주는 함수. =이벤트가 발생했을때실행
        function testDate01(){
            var inputDate = document.getElementById("today");
            var date = new Date();

            inputDate.innerHTML = date.toDateString()+"<br>";
            inputDate.innerHTML += date.toLocaleDateString()+"<br>";
            inputDate.innerHTML += date.toLocaleString()+"<br>";
            inputDate.innerHTML += date.toLocaleTimeString()+"<br>";
        }
        function testDate02(){
            //"2022/10/7/금"
            var dayOfWeek=["일","월","화","수","목","금","토"];
            var date= new Date(); //오늘 날짜를 date에 담음
            var year=date.getFullYear();//date.getFullyear=년도4자리를 변수 year에담음
            var month=date.getMonth()+1;//0부터시작해서 +1
            var day=date.getDate();
            var week=date.getDay();
            const options={weekday : "long",year:"numeric",month:"short",day:"numeric"}
            //weekday:short or long/month:short or long
            document.getElementById("today").innerHTML=year+"/"+ "/"+day+"/"+dayOfWeek[week];
            document.getElementById("today").innerHTML=date.toLocaleDateString("en-us",options);

        }
        function testDate03(){
            var year=2023;
            var month=1;
            var day=27;
            var end = new Date(year,month-1,day); //날짜를 '가져올때는+1', '넣을때는 -1' end 에 날짜 이어 먼스 데이를 넣음
            document.getElementById("sp").innerHTML=end;

        }
        function testDate04(){
          var dates=document.getElementById("dates").value; //해당 리턴날짜
         
          var inputDate=document.getElementById("inputDate").value;//인풋타입에서 밸류를가져오면 다 '문자'임.
          var date= new Date(dates);
          date.setDate(date.getDate()+inputDate);
          document.getElementById("result").value=date.toLocaleDateString();
            //변수명=new date(변수나 변환할것 아니면빈값)/array(..) 은 새로생성해서 변수명에넣어주거나, 타입을 변환해준다.
        }

        function testDate05(){
            
            var start=document.getElementById("a").value;
            var end=document.getElementById("b").value;
            var startDate= new Date(start);
            var endDate= new Date(end);
            var todayd=(endDate.getTime()-startDate.getTime())/(1000*60*60*24); //밀리초로 반환하니까. 1000해서 분,60해서 시간,24해서 '일'로
            document.getElementById("c").value=todayd;

        }
    </script>
</head>
<body>
    <h1>오늘 날짜 출력하기 </h1>
    <span id="today"></span>
    <br>
    <button>오늘날짜</button>
    <button>오늘 날짜(표현)</button>
    <h1>특정 날짜출력하기</h1>
    <span id="sp"></span>
    <button>특정날짜</button>
    <br>

    <h1>경과 날짜 구하기</h1>
    <label>지정날짜</label>
    <input type="date" id ="dates"> <!--date 형식이면 누르면 달력이나옴-->
    <br>
    <lable>경과일</lable>
    <input type="number" id ="inputDate">
    <br>
    <lable>경과 후 날짜</lable>
    <input type="text" id = "result" readonly>
    <button>경과날짜</button>

    <h1>D-day기능 만들기</h1>
    <label>시작날짜</label>
    <br>
    <input type="date" id="a">
    <br>
    <label>종료날짜</label>
    <br>
    <input type="date" id="b">
    <br>
    <label>남은 일수</label>
    <input type="text" id ="c" readonly>
    <button>남은 일수 구하기</button>
    <!-- getTime() 무조건 사용하기!-->

</body>

```
2. ★배열

```HTML
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script>
        //배열선언.새로운 어레이 객체 arrayObj를 생성
        var arrayObj=new Array();
        //(n)=길이지정. 값이없고 다섯칸이있음
        var arrayObj2=new Array(5);
        // 초기값을 정의한 선언
        var arrayObj3=new Array(1,2,3,4,5);
        //var arrayVal=["v","v1","v2","v3"]; 이런방식으로 해도 배열객체가 생성된다.

        function multiArr(){ //총9개의 칸이생김 큰세개짜리를 다시 세개로쪼개서 3*3
            var len=3;
            var arr=new Array(len);
            for (var i =0; i<arr.length; i++){
                arr[i]=new Array(len);
            }
            arr[0][0]="사과";
            arr[0][1]="바나나";
            arr[0][2]="딸기";
            arr[1][0]=1;
            arr[1][1]=2;
            arr[1][2]=3;
            arr[2][0]=["test","js"];
            arr[2][1]=["java","script"];
            arr[2][2]=["de","ds"];

            //  alert(arr);
            //  alert(arr.toString());
            //console.long(arr);
            alert(arr[2][0][1]);
        }
        function joinTest(){
            var nums =["1","2","3"];  //1+2+3=6출력.
            var res=nums.join("+"); // join("문자")는 nums요소 사이사이에 문자를넣어서 문장을만들어줌
            alert(res+"="+eval(res)); //eval은 문자열 식을 반환한다.

        }
        function sortTest01(){
            var arr=["a","c","d","b"];
            arr.sort();
            alert(arr);

        }
        function sortTest02(){ //아스키 코드 기준으로 정렬한다.(눈으로보기엔 첫글자기준같아보임)
            var arr=[1,3,2,11,23,41,100]; 
            arr.sort(compareNum);
            alert(arr);   
        }
        function compareNum(a,b){ //파라미터로 a와b를받음
            return a-b;         //a-b=양수:자리를바꿈 a와b의자리를.그럼 b가 앞으로가게됨.
                                //a-b=음수:자리를안바꿈.어차피 작은값이 앞에있으니까.
                                //0이면 냅둠. 그래서 a-b=는 오름차순. b-a=내림차순이된다.(b가큰값)
        }
        function reverseTest(){
            var arr=[1,3,2,11,23,200,41,100]; //desc가아니라 그냥 역방향으로 출력.
          //  arr.reverse();
          //  alert(arr);
            arr.sort(function(a,b){return b-a;}); //얘는 내림차순.리버스와 다름.
            alert(arr);
        }
        function psuhandshift(){
            //queue. 이벤트가 전파가된다. pop/shift를눌러도 출력이된다.
            var  queue = new Array();  //queue =물컵같은느낌이다.1,2,3이렇게 위로 쌓여잇다.
            queue.push("first");  //배열에 값추가.
            queue.push("s");
            queue.push("t");
            
          // alert(queue);

        //  var a =queue.pop(); //queue의 맨끝에있는t를 a안에 잘라내서 넣는다.그럼2번째자리는없어지게된다.
       //   alert(queue);
         // alert(a);

         var b =queue.shift(); //pop반대. 첫번째잇는값을 잘라내서 b에넣는다.그럼한칸씩밀려서 s가 0번째됨
         alert(queue);
         alert(b);
        }
        function sliceTets(){
            var arrayOriginal01=new Array(1,2,3,4,5,6,7);
            var arraySlice01=arrayOriginal01.slice(1,3); //1번지부터3번지전까지 자름.즉2,3이나옴
           // alert(arraySlice01); 

           var arrayOriginal02=new Array(4); //아래로 4칸짜리
           arrayOriginal02[0]=new Array(1,2); //가로로 두칸짜리 총 8칸짜리
           arrayOriginal02[1]=new Array(3,4);
           arrayOriginal02[2]=new Array(5,6);
           arrayOriginal02[3]=new Array(7,8);

           var arraySlice02=arrayOriginal02.slice(1,3); //오리지널과슬라이스는 같은 주소를 참조한다.
           //alert(arraySlice02);
           arraySlice02[0][0]=33;
           alert(arrayOriginal02);
           //즉 메모리상의 주소는 같고 슬라이스로 잘라서 보이는것만다를뿐이지. 메모리에 저장은 그대로되어잇다.

        }

    </script>
</head>
<body>
    <h1>배열 객체</h1> <!--파이썬의 리스트객체와비슷-->
    <ul>
        <li onclick="multiArr();">다중 배열</li>
        <li onclick="joinTest();">join함수</li>
        <li>
            배열정렬
            <ul>
                <li onclick="sortTest01();">sort()</li> <!--sort=배열정렬. sort(오름,내림,문자열,객체)-->
                <li onclick="sortTest02();">sort()</li>
                <li onclick="reverseTest();">reverse()</li>
            </ul>
        </li>
        <li onclick="psuhandshift();">
            배열저장방식
            <ul>
                <li>push()</li>
                <li>pop()</li>
                <li>shift()</li>
            </ul>
        </li>
        <li onclick="sliceTets();">배열 부분을가지고 새로울 부분배열 생성</li>
    </ul>
</body>

```
3. 팝업창

```HTML
팝업
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>
        function popUp(){//window.open 오픈한다 js12-pop~을 
            window.open("js12-popup-res.html","","");    
        }
    </script>
</head>
<body>
    <button onclick="popUp();">눌러</button>
</body>

팝업-레스

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    화이팅!
</body>

```
4. 윈도우

```HTML

1. 윈도우 메인페이지(회원가입과 팝업창이있다.)

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style type="text/css">
        #regist { /*회원가입 폼 스타일 */
            border: 1px solid black;
            background: pink;
            position: absolute;
            top: 200px;
            left: 500px;
            display: none; /*none으로 보이지않음 자리차지x*/
        }
    </style>
    
    <!-- 
        display : none;			//공간을 차지하지 않는다 (만들어지지 않은 상태)
        visibility: hidden;		//공간을 차지하고, 보이지 않는다 (만들어져 있는 상태)
     -->
    
    <script type="text/javascript">
        function openWin() { //팝업창의 버튼을 눌렀을시 실행
            var url = "js13-window-popup.html";
            var title = "myframe";
            var prop = "top=200px,left=600px,width=500px,height=500px";
            window.open(url, title, prop);
        }
    
        function registForm() {//회원가입 버튼을 눌렀을때 동작되는 함수.
            document.getElementById("regist").style.display = "block";//원래는 가로한줄을 다차지하는데 포지션때문에 다차지안하는거같음
            document.body.style.background = "gray";
    
            var btns = document.getElementsByName("btn");
            for ( var i in btns) {
                btns[i].disabled = "disabled"; //다른버튼 비활성화
            }
        }
    
        function closeWin() { //닫는폼
            document.getElementById("regist").style.display = "none";
            document.body.style.background = "white";
    
            var btns = document.getElementsByName("btn");
            for ( var i in btns) {
                btns[i].disabled = ""; //팝업창을 닫으면 버튼들을 활성화시킴
            }
        }
    
        function idchk() {
            alert("중복체크를 확인하세요"); //아이디창을누르면 alert
        }
    
        function idCheck() {
            open("js13-window-id-check.html", "", "width=300px,height=300px");
        }	//중복체크버튼을누르면 id-check html을 팝업창으로 불러오는데 300x300
    </script>
    
    
</head>
<body>
    
    <h1>window객체</h1>
	
	<pre>
	프로퍼티
	 -document
	 -history
	 -location
	 -navigator
	 -screen
	 -frames
	 -parent
	 -top
	 -self
	메서드
	 -alert()
	 -confirm()
	 -prompt()
	 -back()
	 -forward()
	 -setInterval()
	 -clearInterval()
	 -setTimeout()
	 -open()
	 -close()
	 -scroll(),scrollBy(), scrollTo() 
	</pre>

    
	<div id="f1">
		<h1>팝업창 만들기</h1>
		<button onclick="openWin()" name="btn">창열기</button>
		<hr>
		<h1>회원가입하기(div팝업창)</h1>
		<button onclick="registForm()" name="btn">회원가입</button>
	</div>

	<div id="regist"> <!--회원가입폼뜨는거-->
		<form>
			<table>
				<caption>회원가입</caption>
				<tr>
					<td>아이디</td><!--읽기전용으로 열어서 입력,수정x.복사o.서버에 제출.-->
					<td><input type="text" name="id" onclick="idchk()" readonly="readonly" /> <!--누르면중복체크호출-->
					<input type="button" value="중복체크" onclick="idCheck()" /></td><!--중복체크창띄움(버튼)-->
				</tr>
				<tr>
					<td>패스워드</td>
					<td><input type="password" name="pwd" alt="" style="color: red;" checked="checked" /></td>
				</tr><!--alt:이미지대체텍스트--><!--checked="checked":체크버튼류가없어서 의미없다생각.-->
				<tr>
					<td colspan="2" align="center"><input type="button" value="확인" onclick="closeWin()" /></td>
				</tr><!--colspan:컬럼두개합침 align=center 버튼을 중앙으로. 없애거나 text-align쓰면 버튼이 왼쪽으로붙음-->
			</table>
		</form>
	</div>

	<br/><br/><br/>
	<iframe name="myframe"></iframe>

<!--★중요!! Iframe은 되도록 안쓰는게 좋다. 크롤링할때도 불편하고 요즘 트렌트에 안맞아서-->


</body>

2. 아이디 중복확인 페이지

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
    <script type="text/javascript">
        var ids=["multi","java","script"]; //이미 만들어져있는 아이디들 중복일시 아래 아이디가존재합니다 출력
        
        function confirmChk(){
            var id=document.getElementsByName("id")[0].value;
            var div=document.getElementsByTagName("div")[0];
            if(ids.indexOf(id)!=-1){ //ids의 목록과 입력받은 id를비교해서 겹치면 아이디가 존재합니다.(안겹치면 -1인데 -1이아니면=겹친다)
                div.innerHTML="<b>아이디가 존재합니다.</b>";
            }else{
                var userId="사용할 수 있는 아이디입니다."
                        +"<input type='button' value='확인'" //버튼생성
                        +"onclick='insertId(\""+id+"\")'>";  //확인을누르면 id에 입력한아이디를넣어서
                div.innerHTML=userId;     
                //  '\'  id '\' = 안에들어가는 값이 변수가아니라 문자임을 알려주려고.
                // 없이쓰면 insertId(ads)가되고 있으면insertId('ads')가되서 문자열 값ads를 정상적으로 뿌려줄수있게된다.
            }
        }
        
        function insertId(id){
            opener.document.getElementsByName("id")[0].value=id;
            opener.document.getElementsByName("pwd")[0].focus();
            close();
        }
    </script>

</head>
<body>
    
	<table>
		<tr>
			<td>아이디</td>
			<td><input type="text" name="id"/></td>
		</tr>
		<tr>
			<td colspan="2">
				<input type="button" value="중복확인" onclick="confirmChk()"/>
				<input type="button" value="취소" onclick="self.close()"/> <!--윈도우의 close()를불러오는듯..한..데?-->
			</td>               <!--셀프.클로즈=본인...?창을닫는다-->
		</tr>
	</table>
	<div></div>

</body>

3.팝업페이지

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script type="text/javascript">
        function test(){
            var val=document.getElementsByName("test")[0].value; //자식창
            opener.document.getElementsByTagName("h1")[1].innerHTML=val; //인덱스1번째h1에 test창에서 입력한 값을 반영
            close();
        }
    </script>
    
</head>
<body>

	<input type="text" name="test"/><!--부모창-->
	<input type="button" onclick="test()" value="전달"/>
	<input type="button" onclick="self.close()" value="창닫기"> <!--window.opener.close() 이렇게쓰면 부모창이꺼진다-->


</body>

```
5. loction(로케이션)

```HTML

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
        <script>
            function locTest(){
              //  location.reload(); 
               // location.href="https://www.naver.com"; //href=링크
                location.assign("https://www.google.com");//얘는 href와 비슷하다 뒤로가기도가능.
             //location.replace("https://www.daum.net");//기존의페이지를지워버리고 그 페이지를 링크가 대체한다.

            }
//즉 a태그를 타고가도 그 위치가 그려져있는걸 보내준다고생각하면댄다.
//★reload->새로고침 =클라이언트가 서버에게 리퀘스트(요청)을 다시보내서 다시응답받아 브라우저가 그림을 다시그렸다.
        </script>
</head>
<body>
    <button onclick="locTest();">이동</button>
</body>

```
