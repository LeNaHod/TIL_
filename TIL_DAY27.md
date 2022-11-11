# TIL DAY 27 (2022-11-10)

# Oracle2

## 데이터모델링 기획,설계

논리 ERD : 사원/ 부서 /주소 / 직업... 설계단계에서 어떤데이터를 어떻게 규정하고 관계를지을것인가를 정의 (스케치단계)

물리 ERD : 실제 사용할 컬럼명을 정한다. 

물리적으로 다 해보고 TABLE을 구현하는것.
 
```sql
1.create table test(Id varchar(10),Pw char(10));

2.create table test01 as select * from emp;

3.create table test02 as select empno,ename from emp;

4.create table test03 as select * from emp where 1=2; (1=2는 조건이 false)


5.★emp테이블에서 empno,ename을 m1,m2로 이름을바꿔서 복사해오자!
  - create table test04(M1,M2) as select empno,ename from emp;
  - create table test04 as select empno as m1,ename as m2 from emp;

6.create table test05 as select *from dept;

BUT,제약조건은 복사가안되므로 
alter table(add, modify 등)으로 제약조건을 추가해줘야함


Insert

insert into test05 values(10,'develop','seoul');
select * from  test05;


지정해준컬럼에만 값넣기(test05의구조는 deptno, danme, loc)

insert into test05(deptno,dname) values(20,'data'); ->loc컬럼의 값은 비어있게됨

현재날짜를 확인해보자

select sysdate from dual;
22/11/10 이렇게나옴
```
## Update

기본형태:update 테이블명 set 컬럼=값, 컬럼=값,..
조건이중요함. 

위의 코드같은경우는 **'모두'**바꾸기때문
조건으로 바꿀애들만 지정해줘야함!

**★update 테이블 set 컬럼 = 값, 컬럼=값,... where 조건;**

## delete

update와 마찬가지로 조건!이중요함

기본형태는 delete from 테이블명;
->모든테이블이 사라짐.

고로,
= **★delete 테이블 set 컬럼 = 값, 컬럼=값,...where 조건;**

```sql
1.select * from emp;

2.select ename,empno,sal from emp;

3.select ename,sal from emp;

4.select ename,hiredate,deptno from emp;

5.select ename,mgr from emp; 
->mgr번호는 empno를 참조하는데 자기자신의 empno를 참조하는경우도있다.

6.select ename,sal,comm from emp;

7.select ename||'님이'||hiredate||' 에 입사를하고 '||sal||' 의 월급을 받습니다.' from emp;->컬럼은""(별칭등 as ~할때),값은 ''
8.desc dept;

9.select empno,ename,sal*12 from emp where empno='7844'

10.select empno,enam,sal*12 from emp where ename='SMITH'

11.select * from emp where hiredate='1980-12-17' 
->// 80/12/17 // 1980/12/17 모두가능

12.select ename,hiredate from emp where hiredate between '1980-01-01' and '1982-12-31';

13.select ename,sal*12 from emp where sal*12 < = 2000

14.select ename,sal*12 as "월급" from emp where sal*12 between 1000 and 2000

15.select ename,sal*12 from emp where empno in('7369','7499','7521');
-># where empno='7369' or empno='7499' or empno='7521';

16.select ename,sal from emp order by sal desc;

17.select job,avg(sal) as 평균 from emp group by job order by avg(sal) desc;

18.select avg(sal) from emp;

19.select deptno,avg(sal) from emp group by deptno having deptno='10';

20.select job,avg(sal) from emp group by job;

21.select deptno,max(sal) from emp group by deptno having deptno='10';

22.select deptno,max(sal) from emp group by deptno;

23.select job,sum(sal) from emp group by job having sum(sal) >= 5000;

24.select deptno,sum(sal) from emp group by deptno having not deptno = '30' and sum(sal) >= 8000 order by sum(sal) desc;

# or
select deptno,sum(sal)
from emp
where not deptno = '30'
group by deptnoh
having sum(sal) >=8000
order by sum(sal) desc;


# R,L PAD:컬럼을 길이만큼 정렬하고 빈공간은 값으로채운다.
select rpad(ename,10,'*') from emp; -오른쪽으로 ****(*가 값이니까LPAD는 왼쪽으로 ******)


# LTRIM , RTRIM:문자열에서 제거할 문자(열)제거. 패턴제거X

기본형태 L,RTRIM(문자열,제거할 문자(열))

select ltrim('xyxzyyTech6 327', 'xyz') from dual;
->왼쪽에서부터 xyz를삭제 Tech6 327만나옴

# rtrim은 오른쪽에서부터 삭제.

# trim:문자열 양쪽에서 제거할 문자 제거

SELECT TRIM('x' FROM 'xxxxyxzyyTech6 327xxxxx') FROM DUAL;
->양쪽x가 다 지워진다.

## 문자열 자르기
substr(컬럼 or 문자열 , 시작위치 [,반환할 갯수])
(시작위치는 0
0 or 1 :처음부터
양수: 끝 방향으로
음수 : 시작 방향으로
★반환할 갯수가 음수일때 null반환
)
```

