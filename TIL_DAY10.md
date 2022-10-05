TIL DAY 10(22_10_05)


# CSS를 배워보자
css는 html을 더 편리하게 조작할수있는(꾸미는)스타일시트이다.

- 기본문법
적용은 인라인이 1순위이다.
외부로 css를 가져와도 인라인이 있으면, 인라인에 적용한것으로 다시바뀜.(=적용이안된다.)


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        p{
            background-color: beige;
        }
    </style>
    <link rel="stylesheet" href="./css01.css">
</head>
<body>
    <h1>CSS 기본 문법</h1>
    <b style="color: red;">1. 인라인 스타일 시트</b><!--우선순위1순위 인라인-->>
    <p>
        <span>2. 내부 스타일시트</span> <!--헤드의style을가져옴-->
        <br>
        <b>3.외부 스타일 시트</b><!--헤드의 link로 외부css를가져옴-->
    </p>
</body>
</html>

```  
- 엘리먼트:시작태그부터 종료태그까지를 엘리먼트라고한다.
- ★selector : 크롤링 등 많이쓰인다! 중요
- id와class를 많이쓰는데,
    id = #id명{}
    class = .class명{}
    클래스는 . id #으로 구분한다!

- 전체선택자와 자식선택자는?
  *{} 이렇게쓰는데 우선순위제외하고 다바꿔준다.
  자식선택자는 >이다. div>h1이면, div안의 h1만 바꿔준다.

- pre,dd,dt,p,..{} 콤마로 구분하면 다중선택. 앞에 선택한애들한데 {}안의내용을 적용
- p+b+dd+dt {} +(더하기는) p안의b안의dd안의dt를 찾아라.한개씩만 적용된다. 위의경우 최종적으로 **dd 아래에있는dt만 적용**된다.
  
- 아래 css를 보면 다른것들은 어떻게 적용되는지 알 수있다.
 
```css
/*타입*/
pre{text-align: center;}
/*id*/
#s-id01{
    color:aquamarine
}
#s-id02{
    color :violet;
}
/*클래스*/
.s-cls01{
    background-color: black;
    color :white;
}

.s-cls02{
    background-color: cornflowerblue;
}

.s-cls03{
    background-color: coral;
}
/*전체선택자
*{
    color: darkblue;
}
*/

/*자식선택자*/
#atc > p{  /*div안에있는<p>는선택되지않음*/
    color:gold; 
}

/*인접*/
b + span + pre{ /*b 다음 span다음 pre에 적용해라*/
    background-color :red; 
}

/*하위*/

#atc02{ /*하위의 모든요소를 다찾아줌*/
    background-color :chocolate
}

/*속성 크롤링할때 속성선택자로 이것저것 선택해보기ppt참조*/
p[title]{ /*타이틀이 있는애만*/
    background-color: blueviolet; 
}
p[title="b"]{ /*타이틀이b인애만*/
    color : red;
}
p{ /*그냥 p태그인애만*/
    color: chartreuse;
}

/*가상 클래스 선택자*/
a:link{ /*안가봤던 링크 색 바꾸기*/
    color:crimson;
    font-size : 20pt;
}

a:visited{ /*방문했던 링크 색 바꾸기*/
    color :hotpink;
    font-size:20px;

}

a:hover{ /*커서올라갔을때*/
    background-color: cyan;
    color: yellow;

}

a:active { /*클릭하는 순간! 의 색을바꿔줌*/
    background-color: black;
    color: green
}

input:checked{ /*체크하면 커짐  해제하면작아짐*/

    width:100px;
    height:100px
}
```
- 이하 코드 첨부(주석포함)
 
<details>
<summary>html2일차</summary>

## font,box,float,disply등등..

```html
    <title>Document</title>
    
    <style typel="text/css">
        div > h1{      /*div>h1은 div의 자식태그에게 적용해라.div안의h1을바꿔라*/
            font-weight: bold;
            font-style: italic;
            font-variant: small-caps;
            font-size:25px;
            line-height:500%;
            font-family:"궁서";}
        /*font 등록*/
        @font-face{
            font-family :"Goyang"; 
            src:url("./fonts/Goyang.ttf")
            format("truetype")
        }
        div+p{font-family: "Goyang";} /*div다음p를찾아라(한개의p만적용)*/
      
    </style>

</head>
<body>
    
    <div>
        <h1>Data Science/ Data Engineering 과정</h1>
    </div>
    <p>Data Science/ Data Engineering 과정</p>
</body>


----
    <style>
        dl,dt,dd,p{margin:0px; padding:0px;} /*dl,dt,dd,p를 다중선택*/
        .box{
            width:600px;
            border:3px #123456 double; /*두칸씩잘라서 rgb를만듦*/
            }

        dt{
            background: #abcdef;
            text-align:center; /*문자정렬*/
            font-size:20px;
            letter-spacing:15px; /*글자간격*/
            padding:15px;
            border-bottom : #123456 5ps double; /*하단테두리 너비,색상,스타일 지정 상속x*/

        }
        
        dd{
            padding:10px;
        }
        .line{
            border-bottom:#123456 1px double;
            }
    </style>

