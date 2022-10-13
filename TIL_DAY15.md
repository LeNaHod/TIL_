TIL DAT15 (22_10_13)

# js2일차

## 헷갈리는거 정리
- each():요소,함수,매개인자등을 배열처럼만들어서 for 반복문처럼 돌게하거나,검사를하게해줌
- nth-child(N):부모요소안의 n번째요소를찾는다. div p:ntt-child(N)이면 div안의 p태그안의 n번째자식요소
- contains(찾을문자열):찾을문자열이 포함된 결과를 찾음. empno:contain("1132") =1132라는값을 포함하는 empno를 찾는다.
 
## 코드를 통해알아보자
```html
01. event

    <style>
    div{
        width:400px;
        height:200px;
        border: 2px solid red;
        padding:20px;
        overflow:auto;
    }
    div p:first-child{
        float:left;
        border :1px solid blue;
        width: 150px;
        height: 150px;
        text-align: center;
        line-height: 150px;

    }
    div p:last-child{
        float:right;
        border:1px solid blue;
        width: 150px;
        height: 150px;
        text-align: center;
        line-height: 150px;
    }
    </style>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <script>
        $(function(){
            $("a:eq(0)").click(function(e){//파라미터e 이벤트객체가올것임
                alert("a click"); //a태그를 p태그가 감싸고있기때문에 아래 이벤트는 전파된다
               // e.stopPropagation();//p태그클릭!만 출력
                e.preventDefault();//alert창은div까지뜨지만, 네이버로 넘어가지않음
                
            })
            $("p").click(function(){
                alert("p click");//그래서 a태그를 누르면 p click도같이뜬다.
              //  e.stopPropagation();
                e.preventDefault();
            });

            $("div").click(function(){
                alert("div click");
            });
            // $("a:eq(1)").bind("mouseover mouseout",function(e){
            //     if(e.type=="mouseover"){
            //         $(this).css("background-color","skyblue");
            //     }
            //     if(e.type=="mouseout"){
            //         $(this).css("background-color","");
            //     }
            // }); //.bind( eventType [, eventData ], handler )위는 타입과 핸들러만사용
            //키:밸류 형식으로 아래 식을 작성. 이렇게 써도된다.
            //펑션으로 밸류값을 받는형식 마우스오버(키) :펑션(값)
            $("a:eq(1)").bind({
                "mouseover":function(){
                    $(this).css("background-color","khaki");
                },
                "mouseout":function(){
                    $(this).css("background-color","");
                }
            });
            document.getElementsByTagName("span")[0].addEventListener("click",function(){
                alert("span click");
                $("a:eq(1)").unbind(); //바인드해제.이벤트가 더이상 걸리지않음
            });
            //버튼으로 눌러서 새로추가된p태그에 기존이벤트를 연결시켜보자(p누르면 p click뜨게)
            $("button").click(function(){
                $("body").append("<p>새로 추가된 p</p>");
            });

            $("p").on("click",function(){//자바스크립트,제이쿼리의 on/on~:이벤트엮어주는친구
                alert("p!!");
            });
            $("body").on("click","p",function(){
                alert("new p!!");
            });
        });
        /*위에서 알수있는것은 각 요소가 서로 포함관계(중첩,부모-자식)인 경우,
        요소 중 하나에 이벤트가 발생되면 중첩된 요소들도 이벤트가 전파된다.
        이벤트 전파를 막고싶을땐? 
         1.stopPropagation():이벤트 요소의 전파 막기
         2.preventDefault():이벤트에 의한 기본 동작 막기
         3.return false:둘 다 막기
         사용방법:함수에 파라미터를하나주고, 함수안에서 파라미터(매개변수).막을이벤트함수*/
    </script>
</head>
<body>
    <sapn>unbind():이벤트해제</sapn>
    <div>
        <p>
            <a href="https://www.naver.com">클릭</a>
        </p>
        <p><span>클릭</span></p>
        

    </div>
    <div>
        <p>
            <a href="https://www.google.com">클릭!</a>
        </p>
        <p>클릭</p>
    </div>
    <button>요소 추가</button>
</body>

02.아코디언

    <title>Document</title>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <style>
        .main_menu{width: 300px;}
        .sub_menu1{cursor: pointer;}
        .sub_menu2{display: none; cursor: default;}
    </style>
    <script>
        $(function(){
            $("b").click(function(){
               // $("ul:eq(1)").css("display","block");
              //  $(this).next().slideToggle(); //this.next=지금누른(클릭한)태그의 바로 다음태그를찾음. 즉 b태그를클릭하면 ul을 토글한다.
              //  $(this).parent().siblings().find("ul").slideUp();//현재선택된태그의 부모를찾고,부모의 형제들을 찾는데 그중 ul만찾아 슬라이드 업을함
                //선택된태그의 .siblings()형제들을 찾아줌
                $(this).next().slideToggle().end().parent().siblings().find("ul").slideUp();//end로 한줄로만들어주기.(end !=and 하지만비슷)
            })
           
        });

    </script>
</head>
<body>
    <p>메뉴만들기</p>
    <ul type="square" class="main_menu">
        <li class="sub_menu1"><b>(1)css선택자</b>
            <ul type="circle" class="sub_menu2">
                <li>tag선택</li>
                <li>id선택</li>
                <li>class선택</li>
                <li>p c선택</li>
                <li>p &gt; c선택</li>
                <li>:nth-child(n/odd/even)</li>
                <li>:first-child</li>
                <li>:last-child</li>
            </ul>
        </li>
        <li class="sub_menu1"><b>(2)속성 선택자</b>
            <ul type="circel" class="sub_menu2">
                <li>[attr]</li>
                <li>[attr=value]</li>
                <li>[attr!=value]</li>
            </ul>
        </li>
        <li class="sub_menu1"><b>(3)폼 선택자</b>
            <ul type="circle" class="sub_menu2">
                <li>input:type</li>
            </ul>    
        </li>
        <li class="sub_menu1"><b>(4)사용자 정의 선택자</b>
        <ul type="circle" class="sub_menu2">
            <li>:eq(n)</li>
            <li>:first</li>
            <li>:last</li>
            <li>:even</li>
            <li>:odd</li>
            <li>:parent</li>
            </ul>
        </li>
    </ul>
    
</body>

03.클래스

    <title>Document</title>
    <style>
        img{width: 200px; height: 200px;}
        .addsize{width: 300px; height: 300px;}
        .onOffImg{display: none;}
    </style>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <script>
        /*★js에서 스타일 class를 넣어줘서(위에서 만들어진애들 .add~.on~) 스타일이 지정이되는것
        .css를하지않고 .~clsss(클래스형식의 스타일이름)해서 요소에 지정해줄수있는것!
        ex)이미지를 클릭하면 class를 지정해줄거야->지정할 클래스가있으면!(클래스가 무엇을하느냐에따라 작동이달라짐) */
        $(function(){ //각각 아래 다른동작을하는 제이쿼리. 이렇게 큰 펑션을하나만들어놓고쓰는게 난 더편한듯

            $("button").click(function(){
                $("img").toggleClass("onOffImg"); 
            });

            $("img").click(function(){ //
                if($(this).hasClass("addsize")){
                    $(this).removeClass("addsize");
                }else{
                    $(this).addClass("addsize");
                }
            })
        });
    </script>
</head>
<body>
    <button id="btn">class on/off</button>
    <br>
    <img src="resources/imgs/img01.png" alt="img01" title="img01">
    <img src="resources/imgs/img02.png" alt="img02" title="img02">
    <img src="resources/imgs/img03.png" alt="img03" title="img03">

</body>

04.insert(내부추가)

    <title>Document</title>
    <style>
        div{
            border:1px solid red;
        }
        .prepend{
            border:1px dotted blue;
        }
        .append{
            border:1px dotted green;
        }
    </style>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <script>
        $(function(){
            $("button:eq(0)").click(function(){ //.perpend는 . 한곳의 자식요소 중 가장처음으로들어감(기존내용이전,상단).얘도 자식요소로들어감
                $("div").prepend($("<p>").addClass("prepend").text("prepend"));
            });
           
            $("button:eq(1)").click(function(){
                $("div").append($("<p>").addClass("append").text("append"));//.append자식요소중마지막인데,append($("<p>"))->create엘리먼트("p")와같다.
            });
            $("button:eq(2)").click(function(){ //html로 출력되기떄문에 <b>태그가 적용이된다.
                $("div").html("<b>html요소를 변경</b>"); //=JS의innerHTML. 그래서HTML★노드★로들어가고
            })
            $("button:eq(3)").click(function(){//얘는 text기때문에 <b>태그가 문자열로 그대로 출력
                $("div").text("<b>text요소를 변경</b>"); //=JS의textcontent. 얘는 TEXT로들어감
            });
        });
    </script>
</head>
<body>
    <button>prepend</button>
    <button>append</button>
    <button>html</button>
    <button>text</button>

    <div>
        <p>내부 추가1</p>
        <p>내부 추가2</p>
    </div>
    
</body>

05.insert(외부추가)

    <title>Document</title>
    <style>
        div{border:1px solid red;}
    </style>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <script>
        $(function(){ //.after:선택한요소의 뒤에 지정한내용을 새로운 요소로 내용을추가한다. 
            $("button:eq(0)").click(function(){
                $("#base").after("<div>새로운 엘리먼트(after)</div>"); //이경우 base뒤에 div로 새로운엘리먼트~가생성
            });
            $("button:eq(1)").click(function(){
                $("<div>새로운 엘리먼트(insertAfter)</div>").insertAfter("#base");
            });//after(a뒤에b) / insertAfter(b뒤에a) 타겟의 위치가다르다. 위치.내용 <->내용.위치 정도의차이인듯
            
            $("button:eq(2)").click(function(){
                $("#base").before("<div>새로운 엘리먼트(before)</div>");
            });
            $("button:eq(3)").click(function(){
                $("<div>새로운 엘리먼트(insertBefore)</div>").insertBefore("#base");
            });
        });
    </script>
</head>
<body>
    <button>after</button>
    <button>insertAfter</button>
    <button>before</button>
    <button>insertBefore</button>

    <div id="base">
        <p>외부추가</p>
    </div>
</body>

```

