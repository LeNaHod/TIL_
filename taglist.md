# 태그정리

- nav(네비게이션):목록생성(ul,li,ol)과 같이 쓰는게 일반적.nav안에 목록태그들을 주로쓴다.
    주로 nav>ul>li>li안에 a태그 보통 링크메뉴들을 넣을때 사용한다. 즉 메뉴바는 nav

- text-align:center,left,r..(텍스트정렬)
- text-decoration-라인,스킵,스킵링크,컬러,스타일.. / text-decoration-line:none(밑줄없애기),underline(밑줄생성),through(취소선),overline(줄이 위에생김)
- resize:none=조정불가 / both=높이와 너비 둘다조정가능 /horizontal=너비만 조정가능 /vertical=높이만조정가능 /initial=해당속성의 기본값으로지정. 이건 다른 태그도 마찬가지/inherit=부모요소의 속성값 상속
    inline 요소나 overflow:visible 인 block 요소엔 적용 안 됨.
    overflow 속성값이 "scroll", "auto" , "hidden" 인지 먼저 확인하고 보통 overflow:auto와같이씀

보통은, overflow:auto 와 함께 사용.
- imag:url(""):css에서 이미지 가져오기
- line-height:n px 텍스트 위아래 줄  간격
- vertical-align: top,middle,bottom(이미지+텍스트를 같이 중앙정렬할때 많이씀) 수직정렬.
  ex)verticla-aling + line-height

    vertical-align를 폰트에 잘 안쓰는이유
    정의:해당 엘리먼트의 middle을 부모의 baseline + x-height / 2 로 정렬합니다.(폰트)
    폰트의 베이스라인 +x-height(베이스라인으로부터의 높이)/2 이기때문에 middle을써도 중앙정렬이안된다.

-  list-style: none; =li 동그라미 없애기.



