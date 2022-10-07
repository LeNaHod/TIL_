TIL DAY 11(22-10-06)

# 자바 스크립트

## 1. 기본문법
 
```HTML

    <script> /*펑션 이름 (파라미터) {바디} */
        function embeddedTest(){ /*embeddedTest는 내부작성방식을 클릭했을때,빨간글씨로 java~가html~출력하는함수*/
            var doc = document.getElementsByTagName("li")[1]; /*li의첫번째인덱스(0부터니까내부작성방식)*/
            doc.style.color='red';
            doc.innerHTML="<strong>javascript가 html문서(documnet)를 변화시켰습니다.</strong>";
        }
    </script>
    <script src="./resiurces/js/js01.js"> /*= import  ~ */

    </script> 
</head>
<body>

    <h1>JavaScript 기본문법</h1>
    <ol>
        <li onclick="alert('inlune!')/*자바스크립트영역*/;">inline방식</li>  
        <li onclick="embeddedTest();">내부 작성 방식</li>
        <li onclick="fileTest();">외부 js 작성 방식</li>
    </ol>
</body>
``` 
## 2. 타입,변수
   
```HTML
    <script> /*val01은 버튼을 클릭할때마다 값이 5씩올라간다.*/
        var variable =10;
        function val01(){variable=variable +5; document.getElementById("value01").innerHTML=
        "<b style='color:red;background:yellow'>"+variable+"</b>";}

        function val02(){var innerVal=variable+10; 
            document.getElementById("value02").innerHTML=
            "<b style='color:red; background:yellow'>"+innerVal+"</b>"}
        
        function jsType(){ /*alert(노출할값)=경고창노출. 리터럴=순수값*/
            var inferVal='문자';
            alert(inferVal + '의 타입 : ' + typeof(inferVal)); /*var:값의 리턴타입을 추론해서 반환해줌.*/

            inferVal=33;
            alert(inferVal + '의 타입 : '+typeof(inferVal));

            inferVal=true;
            alert(inferVal + '의 타입 : '+typeof(inferVal));

            inferVal=null;
            alert(inferVal + '의 타입 : '+typeof(inferVal));

            inferVal=new val01(); /*객체이다!출력하면[object Object의 타입]이런식으로나옴*/
            alert(inferVal + '의 타입 : '+typeof(inferVal));

            inferVal=function(){ /*function=익명함수.파이썬람다임.자바스크립트에서 함수를 값으로쓸수잇다.*/
            alert('타입추론');
        }
            alert(inferVal +'의 타입:' + typeof(inferVal));

        }
    </script>
</head>
<body>
    <h1>var 변수=값;</h1>
    <dl>
        <dt>변수 선언 규칙</dt>
        <dd>대소문자 구분</dd>
        <dd>영문, $, _ 로 시작</dd>
        <dd>영문, $, _, 숫자 사용가능</dd>
        <dd>키워드(에약어)사용불가</dd>
        <br>
        <dt>변수의 범위</dt>
        <dd>
            전역변수 : window 객체에 포함됨
            <button onclick="val01()">확인</button>
            <p id="value01"></p>
        </dd>
        <dd>
            지역변수:함수나객체내부에선언
            <button onclick="val02();">확인</button>
            <p id="value02"></p>
        </dd>
        <br>
        <dt>타입의 종류
            <button onclick="jsType();">확인</button>
        </dt>
        <dd>String</dd>
        <dd>Number</dd>
        <dd>Boolean</dd>
        <dd>Null</dd>
        <dd>Object</dd>
        <dd>Function</dd>
    </dl>
</body>
``` 
## 3. 경고창(alert)
   
```HTML
    <script>
        function alertTest(){alert("내용 출력(단순 대화창)");}

        function confirmTest(){
            var result=confirm("배경을 파란색으로 변환하시겠습니까?");
            if(result){
                alert("파란색으로 변환합니다.");
                document.body.style.backgroundColor="blue";/*document=현재문서에서.body부분을찾아 스타일을 블루색으로바꿔라*/
            } else{
                alert("배경색을 없앱니다.");
                document.body.style.backgroundColor="";
            }
        }
        function promptTest(){var txt = prompt("좋아하는 과목을 선택해주세요\n[1:python 2: database 3:web]");
                    if(txt==1){
                        alert("python재밌죠!");
                         } else if(txt==2){
                            alert("database orcle 신나죠");
                         }else if(txt==3){
                            alert("아직몇개안햇는데..");
                         }else if(txt==null){ /*취소버튼을누르면 null값리턴*/
                            alert("취소 ㄴㄴ");
                         }else {
                            alert("1,2,3,중에 하나만 선택해주세요!");
                         }
             }
    </script>


</head>
<body>
    <h1>Window 객체의 대화창 메서드</h1> <!--함수=독립적, 메서드는=종속되어잇는함수들-->

    <p>
        alter():경고창
        <button onclick="alertTest();">확인</button>
    </p>

    <p>
        confirm():확인 /취소 버튼
        <button onclick="confirmTest();">확인</button>
    </p>
    <p>
        prompt():텍스트박스 +확인/취소버튼
        <button onclick="promptTest();">확인</button>
    </p>

</body>
```
## 4. 함수

