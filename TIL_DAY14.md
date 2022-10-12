TIL DAY 14 (22_10_12)
 
## 헷갈리는 것 정리하고가기

- TR/TD/TH:테이블을을 만들때 사용하는태그들

- TR(가장큰개념)>TD=TH 로 볼수있다. 
 
    보통 테이블을 만들 때,TH로 표의제목을 만들고 TD로 데이터를넣고 이 TD들을 모아 TR로 묶어서 하나의 **행**을 생성한다.
    TH로만들수있는것은 TD로도 만들수있다.

**FORM 태그**

<fomr action="폼을 전송할 서버 쪽 스크립파일 경로", method="작동방식 get,post" name="폼을 식별할 이름"
 [target(action에서 지정한 파일을 현재창말고 오픈 할 위치)/accept-charset(폼 전송에 사용할 문자 인코딩)])>


- childNodes: 자식 노드에 접근 (요소가아니라 정말 노드리스트에 나오는애들에 접근 (비요소 포함 공백,주석,기타등등 모두포함))

- children: 자식 요소에 접근 (요소에만. 접근을하는것. 자기를 감싸고있는태그 등을 요소라고한다.)

- ex)document.querySelector("div").children ->div안에있는 요소만(p태그, b태그 tr td등)을 HTMLCollection으로반환.

- ex)document.querySelector("div").childrenNodes ->div안에있는 비요소모두 포함하여 **노드리스트**로 반환.

 ## 동기와 비동기 (AJAX)

- 비동기통신(요청해놓고 할일하는거),주소안바뀌고 필요한데이터를 가져오는것. 즉 서버에 요청한페이지는 그대로지만, 데이터만 다른걸 가져온다고 생각하면된다.
- 동기(요청해놓고 응답까지기다리는것)
- 비동기를 왜쓰는가?
    동기는 계속 새로요청해서 받아와 새로 그려야하기때문에 비동기 통신으로 해결할 수 있는 부분은
    무거워져서 느려지는것을 방지하기위해 사용한다.
- xml:확장형 마크업 랭귀지. 태그 내가편한대로 만들수있는것.


