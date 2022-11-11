# TIL DAY28(2022-11-11)

# Linux

버전,실행프로그램: Ubuntu-20.04.5 /VMwarer

## 계정관련

big@ubuntuL~$
:계정@호스트 구조.

sudo apt update : 업데이트할게있으면 리스트로 보여줌

sudo apt upgrade -y : 물음에 y로할거고 update해야할것을 정말 upgrade한다

superuser = admin= root

sudo:super user do. 슈퍼유저'처럼' 사용하는 계정.
다만 sudo계정에서 실행한 로그가남음

sudoers:sudo관련한 파일이 모여있는곳

su:스위치 유저(유저 바꾸기)
su 바꿀계정명 / ★su 만쓰면 root계정으로 로그인한다.

**★다만 이렇게하면 쉘이 한개 더 켜진다고 생각해야한다. 기존에있던 쉘 위에 내가 바꾼유저의 쉘이 켜진것**

쉘과 커널 : 커널을 바로사용하면 위험하니까 쉘 이라는 껍데기로 한번 감싸서 **간접적**으로 **커널을 사용하게**해주는 역할을한다.

그래서 쉘안에 커널이있는 구조.


    ex)멀티를 관리자 계정으로만들어보자
    1.일단 그냥 multi에서 sudo adduser를하면 안만들어진다.(sudoers에 파일이없어서)
    2.그리고 그냥 adduser를하면 관리자만 추가할수있다고함.
    3.sudo usermod -aG sudo multi ->멀티에게 권한을 준다.
    4.su multi
    5.su multi -> 실행x
    6.sudo adduser test 
    7.완성




uid /gid :현재접속중인 계정의 uid(계정아이디), gid는 그룹아이디, groups는 속해있는 그룹목록.

그룹은 여러개를 가질수있다. 

    ex)
    uid=1001(multi) gid=1001(multi) groups=1001(multi),27(sudo) ->지금 멀티가 sudo,multi그룹에 속해있다는소리(추가할수도있다. )
    그룹에 속하게되면 그 그룹이 가지고있는 '권한'도 사용할수있다.

whoami:현재접속되어있는 내계정의 이름확인

useradd 옵션 사용자명:사용자추가

usermode 옵션 사용자명:사용자 정보수정

userdel 옵션 사용자명명:사용자삭제


chmod 옵션 파일명 :'파일'권한 변경

chown  옵션 유저소유자 그룹소유자 파일이름: 지정한 파일의 소유자,그룹 변경

옵션으로 u(사용자부분에) g(그룹부분에) o(그외의부분에) +(권한추가) -(권한삭제) 

    ex)chmod g+x test01 ->테스트01의 그룹부분에 실행권한추가.
    chmod u-w test01 ->테스트01의 유저권한에서 쓰기권한 뺏기

**★/boot :부팅관련디렉터리.** 조심해서 다룰것.

**superuser 로 로그인하는건 자제.**

## 경로

~ : (내계정의)홈디렉터리이다 /home/사용자명 이생략되어있다.

pwd : 지금내가 위치해있는 경로를 보여준다.

symbolic link : 윈도우의 바로가기

cd / :
최상위 디렉터리(root)로 이동 (cd자체는 체인지 디렉터리로 디렉터리 변경명령어)

cd [디렉토리 경로] or 디렉터리명

이동하려는 디렉토리로 이동

cd .

현재 디렉토리

cd ..

한 단계 상위 디렉토리로 이동

cd /

최상위 디렉토리로 이동

cd $변수명

변수에 저장된 경로로 이동

cd ~

cd $HOME

cd 

사용자 홈 디렉토리로 이동

cd ~계정명

입력한 사용자의 홈 디렉토리로 이동

cd -

이전 경로로 이동

/: 루트
./: 현재위치
../: 현재위치의 상단폴더

    ex)cd ./home ->현재위치를 home으로


## 파일생성, 권한, 설치

mkdir 폴더명 :디렉터리생성. 디렉터리는 파란색으로보임

touch 파일명:파일생성

cp 원본명 새로만들것의이름: 원본파일을 카피해서 새로운것으로 만듦


    ex)/home/test의 위치에 multi02를 생성 밑 확인
    sudo cp multi01 /home/test/multi02
    cd /home/test
    ls
    multi02

mv : 기본적으로 이동명령어인데, 이동하면서 파일이름을바꾸고 경로를지정해줄수있다.

mv 기존(파일,폴더)명 경로/바꿀이름

or 

mv 기존(파일,폴더)명 / mv 기존(파일,폴더)명 경로

ls : 현재위치해있는 경로상의 파일,폴더 리스트 출력

drwx: d는 디렉터리. 파일이면 -  

**drwxrwxrwc : d/ rwx(유저권한,소유자권한) / rwx(그룹권한)/ rwx(모든유저권한,다른그룹의 애들이 사용할수있는권한을 의미한다.)**

숫자로도 표현할수있는데, 각각 **rwx(421)**이다. 
총7이고 0~7까지로 나타낼수있다.

권한종류가 **세개**니까 **777**로 표현가능

    ex)chmod 777 test01 -> 유저/그룹/그외의 권한을 모두 rwx가능하게

