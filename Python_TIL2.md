Python TIL2(22_09_08 ~ 22_09_09)

# [1] For,list For, 흐름제어,중첩
- for와같이쓰는 함수들 대략 정리

- enumerate(객체 or 시퀀스값,start=n[생략가능 기본0])
    ->시퀀스 객체나 시퀀스값을 인덱스랑 매치시켜줌 start를이용해 시작할 인덱스값지정가능

- zip(객체1,객체2,strict=Flase[생략X 기본 펄스])
    ->두개이상의 시퀀스 객체를 각각 인덱스0번부터 매치시켜줌
      옵션이 기본 펄스인건 데이터갯수?속성이 안맞아도 0번부터 알아서매칭해주고
      트루면 무조건 맞춰줘야한다.

- ★enumerate, zip은 아래 매개변수있는 함수쪽에서도 다뤘다.

- range ->텍스트 출력 길이조정 range(start,end-1,step_size)
- range(스타트,마지막길이-1,스탭사이즈)
       리스트나 for문에 자주씀
       list(range(10,20,5))이런식이면 10-20까지의 리스트를출력하는데 거기서 -1을함
       그래서 10-19까지의 값에서 5씩증가 즉 10 15 만나온다는소리 20안된다.
       마지막숫자를 안써주면 기본 0에서 스타트번호까지나옴(리스트로 묶었을경우 0~스타트번호)
       그냥 range(n)으로쓰면 0,n이렇게만나옴.

<details>
<summary>for list/for/흐름제어문,중첩문 예제</summary>