```HTML
    <script>
        function func01(){
            alert("함수의 이름이 있습니다.")
        }
        var func02=function(){ /*var 변수=값 의 형태 var은 추적형*/
            alert("함수의 이름이 없어요.");
        }/*그냥 function()이라고 이름없이쓰면 순수하게 값만 있는상태와같다. 고로 변수=값형태로바꿔주면 사용할수있다.*/
        
        function func03(){
            (function(){alert("즉시 실행 함수")})();/*func03펑션안에서 펑션을 실행해 값을리턴.*/
        }
        function literalPrn(literal){literal("안녕하세요,함수형태의값입니다.")}
        /*파라미터=매개변수=매개인자*/
        function func04(){
            literalPrn(function(msg){alert(msg);}) };
        // function func05(){
        //     literalPrn(alert);
        // }
        // function func05(){func01();} /*함수에서 함수를 불러옴*/
        // function func06(){function test01{alert("반가워요 test01입니다.")}() =04와같다.04는값을 대신다른펑션에서 가져올뿐임}
        function closureFunc(val){
            var suffix="님, 안녕하세요!"
            function innerFunc(){
                alert(val+suffix);
            }
            return innerFunc;
        }
        var closureTest01 = closureFunc("이나경");

        function closureTest02(){
            closureFunc("아이유")(); /*함수를바로실행시키기위해 ()*/
        }
    </script>

</head>
<body>
    <h1>function</h1>
    <h2>함수의 종류</h2>
    <p onclick="func01()">명시적 함수</p>
    <p onclick="func02()">익명 함수</p>
    <p onclick="func03()">즉시 함수</p>
    <p onclick="func04()">함수리터럴</p>
    <p onclick="closureTest01()">클로저</p>
    <p onclick="closureTest02()">클로저</p>
</body>
```
## 5. 제어문

```HTML
    <title>Document</title>
    <style>
        button{
            width:250px
        }
    </style>
    <script>
        function ifTest(){
            var i = prompt("숫자 1이나 2를입력","1");
            if(i==1){
                alert("1입니다.");

            }else if(i==2){
                alert("2입니다.");
            }else{
                alert("다른숫자입니다.");
            }
        }

        function switchTest(){
            var season=prompt("봄 여름 가을 겨울 중 좋아하는 계절을 입력해주세요.");
            switch(season){
                case"봄":
                    alert("봄엔 벚꽃엔딩");
                    break;
                case "여름":
                    alert("여름엔 바다");
                    break;
                case "가을":
                    alert("가을엔 단풍구경");
                    break;   
                case "겨울":
                    alert("겨울엔 스키장");
                    break;
                default:
                    alert("봄 여름 가을 겨울 중 하나를 선택해주세요");
                /*prompt는 창을 띄워서 데이터를 입력받는 함수이다. prompt("내용","입력창의 내용")형식. */
            }
        }
        function forTest(){
            // 증감연산자(++/--)
            // 변수의 앞 뒤에 증가/감소 연산자를 붙이게 되면
            // 변수가가진 값을 1씩 증가/감소하게 된다
            // 변수의 앞 : 전위 연산자(연산을 먼저하게 되고, 값을 나중에 리턴)
            // 변수의 뒤: 후위 연산자(값을 먼저 리턴하고,연산을  나중에함)
            // 파이썬에서의 i+=1 -> i++ 와 같다. i=i+1 == i +=1 == i++

            var a= 10;
            var b=3;
            var result = a++ + --b + b++ + ++a;
                /*a++10(11)+ --b(2) + b++2(3) + ++a(12)* ()안의값은 내부값.
                실제계산값은 10 2 2 12
                연산자가 뒤에붙으면 값먼저 가져오고 , 앞에있으면 연산을먼저함*/

            alert(result);

            //for(초기값;조건식;증감식){}, 구구단.
            for(var i = 2; i<10;i++){
                console.log(i+"단"); //console의 print와같다.
                for(var j =1; j<10; j++){
                    console.log(i+"*"+j+"="+(i*j));
                }
            }
        }
        function whileTest(){ 
            var i =0;
            while(i<10){ /*조건먼저 확인하고 만족하면실행*/
            console.log(i); 
            i++;
        }
            var j=10;
            do {  /*실행먼저하고 조건을 확인한다.*/
                console.log(j);
                j--;
            }while(j ==0 );
        }
    </script>


</head>
<body>

    <button onclick="ifTest();">if</button>
    <br>
    <button onclick="switchTest();">switch</button>
    <br>
    <button onclick="forTest();">for</button>
    <br>
    <button onclick="whileTest();">while</button>

</body>
```
<details>
<summary> 이하 아래에 코드첨부</summary>