<details>
<summary>replacec,슬롯머신제작,menu,delete,ajax</summary>

```html

06.리플레이스

    <title>Document</title>
    <style>

    </style>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <script>
        $(function(){
            $("button:first").click(function(){
                $("p").replaceWith("<p><b>replaceWith</b></p>");
            });

            $("button:last").click(function(){
                $("<p><b>replaceAll</b></p>").replaceAll("p");
            });
        })
    </script>
</head>
<body>
    <div>
        <p>DOM대체</p>
    </div>
    <button>replaceWith</button>
    <button>replaceAll</button>
</body>

07.슬롯머신

    <title>Document</title>
    <style>
        img{
            width:150px;
            height: 150px;
            float:left;
        }
        #menebox{
            position:relative;
        }
        #menu{
            overflow: auto;
        }
        .sel{
            width: 140px;
            height: 140px;
            border: 5px dotted red;
            position:absolute;
            left:300px;
        }
        button{
            width: 150px;
            height: 50px;
            margin-left: 300px;
        }
    </style>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <script>
        $(function(){
            setInterval(function(){ //setInterVal=일정시간동안 반복하는함수 1000=1초
                var div=$("#menu"); //
                $(".active").first().appendTo(div); //.active의 첫번째자식요소를! div의 마지막자리에 추가를하는데,
            },1000); //기존에있는값이니까 '추가 X' '이동O'. 그래서.빙글빙글 돌게되는것.
                    //액티브는 어디서 생성이되느냐? 저 밑에 액티브토글(액티브)에서, 스타트버튼을 누르면 액티브클래스추가를 활성시킨다.

            $("button").click(function(){ //실질적으로 슬롯머신돌려주는문
               $("img").toggleClass("active");//start버튼을누르면 div..#menu안의 이미지들이 무작위로 계속돌기시작
                        //액티브를 토글..on/off한다?

                if($("button").text()=="start"){//text start->stop변경되고,
                    $("button").text("stop");
                }else{
                    $("button").text("start");//의외의경우 start를유지하고 경고창을띄움
                    alert($("img:eq(2)").attr("alt")); //img:eq(2)의속성alt값을(img0n)경고창으로출력한다.
                }   //0~4무작위값으로 돌고 기준이 2?eq가1이나0이면 왜 제대로안나오는지

            });
        })
        /*★스페이스바,엔터를 눌러도멈춰진다.
        코드정리: $("button").click(function(){ 
               $("img").toggleClass("active"); 이부분이 img태그에 액티브라는이름의 토글클래스(활성비활성)을 생성한다.
        그리고 아래부분에서
        setInterval(function(){ 
                var div=$("#menu"); //
                $(".active").first().appendTo(div); 
            },1000); 액티브클래스를 제어한다. 액티브클래스가 img태그에 버튼을누르면 생성되도록 되어있기때문에,
            버튼을 누르면 <img src="./resources/imgs/img01.png" alt="img01" class="active">와 같은형태가된다.
            그래서 액티브 클래스의 첫번째자식요소 (img1번)을 div의 마지막에 추가하는데, 기존요소라 이동이되서
            2
            3
            4
            1
            ... 다시 반복하면서 3 4 1 2->하나씩밀림
        
        ----------------------------------------------------------------------------
        선택자
        .fist():현재위치(.앞)에 해당하는 가장 첫번째 엘리먼트반환

        ex)div안에 여러p태그가있다 가정
        ★nth-child(N)= 부모안에 모든 요소(자식요소) 중 N번째 요소
        jq: $("div p").first || $("div p").eq(0) || $('div p:nth-child(1)')
        js: document.querySelector('div p'); || document.querySelectorAll('div p')[0];
        ------------------------------------------------------------------------------
        내부추가
        append(): 타겟.append(소스) 소스(요소,컨텐츠)를 타겟의 마지막요소로 추가
        appendTo():소스.appendTo(타겟)  타겟의 마지막에 소스(요소)를 추가한다.
        prepend():append와 동일 대신 추가위치가 자식요소 중 첫번째 
        prependTO(): appendTo와 동일 추가위치가 자식요소 중 첫번째

        외부추가
        before():타겟.before(소스)바로앞쪽에 콘텐츠나 요소 추가
        after(): 타겟.after(소스)바로뒤쪽에 새로운 요소나 콘텐츠를 추가
        insertBefore():before와 동일하지만 소스와 타겟위치 반대. 요소만추가
        insertAfter():after와 동일하지만 소스와 타겟위치반대. 요소만추가
        */
        
    </script>
</head>
<body>
    <h1>Slotmachine</h1>
    <div id="menubox">
        <div class="sel"></div>
        <div id="menu"> 
            <img src="./resources/imgs/img01.png" alt="img01">
            <img src="./resources/imgs/img02.png" alt="img02">
            <img src="./resources/imgs/img03.png" alt="img03">
            <img src="./resources/imgs/img04.png" alt="img04">
        </div>
        <button>start</button>
    </div>
</body>

08.메뉴

    <title>Document</title>
    <style>
        .box{border:2px solid red}
        #menu{background-color: beige; text-align: right;}
        a{text-decoration: none; font-size: 20pt;}
        #menu div{display :inline-block;margin-right: 10px;}
    </style>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <script>
        $(function(){
            var $box=$("<div>").addClass("box"); //이런식으로 제이쿼리객체만들수도있다.
                //=<div ~~class=box>인 객체 $box생성

                $(".sub_menu").click(function(){
                $(".sub_menu").each(function(){ //=반복문같은거 돌면서 if로검사함
                    if($(this).parent().is(".box")){ //내가선택한애가 .box라는 속성을 가지고있는지판단(.is가 판단)
                        $(this).unwrap(".box");//있으면 .box를 unwrap한다 
                    }
                });
                $(this).wrap($box); //저위의this는 서브메뉴하나하나, 여기의 this클릭한 하나하나
            }); //=내가 클릭한 박스객체를 빨간테두리로 감싸준다.

            $("a").wrapInner("<span></span>") //선택된 요소의 자식요소를 지정한 태그로 감싸라
                                            //<a hraf~><span>과정</span></a>형태가된다.
            $("a").wrapAll("<b></b>")//b태그안에a를 다넣어버림
            });


            /*
            each():메서드는 매개 변수로 받은 것을 사용해 for in 반복문 과 같이 
            배열이나 객체의 요소를 검사할 수 있다.
            */
    </script>
</head>
<body>
    <div id="menu">
        <div class="sub_menu">
            <a href="#"><span>국비지원</span></a>
        </div>
        <div class="sub_menu">
            <a href="#">훈련검색</a>
        </div>
        <div class="sub_menu">
            <a href="#"> 기관검색</a>
        </div>
        <div class="sub_menu">
            <a href="#"> 질문답변</a>
        </div>
        <div class="sub_menu">
            <a href="#"> 과정후기</a>
        </div>
    </div>
</body>

09.삭제(delete)

    <title>Document</title>
    <style>
        div{border:2px solid red;width: 200px; padding:10px 10px;}
        p{background-color: yellow;}
        h1{border:1px solid blue;}
    </style>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <script>
        $(function(){ //문서가 작동된 이후(콜백)
            $("p:eq(0)").click(function(){
                $(this).remove(); 
            });
            $("p:eq(1)").click(function(){  //1번지를 detach=잘라낸다.
                var det=$(this).detach();
                $("h1").append(det); //h1에 어팬드(마지막으로추가함)한다 잘라온det정보를=1번지의정보를잘라서 h1에붙인다.
            });
            $("p:eq(2)").click(function(){
                $(this).parent().empty(); //empty:선택된녀석의 부모태그안에있는 애들(자식)을 삭제해줌.같이있는애들 자기를포함하여 삭제
            });                         //여기서는prent()붙어서 부모의자식요소를삭제하게된다.
        });                                
    
        /*empty():내가선택한녀석의 자식들을 날려버림 empty쓰레기통에버리기
        remove():내가선택한애를 날려버림 remove쓰레기통자체로버려버리기
        */
    </script>
</head>
<body>
    <h1>엘리먼트 제거하기</h1>
        
    <div>
        <p>remove</p>
        <p>detach</p>
        <p>empty</p>
    </div>
</body>

10.ajax

    <title>Document</title>
    <script src="./resources/js/jquery-3.6.1.min.js"></script>
    <style>
        *{margin:0px;padding:0px;}
        table{width: 400px;}
        table tr:nth-child(odd){background-color:orange}
        fieldset{width: 400px;}
        body{width: 1000px; margin: 50px auto;}
    </style>
    <script>
        $(function(){
            $("#emp_search").click(function(){ //emp_search는 버튼이름
                var empid=$("input[name=empid]").val(); //이름이empid인 input태그를 empid변수로선언
                if(!isNaN(empid) && empid >=100 && empid <=206){  //그외조건만족시 비동기 통신시작
                    //alert(empid);

                    $.ajax({ //ajax라는 함수를만들음
                        url:"emplist.xml",   //요청할 주소
                        method:"get",   //요청방식 get|post
                        //data:{"key":"value"}, 요청하면서 함께보내는데이터. 데이터:{키:밸류는}내가 ★보낼때★.
                        dataType:"xml", //응답'받는'데이터의 형태를 지정해주는것.!!!!datatype은!!받는데이터포맷!!!!!!!
                        
                        success:function(data){ //비동기 통신이 성공했을 시 실행.이미 data는xml객체로들어온다.
                            var empInfo=$(data).find("EMPLOYEE_ID:contains("+empid+")").parent(); //부모니까 row객체가된다.
                            if((empInfo).is("ROW")){ //내가찾아온태그가ROW태그라면
                                $("table input").each(function(i){ //테이블안의 인풋태그모두 선택해서.each =선택자
                                    $(this).val($(empInfo).children().eq(i).text()); //내가선택한 요소의 자식을 eq(i)=잇는만큼 text로가져온다.
                                });
                            }else{
                                alert("검색대상이 존재하지 않습니다.");
                        }},
                        
                        error:function(request,error){   //통신실패시 작동할것
                            alert("code:" + request.status + "\n"+"message:" + request.responseText +
                            "\n"+ "error:" + error ); //request.responseText:특정에러가났을때 출력하는 문서


                        }
                    });
                }else{
                    alert("사원번호를 제대로 입력해주세요")
                }
            })
        });






    /*
    var xhr =new XMLHttpRequest()
    xhr.onreadystatechange==callback(); 콜백함수가들어감
    ----------------------------------------------------
    callback hell을 해결하기위해 promise를사용한다.
    each():배열, Map, 그리고 객체를 매개변수로 받아 for문처럼(반복문처럼) 그 요소를 검사or반복할수있도록 하는 함수임
    fieldset: 관계된 요소들끼리 묶어주며 그룹화 하는데 그룹화 된 주위에 얇은 테두리를 이용하여 박스를 그린다.
     주로 해당 그룹의 이름을 정할 수 있는 legend와 함께 쓰임. 그룹지을때 활용한다고 생각하면된다.
    legend:fieldset 의 제목을달아줌. filedset과 legend는 친구다.
    isNaN():매개변수가 숫자인지 검사하는 함수(NaN은 Not a Number)
    jQuery.ajax( url [, settings ] )인데, url생략가능 =$ajax({url:,method:,data:{key:value},dataType:xml,json... ,
    성공함수명:function(가져올데이터,매개변수){내용}, 실패함수명:function(request,error등 필요한것)내용})
    -----------------------------------------------------
    data(문서전체).find("찾을곳:contains("+empid+")").parent() :내가 입력한녀석(empid)과 일치하는애를 찾을건데, 일치하는애의 '부모'를가져옴
    contains(찾을문자열):특정문자열을찾는메소드 
    EMPLOYEE_ID:contains("+empid+") : 이 형태면, empdid(인풋으로받은값)를 포함한 EMPLOYEE_ID를 선택한다.라고 생각하면된다.
    */
   
    </script>
    
</head>
<body>
    <fieldset>
        <legend>사원정보 조회</legend>
        <input type="text" name="empid">
        <input type="button" value="조회" id="emp_search">
    </fieldset>
    <table> <!--테이블하나를만드는데 tr하나가 컬럼한줄 정도라고생각하면댐td는 컬럼의데이터고 모여서 tr들이모여서1행이됨-->
        <tr>
            <th>사원번호</th>
            <td><input type="text"name=""></td>
        </tr>

        <tr>
            <th>이름</th>
            <td><input type="text"name=""></td>
        </tr>

        <tr>
            <th>이메일</th>
            <td><input type="text"name=""></td>
        </tr>

        <tr>
            <th>전화번호</th>
            <td><input type="text"name=""></td>
        </tr>

        <tr>
            <th>입사일</th>
            <td><input type="text"name=""></td>
        </tr>
        
    </table>

    
</body>

```
</details>