```python

#for문을 이용해서 1-10까지 출력
#*sep는 리스트,튜플 등 시퀀스(순서자료형)에는X

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c=0

for a in b:
    c += a      #c는 토탈값,즉 sum이고 for a의 값을 더한다.
                #객체변수 a에는 b의값이 하나하나씩 대입이되는거니까 a=1 한순환끝,a=2순환끝
                # c +=a 는 c= c+a라는의미니까 0(c)+a(b의리스트값,1,2,3,...)
                #그리고c또한반복이기때문에 더한값이 자꾸 누적되는것
else:
    print(c)

#for 를 이용해 변수두개받기 (리스트,튜플)

c=[(1,2),(3,4),(5,6)]        #리스트 1,2가 인덱스0번지, 묶여있는게 한세트

for (a,b) in c :            #a,b라는애가 in에서 2개만 출력하는것, a,b는1,2
        print(a,b)          #c에서 a,b 즉 리스트의 첫번쨰 두번재 저 형식대로 가져오는것.
                            #출력도 a,b로하면 당연히 c에서가져온 각 묶음의 앞 두개의숫자 출력함
                            #그래서 중요한건 가져오려는갯수와 출력하려는 갯수가 같아야한다
                            #ex) c안에 (1,2),(3,4),(5,6)인데 for에서 (a,b,c)를 가져온다면 오류남!

#enumerate,zip

for x,y in enumerate(['abc','111','322','4444'],start=111):    #스타트값은 enumerate갯수만큼 증가
    print(x,y)                                                 #여기는 x자리에 스타트번호 y에는 enumerate안의                                                   리스트값


print('사용x')            #이거는 range와len이용. ragne안에는 숫자가와야하니까 len으로 a의 갯수를 세어가지고옴 3
a=['111','222','333']
for i in range(len(a)):         #그러면 이제 i가 100에서부터 세개만큼증가함(a의갯수만큼)
    print(i+100,a[i])



a01=[1,2,3,4]
a02=['a','b']
for res in zip(a01,a02 ,strict=False):
    print(res)              #이건 각각 변수의 값들과 하나씩 매치함 1은 a 2는b
                            #FALSE를 쓰는이유는 저렇게 두 변수가 데이터의 길이가 달라도
                            #알아서 처리할수있기때문임. TRUE쓰면 데이터갯수안맞으면 큰일
#1. zip
names = ['홍길동', '김길동', '이길동']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)

#2. 추가된 목록
points = [100, 85, 90]

for name, age, point in zip(names, ages, points):
    print(name, age, point)


#zip_logest(iter1,....fillvalue=20)
#3. 추가된 목록을 이용해서 없는 데이터는 None로 채움
from itertools import zip_longest   #itertools에서 zip_longeset을 불러와서실행 꼭불러와줘야함
                                    #개수가 남는부분,즉 잉여값은 None으로 처리함(오류x)
names = names = ['홍길동', '김길동', '이길동','최길동']
ages = [24, 50, 18]

for name, age in zip_longest(names, ages):
    print(name, age)


#4. 추가된 목록을 이용해서 없는 데이터는 값 20으로 채움
for name, age in zip_longest(names, ages, fillvalue=20): #위와같은건데 값20으로채움
    print(name, age)


#5. 추가된 목록을 이용해서 없는 데이터는 값 20으로 채움
points = [100, 85]
for name, age, point in zip_longest(names, ages, points, fillvalue=20):
    print(name, age, point)

★for list를 알아보자★

#1 구문을 살펴보기
res =[a**2 for a in range(10)]  # 리스트로 묶었기때문에 a가 0부터9가될때가지(range가10이라 0-10인데 -1한값까지만)
                                #튼a가 9가될때까지 a(1,2,3,4,5,5,6..)**2(제곱)을 반복
                                # **2 는  2제곱
print(res)

for+if 를 리스트로
[수식 및 리턴변수 (3) for 변수(2) in 시퀀스(1) if 조건식]
    #ex)my_list = [a for a in range(10) if a % 2 == 0]
        #->a먼저 선언하고, 또 a를 for에서 리턴값을가져오는 변수로 선언하고 마지막에 조건식


print('for 문을 조건식과 함께 출력 해보자')

odd_even=[]
for i in range(10):
    if i%2 == 1:
        odd_even.append('odd')
    else:
        odd_even.append('evenn')
print(odd_even)

else값이 있는 for+if 리스트
#변수명 = [true리턴값 if 조건식 else false리턴값 for 변수 in 시퀀스]

odd_even=['odd' if i % 2 ==1 else 'even' for i in range(10)] ,와 줄바꿈이없다. 위,아래 같은결과

#7 zip을 이용해서 list for

names = ['홍길동', '김길동', '이길동']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)

a = [(name,age)for name, age, in zip(names,ages)] #(a,b) for 객체1,객체2 in zip(name,ages)
                                                  #객체 1,2를 zip함
print(a)

#zip

#목록을 한꺼번에 묶어서 리턴 1,10 : 2,20: 3,30
for x ,y in zip([1,2,3],[10,20,30]):
        print(x+y)


#목록을 묶어서 set으로 리턴
print(set(zip(['a','b','c'],[1,2,3])))

#목록을 묶어서 dict으로 리턴

keys=('cat','dog','duck')
valuse=('야옹','멍멍')
#a=('ad','dd','aaa')
print(dict(zip(keys,valuse)))


#outer for 와 inner for
# ↓ 기본형
for 변수 in 시퀀스 :   ---outer for
    for 변수 in 시퀀스 :  ----inner for
        명령

#응용 중첩for를 이용해 구구단을출력
print('1.중첩 for를 이용해서 구구단을 출력해보자')

for a in range(2,10):    # outer 2~9. 앞의숫자 n*m의 n
    print(f'나는{a}단')
    for b in range(1,9): #ineer 1~8 뒤의숫자  n*m의 m
        print("%d * %d = %d" % (a,b,(a*b)))

    print(end="\n")


print('case 1')
l1 = [1, 2, 3]
l2 = [10, 20, 30]
for i in l1:             #1,2,3이 각 이너의값을 하나씩 매칭.
    for j in l2:        #10,20,30 .. 10,20,30 위의 아웃for가 끝날때마다 초기화
        print(i, j)     # 1 10 2 10 1 30 2 10 2 20 2 30 .식으로 나옴.
```
</details>

