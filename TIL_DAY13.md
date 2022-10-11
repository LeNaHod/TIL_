TIL DAY 13(22_10_11)

여태까지배운것을 정리해보자.

## 1) html 
- HTML(하이퍼 텍스트 마크업 랭귀지):데이터를 태그로 구조화시키는언어.
- <form action="경로" method="요청방식(get=리퀘스트의 헤더에/post=리퀘스트의 바디에)">
- get방식일때:<!--queryString ?key=value&ket=vale..형식으로 주소창에보임 > 보통 input type ="text" ★name★="key" value="value"  여기서 name이 키, value가 밸류로 들어가기때문에
- set방식일때:위의것이 보이지않음
- <input type ="submit" value="전송">

## 2) css 
#id
.class
ele>ele
ele+ele
ele ele
ele[attr]
...등등등

## 3) 자바스크립트

- function ->값이다. 펑션값 함수값
- sort를 이용한 정렬기준주기 이런거
- dom
- document.get~...


## 오늘 실습코드를 통해 복습해보자!


```HTML
-CHECK
    <style>
        #colorbox{
            width: 320px;
            height: 320px;
            position:relative;
        }
        #red,#yellow,#blue,#green{
            width: 150px;
            height: 150px;
            border:1px solid black;
            position:absolute;
        }
        #yellow{left:160px;}
        #blue{top:160px;}
        #green{left:160px;top:160px;}
        button{
            width: 150px;
            height: 150px;
            left:160px;
        }
    </style>
    <script>
        function allselect(check){
            var chks=document.getElementsByName("chk");
            for(var i = 0; i<chks.length;i++){//chks라는노드에 t/f를넣는다.
                chks[i].checked=check;
                if(chks[i]==true){
                document.getElementsByName("all")[0].checked=true;
            }else if(chks[i]==false){
                document.getElementsByName("all")[0].checked=false;
            } 
            }
        }
        function sel(){
            var chks = document.getElementsByName("chk");

            for (var i = 0; i < chks.length;i++){
                if(chks[i].checked){
                    document.getElementById(chks[i].value).style.backgroundColor =
                    chks[i].value;
                }else{
                    document.getElementById(chks[i].value).style.backgroundColor="";
                }
            }
        }
    //     function clearDivs(){
    //         var chks = document.getElementsByName("chk");

    //         for (var i = 0; i < chks.length;i++){
    //             if(chks[i].checked){
    //                 document.getElementById(chks[i].value).style.backgroundColor =
    //                 "";
    //                 chks[i].checked=false;
    //             }
    //     }
        
    // } //ver 1
    function clearDivs(){
        var divs=document.querySelectorAll("#colorbox>div");
        for(var i =0; i < divs.length; i++){
            divs[i].style.backgroundColor="";
        }
        allselect(false);
        document.getElementsByName("all")[0].checked=false;
    }//ver2

    //     function testselect(){ //하나라도 선택해제되어있으면 전체선택박스해제되고, 다체크되어있으면 전체박스선택되게
    //     var chks = document.getElementsByName("chk")
    //         if(chks[i]==true){
    //             document.getElementsByName("all")[0].checked=true;
    //         }else if(chks[i]==false){
    //             document.getElementsByName("all")[0].checked=false;
    //         }
    //  }
    </script>
</head>
<body>
    <div id="colorbox">
        <div id="red">red</div>
        <div id="yellow">yellow</div>
        <div id="blue">blue</div>
        <div id="green">green</div>
    </div>

    <div id="base">
            <form>
                <input type="checkbox" name="all" onclick="allselect(this.checked)">전체선택<!--this=onclick이벤트 자체를 가르킨다. 온클릭이 작동되면checked를 발생(?)-->
                <br><!--checked속성은 t/f로 이루어져잇고 위의같은경우 온클릭이 일어날시t,해제시f-->
                <input type="checkbox" name="chk" value="red">빨강<br>
                <input type="checkbox" name="chk" value="yellow">노랑<br>
                <input type="checkbox" name="chk" value="blue">파랑<br>
                <input type="checkbox" name="chk" value="green">초록<br>

                <input type="button" value="선택" onclick="sel();">
                <input type="button" value="clear" onclick="clearDivs();">
            </form>
        </div>
</body>

-DOM01

    <style>
        a>img{
            width:50px;
            height: 50px;

        }
        #gallery{
            width: 200px;
            height: 200px;
        }
        p{
            width: 350px;
            height: 350px;
        }
        img{
            vertical-align:middle;
        }
        a{
            text-decoration: none;
        }

    </style>

    <script>
        var num=1;
        function preveGallery(){//이전버튼
            num--;
            if(num<1){
            num=6;
            }
            document.getElementById("gallery").src="resiurces/imgs/img0"+num+".png";
            return false;//이벤트 전파 막기 그래서 naver로 돌아가지않음
        }
        function nextGallery(){
            num++;
            if(num > 6){
                num=1;
            }
            document.getElementById("gallery").src="resiurces/imgs/img0"+num+".png";
            return false;
        }
        // var cut=0;
        // var imglist=["img01.png","img02.png","img03.png","img04.png","img05.png"]
        // function changeimgR(){
        //     var mimg=document.getElementById("img1");
        //     cut++;
        //     if(cut>=imglist.length)
        //     {
        //         cut=0;
        //     }
            
        //     mimg.src=imglist[cut];
        // }
        // function changeimgL(){
        //     var mimg=document.getElementById("img1");
        //     cut--;
        //     if(cut<0) 
        //     {
        //         cut=4;
        //     }
        //     mimg.src=imglist[cut];
        // }  
    </script>

</head>
<body>
    <div id="galleryWrap">
        <p> 
            <a href="https://www.naver.com" onclick="return preveGallery();">
                <img src="./resiurces/imgs/arrowleft.png" alt="이전그림">    
            </a>
                <img src="resiurces/imgs/img01.png"alt="갤러리" id="gallery">

                <a href="#next" onclick="return nextGallery();">
                    <img src="resiurces/imgs/arrowright.png" alt="다음그림">
                </a>
        </p>
    </div>
</body>

-DOM02
    <style>
        
    </style>
    <script>
        function searchPar(){
            var child02=document.getElementsByTagName("p")[1];
            var parent=child02.parentNode; //p태그를 감싸고있는 태그를 부모노드라고한다.여기선 div인데,대문자로반환한다.
            console.log(parent);
        }
        function searchChi(){
            var div=document.getElementsByTagName("div")[0];
            var divChildren=div.childNodes;//nodes=노드리스트여서 bytagname에 [0]을 붙여줘야한다.div가하나만 들어있는 리스트라는의미.
            console.log(divChildren);//txt(div와p태그사이의 공백,p와p태그사이의 공백이 다 txt처리)-p-txt-p-txt...해서 두번째p는 3번지
            //divChildren[3].style.backgroundColor="pink";//<p>1</p><p>2</p><p>3</p>이여야 p-p-p가뜬다.
            console.log(divChildren[0].nodeName);//#text를 반환.0번지noed가 text라서
            console.log(divChildren[0].tagName);//언디파인드 반환. 태그는아니라고뜬다.(text니까)
            console.log(divChildren[1].nodeName);
            console.log(divChildren[1].tagName);
        }
    </script>
</head>
<body>
    <h1>부모,자식 탐색</h1>
    <div>
        <p>child01</p>
        <p>child02</p>
        <p>child03</p>
    </div>
    <button onclick="searchPar();">부모탐색</button>
    <button onclick="searchChi();">자식탐색</button>
</body>

-DOM3

    <style>

    </style>

    <script>
        function eleCreate(){ //html문서안에 없는 친구를 자바스크립트에서 만들어서 생성해줌=버튼을누르면 body안에 뭔가생김
            var div=document.createElement("div");//div를만든다.
            
            //속성을 만드는법 1. 1번방법은 속성 node를만들어서 노드를 셋팅해주는것
           // var attr=document.createAttribute("style");//스타일 속성을 생성해서attr에넣음
          //  attr.nodeValue="border:2px solid blue"; //=style="border:2px solid blue"(세부속성을넣음)
          //  div.setAttributeNode(attr);//<div style="border:2px solid blue"></div>

            //2.노드생성안하고 바로 넣어줌
            div.setAttribute("style","border : 2px solid red") //2번방법 객체.셋어트리뷰트("속성이름","세부속성지정").이쪽이 더편함
            
            var txt=document.createTextNode("엘리먼트 생성");
            div.appendChild(txt); //div안에 자식추가. txt노드타입의 엘리먼트생성!이라는애를 추가
            //<div style="border:2px solid blue">엘리먼트 생성</div>
            document.body.appendChild(div);
        }
    </script>
</head>
<body>
    <button onclick="eleCreate();">엘리먼트 생성하기</button>
</body>

-DOM04

    <style>
        img,#imgView{
            width: 300px;
            height: 300px;
        }
    </style>

    <script>
        function createImg(){
            //1.이름이 rdoBtn인 요소들을 가져요자
            var raidos=document.getElementsByName("rdoBtn"); //노드 리스트로 가져와서
            var radioVal="";
            //2.가지고 온 rdoBtn요소들의 length만큼 for문을 돌면서
            for(var i=0; i< raidos.length;i++){  
                 //3.각 요소가 체크되어 있는지 확인하고 
                if(raidos[i].checked){  //checked은 선택버튼류에있다. i번째 인덱스가 체크되어있는지 확인
                    radioVal="resiurces/imgs/"+raidos[i].value; ////4.체크되어있다면,자신의 value속성값을 가지고와서 경로 문자열을 만들어준다.
                }
            }
                var img=document.createElement("img");
                img.setAttribute("src",radioVal);
               
            //5.img태그를 생성하거

            //6.img태그에 src속성을 만들어서 위에 저장해둔 경로문자열(radioVal)을 값으로 넣어주자
            
            //7.
            var div = document.getElementById("imgView");
            var chd = document.querySelector("#imgView>img");
            div.replaceChild(img,chd);//리플레이스차일드=자식노드를 새 노드로 '대체'하는것.
                    //리플레이스차일드(뉴노드(대체할노드),올드노드)리무브.차일드()=괄호안의 요소삭제가능.
        }   
        function deleteImg(){
            document.getElementById("imgView").innerHTML="<img src=''>";

        }
    </script>
</head>
<body>
    <input type="radio" name="rdoBtn" value="img01.png">img01<br>
    <input type="radio" name="rdoBtn" value="img02.png">img02<br>
    <input type="radio" name="rdoBtn" value="img03.png">img03<br>
    <br>
    <button onclick="createImg();">이미지 생성</button>
    <button onclick="deleteImg();">이미지 삭제</button>
    <br>
    <div id="imgView"><img src=""></div>

</body>

-DOM5

    <style>
        img{
        vertical-align:middle;
        width:300px;
        height:300px;}

    </style>
    <script>
        // 1. document.querySelectorAll : 해당 선택자로 선택되는 요소를 모두 선택
    	// 2. document.querySelector : 특정 태그에 포함된 "첫번째 요소를 반환" 합니다
    	// 3. 쿼리셀렉터=겟엘레먼트바이 아이디 둘이 비슷하지만 속도는 엘레멘트가빠름.    	
    	// 
    	    	

        onload=function(){

        var anchs=document.querySelectorAll("a");
        var img=document.querySelector("img");
        var count=1;
        anchs[0].onclick=function(){
         if(img.getAttribute("alt")=="img01"){
            img.setAttribute("alt","img05");
            img.setAttribute("src","resiurces/imgs/img06.png");
            count =5;
         }else{
            img.setAttribute("alt","img0"+ (--count));
            img.setAttribute("src","resiurces/imgs/img0"+count+".png");
         }

        }

        anchs[1].onclick=function(){ //▶를의미함. 1번지채워보자.
         

        }
    }

    </script>
</head>
<body>
    <div>
        <a href="#" id="lt">◀</a>
        <img src="resiurces/imgs/img01.png" alt="img01">
        <a href="#" id="rt">▶</a>
    </div>
    
</body>

-DOM6

    <style>
        p{
            border : 1px solid red;
        }
    </style>
    <script>
        function addAppend(){
            var fieldset=document.getElementById("addele");
            var p = document.createElement("p");
            p.textContent="자식태그들 중 마지막에 붙여넣는다"; //텍스트를 엘리먼트를추가할경우 가장일반적임=textContent
            fieldset.appendChild(p); //가장 마지막 노드로 넣어준다.막내로 추가해준다 괄호안의 요소를.
            count=1; //해당 엘리먼트의 텍스트 값을 반환하고, 텍스트'노드'를추가함.
        }
        function addBefore(){
            var fieldset=document.getElementById("addele");
            var p =document.createElement("p");
            p.textContent="엘리먼트의 앞에 붙는다.";
            var div=document.querySelector("#addele>div");
            fieldset.insertBefore(p,div);
        }
        function moveElement(){ //필드셋안에있는친구들이 moveElement를 누르면 밖으로 튀어나온다.슉슉...
            var moveEle=document.querySelector("fieldset").children[1]; 
            var addEle=document.body; //필드셋안에 있는 친구들을 바디에추가를해라
            addEle.appendChild(moveEle); 
        } //어떤요소.appendChild(추가할 노드):요소에 마지막 자식노드를 추가한다.한번에 한개추가 가능, 노드만가능
          //어떤요소.children(선택할 태그나 분류):어떤요소의 자식을 선택하는것.
          //그냥 .append:텍스트,노드 둘 다 자식노드로 추가 가능. 한번에 여러개 가능
          //ex) div.children("p.hi").css("color","red")면 p태그의 hi라는 이름의 클래스를 선택해서 컬러를 red로바꿈

    </script>
</head>

<body>
    <h1>태그추가하기</h1>
    <button onclick="addAppend()";>appendChild()</button>
    <button onclick="addBefore()";>insertBefore()</button>
    <button onclick="moveElement()";>appendChild를 이용한 엘리먼트 이동</button>

    <fieldset id="addele">
        <legend>부모태그</legend>
        <div>div태그</div>
    </fieldset>
</body>

-DOM7

    <script>
        function tableVal(){ //추가버튼 함수
            var doc=document.forms[0]; //forms->리스트형식이니까 0번째
            var vals=[doc.id.value,doc.pw.value,doc.addr.value,doc.phone.value]; //form안의 id,pw,addr,phon의 인풋속성값(입력값을 가져옴)
            //유효성검사
            for(var i = 0; i<vals.length; i++){ //vals중 비어있는값이없는지 체크하고 null or "" or undefined 있을시 모두 다 입력해주세요 출력
                if(vals[i]==null || vals[i]=="" || vals[i]==undefined){
                    alert("모두 다 입력해 주세요!!");
                    return;
                }
            } //tbody id =addtr에 createRow(vals)함수에서 가져온 데이터를 자식노드를추가한다. 
            document.getElementById("addtr").appendChild(createRow(vals));//appendChild=한번에 하나의 노드만추가가능. 노드객체만 받을수있다.
        }//tbody는 이름, 비밀번호, 주소 등 컬럼 밑부분이 tbody영역

        function createRow(vals){
            var tr=document.createElement("tr");
            for(var i=0; i<vals.length; i++){
                var td =document.createElement("td"); //td를생성해서
                td.textContent=vals[i]; //td안에 각 아이디 패스워드 주소 등의 인풋속성값을 할당해줌
                tr.appendChild(td); //td를하나씩 추가하는이치와같다.
            }
            var dTd= document.createElement("td"); //새로 행을 추가했을때 생기는 삭제버튼동작
            dTd.innerHTML="<input type='button' value='삭제' onclick='delRow(this)'>";//onclick='delRow(this)=온클릭을 동작시켜주는 태그에서 실행한다.여기선 input태그.
            tr.appendChild(dTd);//위의 코드는 createRow(vals)와 똑같은 구조로 만들수있고 반대로 createRow를 dTd구조로만들수있다.

            return tr; //appendchild는 리턴값을 반환한다
        }
        function deleteVal(){
            var tbody = document.getElementById("addtr");
            while(tbody.hasChildNodes()){ //전체삭제 버튼. =tbody안에 자식노드 유무확인
                tbody.removeChild(tbody.lastChild); //.lastChild=맨끝에있는노드를 삭제한다는것.맨끝부터하나하나삭제한다고생각
            }//hasChildNodes=일단 지정된 노드안에 자식노드가있는지 확인.t/f값 반환 ★공백,줄바꿈도 자식으로침
        }

        function delRow(ele){
            var delTr=ele.parentNode.parentNode; //부모의 부모를감싸고있는 태그까지 삭제.그래서 tr(row)를 삭제하게된다. tr->td->현재 이렇게잇으니까
            var tbody=document.getElementById("addtr");
            tbody.removeChild(delTr);

        }
    </script>
</head>
<body>
    <form>
        <table id ="intable">
            <tr>
                <th>아이디:</th>
                <td><input type="text" name="id"></td>
            </tr>
            <tr>
                <th>비밀번호:</th>
                <td><input type="text" name="pw"></td>
            </tr>
            <tr>
                <th>주소:</th>
                <td><input type="text" name="addr"></td>
            </tr>
            <tr>
                <th>전화번호:</th>
                <td><input type="text" name="phone"></td>
            </tr>
        </table>
        <input type="button" value="추가" onclick="tableVal();">
        <input type="button" value="삭제" onclick="deleteVal();">
    </form>    
    <div id="addtable">
        <table border="1" id="ctb">
            <col width="100px">
            <col width="100px">
            <col width="300px">
            <col width="200px">
            <col width="100px">
            <thead>
                <tr><!--th~ 컬럼-->
                    <th>아이디</th> 
                    <th>비밀번호</th>
                    <th>주소</th>
                    <th>전화번호</th>
                    <th>삭제</th>
                </tr>
            </thead>
            <tbody id="addtr"></tbody> 
        </table>
    </div>
</body>
```