## INSTR:찾는 문자의 시작위치반환 | 찾는문자의 시작위치부터 횟수만큼 나타난 시작위치 반환


예를들어 안에값이 SMITH이면
select ename,instr(ename,'S',1,1)from emp;
1을반환

(시작위치가 양수:끝방향, ->방향

음수:시작방향  <-방향

무조건 '인덱스값'을 반환하기때문에 양수/음수상관없이 왼쪽부터1)


## 날짜 더하기 add_months
기본형태(날짜,더하려는 개월)

지정한 날짜부터 '개월수'를 더한 날짜 반환.

select ename hiredate,add_months(hiredate,,240) from emp; ->입사한지 20년이 되는 달


## 날짜사이의 개월수를 구하자!
months_between(날짜1, 날짜2)

아래는 00년 1월1일을 기준으로 10년이상 근무한 사람의 이름,직업,입사일,근무년을 구하는것!
```sql
SELECT ENAME, JOB, HIREDATE, 

       TRUNC(MONTHS_BETWEEN(‘2000/01/01’, HIREDATE)/12) 
FROM EMP

WHERE MONTHS_BETWEEN(‘2000/01/01’, HIREDATE) > 120
```

## ★★★★★데이터형태 변환하기

TO_NUMBER  <->  TO_CHAR <->  TO_DATE

to_number(값) to_char(값) to_date(값) 으로 사용하는데,

정말 자주 쓰이니 중요!!!!!

**★단 date와 number는 바로 변환x 캐릭터를 거쳐야함**

날짜포맷중에서는 yyyy-mm-dd 를 가장많이씀 

```sql
select to_char(to_date('20100101', 'yyyymmdd'), 'yyyy, mon') from dual;

20100101을 yyyy mm dd 형식으로 날짜로바꾼후에, 다시 yyyy, mon 형식의 캐릭터로 바꿈.
뒤에 fm을붙이면 공백제거. yyyymmdd fm 이런식으로
```

## Decode

입력한값이 같으면 반환값을 반환, 다를땐 기본값을 반환

기본형태

decorde(컬럼or문자열,비교값, 같을 때 반환값 [,비교값, 같을때 반환값,..][다를때 기본값]
```sql
select ename,job, decode(job,'manager','0')from emp;
->job이 manager이면 문자0출력


ex)
job의값이 manager라면0, 아니면 president면 1, 그외의값은 2

select ename,job, decode(job,'manager','0','president','1','2')from emp;
```

## 스위치케이스문

기본형태
case when 조건 then참일때 값, [,when then ...][else 거짓말일 때 반환값]end

**★else 지정하지 않으면 거짓일때 null값반환**

```sql
select ename, sal,case when sal<=1000 then '초급' when sal<=2000 then '중급'else '고급' end
from emp;
```

## nvl:널값일대 대체할값

기본형태

nlv(컬럼명,대체할값)

```sql
select ename,sal,comm,nvl(comm,0) from emp;
```

# ROLLUP,CUBE,GROUPINF SETS

GROUP시에만 사용가능

### ROLLUP

전체집계에대한X, 그룹된 그룹의 집계O.

(Ex) MANAGER이고 DEPTNO가10번인 애들의 평균월급+20번인애들 평균월급+ 30번인애들 평균월급 의 값이 나옴)


### CUBE

ROLLUP이랑 출력순서도 다른데 B에대한 집계도 같이나옴. 
= ROLLUP보다 집계 한개가 더나온다고 생각하면됨.

ROLLUP의 예제에서 DEPTNO별 집계가 모아져서나옴


### GROUPING SETS

ROLLUP한 결과에 GROUPING SETS으로 추가하려는 컬럼의 결과를 추가해주세요 라는 의미로생각하면된다.

그래서 ROLLUP결과 끝에 각각 추가가됨 



## rowid,rownum이란?

테이블생성시 명시하지않아도 자동으로 생성되는친구들

rowid= mongodb의 _id같은존재(자동생성 행의 id)

rownum= 행의 넘버(자동넘버링. from 단계(첫번째단계)에서 가지고오는 행의 갯수에따라 번호할당)


## top n query (어디서부터 n번째 결과찾기)