# [2] 함수선언,호출

### 함수만들기

def 함수명:
    
소스코드
    
return 리턴받을값

### 매개변수있는 함수

def 함수명(매개변수. 매개변수:타입 ok):

return (매개변수)

※만약 def위에 a=1 선언해놓고 def안에 a를 넣고 리턴값도a
이면, 밑에 매개변수를 호출하면 1이나오는게아니라 내가입력한값이나오고
a라고 입력시에 1이나오게되는것!

    [형식]
        def 이름(변수,*가변변수(튜플이나리스트),**가변변수(딕트형))
            소스
            return
-  호출할떄 데이터와 함수의 선언된 변수의 타입은 가변이 있을 경우 맞아야한다(순서맞고 갯수맞고 튜플 딕션맞고 이런거)

- 가변없을 경우에는 1:1개수로 결정된다.

- 함수선언시 일반변수는 초기값을 가질수있다 def 이름(1): 


- enumerate: 시퀀스의 인덱스값과 시퀀스의값을 매치하고싶을때 주로 사용
    for랑 같이씀. enumerate(객체 or 시퀀스값(리스트,튜플 등))

- zip:  두개이상의 시퀀스'객체'를 하나로 순서대로 매치해서 묶고싶을때
    zip(객체1,객체2,strict=False<옵션!)
    false를 쓰는이유는 객체1,2..등의 데이터 갯수가 안맞아도 알아서매칭 해주기 때문이다.
- self 는 주소값을 전달해주는데 self를 안써도 파이썬 내부에서 자동으로 주소값을 넘겨준다.
- 또 self자리에 다른이름으로 넣으면 self자리에 있는 인자가 주소값을 전달해준다.
- self는 함수내부에 접근할수있도록 해주는것
<details>
<summary>함수예제</summary>

## Funtion2(생성,사용)