## 6. 돔
 
```HTML
   <title>Document</title>
    <script>
        function searchQS(){
              var doc=document.querySelector("#test01"); //원하는 id나 class를 한개 가져올수있음.
           // doc.innerHTML="querySelector(css표현식)"; //dom탐색 메서드를 클릭하면 id test01이 querySelector(css표현식)로바뀜
        
        /*Node->document(text)를 객체(object)로바꾼것. ex)p태그를 객체로 바꾼거 그게여러개면 NodeList*/
        /*문서를 가져와서 특정 이벤트를 걸어주거나 바꾸거나하고싶을때. */
        /*자바스크립트는 태그가 걸려있으면 text로간주안하고 객체(object)=(자바에선 node)로 인식한다.*/
        
        var doc=document.querySelectorAll("#test01");/*()안에 값이 있든 없든, 한개이든 노드 리스트로반환한다.*/
        //alert(doc);
        doc[0].innerHTML="querySelector(css표현식)";}
        
        function searchId()
        {
            var doc = document.getElementById("test01");
            doc.innerHTML="id로탐색";
            doc.style.color="red";
        }
    
    function searchName(){
        var doc = document.getElementsByName("test02");/*노드 리스트를 반환.*/
        doc[1].value="name으로 탐색";/*인풋타입이니까 인풋타입의 밸류속성안에 값을 넣어라.*/
    }
    
    function searchTagNanme(){
        var doc= document.getElementsByTagName("p"); /*현재문서의 p태그를 찾아 doc에넣는다*/
        doc[3].innerHTML="태그네임으로 탐색"/*그냥 문자를 바꾸려면*/
        doc[3].style.color="blue";
    }
    
    </script>
</head>

<body>
    <p onclick="searchQS();">DOM 탐색 메서드</p>
    <P id="test01" onclick="searchId();">1.엘리먼트의 ID로 탐색 : 엘리먼트 하나를 선택 - 반환 : 값 하나</P>

    <P onclick="searchName();"><!--2.엘리먼트~를 클릭하면 name이test02인애들 중 1번째 인덱스를 찾아 'name으로탐색'출력-->
        2.엘리먼트의 NAME으로 탐색: 엘리먼트 여러개를 선택-반환:배열(nodeList)
        <input type="text" name="test02"><br>
        <input type="text" name="test02"><br>
        <input type="text" name="test02"><br>
    </P>

    <p onclick="searchTagNanme();">3. 엘리먼트의 tag name으로 탐색 : 엘리먼트 여러개를 선택 - 반환 : 배열(nodeList)</p>

</body>

```
## 7. 오브젝트
```HTML
    <title>Document</title>

    <script>
        function object01(){
            this.name01="홍길동"; 
            var name02 = "hong-gd";
            this.getname02=function(){
                return name02;
            }
        }
        function objTest(){
            var obj01=new object01();
            alert(obj01.getname02());
            alert(obj01.name01);//01은 this.를써서 외부접근이되지만
            alert(obj01.name02); //02는 var로 지역변수선언됐기때문에 접근이안되서 언디파인드뜬다.
            /*null:아예값이없음.안들어온것
              unefine:정의되지않은것.변수가아예없다.정의되지않은 변수를의미*/
        }
        //객체 리터럴
        var object02={
            name:"kim-sa",
            prn:function(){
               alert(object02.name +"010-1111-2222");

            }
        }
        function objTest(){
            var obj01 = new object01();
            //alert(object02.name)
           // object02.prn(); ->위의 obj02의값(1111 - 2222q반환.)
            obj01.prn(); //->아래 프로토타입을 반환한다.
            //object02라는객체를 값화시켜서 objTest()에서호출
        }
        
        //prototype
        object01.prototype.prn=function(){
            alert(this.name01 + ": 010-2222-3333");
        }
        

    </script>
</head>

<body>
    <h1>객체</h1>

    <p> 
        객체의 구성
        - property : 속성
        - function(method):기능
        - this : 객체 내부의 메서드나 속성을 정의
        - prototype : 객체의 기능을 확장

    </p>
    <button onclick="objTest()">확인</button>

</body>

```
## 8. 스트링
   