</head>
<body>
    <dl class="box">
        <dt>드래곤라자명언</dt>
        <dd class="line"></dd>
            <h2>샌드 네드발</h2>
            <p>저와 말이 함께 후치를 타면 됩니다.</p>
        </dd>
        <dd>
        <h2>핸드레이크</h2>
        <p>나는 단수가 아니다.</p>
        </dd>
    </dl>
</body>

-----
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        body{width:300px;} img{width:100px; height : 100px;}
        h1{float :left; background-color: orange;} 
/*float를 왼쪽으로 주니까,왼쪽으로 붙고,오른쪽남는 부분들은 글자가 채워진다.*/
        p{text-align:justify;}p span{border:3 px dotted red; float:right;}
/*float를 오른쪽으로 주니까,오른쪽으로 붙고,왼쪽남는 부분들은 글자가 채워진다.*/
/*그냥 float는 혼자 한줄을 다차지한다.*/
    </style>
</head>
<body>
    <h1>드래곤 라자</h1>
    <p>
        "우리는 별이오."
        "별?"
        "무수히 많고 그래서 어쩌면 보잘것없어 보일 수도 있지. 바라보지 않는 이상 우리는 서로를 잊을 수도 있소. 영원의 숲에서처럼 우리들은 서로를, 자신을 돌보지 않는 한 언제라도 그 빛을 잊어버리고 존재를 상실할 수도 있는 별들이지."
        숲은 거대한 암흑으로 변했고 그 위의 밤하늘은 온통 빛무리들 뿐이었다. 칼의 말은 이어졌다.
        "그러나 우리는 서로를 바라볼 줄 아오. 밤하늘은 어둡고, 주위는 차가운 암흑 뿐이지만, 별은 바라보는 자에겐 반드시 빛을 주지요. 우리는 어쩌면 서로를 바라보는 눈동자 속에 존재하는 별빛 같은 존재들이지. 하지만 우리의 빛은 약하지 않소. 서로를 바라볼 때 우리는 우리의 모든 빛을 뿜어내지."
        "나 같은 싸구려 도둑도요?"
        네리아의 목소리는 슬프지 않았다. 그리고 칼의 대답도 평온했다.
        "이제는 아시겠지? 네리아 양. 당신들 주위에 우리가 있고, 우리는 당신을 바라본다오. 그리고 당신은 우리들에게 당신의 빛을 뿜어내고 있소. 우리는 서로에게 잊혀질 수 없는 존재들이오. 최소한 우리가 서로를 바라보는 이상은."
        어둠 속에서 네리아의 눈이 별처럼 아름답게 반짝였다.
        <span>
            <img src="https://w.namu.la/s/c182412ae18194dc4945588a576d1991b12e6ffd025b4742f7d4482b0e8ccdcbce3f96e251ab3a45b56c00816bf3dfd07e3558b6f859bbdc08d80136bba4301806a42be7d93548147b9843961c9d67a7dbc3999d50237bb1e33b63a6235805033312e9e7fe36f5a7ddfe3aa4d6222687" 
                 alt="">
        </span>
        나는 혹시 반짝인 것은 그녀의 눈물이 아닐까 따위의 생각은 관두기로 했다. 그래서 고개를 돌려 밤하늘을 바라보았다.
        내가 바라보자, 별들은 나에게 빛을 주었다.
        - 본문 중-
    </p>
</body>

-----


    <style>
        *{padding : 0px;
            margin:0px;}
        #wrapper{ width:600px; border : 1px dotted red;}
        #box01{float :right; width:200px;padding:15px; background-color: #ccc;}
        #box02{float :left; width:200px;padding:15px;background-color: pink;}
    /*box01은 오른쪽. box02는 왼쪽으로정렬되서 03은 샌드위치마냥낑기게됨*/
        #box03{ clear:both}
    /*both:밑으로내려감. 왜냐면 오른쪽,왼쪽으로도 가면안된다고했으니까
    left,right,both두개있음*/
    </style>