```HTML
   <title>Document</title>
    <script>
        //ajax:Asyncronous Javascript And Xml(비동기 요청)
        function ajaxTest(){
            var xhr=new XMLHttpRequest(); //자바스크립트가 가진 내장객체. 자바스크립트 오브젝트, http를 통한 데이터 송수신 지원
            //callback. onreadystate/change 이게 체인이되는 이벤트가 일어날때마다 펑션을호출. 얘들은 0일때도 1일때도 2일때도 계속 "호출"은되고있다.
            xhr.onreadystatechange=function(){ //전부 소문자이다.
                if(xhr.readyState==4){ //4는 통신완료니까 통신이제대로 이루어지고잇을때 라는의미
                    if(xhr.status==200){  //=if(xhr.readyState==4 &  xhr.status==200 or로도씀)
                      //  alert(xhr.responseText);
                     // console.log(xhr.responseXML); JOSN이면 responseJosn 같이 객체로응답해줌
                     var respXML=xhr.responseXML;
                     var table = document.getElementById("tb"); //컬럼들이 td가되게
                     var rows=respXML.getElementsByTagName("ROW")//respXML에서 row라고 적힌태그이름을가져온다.
                   // console.log(rows); xml문서를 객체화시켜서 row를추출  객체화=dom(doucmet~.get~이런거). 실행결과 배열로 가져온다.[row,row,row,row..]
                    var thead = document.createElement("tr");
                    for(var i =0; i<rows[0].children.length; i++){ //row태그안의 컬럼들을 컬럼갯수만큼 tr로가져와서 넣어주고
                        var th=document.createElement("th");//th를하나생성해서
                        th.appendChild(document.createTextNode(rows[0].children[i].nodeName)); //어펜트차일드(노드류만가능).
                                        //textnode로(text로) 컬럼을 rows0번지 안의 자식으로  컬럼갯수만큼 노드네임만가져와서 추가한다
                        thead.appendChild(th);
                    }
                        table.append(thead);
                    //안의값들을 td로바꿔서 tr로 묶어보자
                    for (var i =0; i<rows.length;i++){
                        var tr=document.createElement("tr");

                        for(var j =0; j<rows[i].children.length;j++){
                            var td=document.createElement("td");
                            td.appendChild(document.createTextNode(rows[i].children[j].textContent));
                            tr.appendChild(td);

                        }
                        table.appendChild(tr);
                    }
                    }else{              
                        alert(xht.status);
                    }
                }
            }
            /*
                readystate
                0:uninitiallized-실행되지않음
                1:loading -로딩중
                2:loaded - 로딩완료
                3:interactive - 통신 됨
               ★ 4:complete - 통신 완료 4의상태가 중요. 제대로통신됐다는의미니까. 

               status
               200:성공
               400:bad request
               401:unauthorized
               403:forbidden
               404:not found 서버는 요청받은 리소스를 찾을 수 없습니다.경로잘못적었을때가 대부분
               500:internal server error 서버가 처리방법을 모르는상황. 장고 오타났을때, 장고<->db사이에 뭔가 오류났을때.
                구조가 특정이벤트->콜백을일으킴(통신상태에따라)->객체화시켜서가져와서->통신방법(open(통신방식 ,오픈할파일))->send()진짜가져와줘
               */

           //실제실행부.=<form action="경로(emplist)" method="방식(get)"><input type="submit"(.send)>
            xhr.open("GET","emplist.xml"); // get방식으로 exmplist.xml을 연다.
            xhr.send(); //send를 호출하게되면 위의 오픈방식으로 파일을 실행하게된다.

        }
    </script>
</head>
<body>
    <button onclick="ajaxTest();">ajax</button>
    <table border ="1" id="tb">
    </table>
</body>

```

## 라이브러리와 모듈 
두개 다 누군가 만들어서 '배포'하는것을 가져와서 쓰는것. 필요한 기능을 가진 코드모음이라고 생각할 수 있다.
라이브러리와 모듈이 같진않지만 정의는 비슷하다.

## jquery
빠르고 가벼움에 중점을 둔 **자바스크립트 라이브러리**이다.