### 1.rowsnum을 이용하여 구하는방법(+서브쿼리)
(※주의해야할점은, order by가 from 뒤에 실행되기때문에 desc의 경우는 순서가 뒤죽박죽이된다.)
그러므로 서브쿼리를 같이 이용해야한다.

```sql
# How?
from 으로 desc한 결과를 가져오면, 월급이 많은순서대로 rownum이 할당이된다.
= select ename,sal,rownum from(select ename,sal from emp order by sal desc);

# 완성형:
select ename, sal, rownum from (select ename, sal from emp order by sal desc) where rownum <=5;

# 틀린예제:
select ename,sal, rownum from (select ename,sal from emp order by sal desc)where rownum>=3 and rownum<=5;
->3보다 크고 5보다 작은거면, 아예 3개만! 가져와버려서 자동으로 넘버링이 123이되어버린다고 생각하면됨 그렇게되면 3보다 크고 5보다작은걸 찾을수없게되어버림.

# 꼭 이상이하를 쓰고싶으면? ↓

select * from (select ename,sal,rownum as rn from(select ename, sal from emp order by sal desc)) where rn >=3 and rn <=5; (as는안해줘도 무관)
```

## 2.rank,dense_rank를 이용해보자

차이점

rank:겹친만큼 다음등수를 건너뜀

dense_rank:다음등수를 건너뛰지않음.

그리고 같은값이여도 등수가 다르다고 알려줌

기본형태

    rank()over (order by 컬럼명 asc/desc)
	dense_rank() over(order by sal asc/desc)
    from ~

복합문제

```sql
1.
select initcap(ename) from emp;

initcap:첫글자는'대문자',나머지는'소문자'
upper,lower는 전체 대/소문자

2.(두번째부터, 네번째글자까지만)
select ename, substr(ename,2,3)
from emp;

3.
select ename,months_between(hiredate,sysdate)*30
from emp; ->한달을 30일기준으로계산

4.
select length(ename)
from emp;

regexp_count('문자열','찾을문자열')=문자열에서 찾을 문자열의 갯수를세어줌

length는 그냥 문자열의 갯수. 
legth로 전체 문자갯수 - length(replace('문자','찾을문자'))로 특정문자 갯수를 찾을수도있음.

5.
select ename
from emp
where ename like 'M%';
```

## 서브쿼리

```sql
(jones보다 더 많은 월급을 받는 사원의 이름과 월급출력)
select ename,sal 
from emp
where sal>(select sal from emp where ename='jones');


(부하직원이 없는 사원의 사원번호와 이름출력 =매니저 번호가없는!사원의 이름과번호)

select empno,ename from emp
where empno not in (select nvl(mgr,0) from emp) ->null이있으면 계산이안되니 0으로 일단처리 하고가져옴



1.
CHICAGO’에서 근무하는 사원들과 같은 부서에서 근무하는 사원의 이름과 월급을 출력하자. 

select e.ename,e.sal
from emp e , dept d
where e.deptno=d.deptno and d.loc='CHICAGO';

2.
관리자의 이름이 ‘KING’인 사원의 이름과 월급을 출력하자. 

select ename,sal
from emp
where mgr = (select empno from emp where ename ='KING');

3.
전체 사원 중, 20번 부서의 사원 중 가장 많은 월급을 받는 사원보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력하자. 

select ename,sal from emp where sal>(select max(sal) from emp where deptno=20);

4.
전체 사원 중, 직업이 ‘SALESMAN’인 사원 중 가장 많은 월급을 받는 사원보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력하되, MAX()함수를 사용하지 말자. (ANY, ALL 연산자) 

select ename,sal from emp where sal> all(select sal from emp where job = 'SALESMAN');

5.
'BLAKE'가 근무하는 부서의 위치(LOC)를 출력하자.

select loc from dept where deptno =(select deptno from emp where ename ='BLAKE');

6.
이름에 ’S’가 들어가는 사원과 동일한 부서에서 근무하는 사원 중, 자신의 월급이 전체 사원의 평균 월급보다 많은 사원들의 사원번호, 이름, 월급을 출력하자.

select empno,ename,sal
from emp
where empno in(select epmno,ename,sal from emp where ename like '%S%')and sal>(select avg(sal) from emp);


7.
사원번호가 7369인 사원과 같은 직업이고, 월급이 7876인 사원보다 많이 받는 사원의 이름과 직업을 출력하자.
select ename,job from emp where job = 
(select job from emp where empno =7369)
and sal>
(select  sal from emp where empno = 7876);
```

## Join

조인할 컬럼이같은경우 **using을쓰면 중복컬럼제거**되어서,

