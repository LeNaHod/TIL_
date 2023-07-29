# TIL DAY 35(2022-11-23)

## 장고특강

**데이터베이스랑 연결될 모델파일이있는앱**만 인스탈드앱에 **추가**해도되긴함

>작업전에)</br>새로운 프로젝트를 만들거니까 cd ..으로 터미널 경로를 최상위로 이동해준다.</br>최상위 경로에서 django-admin startproject 프로젝트폴더명 입력


```python

#settings.py


#DB설정

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql', #연결될 db명.내가 다른 db를만들면 그db의이름
        'USER':'사용할유저명',
        'PASSWORD':'사용할유저의패스워드',
        'HOST':'localhost',
        'POST':'포트번호'
    }
}

#언어,시간설정

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False

시간,언어설정을 바꿔줬다 ↑

#스태틱

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/'static'] ->스태틱파일이 실제로 어디에들어갈것인지 경로


https://docs.djangoproject.com/en/4.1/howto/static-files/
->스태틱 파일을 어떻게쓰는지 매뉴얼 주소

스태틱_ROOT:이 프로젝트말고 프로젝트외부에있는 폴더를 스태틱 폴더로 쓰고싶을때 사용한다

스태틱_ROOT:경로



#models.py


★주소록을 하나 만들어보자(데이터베이스  생성이라고 생각하면됨)

from django.db import models


class Member(models.Model):
    id=primary_key =True ->프라이머리키를 설정했다. 꼭 컬럼 이름이 id 여야 할 필요 없다. 장고는 primary_key =True 값을 준 컬럼이 있다면, 프라이머리키를 자동생성하지않는다.
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addr = models.CharField(max_length=1000)
    email =models.EmailField()
    birth=models.DateField()

    def __str__(self):	->클래스를 호출했을때 class대신 호출되는친구 __str__안의 내용이나온다.
        return str({'id':self.id,'name':self.name,'age':self.age,'addr':self.addr,'email':self.email,'birth':self.birth})


★프라이머리키를 지정해주지않으면? 알아서 id 컬럼을 추가해서 id가 프라이머리키가된다

#터미널

1.python manage.py makemigrations bonus ->마이그레이션 진행(적용x/테이블생성 해준다고 생각하면됢)

2.python manage.py migrate ->마이그레이션 적용(생성한 테이블 적용)


단,경로에 주의. 장고 처음만들때도 경로에 주의해야한다

#index.html(장고탬플릿.홈이름이 index)

{%} ->이런식으로되어있는애들은 명령어이고
{{}}-> 변수가된다. html의 값이됨


{% url 'insert' %} ->원래는 /insert 이런식으로쓰는데 경로가 자꾸바뀔수있으니 1번방식이 더 낫다. urls.py의 path name이 insert인 친구를 불러오는것!


<input type="button" value="Delete" class="my-btn delete-btn layout-right" onclick="deleteMember({{ member.id }}, this);"> ->this  =  클릭 이벤트를 발생시킨 input태그가 된다.그 input태그의 정보

#views(요청이들어왔을때 요청에대한 처리)


from django.shortcuts import render,redirect
from .models import Member
from django.http import JsonResponse


def index(request):
    members =Member.objects.all()
    print(members)
    return render(request,'index.html',{'list':members}) ->render = 탬플릿 레이어에있는것을 그린다. {list:members}의 값으로 값을 채워서

↑주소가 index.html로 요청되었을때 무엇을 응답해줄건인가 처리해주는것


def insert(request):
    name = request.POST['name'] ->index.html의 액션 리퀘스트.post의 name이라는 값을가져와서 변수name에담음
    age = request.POST['age']
    addr = request.POST['addr']
    email=request.POST['email']
    birth = request.POST['birth']
    Member(name=name,age=age,addr=addr,email=email,birth=birth).save() ->클라이언트에게 값을 입력받아서 저장.리다이렉트이기때문에 저장하면, index페이지로 다시돌아가기때문에 저장된 내용이나온다.
    return redirect('index') ->redirect 인덱스를 다 그린다음 다 그린 인덱스를 돌려준다. 클라이언트에게 응답하다가 다시 서버로 돌아가는구조


def delete(request,id):
    deleteMember = Member.objects.get(id=id).delete()

    if deleteMember[0] > 0:
        return JsonResponse({'msg':'success'},status=200)
	->JsonResponse=딕트형태로 데이터가들어오면 알아서 JSON으로 바꿔준다.
    else:
        return JsonResponse({'msg':'fail'},status=500)

def delete는 비동기통신으로 되고있다. 그래서 data만 주고받는다. 그걸 json으로 받을것임


#urls


from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'), ->이 path의 대한 이름
]

#members.js

function deleteMember(id, member) {
    xhr = new XMLHttpRequest();
    xhr.onreadystatechange=function(){
        if (xhr.readyState==4 & xhr.status == 200) {
            if(JSON.parse(xhr.responseText)['msg'] == 'success'){
                member.parentElement.remove();
            } else {
                location.href="/";
            }
        }
    }
    xhr.open("GET", "/delete/"+id);
    xhr.send();
}

최종적으로는 index.htm안에 삭제버튼이눌린 input태그의 부모의 부모를삭제하게된다.


```

# TIL DAY 37(2022-11-25)


일반통계분석과 ML / DL

- 일반통계분석 : 어떤값을 계산해서 평균을내거나 **학습하지않고** 통계를내는것
- ML / DL : 여러 학습모델로 입력데이터셋 (X) 를 **학습하여** 출력데이터(Y)를 내는것

    EX) 
    1.입력데이터셋을(X) 꽃의 잎의 크기 ,색상 ,종류 , 브랜드 등을 주고 원하는 학습모델(지도,비지도,군집 등등)로 학습시켜서
    꽃잎의 크기나 색상을 입력하면 X를 토대로 출력데이터(Y값)을 보여준다.

    2.입력데이터를 부동산을 넣고 부동산의 가치(Y)를 측정할수도있다.

    3.체스를 위치를 주면 다음 체스위치를 지정하는것 등등


- 즉, 학습하여 **예측**/**군집**/**분류**를 한다.


![기본작동구조](/M_D.PNG)


기본적으로 예측은 위와같다



![지도학습](/%EC%A7%80%EB%8F%84%ED%95%99%EC%8A%B5.PNG)

지도학습 구조




[참고자료](https://hyeshin.oopy.io/ds/data/20210125_ml00_overview)