**※대중적으로 755가 가장 보편적이다. 777은 위험**

apt : 데비안계열 패키지 인스톨러! apt install 설치할것

wget : **web get의 약자. 웹상의 파일을 다운로드**받을때 사용하는 명령어이다. 비상호작용 네트워크 다운로더인데, http,https,ftp 프로토콜, http proxxy에서 데이터 가져오는거 가능!

### 그외에 

rpm(의존성 관련 패키지들은 모두'직접설치'해야함) 

yum(rpm기반이긴한데 의존성문제해결, 자동설치!임)


### 의존성이뭔데?

리눅스에서 패키지를 설치할때 필요한 라이브러리의 버전호환,설치유무
보통은 알아서 설치가되지만 어떠한이유로 제대로 설치가 되지않았을때 의존성문제가 생기면서
정상동작이 되지않음.

### 압축파일 종류

tar :속도 빠름/ 압축률 낮음 / 확장자 .tar

**gzip(★) : 속도 보통 / 압축률 보통 / 확장자 .gz**
**파일하나하나만 압축가능, 그래서 tar와 같이사용(*,tar.gz = tgz)**

bzip2 :속도 느림 / 압축률 높음 / 확장자 .bz2

압축을 실행하려면: **파일 -xvzf**

->압축해제하고 처리정보를 출력할건데 z는 gzip파일사용하고
여러개의 파일을사용한다.

tar **-cvzf** 생성할압축파일명.확장자 압축할 파일명 : 파일압축하기

tar -xvzf 파일명 :압축해제

-------
단어[tab] : 단어로시작하는 자동완성

ls -lh : 파일,폴더별 사이즈

**ls -a**: 숨김파일도 보여줌. 

**단, 이름앞에 '.' 이붙은애들은 다 숨김파일이다.**

**cat:** 연결시키다(con'cat'enate)의 cat이다. **파일의 내용을 출력**하는데 사용한다.

----------

## vim , crontab

vim은 리눅스 편집기 중 하나이다.  

vim을 제외한 다른 편집기 종류로는 아래와같은게있다.

- emacs(매크로기능o)
- ★nano(pico복제버전. 자동 들여쓰기,정규표현식 검색 등등)
- pico(유닉스기반, 메모장과 흡사)
- gedit(uf8과 호환하며 텍스트편집. **텍스트기반 콘솔에서는 사용x**)

vim 파일명 : 파일을 vim으로 오픈.

기본은 r. 읽기모드이다. 아무거나 누르면 편집모드, w할수있다. 입력가능해짐

- esc:취소
- : 라스트라인모드 
- o:한칸아래로
- :q!:저장안하고 종료
- :wq!:저장하고 종료

![vim단축키](https://gmlwjd9405.github.io/images/etc/vim-shortkey-keyboard.png)

[이미지출처](https://gmlwjd9405.github.io/2019/05/14/vim-shortkey.html)


### crontab 스케줄러같은것. 설정해놓으면, 지정해놓은 시간에 실행시켜준다

crontab -e :cron작업설정,  *****(분 시 일 월 요일 명령 순서) 명령어
->설정하고 : 입력 후, wq로 빠져나오고 crontab을 갱신시키면 설정해놓은 시간에 명렁어를 실행한다.

crontab -l : cron 작업리스트 확인

crontab -r : crontab 삭제

## 파일설치와 PATH설정

sudo apt install openssh-server -y
sudo apt intsall ssh-askpass -y : 통신할때 매번 y누르는거 패스해주는것

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 공개키 암호화=비대칭 키 암호화.

**암호/복호화 의 키가 서로 다름!**

### 심볼릭 링크(바로가기)를만들자

ln -s amazone[tab].[tab] java (탭할때 공백있으면안되고 아마존자리에는 하고싶은 파일이름)

ab.aa

ab.ab 

이면 ab.[tab]

### PATH등록
```
exprot JAVA_HOME=/home/big/java JAVA_HOME이라는변수에 경로를넣고

export PATH=$PATH:$JAVA_HOME/bin PATH라는변수에 $PATH,PATH에있는값을가져와라, $JAVA_HOME의 값을 가져와라, 

그래서 최종적으로 home/big/java/ (<JAVA_HOME변수값)bin 이되고, 이게 PATH에들어가게되는것 

★경로에 공백있으면안됨!!!
```

sudo vim ~/.bashrc (vim으로 bashrc열기)

.bashrc:가장나중에읽어지는데 배쉬창이 열릴때 실행된다.

source ~/.bashrc :.bashrc를 적용시키려면 껏다켜야하는데 그 작업을 건너뛰고 바로적용

## Linux에서 한글설정하기

settings -> region & language ->  + 클릭 -> ... 클릭 ->  other -> korean -> add -> english(us) 삭제 

manage installed languages -> install -> install/remove languages -> korean -> 재부팅

settings -> region & language ->  + -> ... -> other -> korean(hangul) -> add -> korean 삭제 -> korean(haugul) 톱니바퀴 -> hangul (toggle key) 삭제

+)시간설정

settings -> date & time -> timezone -> seoul