```python

#기본
def getA():
    return 100
def getB():
    return (1,2,3,4)
def getC():
    return [1,2,3,4]
def getD():
    return '"abcd"'
def getE():
    return "'A'"
def getF():
    return {'a':('a','b','c','d','e')}

if __name__ =='__main__' :
    print(getA())
    print(getB())
    print(getC())
    print(getD())
    print(getE())
    print(getF())

#매개인자가 있는 리턴형 함수를 만들어보자.
#리턴은 현재함수를 종료하는키워드
#지역변수는 def안에서만 쓸수있음.즉,def A안의 D라는애와 def B안의 D라는애는 서로다르므로 저 이름이 같아도됨
#단 매개변수의 갯수와 입력하려는 갯수는 동일해야함
#*args ->인자를 여러개받는다.함수내부에서는 튜플로받는것으로 인식


def getTot(a,b,c):
    a=a+b+c
    return a


if __name__ == '__main__':
    print(getTot(1,2,3))


#매개 인자 있는 함수를 구현하자.(리턴이 x)
#매개변수에 기본값이있으면 아무것도 안넣었을시 기본값반환
#아래처럼 이름이 겹쳐도 기본값이 있고없고에 따라 중복여부가갈림 = 오버로드

def Test(a=1):
    print(a)

def Test():
    print('None')

def getB(*args):            #꼭 args가아니여도된다. 하고싶은 이름대로
    print("여기부턴 args입니다.")
    return args

if __name__ == '__main__':
    Test()    #이름이 같으면,동일한 타입의 매개인자가있는 함수가 우선순위를가진다
    print(getB("%d,%d,%d" %(1,2,3)))

#5.리턴 타입과 매개인자의 타입을 가변으로 설정을 해보자.
#하나이상의 데이터를 리턴

def getTest():
    return 1,2;

def getTets02(*a):
    print(a,type(a))

def getTets04(d,*a,**b):     #dict형
    print('d=',d)            
    print('a=',a)            #가변인자를 섞어쓰고싶다 *,** 저거두개를 다넣을수있다.
                             #단, dict형(**)가 무조건뒤로오게.
    print('b=', b)           #순서는 단일인자->*->**순서이고 입력순대로 그 자리에 대입된다.


if __name__=='__main__':
        getTets02(1,2,3,4,5)
        getTets02(1, 2, 3)
        getTets02(3, 4, 5)
        getTets04(1,2,3,4,5,a=1,b=2)

#exam

#for list를 이용한 5배수 출력

#방법1
res =[a-1 for a in range(1,101,5)]

print(res[1::])

#방법2
def ppp():
    a=range(1,101)
    return a

#이름,국어,영어,수학을 main에서 입력받아서 getTOt(국,영,수)점수를 전달해서
#총점을 리턴받고,getAvg()를 통해 평균을 리턴받는다.getGrade()를 통해 학점리턴

import datetime

def sum_list(_list:list):
    m_dic = ['이름', '국어', '영어', '수학', '총점', '평균', '학점']
    result = 0
    for num in range(1, len(_list)):
        result += _list[num]
    g_avg=round(result / 3,1)
    if g_avg >= 90:
        a=[result,g_avg,'A학점']
        _list.extend(a)
        b = dict(zip(m_dic, _list,strict=False))
        for i,n in b.items():
            print(f'{i}:',n)
    elif g_avg >= 80:
        a = [result,g_avg,'B학점']
        _list.extend(a)
        b = dict(zip(m_dic, _list,strict=False))
        for i,n in b.items():
            print(f'{i}:',n)
    elif g_avg >= 70:
        a = [result, g_avg, 'C학점']
        _list.extend(a)
        b = dict(zip(m_dic, _list,strict=False))
        for i,n in b.items():
            print(f'{i}:',n)
    else:
        a = [result, g_avg, '재수강']
        _list.extend(a)
        b = dict(zip(m_dic, _list,strict=False))
        for i,n in b.items():
            print(f'{i}:',n)
    return sum_list

if __name__ == '__main__':

    sum_list(['스폰지밥',80,90,70])
    print(datetime.datetime.today().strftime('%y-%m-%d/%H:%M'))
```
</details>

------------------

# [3]고차함수

### 고차함수란?

고차 함수(Higher order function)는 함수를 인자로 전달받거나 함수를 결과로 반환하는 함수를 말한다. 다시 말해, 고차 함수는 인자로 받은 함수를 필요한 시점에 호출하거나 클로저를 생성하여 반환한다. = 함수의() 전달 받는 매개인자를 함수로 가진형식을 말한다


- 1-1)   filiter(funtion or None, iterable(시퀀스자료형)-->filter object
                   (조건함수         , 목록)목록이 조건함수 트루값만 가져다가 필터링하겠다.
                                          =목록의 데이터를 조건함수에 대입시켜 맞는애(true값)만 모아 리턴
- 1-2)    map(func,*iteralbes('*'이 오면 리스트,시퀀스,문자열(딕셔너리X))) --> map object
              ->연산 후 리턴.
- 1-3)    functools 모듈의 reduce 
              from functolls import reduece
              reduce(function,iterable,[, initial])->value(단위값)
    - 1-3은 집계를 수행하는 함수와 시퀀스를 매개인자로 갖는다. 누적데이터
    - 1-2에서 넘겨받아온애들을 집계하는거임 더하거나 뭐 모으거나해서 값으로만드는거임
    - 1,2는 오브젝트를 반환하기때문에 pirnt할때 list를써줌 아니면 출력아무것도안함
  