</head>
<body>
    <h1>Lorem Ipsum</h1>
    <div id="wrapper">
        <div id="box01">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sed massa convallis, cursus leo non, eleifend libero. Suspendisse placerat tincidunt turpis, ut molestie turpis lacinia quis. Duis a felis nec nulla facilisis vulputate. Suspendisse semper accumsan ipsum, et pulvinar metus luctus id. Suspendisse facilisis at est in viverra. Curabitur dui est, efficitur vitae quam sit amet, feugiat bibendum risus. Suspendisse dignissim, massa vitae iaculis tincidunt, nisi mi mollis nulla, eu porta dolor ex non diam.
        </div>
        <div id="box02">
            Mauris eget eleifend sapien. Nunc vulputate tortor a risus tempus dapibus. Mauris porttitor, turpis sed condimentum ornare, lorem justo mollis leo, et tincidunt lacus risus nec orci. Duis at semper velit. Vestibulum consequat mattis lectus quis imperdiet. Vivamus pharetra non nibh ac placerat. Maecenas luctus orci vel fringilla consequat. Suspendisse venenatis laoreet magna, eget imperdiet quam pretium quis. Curabitur et dui at quam faucibus accumsan. Vestibulum ut mauris nec risus rhoncus commodo et et tellus. Vivamus commodo metus vitae tellus hendrerit faucibus. Maecenas augue turpis, convallis eu lorem ut, pharetra egestas ante. Aenean leo elit, convallis nec massa quis, mattis tincidunt mauris. Integer a convallis eros. In hac habitasse platea dictumst. Phasellus posuere eleifend ipsum.
        </div>
        <div id="box03">
            Praesent vitae sapien vitae sem tincidunt fermentum ac et risus. In hac habitasse platea dictumst. Suspendisse potenti. Vivamus non interdum nibh, blandit sollicitudin nunc. Sed maximus molestie vulputate. Quisque accumsan massa a hendrerit consectetur. Integer ipsum tortor, varius vel consequat eget, rhoncus eu nunc. Quisque fringilla vel diam quis ultrices. Aenean euismod, libero facilisis scelerisque elementum, elit neque vestibulum mi, ut hendrerit sem ante ac dolor.
        </div>
    </div>
</body>

-----
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        #menu > p {
            display:inline; /*블록->인라인, 인라인->블록요소로 바꿀수있다. 메뉴1메뉴2메뉴3일렬로나옴*/
        }
        #login{display:none;} /*있는데 안보이는게x,아예안만드는것=none. 안보이게하는건 히든*/
    </style>

</head>
<body>
    <div id="header">
        <h1>제목</h1> 
        <div id="menu">
        <p><a href="#">메뉴1</a></p>
        <p><a href="#">메뉴2</a></p>
        <p><a href="#">메뉴3</a></p>
        <p><a href="#">메뉴4</a></p>
    </div>
    <div id="login"><a href="#">login</a></div>
</div>
</body>
-------
<body>
    <style>
            #body{width:300px; height:300px; border:1px solid red; /*overflow:hidden*/
                /*overflow:scroll;*/overflow: auto;}
                /*overflow:hidden이면,300 300만큼 넘어간 글들은 짤리게된다.(안보이게됨)*/
                /*auto=위아래 스크롤바만생김.scroll은 위아래이동스크롤생기고 하단바는 생기기만함*/
    </style>
    <div id="body">
        <blockquote>드래곤자라</blockquote>
        <p>
            "우리는 별이오."
            "별?"
            "무수히 많고 그래서 어쩌면 보잘것없어 보일 수도 있지. 바라보지 않는 이상 우리는 서로를 잊을 수도 있소. 영원의 숲에서처럼 우리들은 서로를, 자신을 돌보지 않는 한 언제라도 그 빛을 잊어버리고 존재를 상실할 수도 있는 별들이지."
            숲은 거대한 암흑으로 변했고 그 위의 밤하늘은 온통 빛무리들 뿐이었다. 칼의 말은 이어졌다.
            "그러나 우리는 서로를 바라볼 줄 아오. 밤하늘은 어둡고, 주위는 차가운 암흑 뿐이지만, 별은 바라보는 자에겐 반드시 빛을 주지요. 우리는 어쩌면 서로를 바라보는 눈동자 속에 존재하는 별빛 같은 존재들이지. 하지만 우리의 빛은 약하지 않소. 서로를 바라볼 때 우리는 우리의 모든 빛을 뿜어내지."
            "나 같은 싸구려 도둑도요?"
            네리아의 목소리는 슬프지 않았다. 그리고 칼의 대답도 평온했다.
            "이제는 아시겠지? 네리아 양. 당신들 주위에 우리가 있고, 우리는 당신을 바라본다오. 그리고 당신은 우리들에게 당신의 빛을 뿜어내고 있소. 우리는 서로에게 잊혀질 수 없는 존재들이오. 최소한 우리가 서로를 바라보는 이상은."
            어둠 속에서 네리아의 눈이 별처럼 아름답게 반짝였다. 나는 혹시 반짝인 것은 그녀의 눈물이 아닐까 따위의 생각은 관두기로 했다. 그래서 고개를 돌려 밤하늘을 바라보았다.
            내가 바라보자, 별들은 나에게 빛을 주었다.
            - 본문 중-
        </p>
    </div>