```html
01.basic
    <title>Document</title>
    <style>
        img{
            width: 200px;
            height: 200px;
        }
    </style>
    <script src="./resources/js/jquery-3.6.1.min.js"></script> <!--외부에서 스크립트 가져올땐 스크립트단안에 뭐쓰면 절대 ㄴㄴ(펑션같은거 ㄴ)-->
    
    <script> //함수만드는 스크립트와 가져오는스크립트는 분리해야한다.
        function showImg(){
            $("img").show(); //$=제이쿼리이다라는 뜻. 이미지를보여주는 함수
        }
        //onload=function(){}과 아래코드가 동일. 펑션을 값으로 쓰고있다.
        $(function(){
            //documnet.querySelector("#test-btn").onclick=function(){}; 과 동일하다.
            $("#test-btn").click(function(){; //해당선택자를 통해서 객체가되어서 클릭이벤트를 일으킬수있다.
                alert("버튼클릭함!!");
        });
        $("img").click(function(){//현재 이미지를 클릭하면
            $(this).hide();   //클릭이벤트를 실행한img를 숨긴다 this가 가르키는건"img"
        }) //★즉 $("태그").이벤트(function()or 비워두기{})이 기본문법
        });
        function resizeImg(){
          //  $("img").css("width","100px").css("height","100px");// $는 제이쿼리 객체로반환해서 .css().css로 쓴것
            $("img").css({"width": "100px", "hright":"100px"}).css("opacity","0.5");//↑↓코드 동일
        }                                                   //이부분까지j쿼리객체로 리턴하기에 뒤에 .css로 투명도도줌
        /*
        .css( propertyName )
        .css( propertyName )
        .css( propertyNames )
        ------여기까지 get
        .css( propertyName, value )
        .css( propertyName, value )
        .css( propertyName, function )
        .css( properties )
        -------여기까지 set
        */
       function addImg(){
        $("img").last().after("<img src='resources/imgs/img01.png'>");//마지막 이미지를 불러와서 버튼을누르면 추가한다.

       }
       function toggleImg(){
        $("img").toggle(); //toggle()=숨김/해제 가능.img 즉 img태그를 숨겻다 보였다해라
            
        }
                                              
    </script>
    
</head>
<body>
    <h1>jquery = javascript library</h1>
    <button id="test-btn">클릭</button>
    <br>
    <button onclick="showImg();">이미지 보이기</button>
    <button onclick="resizeImg();">이미지 축소</button>
    <button onclick="addImg();">이미지 추가</button>
    <button onclick="toggleImg()">이미지 숨기기/보이기</button>
    <br>
    <br>
    <div>
        <img src="resources/imgs/img01.png">
    </div>
    
</body>

02.selector
    <title>Document</title>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <script>
        //onload=function(){}
        //$(function(){})
        $(document).ready(function(){
            $("div:eq(0)").css({"border":"1px solid red","width":"400px","height":"200px"});
            $("#view").css({"border":"1px soilc red","width":"400px","height":"100px"});
        });

        function a1(){
            $("span").css("color","skyblue");
            $("#view").text('$("span").css("color","skyblue")'); //js의textcontant랑동일
        }
        function a2(){
            $("#t1").css("color","hotpink")
            $("#view").text('$("#t1").css("color","hotpink");');
        }
        function a3(){
            $(".t2").css("color","navy")
            $("#view").text('$("#t2").css("color","navy");');
        }
        function a4(){
            $("li span").css("color","orange")
            $("#view").text('$("li span").css("color","orange");');
        }
        function a5(){
            $("li>span").css("color","purple");
            $("#view").css('$("li>span").css("color","purple");');
        }
        function a6(){
          //  $("li:nth-child(6)").css("background-color","gray");
          //  $("li:nth-child(odd)").css("background-color","gray"); //odd니까 홀수행만선택되게
            $("li:nth-child(even)").css("background-color","gray"); //even이니까 짝수만
            $("#view").text('$("li:nth-child(6)").css("background-color","");');
        }
        function a7(){
            $("li:first-child").css("background-color","lime");
            $("#view").text('$("li:first-child").css("background-color","lime");');
        }
        function a8(){
            $("li:last-child").css("background-color","lightblue");
            $("#view").text('$("li:last-child").css("background-color","rgb 200,200,200");')
        }

        function cls(){
            $("li").css("color","black").css("background-color","");
            $("span").css({"color":"black","background-color":""});
            $("#view").text("");

        }
    </script>
</head>
<body>
    <h1>css selector</h1>
    <div>
        <ul>
            <li><span>tag로 선택</span></li>
            <li id ="t1">id로 선택</li>
            <li class ="t2">class로 선택</li>
            <li><span>parent child로 선택</span></li>
            <li><b><span>parent &gt; child로 선택</span></b></li>
            <li>:nth-child(n / odd /even)로 선택</li>
            <li>:first-child로 선택</li>
            <li>:last-child로 선택</li>
        </ul>
    </div>
    <br>
    <div>
        <button onclick="a1();">tag선택(span)</button>
        <button onclick="a2();">id선택(t1)</button>
        <button onclick="a3();">class(선택(t2)</button>
        <button onclick="a4();">p c 선택</button>
        <button onclick="a5();">p &gt; c 선택</button>
        <button onclick="a6();">nth-child</button>
        <button onclick="a7();">first-child</button>
        <button onclick="a8();">last-child</button>
        <br>
        <button onclick="cls()">reset</button>
    </div>
    <h2>코드내용</h2>
    <div id="view"></div>
</body>
03.input
    <title>Document</title>
    <script src="resources/js/jquery-3.6.1.min.js"></script>
    <script>
        function inputText(){//input인데 타입이 text인 인풋태그를 가져와서 
            var inputVal=$("input:text").val();  //text인풋태그의 속성값(입력값)을가져와서
            //js:.value;
            //jq:.val();
            alert(inputVal);//경고창에 뿌려준다.

        }
        function inputRadio(){
            var inputVal = $("input:radio").val();
            $("#a").html(inputVal); //raido버튼을 체크하면 radio Value가 출력된다.a태그에 라디오 밸류값을 innerhtml과비슷한이치.

        }
        function inputCheck(){
            var inputVal=$("input:checkbox").val();
            $("#a").text(inputVal);
        }
        $(function(){ //change(변경)이벤트가 일어났을때.선택박스의 밸류값이 변경이일어났을때 실행.인덱스출력
            $("select").change(function(){
                var option = $("select > option:selected");
                console.log(option.val());
                alert($("select > option").index(option));

            });
        });
    </script>
</head>
<body>
    <form action="">
        <input type="text">
        <input type="button" value="선택" onclick="inputText();">
        <br>
        <input type="radio" value="radio value" onclick="inputRadio();">radio
        <br>
        <input type="checkbox" value="checked value" onclick="inputcheck();">check
        <br>
        <div id="a"></div>
        <select>
            <option value="one">1</option>
            <option value="two">2</option>
            <option value="three">3</option>

        </select>

    </form>

</body>
04.check
    <title>Document</title>
    <script src="resources/js/jquery-3.6.1.min.js"></script>

    <script>
        $(function(){ //.submit():form의 submin이벤트가 발생되면 수행된다. 아래if에안걸리면 그냥 주고받음.(정상작동)
            $("#signal").submit(function(){ //인풋안의 username과 밸류값을여기서가져와서 겟방식으로 넘긴다.
                if($(".infobox").val==null || $(".infobox").val()==""){
                    $(".error").show();
                    return false;
                }
            });
            
            $("#confirm").click(function(){
                $("#result").empty();
                if($("input[name=chk]:checked").legth==0){ //input인데 []=어트리뷰트 값 ㅇㅇ 네임이 chk인애들중 체크가 되어있는애가 0이라면
                        alert("하나이상 체크해주세요");
                }else{
                    var total=0; //.each는 컬렉션..그러니까 조건을 만족하는결과의 묶음보따리같은거임. 결과가 뭉텅이로나와서
                    $("input[name=chk]:checked").each(function(i){ //저 덩어리에서 인덱스를가져온다(반복돌거니까)
                            //var chk=$("input[name=chk]:checked").eq(i); =var chk =$(this); 동일한의미 즉 
                            var chk=$(this); //input에서 체크가되어있는애들중에 하나!가 this인것(근데 반복문이니까 한번 돌때마다 1개씩가져옴)
                            var book= chk.next().text(); //즉 위의 두 코드 다 each한것중에 인덱스번호로 하나씩 가져오려고한것
                            var price =chk.val();
                            $("result").append(book+"가격"+price+"<br>");
                            total +=parseInt(price);
                    });
                    $("#result").append("총"+total+"원");
                }
            });
            //name이 chk인 input태그들이 모두 체크되면
            //name이 all input 태그들의 checked true로
            //name이 chk인 input태그들이 하나라도 체크해제되면
            //name all인 input태그들의 checked fasle로

            $("input[name=chk]").click(function(){
                //if($("input[name=chk]:checked").length ==$("input[name=chk]").length){
                if($("input[name=chk]:checked").length==3){
                    $("input[name=all]").prop("checked",1); //j쿼리는 함수명=true x (자바스크립트형)/ 
                }else{      //$().prop("속성",true or false) ★단, true false에 ""주면 ㄴㄴ!!★ 트루1 펄스0
                    $("input[name=all]").prop("checked",0);
                }

            });
        });
        function allchk(bool){
            $("input[name=chk]").prop("checked","true");
            
            }

        /*
            .attr():html의 어트리뷰트
            .prop():js(jq)의 property
        */

    </script>

</head>
<body>
    <form action ="" method="get" id="signal">
        <div>
            <span class="lable">User ID</span>
            <input type="text" class="infobox" name="userid">
            <span class="error" hidden style="color: red";>
            반드시 입력해 주세요!</span>
        </div>
        <input type="submit" value="입력" class="submit">
        
    </form>
    <hr>
    <fieldset style="width:300px;">
        <legend>체크 여부 확인</legend>
        <input type="checkbox" name="all" onclick="allchk(this.checked)">전체선택
        <br>
        <input type="checkbox" name="chk" value="25000"><b>python</b>
        <br>
        <input type="checkbox" name="chk" value="30000"><b>oralcle</b>
        <br>
        <input type="checkbox" name="chk" value="35000"><b>html/css/js</b>
        <br>
        <input type="button" value="확인" id="confirm">
        <br>
        <span>선택한 책 가격</span>
        <div id="result"></div>
    </fieldset>
</body>

05.dom01
    <title>Document</title>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>

    <script>
        $(function(){
            $("div > p").eq(0).click(function(){
                $("p b").eq(0).toggle();

            });
            $("div >p").eq(1).click(function(){
                $("p b").slice(1,2).toggle(); //1부터 '2전'인덱스 까지니까 1번만나옴
        });
            //eq()메소드가 하는일
            //-선택한 요소의 인덱스 번호에 해당하는 요소를 찾는다.
            //-없으면 null을 반환한다

            $("div >p").eq(2).click(function(){
                // $("p b").first().css("color","red");
                // $("p b").eq(2).toggle();
                $("p b").first().css("color","blue").end().eq(2).toggle();
                //.end()를만나면 다시 맨앞으로 돌아간다. 즉 이 코드에선 "p b "의 위치로 돌아가는것. 돌아가서 eq를실행
        });
        $("div >p").eq(3).click(function(){
            $("p b").last().toggle();
        })
    });

    </script>
</head>
<body>
    <p>
        <b>eq():선택한 엘리먼트들 중에 인덱스로 탐색</b>
        <br>
        <b>slice():선택한 엘리먼트들 중에 인덱스로 길이로 탐색</b>
        <br>
        <b>first():선택한 엘리먼트들 중에 첫번째 요소</b>
        <br>
        <b>last():선택한 엘리먼트들 중에 마지막 요소</b>
        <br>
    </p>
        <div>
            <p>1.eq()</p>
            <p>2.slice()</p>
            <p>3.first()</p>
            <p>4.last()</p>
        </div>
       
    </p>
</body>

06.dom02

    <title>Document</title>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    
    <script>
        //$(document).ready()는 문서가 준비되면 매개변수로 넣은 콜백 함수를 실행하라는 의미 =콜백함수
        //==<script>$(function(){} 위와 아래코드 동일
        $(document).ready(function(){
            $("div").find("b").css({"font-size:":"30pt","color":"red"});//find("b")= div(공백)b랑 같음.div>b와다름
            $("div").children("#chd").text("2.children()메서드");
            $("b").parent().css({"background-color":"skyblue","color":"yellow"})//pre안의b태그도 선택이되서 pre태그영역까지선택이된다.
            $("p > b").parents("div").css("background-color","khaki");//부모들을찾는거라서 바디전체에서 찾는데,바디에서 div영역을 찾아 바꾸게된다.
            $("p").eq(0).next().css({"font-size":"20pt","color":"blue"}); //next()는 바로 다음태그.다음번지의 태그를찾음.저기선eq0번째다음 태그를찾아바꿈
        });
    </script>
</head>
<body>
    <pre>
        <b>find("selector"):선택한 엘리먼트의 자손들 중에 탐색</b>
        <b>children("selector"):선택한 엘리먼트의 자식들 중에 탐색</b>
        <b>parent() / parents("selector"):선택한 엘리먼트의 부모/조상탐색</b>
        <b>next("selector"):선택한 엘리먼트 다음에 따라오는 요소 탐색</b>

    </pre>

    <div>
        <p><b>1</b></p>
        <p id="chd">2</p>
        <p>3</p>
        <p>4</p>
        <p>5</p>
    </div>
</body>

07.dom03

    <title>Document</title>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <script> //jQuery=$ 똑같음 둘다사용가능
        jQuery(function(){
            jQuery("p:eq(0)").add("span").css("color","red");//p태그 0번째선택하고 add(추가)로, span태그'들'을 추가한다.
            //스판태그를 누르면, alert창으로 스판태그 클릭!이라 뜨고, 색이 다크블루색으로 바뀐다.
            jQuery("div").children().click(function(){
                if(jQuery(this).prop("tagName")=="SPAN"){
                    alert("span tag click!!");
                    jQuery(this).css("color","darkblue");
                }//p태그 클릭시 백드라운드 색이 옐로우
                if(jQuery(this).is("p")){ //this.is p니까 이벤트를일으킨애를 찾아간다. 고로 p태그를누르면 배경색이바뀜
                    jQuery(this).css("background-color","yellow");
                }
            })
        });
    </script>
</head>
<body>
    <div>
        <p>add()</p>
        <span>add():선택한 엘리먼트에 추가적으로 selector표현식 작성</span>
        <p>is()</p>
        <span>is():선택한 엘리먼트 중에 구하는 엘리먼트가있는지 확인(ex)체크가 되어있니?같은거 물어볼때)</span>

    </div>
    
</body>

08.dom04

    <title>Document</title>
    <style>
        .menu{width:150px; background-color:aqua; position:absolute;}
        #menu2{left:170px;}
        #menu3{left:340px};
        a{text-decoration: none;}
    </style>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <script>
        $(function(){
            $(".menu div").css("display","none");
        });
        // //커서를 가져다대면 안의 메뉴가보이게하고, 떼면 안보이게하자
        // $(function(){
        //     $("div").mouseenter(function(){
        //         $(".menu div").css("display","block")});
        //     });

        // $(function(){
        //     $("div").mouseout(function(){
        //         $(".menu div").css("display","none")});
        //     })
        
        //hover를 이용해보자!
       $(function(){
            // $(".menu").hover(
            //     function(){
            //         //handler in
            //         $(this).children("div").show();},
            //     function(){//handler out
            //         $(this).children("div").hide();}
            // );
            $(".menu").hover(function(){
            //handler in out
            $(this).children("div").toggle();
        });
            });


        /*
        마우스 이벤트 종류
        click:마우스 클릭시 발색
        dbclick:마우스 더블클릭
        mousedown:마우스 버튼을 누를때 발생
        mouseup:마우스 버튼을 뗄때 발생한다
        mouseenter:마우스가 요소의 경계 외부->내부로 이동할때 발생 ->버블링 발생x.이벤트 한번만적용
        mouseleave:마우스가 요소의 경계 내부->외부로 이동할때 발생
        mousemone:마우스를 움직일 때 발생
        mousemout:마우스가 요소를 벗어날때 발생
        mouseover:마우스를 요소 안에 들어올때 발생 ->버블링발생.두개면 이벤트를 두번발생시킴
        */
           
        
    </script>
</head>
<body>
    <b>DOM 탐색 메서드</b>
    <br>
    <div id="menu1" class="menu">
        <a href="jq05.dom01.html">필터링메서드</a>
        <div>.eq()</div>
        <div>.slice()</div>
        <div>.first()</div>
        <div>.last()</div>
    </div>

    <div id="menu2" class="menu">
        <a href="jq06.dom02.html">트리탐색메서드</a>
        <div>.find()</div>
        <div>.children()</div>
        <div>.parent()</div>
        <div>.next()</div> 
    </div>

    <div id="menu3" class="menu">
        <a href="jq07.dom03.html">기타 탐색 메서드</a>
        <div>.add()</div>
        <div>.is()</div>
    </div>
</body>
```