- 1-4   스코핑룰(scoping) : 함수,클래스를 선언하면서 변수를 사용하게되는데
        선언된 변수를 저장할때, 네임스페이스(저장영역)에 저장하고 호출될때 네임스페이스의 영역의
        우선순위를 갖는 것을 말한다. 지역 전역 내장 함수냐 지정해주는거

        LGB: 변수를 찾을 우선순위를 Local -> Global-> Built-in 순서
        Local(지역)  함수 내부에 선언될 때의 영역을 말한다
        Global(전역) 함수 외부에 선언될 때의 영역을말한다
        Built-in(내장) 파이썬에서 제공하는 함수의 영역을 말함

        MR(Map의약자)작업을 잘해줘야 데이터 처리할때 편함
        Map = Reduce(M/R)
        1번작업  2번작업

        Map에 모든데이터를넣음. 특징량은 숫자로(01010)로들어오는데
        각 들어오는 단어를 판단해서 있으면 1 없으면 0
        예를들어 a와 b라는 txt파일안에 각 우리는 이라는 단어가 한번씩들어가있으면
        a.txt=우리는 1
        b.txt=우리는 1
        a라는파일에 한번이고 b라는 파일에 한번이라서 각1개씩들어감
        이 작업이 컨바이너고
        *컨바이너=맵과 리듀스의 중간에있는데 데이터를 분철해서 리듀스에넘겨주는것

        최종적으로 리듀스에는 우리는2가 담기게되는것.
        컨바이너(맵)+리듀스 -> mr작업이라고 부름(테이터를 집계한것)
        m(c,컨바이너)r


<details>
<summary>고차함수+함수</summary>

## Funtion3+고차함수 