</body>

-----

    <style>/*만들때 * {margin:0 padding:0}해놓고 사작하면 디자인하기 좀 편함*/
        *{
            margin:0px;
            padding:0px;
        }       
        /*  position:속성을 통해 문서 상에 요소를 배치하는 방법지정.
            top, right, bottom, left 속성을 통해 요소의 최종 위치를 결정한다.
            아래 세개는 움질일 기준.
            reative:원래 위치에서 얼마나 움직이는지
            absolute:부모의 위치에서 상대적으로 얼마나 움직이는지
            fixed:브라우저에서 얼마나 움직이는지,최 좌측상단 고정*/
        #box{
            position:relative;
            width:500px;
            margin:10px;
            padding:10px;
            border:1px dotted red;
            }
        p{width:150px;
            height :150px; 
            color:#fff; 
            font-weight: bold;
          } 
        .myred{background-color: red;position:relative} 
        .myblue{background-color: blue;
                position:absolute;/*부모기준으로 왼쪽100 위로30*/
                left:100px;
                top:30px;z-index:2;
                }
        .mygreen{background : green;
            position:relative;
            left:30px;
            top:-30px;
            }   
        .myred:hover{z-index:100px;}    /*:hover는 가상 선택자 zindex가높을수록(모니터쪽에가깝다.즉 겹쳣을때 올라오는 우선순위같은거)*/
        .mygreen:hover{z-index:100px;}  /*만약zindex가없을경우 작성순대로 위로 올라온다.제일처음쓰면 맨밑에깔림*/
        .myblue:hover{z-index:100px;} 
        #fixed{
            width:100px;
            height:300px;
            background-color: silver;
            position:fixed;
            right:50px;
            top:100px;

              }   
    </style>


</head>
<body>
    <div id="box">
        <p class="myred"><span>빨간 박스</span></p>
        <p class="mygreen"><span>초록 박스</span></p>
        <p class="myblue"><span>파란 박스</span></p>
    </div>
    <div id="fixed">
        Fixed!!
    </div>

    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>
    <br><br><br><br><br><br><br><br><br><br>

</body>

------

    <style>
        *{
            margin:0px;
            padding:0px;
        }
        ul{
            margin:100px;

        }
        li{
            list-style:none;
            width:100px;
            height:100px;
            text-align:center;
            float:left;
            border-radius:50px 50px 50px 50px; /*순서대로 왼쪽상단,오른쪽상단,왼쪽하단,오른쪽하단의 ★반지름★이다.*/
            -webkit-border-radius:50px 50px 50px 5px; /*사파리*/
            -moz-border-radius:50px 50px 50px 5px; /*모질라재단 파이어폭스*/
            -o-border-radius:50px 50px 50px 5px; /*오페라*/
            color:yellow;
            font-size:50px;
        }

        #ball01{background-color: red;}
        #ball02{background-color: green;}
        #ball03{background-color: blue;}
    </style>
</head>
<body>
    <ul>
        <li id="ball01"><span>C</span></li>
        <li id="ball02"><span>S</span></li>
        <li id="ball03"><span>S</span></li>
    </ul>
</body>

------

    <style>
        div{width:200px;height:200px; background-color: red;color:white;font-size:30pt;
        word-wrap:break-word;}
        #tlate{
            transform:translate(50px,50px);} /*translate(npx,npx)위치이동*/
        #trota{transform:rotate(30deg);} /*rotate(ndeg)=회전각도*/
        #tscale{transform:scale(0.6,0.6);} /*사이즈 조정,원래사이즈에서*/
        #tskew{transform:skew(20deg,10deg);} /*앞으로,밑으로 비틀림*/
        #tran{transform:width 0.5s,background 1.5s linear,transform 1.5s;}
        #tran:hover{transform:translate(100px,0px);} /*hover:커서가올라갔을때 이벤트발생*/
        li{
            width:300px;
            background:gray;
            margin-bottom:3px;
            font-size:30pt;
            font-weight:bold;
            list-style-type:none;
            transition:width 1s linear,color 1s linear,letter-spacing 1s;
            cursor:pointer;

        }
    </style>

</head>
<body>
    <h1>transform</h1>
    <h2>translate</h2>
    <div id="tlate">translate(x,y):위치이동</div>
    <h2>rotate</h2>
    <div id="trota">rotate(def):회전</div>
    <h2>scale</h2>
    <div id="tscale">scale(x,y):크기</div>
    <h2>tskew</h2>
    <div id="tskew">skew(x,y):변형</div>
    <h2>transition</h2>
    <div id="tran">transition:속성 전환</div>

    <h2>MENU</h2>
    <ul>
        <li>학원소개</li>
        <li>과정소개</li>
        <li>채용정보</li>
        <li>커뮤니티</li>
    </ul>
</body>

```
</details>