```HTML
    <script>
        function strTest01(){
            var str01 = "String";
            var str02 ="Test";
            var str03 = str01+str02;
            alert(str03);

            var str04=str01.concat(str02,"!!!");
            alert(str04);

            var joinTest =["5","10","15","20"].join(""); //5101520 붙어나온다.
            alert(joinTest);
        }
        function strTest02(){
            var numVal=123;
            var boolVal=true;//문자열부터 시작하는데 더하고싶으면 ()로 우선순위 지정
            var result = "String" + numVal + boolVal;//다합치면 string타입 반환.**문자와 다른언어가 만나면 문자가된다**
            alert(result + ":" + typeof(result)); //type()=typeof(). typerof는 타입반환

        }
        function strTest03(){
            var str =prompt("이름을 입력해 주세요 : ");
            var span =document.getElementById("res");
            
            //==. text.Content :출력문. 버튼옆에 문자출력.
            
            // if(str=="멀캠"){
            //     span.textContent =str+"님, 환영합니다."
            // }else if (str == "multicampus"){
            //     span.textContent="hello" + str;
            // }else {
            //     span.textContent = "이름을 다시한번 확인해주세요."
            // }
            
            //숫자10과 문자10이 같다고 나와버린다.
            var numVal=10; //얘가 기본값.
            // if(numVal=="10"){ //var  numVal와 "10"을비교하는데 ==은 같아져버림
            //     alert("문자열 10과 같습니다.");
            // }else{
            //     alert("문자10과다릅니다.");
            // }

            if(numVal==="10"){ //   ===은 엄격하게 비교. 타입이나 형태가 모두 일치해야함.
                alert("문자열 10과 같습니다.");
            }else {
                alert("문자열 10과 다릅니다.");
            }
            
            var strObj = new String("멀캠"); //얘는 오브젝트고
            var strVbj = "멀캠"; //얘는 스트링

            if(strObj == strVal){  //같고 
                alert("같습니다.");
            }else{
                alert("다릅니다.");
            }

            if(strObj === strVal){ //다르다. 고로 타입이안맞아서 같지않다고나옴.
                alert("같습니다.");
            }else{
                alert("다릅니다.");
            }

        //즉, == 는 값만비교하고, ===는 타입과 값을 둘다비교해서 완전히 일치하는것만 true
        }

        function strTest04(){
            var str = "홍길동 이순신 김선달 유재석 강호동 홍길동"
            var prop = prompt("검색할 이름을 입력하세요","입력")
            alert(str.indexOf(prop)); //앞에서검색
            alert(str.lastIndexOf(prop));//뒤에서부터검색. 
            //하지만 인덱스라 값은 앞에서부터 카운팅한다.
            //ex)홍길동이면  indexof=0/ lastindexof=20 이된다.

        }
        function strTest05(){
            var strVal="문자열 추출하기.관련 메서드:indexOf,substring.";
            var popt=prompt("어디서부터 검색할거에요?")

            //alert(strVal.substring(16));
            var sub2=strVal.indexOf(popt); 
            var sub3=strVal.lastIndexOf(popt);
            alert(strVal.substring(sub2+1));//+1은 :떼기.

            var splitVal=result.split(",");
            alert(splitVal[0]+"/"+splitVal[1]);
            
        }

        function strTest06(){
            var prop=prompt("쉼표로 구분하여 키워드를 입력해주세요"
            ,"사과,바나나,딸기,키위,포도");
            var div = document.getElementById("key");
            
            var stv1=prop.split(",");
            var result="";
            for(var i=0;i<stv1.length;i++){
                div.innerHTML+="키워드:"+stv1[i] + "<br>";  //()괄호로묶으면 안나온다!!!!!!!!
                div.innerHTML=rsult;
            }  
        }

    </script>
</head>
<body>
    <p> 문자열 합치기
        <button onclick="strTest01()">클릭</button>
    </p>

    <p>다른 자료형 합치기
        <button onclick="strTest02()">클릭</button>
    </p>

    <p>문자열 비교하기
        <button onclick="strTest03()">클릭</button>
        <span id="res"></span>
    </p>

    <p>문자열 검색하기
        <button onclick="strTest04()">클릭</button>
    </p>

    <p>문자열 추출하기
        <button onclick="strTest05()">클릭</button>
    </p>

    <p>키워드 나누기
        <button onclick="strTest06()">클릭</button>
    </p>
    <div id="key"></div>
</body>

```
## 9. 넘버