이름이 같을땐 on으로 하는것보다 using사용 권장.


**cross join**은 조합할수있는것들 다나옴.

left,right/full outer join은 각각 없는데이터는 null값처리한다.


**일치하는컬럼이없을때(non equi join):**

```sql
오라클
select ename,sal,grade from emp e, salgrade s where sal between losal and hisal;

안시
select ename, sal, grade
from emp join salgrade on (sal between losal and hisal);
```

복합문제

```sql
1.사원들의 이름, 부서번호, 부서이름을 출력하자. 

select e.ename,e.deptno,d.dname
from emp e, dept d
where e.deptno = d.deptno;

ansi

ver1
select ename, deptno,dname
from emp join dept using(deptno);

ver2
select ename,emp.deptno,dname
from emp join dept on(emp.deptno=dept.deptno);


2.‘DALLAS’에서 근무하는 사원의 이름, 직업, 부서번호, 부서이름을 출력하자. 

select e.ename,e.job,e.deptno,d.dname
from emp e, dept d
where e.deptno= d.deptno and d.loc='DALLAS';


ansi

ver1
select ename,job,deptno,dname
from emp join dept using(deptno)
where loc='DALLAS';

ver2
select ename,job,emp.deptno,dname
from emp join dept on(emp.deptno=dept.deptno)
where loc='DALLAS';


3.이름에 ‘A’가 들어가는 사원들의 이름과 부서이름을 출력하자. 

select e.ename,d.dname
from emp e, dept d
where e.deptno=d.deptno and e.ename like '%A%';

ansi

ver1
select ename, dname
from emp join dept using(deptno)
where ename like '%A%';

ver2
select ename,dname
from emp join dept on(emp.deptno=dept.deptno)
where ename like '%A%';


4.사원의 이름과 부서이름, 월급을 출력하되, 월급이 3000 이상인 사원들만 출력하자. 

select e.ename, d.dname, sal 
from emp e, dept d
where e.deptno = d.deptno and sal >= 3000;

ansi

ver1
select ename,dname,sal
from emp join dept using(deptno)
where sal >=3000;

ver2
select ename,dname,sal
from emp join dept on(emp.deptno=dept.deptno)
where sal>=3000;


5.사원테이블과 급여테이블(SALGRADE)에서 커미션이 책정된 사원들의 사원번호, 이름, 연봉, 연봉+커미션, 급여등급(GRADE)을 출력하자. (noneq)

select e.ename,e.empno,e.sal,(e.sal*12)+nvl(e.comm,0),s.grade
from emp e, salgrade s
where e.sal between s.losal and hisal and e.comm is not null;


ansi

select empno,ename,sal*12,(sal*12)+nvl(comm,0),grade
from emp join salgrade on(sal between losal and hisal)
where comm is not null;



6.부서번호가 10번인 사원들의 부서번호, 부서이름, 사원이름, 월급, 급여등급을 출력하자. 

select e.deptno, d.dname, e.ename, e.sal, s.grade
from emp e, dept d, salgrade s
where e.deptno = d.deptno and e.sal between s.losal and hisal and e.deptno=10;

ansi

select deptno,dname,sal,grade,ename
from emp join dept using(deptno) join salgrade on(sal between losal and hisal)
where deptno = 10;


7.부서번호가 10번이거나 20번인 사원들의 부서번호, 부서이름, 사원이름, 급여등급을 출력하되, 부서번호가 낮은 순으로, 월급이 높은 순으로 출력하자. 

select e.deptno, d.dname, e.ename, s.grade
from emp e, dept d, salgrade s
where e.deptno=d.deptno 
and e.sal between s.losal and hisal 
and (e.deptno = 10 or e.deptno= 20)
order by d.deptno, e.sal desc;


ansi

select deptno,dname,ename,grade
from emp e join dept d using(deptno) join salgrade s 
on(e.sal between s.losal and hisal)
where deptno = 10 or deptno= 20
order by deptno, e.sal desc;


8.사원번호와 이름, 관라자의 사원번호와 관리자이름을 출력하자. 

select e.empno, e.ename, mg.empno, mg.ename
from emp e , emp mg
where e.mgr=mg.empno(+);

ansi

select e.empno, e.ename, mg.empno, mg.ename
from emp e left outer join emp mg on(e.mgr=mg.empno);


9.부서이름, 위치, 각 부서의 사원수, 평균 월급을 출력하자.


select dname,loc,count(*),avg(sal)
from emp e, dept d
where e.deptno=d.deptno
group by dname,loc;


ansi
select dname,loc,count(*),avg(sal)
from emp join dept using(deptno)
group by dname,loc;
```

