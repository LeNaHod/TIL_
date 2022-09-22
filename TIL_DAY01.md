# TIL Day 01(2022_09_22)


## [1]Git Hub와 Git이란
* Git ![깃이미지](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/1200px-Git-logo.svg.png)

분산 버전 관리 프로그램
주로 ***백업, 복구, 협업*** 을 위해 사용
[Git 바로가기](https://git-scm.com/book/ko/v2)

* Git Hub ![허브 이미지](https://mblogthumb-phinf.pstatic.net/MjAyMDA3MTNfOTMg/MDAxNTk0NjM0NjI5NzUw.LxX1Whkaof_e-n3N_wO03lSoZl--YMF8dkgRMxImNk0g.BxwVQn5zShY21jnl8r8ynp0Kg9Ggqf1gtZgSMu970KQg.PNG.nms200299/github.png?type=w800)

Git을 사용하는 프로젝트의 협업을 위한 웹호스팅 서비스
포트폴리오를 자랑할 수 있는 공간. 
[Git Hub바로가기](https://github.com/)


## [2]GUI 와 CLI
> GUI (Graphical User Interface, 그래픽 사용자 인터페이스)
> 
    >유저가 편리하게 사용할 수 있도록 입출력 등의 기능을 알기 쉬운 아이콘 따위의 그래픽으로 나타낸 것이다. 흔히 바탕화면의 폴더나 파일 아이콘같은것

> CLI (Command Line Interface, 커맨드 라인 인터페이스)
> 
    >터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식을  뜻한다.
    크게 입력과 출력으로 나눠져있다.

 위와같이 ***CLI 는 터미널방식***,  ***GUI는 그래픽 방식*** 이므로, GUI가 더 친숙하고 대중화 되어있기때문에 CLI가 다소 생소할 수 있다.


## [3] 어떤 명령어들이있을까?

* 경로와 이동관련
    |이름|내용|설명|
    |:------|:---:|:---:|
    |cd|지정한 경로 로 이동|cd ..하면 상위경로로 이동 |
    |mv|파일이나 폴더를 옮길때 사용|mv 파일or폴더 경로|
    |pwd|절대경로를 출력|~가 절대경로| 
    |start .|현재작업중인곳을 띄워준다.|- |

* 생성/삭제/파일조작

    |이름|내용|설명|
    |:------|:---:|:---:|
    |mkdir|디렉터리를 생성|make directory의 약자|
    |touch|파일을 생성|파일명.확장자 하면 원하는 확장자로 생성|
    |open .|파일을 열어줌|-|
    |ls|디렉터리와 파일 리스트 출력.|옵션 -a를 주면 숨겨진것까지 보임|
    |rm|파일과 디렉터리를삭제|디렉터리안에 파일이있을 경우 옵션-r|

## [4] 예시

```bash
$ mkdir test

$ touch a.txt

$ ls
$ ls -a

$ cd ..
$ cd test

$ rm a.txt
$ rm -r test
```

## [5] VSCODE와 Mark Down은 무엇인가?

* VSCODE(Visual Studio Code,비쥬얼 스튜디오 코드)[VSCODE바로가기](https://code.visualstudio.com/)
  
![VS로고](https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_vscode_icon_130084.png)

### 장점

Windows, Mac, Linux 운영체제를 모두 지원한다.
기존 개발 도구보다 빠르고 가볍다.
Extension을 통해 다양한 기능을 설치할 수 있어서, 무한한 확장성을 가진다.
무료로 사용 가능하다.


## Git Bash 연동하기

터미널을 연다. (Ctrl + `)
화살표를 누르고 Select Default Profile을 클릭한다.
Git Bash를 선택한다.
휴지통을 눌러서 터미널을 종료하고, 재시작한다.
휴지통은 Kill Terminal 로써, 터미널 자체를 아예 종료한다.
닫기는 Close Terminal 로써, 터미널을 종료하지 않고 창만 보이지 않게 만든다.
기본 터미널이 Git Bash로 열리는지 확인한다.



+ Markdown(마크다운)

Markdown (마크다운)은 일반 텍스트 기반의 경량 Markup (마크업) 언어이다.

* Markup (마크업)

마크업 이란? 마크(Mark)로 둘러싸인 언어를 뜻한다. 마크란 글의 역할을 지정하는 표시이다.
HTML도 마크업 언어인데, 글에 제목의 역할을 부여할 때 <h1>제목1</h1> 과 같이 작성한다.

마크다운의 장점과 단점

### 장점
문법이 직관적이고 쉽다.
지원 가능한 플랫폼과 프로그램이 다양하다.
단점
표준이 없어서 사용자마다 문법이 상이하다.
모든 HTML의 기능을 대신하지는 못한다.

### **주의 사항**

마크다운의 본질은 글에 역할을 부여하는 것이다.
반드시 역할에 맞는 마크다운 문법을 작성한다. 글씨를 키우고 싶다고 해서 본문에 제목의 역할을 부여하면 안된다.

-------------------------

## [7] Git 사용과 명령어

- Git의 기본적 순서 
 
  git init -> repository 생성 -> git status 로 파일확인 -> 파일수정 ->저장 -> git add 경로/파일명 ->commit -> 파일수정 ...->반복 의 순서를가지고있다.
    
- 단, **주의사항**으로는 init을 쓸때 **경로**확인을 잘 해야하고 COMMIT -M을 써서 코맨트를달것!
- 반드시 저장 후 , ADD를 해야한다.
- 스테이징 에어리어 = ADD된 친구들이 COMMIT전 모여있는곳.
- 수정을 시작하면 MODIFY모드가 된다.
  
### Git 기본
|이름|내용|설명|
|:------|:---:|:---:|
|git init|repository 생성|디렉토리당 최초 한번,경로설정에 주의|
|git status|파일 상태확인|변경사항이 있는지 파일이 어떤지 체크하기 좋음|
|git add|수정사항을 스테이징에어리어에 올린다.|ADD . 하면 다 올림| 
|git commit|ADD한 내용을 반영해준다|옵션 -M을 사용해서 코맨트를 달아주면 관리하기수월하다. |
|git log|COMIIT 내역확인.|--ONELINE으로 한줄로 출력할 수 있다.|
|git chekout [COMMIT ID]|지정한 COMMIT ID에 시점을 둔다.|-B <브랜치>하면 생성과 체크아웃을 같이|
|git push [주소이름] [repository]명|Git Hub에 로컬 커미션을 올린다.| -|
------------------

### Git Hub 연결
|이름|내용|설명|
|:------|:---:|:---:|
|git remote add [주소이름] URL|Git Hub와 연결한다. |-|
|git remot -v|조회 명령어|ADD 가 잘되었는지 확인할 수 있다.|
|git remot rm [주소이름]|삭제 명령어|잘못 연결했을시,유용| 
    
**※ URL의 끝이 꼭 .git으로 끝나야함.특수문자가 있는지 확인 필수**

-------------------
### Config
|이름|내용|설명|
|:------|:---:|:---:|
|git config --global user.email "이메일"|입력한 이메일로 깃에게 사용자를 알린다.|-unset 명령어로 해제할수있다|
|git config --global user.name"유저네임"|입력한 네임으로 깃에게 사용자를 알린다.|-unset 명령어로 해제할수있다|
|git config --global --list|config리스트를 출력 |config가 잘되었는지 확인할 수 있다.| 

-------------------
### Diff
|이름|내용|설명|
|:------|:---:|:---:|
|git diff|커밋된 파일과 현재수정중인 상태비교|-|
|git diff --staged|커밋된 파일상태와 add된 파일 상태 비교|-|
|git diff HEAD HEAD^|가장 최근의 커밋과 그 전의 커밋을 비교한다 |-| 
|git diff [branch1] [branch2]|branch간의 상태 비교한다.|-| 





## [8] 참고자료

Markdown Guide: https://www.markdownguide.org/basic-syntax/

마크다운 문법 정리: https://gist.github.com/ihoneymon/652be052a0727ad59601

