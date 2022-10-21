# TIL DAY21(22_10_21)

## form action="" method ='post' 에 대하여

form 태그는 post방식을 설정할수있어서 post방식으로 통신할 때 자주이용하는 태그이다.
action=''은 경로를 지정해주는 부분이다. 생략시 action='' 으로 간주한다.

```python
action=""   == ./ == localhost:8000/register/

action="register" == localhost:8000/register/register

action= "{% url 'register' %}" == localhost:8000/register

값은 세개가 똑같지만 의미는 다 다름
```
또한 장고에서 post방식을 사용한다면 꼭 <% csrf_token %>을 붙여줘야 오류가 발생하지않고,
제대로 동작한다.

**CSRF_Token 이뭔데??**

CSRF(cross site request forgery)는 웹 사이트 취약점 공격을 방지를 위해 사용하는 기술이다. 장고가 CSRF 토큰 값을 세션을 통해 발행하고 웹 페이지에서는 폼 전송시에 해당 토큰을 함께 전송하여 실제 웹 페이지에서 작성된 데이터가 전달되는지를 검증하는 기술이다.

csrf_token 사용을 위해서는 CsrfViewMiddleware 미들웨어가 필요한데 이 미들웨어는 settings.py의 MIDDLEWARE 항목에 디폴트로 추가되어 있으므로 별도의 설정은 필요 없다.

**다만 토큰기능을 쓰기 싫으면,**
**settings.py파일안의 미들웨어의 토큰부분을 주석처리해주면 된다.**

## Insert 기능 추가부분

    def insert(request):
    if request.method =='GET': //통싱방식이 get방식이면 요청한다, insert.html을.(insert.html페이지로 돌아가게)
        return render(request,'insert.html')
    
    elif request.method == 'POST':
        myname = request.POST['myname']
        mytitle = request.POST['mytitle']
        mycontent = request.POST['mycontent']
        
	게시판에 글을작성하면 추가해주는부분 위에는 글작성부분 밑은 작성하고 게시판에추가하는부분
	오브젝트가 인서트해줄거야. (저 크리에이트가 이름은 크리에이트지만 사실상 인서트역할.)
	create(마이네임은 새로운 마이네임으로 , 타이틀은 새로운 타이틀값으로...)
	
    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

## 회원가입

1.먼저 회원가입 시 데이터를 저장할 새로운 모델객체를 하나 생성한다.

```python

class MyMember(models.Model):
    myname = models.CharField(max_length=100)
    mypassword = models.CharField(max_length=100)
    myemail = models.CharField(max_length=100)

    def __str__(self):
        return str({'myname': self.myname, 'mypassword': self.mypassword, 'myemail':self.myemail})
```
- python manage.py makemigrations 앱 네임(위의 작업폴더같은경우 dbtest2/ add .) 
python manage.py migrate 앱 네임 (commit)
python manage.py showmigrations 앱 네임 (status와 log사이 )
python manage.py sqlmigrate 앱 네임 migration-name(지정된 마이그레이션의 sql내역)

2.탬플릿 밑에 회원가입.html 을 하나 생성(보안문제상 post로와야한다)

3.views에 post,get방식에따른 if로 처리 get이들어오면 메인페이지로 돌아가게 render함

4.post로 들어오면 변수를 선언해서 들어온 값을 변수에 넣어준다. (ex myname=request.POST["myname"]) 이런식.

5.views에 임포트해서 회원모델을 가져오고 회원모델안에 각 컬럼과 값을 매칭해준다

6.회원모델.save() 저장해줌

7.관리자 페이지에 회원가입해서 추가된것이 나와야한다.(슈퍼유저 생성은 아래에있다.)


```python

from django.contrib.auth.hashers import make_password,check_password

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        myname = request.POST["myname"] #post로 요청된정보중에서 myname의 값만가져와서 myname에넣어줌
        mypassword= request.POST["mypassword"]
        myemail= request.POST["myemail"]
        #mymeber안에 위의 포스트에서받아온 애들을 각각 하나씩 넣는데  마이맴버에는 기본적으로 myname, password가잇으니 컬럼명이라고생각해도될듯
        mymember = MyMember(myname=myname, mypassword=make_password(mypassword), myemail=myemail)
        mymember.save() #저장!

        return redirect('/')
```

## 로그인/로그아웃 기능을 구현

회원가입과 비슷함 단, 비밀번호를 바꿔줘야한다(해시)
먼저, django안의 contrib.auth.hashers를 import해서 

- make_password(패스워드를 해시로변환)
- check_password(해시로변환된 패스워드와 들어온 패스워드값을 서로 비교할때 사용)

```python
from django.contrib.auth.hashers import make_password,check_password

↓↓↓↓↓↓

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        myname = request.POST['myname']
        mypassword  = request.POST['mypassword']

        mymember = MyMember.objects.get(myname=myname)
        #비밀번호가 들어온것과같은지 비교하는문. 위에는 정보를 가져와야하니까 모델 오브젝트를 가져옴.

        if check_password(mypassword, mymember.mypassword):
            request.session['myname']=mymember.myname
            return redirect('index')
        else:
            return redirect('login')

def logout(request):
    del request.session['myname'] #세션에서 마이네임을 삭제해버림
    return redirect("/")
```