```HTML
    <style>
        #circle{
            border : 1px solid red;
            display: none;
        }
    </style>
    <!--리터럴 != object-->
    <script>
        function numberObj(){
            //리터럴
            var num01 =3;
            //오브젝트
            var num02 =new Number(3);

            console.log(num01 + ":" + typeof(num01));
            console.log(num02 + ":" + typeof(num02));
            
            //string ->number
           // alert(parseInt("1")+1); //결과값이 2."1"이 숫자화되서

            //NaN:Not a Number 숫자가 아닌
           // alert(parseInt("a"));

            var num=prompt("숫자만 입력해 주세요!");
            if(!isNaN(num)){ //!isNaN = NaN이 아니면 트루로빠짐. isNaN = NaN이면 트루로빠짐.
                alert("숫자가아닙니다.");
            }else{
                alert("숫자입니다.");
            }
        } 
        //is()->판별용 ㅇㅇ인지.t/f반환. has()->ㅇㅇ를가지고있는지.t/f반환.


        function randomNum(){
            //Math.random()  : 0 <= x <1 0부터1사이의값
            //Math.floor(): 버림
            //Math.round():반올림
            //Math.ceil():

            var min = 10;
            var max=100;
/*외우기*/    var ran=Math.round(Math.random()*(max-min)+min); //Math.random()*(max-min)여기서 계산하고버림.
            console.log(ran);
            /*function getRandom(min, max) { 값을 입력하면 그사이에 랜덤정수발생.
               return Math.floor((Math.random() * (max - min + 1)) + min);*/
}
    function randomBG(){
        var rnum=function(){
            return Math.floor(Math.random()*256); //함수로 만든이유는 각각세개씩넣어야하기때문에
                 //함수없이 Math.floor(Math.random()*256)을 넣으면 똑같은값이세번들어갈수있기때문에.
        }
        document.body.style.backgroundColor= "rgb("+rnum()+","+rnum()+","+rnum()+")";
    }

    function randomCircle(){
        var rnum =Math.floor(Math.random()*200);
        var circle=document.getElementById("circle");


        circle.style.display="block";

        circle.style.width=rnum+"px";
        circle.style.height=rnum+"px";
        
        var a=circle.style.width=rnum;
        var d=Math.ceil(a/2); //반지름
        var ab=Math.ceil(Math.PI*(Math.pow(d,2)));
        var abc=Math.ceil(d*2*Math.PI);

        this.getw=function(){
                return a;
            }
        this.getr=function(){
                return d;
            }
        this.getara=function(){
                
                return ab;
            }
        this.circlefer=function(){ 
                
                return abc;
            }  
        circle.style.borderRadius=Math.floor(rnum/2)+"px"; 
    

    }

        
    </script>
</head>
<body>
    <h1>숫자</h1>

    <br>
    <button onclick="numberObj();">숫자</button>
    <br>
    <button onclick="randomNum();">난수</button>
    <br>
    <button onclick="randomBG();">랜덤 배경색</button>
    <br>
    <button onclick="randomCircle();">랜덤 원 그리기</button>
    <button onclick="circleArea();">원의 넓이/둘레</button>
    <br>
    원의 넓이 :<span id="area"></span>
    <br>
    원의 둘레 :<span id="len"></span>
    <br><br><br><br>
    <div id="circle"></div>

    <script>
        function circleArea(){
            var randomc=new randomCircle();
            //넓이 : pi * r * r
            var are = document.getElementById("area");
            are.innerHTML = "(지름):"+randomc.getw()+" (반): "+randomc.getr()+"="+
            randomc.getara()
            
            //둘레 : pi *r *2
            var len1 =document.getElementById("len");
            len1.innerHTML =randomc.circlefer();
       }

    </script>
</body>


```
</details> 