```python

#f리스트 객체로 리턴하는 for 내부연산

a = [1, 2, 3]
print([x * 2 for x in a])
print([x * 2 for x in a if x == 3])
print([[x, x * 2] for x in a])              #x에 1,2,3 x*2에 2 4 6이여서 [x,x*2형태]
print([(x, x * 2) for x in a])

b = [4, 5, 6]
print([x * y for x in a for y in b])        #다중for. 4*1 5*1 6*1 4*2 5*2 6*2...의형태
print([a[i] * b[i] for i in range(len(a))]) #a의 0번째인덱스 * b의0번째 > 1번째 * 1번쨰
                                            #인덱스끼리 연산하면 리스트값의 연산이된다는것.

#재귀함수(recursive 자기 자신을 호출하는함수. 자기 자신을 호출하면 재귀호출)
#goto 함수와 재귀함수는 실행속도가느리기(부하가심하기때문에)자주안쓴다 재귀함수>goto(타프로그램)
#선언된 함수 : 인라인 32비트용 프로그램에서 7줄이하는 속도저하
#위의 세가지는 속도저하가심함. 파이썬은 1번문제(goto문)은 아예없앰으로써 해결
#함수 ->객체 ->모듈 (3번해결)

def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

if __name__ == '__main__':
    print(sum_n(5))

# 5 + 4 + 3+ 2+ 1의 형태가되는것임. 5+(5-1,4-1,3-1,2-1) 정확히는 저5도 계속줄음 리턴만나서올라가니까

x = 50
def func():
    global x  #값 50
    print ( 'x is' , x)
    x = 2       #얘는 지역(로컬) x임. 글로벌이아니므로 2를가짐
    print( 'Changed global x to' ,   x) #2를출력
if   __name__ == '__main__' :
    print(func())   #리턴값없어서 none나옴
    print(x)        #글로벌을 주석처리하면 50나옴 주석풀면 2출력
                    #지역x는 펑션외부로 못나옴. 그래서 글로벌을주석처리해버리면 전역50을가져오고
                    #주석이 없으면 지역x를 가져옴
                    #전역변수에 재대입하는 개념을 가지고있다 그래서 def밑에 if문에 같은이름의 새로운변수를 넣으면 그값이 재대입되서출력됨
                    #if부분 메인에선 글로벌 쓰면안됨  펑션이나 맨위에

#생성순서, 함수의 주소,이름을 알아보자

import dis  #함수를 선언 ->클래스의 인스턴스를 생성함 ->함수객체 -> 함수이름과 동일한이름에게 할당
            #위의 처리과정을 다 거치고 바이트코드를 호출시행함
            #*id(변수명)은 주소값을 돌려줌! 이름으로 구분못할때 아이디로 비교함

def my_fun():
    print( 'Hello, python !' )
                            #def나 변수를 선언하게되면 내부적으로 클래스인스턴스를 생성해 메모리에올림
                            #그래서 우리가 dir했을떄 볼수있는것.
if   __name__ == '__main__' :
    print(vars()) #함수의 변수 사전 이게 dir하면 나오는애긴함. 등록된 목록이 호출되는것
    print(my_fun)  # 함수 이름을 객체로 확인 이름없으면 주소로나오는데 at 0x000002011c이렇게
    print()
    print('함수의 타입',type(my_fun))
    print('함수이름과 동일한 이름의 젼역변수로 할당' , my_fun.__name__)
    print('함수호출실행(바이트코드)',my_fun.__code__)
    print('함수호출실행 16진바이트 코드',my_fun.__code__.co_code.hex())
    print('<<< dis모듈확인>>>>')
    print(dis.dis(my_fun))      #이게지금 생성 순서를 알려줌 **중요. (dis.dis함수이름)
    print(dir(__builtins__))

  # 중요! .__name__은 함수의 이름을 호출해줌
  #__code를쓰면 주로 경로와  16진코드로 호출이고
  #__name__는 함수이름을 반환한다.

#고차함수

#1)고차 함수중  filter함수를 사용해보자.

def f(x):
    return  x %2 !=0 and x %3 != 0   #2와 3이아닌배수의값을 추출해서x에넣음

#1-1) 짝수만 출력
def even(num):
    return (num % 2 == 0)


if __name__ == '__main__':
    #2~24까지의 값을 함수 f를 이용한 필터링
    print(list(filter(f,range(2,25)))) #)2~24까지의 숫자를가지고 2와 3의 배수가아닌거 추출
    print('=============================')
    #0~9까지의 값중에 짝수만 출력
    print(list(filter(even,range(0,10))))
                    #even펑션에 준 조건대로 트루,펄스를 비교해서 값을 출력하는거임
                    #필터는 조건준만큼 반복해서 돌아감 1,10이면 10번돌아가는거지..

    print('=============================')

    #람다(익명)식 함수를 사용 = 익명함수(lambda) = 일회용 함수를 이름없이 사용하는것
    print(list(filter(lambda d: (d % 2 ==0), range(0, 10))))
    #바로 람다로 익명함수 d를 선언하고 d:(조건문 or 명령문,실행시킬범위나 변수 함수)

# 2)리듀스 함수를 사용해보자

from functools import reduce

def m_fun(x,y):
    print('x=',x,'y=',y)
    return x+y

if __name__ =='__main__':

    print(reduce(lambda x,y : x+y, range(1,11)))

    print(reduce(m_fun,range(10,20)))


#3)고차함수 Map을 사용해보자.


def ss(ita):
    return ita*2

#파일의 내용을 라인단위로 읽어서 공백으로 분철한 후 필터를 통해 데이터를 추출후 단어별로 1로 지정
#이게map 이하는 일. map+reduce =mr
#map로 들어온애들 타입을 반환해보면 클래스가 map이라고뜸


#Calc
from Calc import Calc
from Calc import MyTest

if __name__=='__main__':

    c1=Calc(100,200)
    print(c1.getX())
    print(c1.getY())
    c1.setY(5000)
    print(c1.getY())

    c2=Calc(1000,2000)
    print(c2.getX())
    print(c2.getY())
    c2.setY(4000)               #get y에게 4000을줬다. 대신 2000은 위에있으니까 남아있음
    print(c2.getY())            #get y가 4000을출력한다.


    c3=Calc(1,2,3,4,5)          #3,4,5만출력되므로 합은12가맞음
    print(c3.gethap())
    c3.sethap(5,6,7,8)
    print(c3.gethap())
    print('==============================================================')
    res=MyTest()
    print(res)

```
</details>