## 페이징기능  (Paginator)과 더미 데이터만들기
**슈퍼유저 생성**
 
    1.python manage.py createsuperuser
    2.생성할 사용자이름
    3.사용할 패스워드
    3-1.만약 패스워드가 보안이 취약하다면 취약하다는 각종 경고를날림
    3-2.계속사용할거냐는 질문에 yes or no 선택
    4.생성완료

**django 관리자 페이지 접근하기**

    위에서 슈퍼유저가 잘 생성되었다면
    http://localhost:8000/admin/ 로 이동해준다.
    그리고, 위에서 생성한 계정/패스워드를 입력해서 로그인하고

    admin.py라는 파일을 생성 해 준다. 이 admin.py안에 models객체들을 추가해주면,
    장고 관리자 페이지에서 관리할수 있게된다.
    
    amdmin.py

    from django.contrib import admin
    from .models import MyBoard,MyMember

    #레지스터에 내가추가하고싶은 모델명(models.py에서 생성한 클래스명)을 등록해준다.
    admin.site.register(MyBoard)
    admin.site.register(MyMember)

    장고 관리자 페이지에서는 굉장히 많은걸 할 수있다. 수정,삭제,등록,검색(기본x 구현o)등등
    전반적인 관리가 가능하다.

```python
우선, 페이징을위해 paginator 임포트!

from django.core.paginator import Paginator 

    mybord =MyBoard.objects.all().order_by("-id") #id값을기준으로 내림차순
    paginator=Paginator(mybord, 10) #mybord에서 페이지당 10개씩 보여줄것
    page_num=request.GET.get('page',1) #페이지가 없으면 디폴트값은 1이다. 요청된 페이지의 번호?를가져오는거같음
    #겟방식으로가져온 페이지가 없으면 1을 반환한다(디폴트값이 1)
    page_obj = paginator.get_page(page_num) #페이지네이터를 사용해 페이지오브젝트 생성.(내부적으로 해당페이지의 데이터만!조회하도록'쿼리가변경')
                                            #몇페이지라고주면 지정된 페이지객체를 반환
    #터미널에서 문단 구분용으로*씀
    print("*"*10)

    #페이지 객체를 반환한다.
    print(type(page_obj))

    # 총 모델 갯수
    print(page_obj.count)

    # 총 page갯수
    print(page_obj.paginator.num_pages)

    # 총 page에 대한 페이지를 담고있는 range객체
    print(page_obj.paginator.page_range)

    # 다음에 보여줄게 있는지없는지 여부 판단(has~ is~판단해주는애들이 다수. bool값)
    print(page_obj.has_next())
    # 이건 그럼 이전이겟죠
    print(page_obj.has_previous())

    #아래는 예외처리부분
    try:
        #다음 페이지 숫자
        print(page_obj.next_page_number())
        # 이전 페이지 숫자
        print(page_obj.previous_page_number())
    except:
        pass
    # 해당 페이지에서 첫번째 모델에 대한 인덱스
    print(page_obj.start_index())
    # 해당 페이지에서 마지막 모델에 대한 인덱스
    print(page_obj.end_index())

    return render(request, "index.html", {"list": page_obj})

```

## session(세션)에 대하여

**세션이 뭐야?**

'서버'에서 
'클라이언트의 정보'를 관리하는 객체이다.

그럼 세션과 뭐가 비슷하느냐? 우리가 흔히 아는 '쿠키'(임시저장)와 비슷하다.
다만 쿠키는 클라이언트의 컴퓨터에 임시저장되는 정보이고 별로 중요하지않은 정보(클라이언트입장) 들을 주로 저장

중요한정보는 서버의 세션에서 관리되고 저장한다.

쿠키:클라이언트,중요하지않은정보,서버에 저장 X, 컴퓨터에저장O.(단 브라우저마다 쿠키저장장소가다름)

세션:서버, 중요한정보, 서버에 저장O


## 기타
날짜와 시간 설정

일단 기본적으로 UTC기준으로 맞춰져있다.
그래서 한국기준으로 맞추려면 
settings.py를 수정해줘야한다.

```python
LANGUAGE_CODE = 'ko-kr' #국가 설정
TIME_ZONE = 'Asia/Seoul' #시간대 설정
USE_I18N = True #국제화(Internationalization)
USE_L10N = True #지역화(localization)
USE_TZ = False #장고 시간대
```
데이터필드:간단한 날짜가나옴.
import datetime now
변수.datetime.datetime.now()

타임존:상세한 날짜가나옴.
from django.utils import timezone now
변수.timezone.now()


debug=ture(개발모드)
debug=false(운영모드)

get(id=id)}:get은 값을 하나만가져옴
filter:필터는 복수. 값을 여러개가져옴

## register.html(회원가입 html)

회원가입하는 html은 굉장히 짧다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Register</h1>
    <form method="post">{% csrf_token %} <!--action이 없어도 동작은됨. action=""으로 간주해서 현재경로로 잡힘(localhost/register/)이렇게.-->
        NAME : <input type="text" name="myname">
        <br>
        PASSWORD : <input type="password" name="mypassword">
        <br>
        EMAIL : <input type="text" name="myemail">
        <br>
        <input type="submit" value="회원가입">
    </form>
</body>
</html>

```
