SQL TIL1(22_09_24)

안한거= INDEX,VIEW,TRIGGER

프로시저:작업을 수행하기 위한 서브 프로그램
함수:값을 리턴하는 서브 프로그램
트리거:특정 이벤트가 발생될때 자동으로 다른것도 되게. 
    
    EX)회원탈퇴할'때' 게시판글도 삭제해줘 같은. ㅁㅁ할때 ㅇㅇ을 수행해줘

# [1] JOIN

- INNER JOIN
  각 테이블의 조인 컬럼(공통 컬럼)을 비교하여 **조인조건을 만족하는 레코드만 선택하는 조인** = Ture값만가져온다. (Fasle,**NULL** X) 여기서 공통컬럼은 **이름은 달라도 되지만 밸류값이 일치해야한다**
  - USING: 조인테이블의 같은 컬럼명.이퀄 조인에만 해당되고, 두 테이블의 동일한 컬럼명이여야함
    테이블,뷰,서브쿼리중 1개  
  - ON: 조인테이블에 다른 컬럼명(조건부분같은거) A.컬럼 =B.컬럼 다양한 조인식이올수잇다
      조인조건
  - A와B와C를조인한다면 A+B 1차조인한결과 +C를 조인해서 두번의 조인이 일어나게된다.
  - 결과가 동일한 값이있는 **한줄**을 리턴한다 만약 M1에 AB M2에 1 2이고 S1에 ABC S2에 3 4이면
  - M1 S1을 조인햇을때 일치하는 AB와 같은줄에있는 M2 1 2 S2 3 4가 나오게되고 S1은 C빼고가져온다. 
  - JOIN = INNERJOIN
  - EX
  ```SQL
    셋다 조인이지만 문법이 조금다름
        --ansi
        FROM M JOIN S ON(M1=S1); 
        FROM M INNER JOIN S ON(M1=S1);
        --orcle
        FROM M,S WHERE M1=S1;
  ```
   - Static:테이블.컬럼 =CLASS이름.멤버/직접호출은 static 고정. 즉 '고정된'값(const value(상수)) 이나 고정된것(고정틀,고정메뉴..등/공유변수 공유기능) 중요한것 **고정되고 공유하는것**
   - Non-static:객체를 통해 호출하고있다 객체.멤버=객체.컬럼=non-static. static아닌게 다 non-static
   - 데이터 웨어하우스 >편집:데이터 웨어하우징 
- CROSS JOIN
 각 테이블의 모든 로우에 대해서 가능한 모든 조합을 가진느 쿼리 결과를 만들어 내는 조인. 기준점을 가지고있는
 컬럼 (PK)의 데이터 갯수 X 조인한 컬럼의 데이터 갯수를 반환한다. 
- EX
    ```SQL
        --ansi
        SELECT * FROM M CROSS JOIN S
        --SQL SERVER JOIN
        SELECT * FROM M,S
    ```
- OUTER JOIN
   두 테이블 간에 주,종관계를 두고 주 테이블의 모든레코드와 종 테이블에서 조인 조건을 만족하는
   레코드만 가져올때 사용한다.
    - 주테이블의 위치에 따라서 LEFT OUTER JOIN,RIGHT OUTER JOIN, 그리고 두개의 결과를 합한 FULL JOIN
       으로 구분된다.
- **주 테이블**은 모든 레코드가 나오고, **종 테이블**은 조건을 만족하는 레코드만 출력
- LEFT OUTER JOIN
    - M 테이블을 주 테이블로 놓고, S테이블을 종 테이블로 하여 조인을 걸어서 M1=S1조건을
      만족하는 레코드를 가져오는 LEFT OUER JOIN을 작성
    - 오라클에선 종테이블에 (+)를붙인다.
    - **중요** NULL로채워지는것이아니라 **값을 안줬기때문에 NULL을 출력**하는것
- RIGTH OUTER JOIN
   S 테이블을 주 테이블에 놓고 M테이블으 종테이블로 한 RIGTH OUTER JOIN을 작성
    - 오라클은 종테이블에 +를 붙이기때문에 M1에 +가 붙는다. WHERE M1(+) =S1 이런식
- 세개를 조인걸려면 ON하고 또  JOIN하고
- SELF JOIN
  하나의 테이블 내에서 서로 다른 컬럼간에 참조 관계가 있을 때 걸리는 JOIN
- NONEQUI JOIN : 조인하려는 테이블의 데이터의 값이 다를때. where과 on안에 조건식이온다. between으로 범위를 지정할수도있다.
- 
  ```SQL
  --SQL SERVER JOIN
    SELECT E.ENAME, E.SAL, D.DNAME, S.GRADE
    FROM EMP E, DEPT D, SALGRADE S
    WHERE E.DEPTNO=D.DEPTNO
    AND E.SAL BETWEEN S.LOSAL AND S.HISAL;

  --ANSI
    SELECT ENAME,SAL,DNAME,GRADE
    FROM EMP JOIN DEPT USING(DEPTNO) --1차 조인(EMP+DEPT를 DEPTNO로 조인)
    JOIN SALGRADE ON (SAL BETWEEN LOSAL AND HISAL); --(그 결과물을 SALGRADE와 조인한다 ON으로)

  ```
- ANSI : JOIN=INNER JOIN , LEFT/RIGTH OUTER JOIN 등 ON USING이잇는건 ANSI
- ORACLE/SQL SERVER : JOIN이 명시되어있지않고 (+)가 어디붙어있는지에따라 LEFT,RIGTH가 나뉜다.
  WHERE 가붙어있음. ANSI는 ON안에 조건식. 오라클이 전체적으로 ↓이 런느낌
    ```SQL
    SELECT 사원.EMPNO,사원.ENAME,관리자.EMPNO,관리자.ENAME
    FROM EMP 사원, EMP 관리자
    WHERE 사원.MGR=관리자.EMPNO(+);

    ```
# [2] 짤막한 Python + Orcle 진척상황
import statistics
 dir(statisics)/ math dir(math) 이거 두개(안에 들어있는 목록) 많이씀. 단,하나이상의 값을 넣어서 시퀀스값을 관리함

statistics.mead(data)->데이터안에있는애들
data=(1,2,3,4,5) 면 3이출력!

도움말은 -> help(statistics.mean)

기본자료형 -> 연산자 -> 제어문 ->함수[고차함수:맵 리듀스 집 함수안에 함수불러오는거]->클래스 ->상속->다형성(@,데코레이터)-> 파일 입출력(xml,json 웹) -> os,sys등등 모듈

oracle
select문 -> where 연산자 and between .. ->집계함수를 통한 group by -> having -> order by 
->rollup,group,cube,grouping set->서브쿼리->조인 -> 데이터 무결성(제약조건)->테이블 crud->시퀀스
->[view,index]->pl/sql->함수,프로시저,트리거

# [3]CRUD
 기본형태
 create table 테이블명
 (컬럼명1   컬럼타입  [제약조건],
  컬럼명2  컬럼타입  [제약조건],.....);

- 다른테이블에있는 값을 추출해서 새로운 테이블로 생성해보자
```sql
  --Q10)사원테이블에 있는 EMP -> TEST_EMP
    CREATE TABLE TEST_EMP AS
    SELECT * FROM EMP;
  --Q12)JOB이 SALESMAN인 데이터만 추출
    CREATE TABLE TEST_EMP03(사원이름, 봉급)
    AS
    SELECT ENAME,SAL
    FROM EMP
    WHERE JOB='SALESMAN';
```
- ROLLBACK : CRUD중 UD를취소함. 단, 커밋이후만 취소가된다. 커밋해버린건 ROLLBACK으로 취소X

-  문자로시작(30자이내) : 영문 대소문자,숫자,특수문자( _ , $ , # ),한글
-  중복되는 이름은 사용안됨
-  예약어(create, table,column등)은 사용할수 없다
-  자료형
   - number :  number(전체자리,소수이하), number  ==> 숫자형(가변형)
   - int    :  정수형 숫자(고정형)
   - varchar/varchar2 :  문자,문자열(가변형) ==> 최대 2000byte/ 4000byte (한글3byte)
   - char :문자,문자열(고정형) ==> 2000byte
   - date :날짜형
   - ★clob : 문자열 ===> 최대4GB
   - ★blob :바이너리형(그림,음악,동영상..)  ===> 최대4GB 동영상을 담을건지, 경로만담을건지 판단해야함

## 제약조건

- 제약조건
    not null :  해당컬럼에 NULL을 포함되지 않도록 함         (컬럼)
    unique  :  해당컬럼 또는 컬럼 조합값이 유일하도록 함   (컬럼,테이블) /널값 포함하면서 유일한 값
    primary key : 각 행을 유일하게 식별할수 있도록함         (컬럼,테이블)
    references  table(column):                                               
              해당 컬럼이 참조하고 있는 (부모)테이블의 특정   (컬럼,테이블)
               컬럼값들과 일치하거나 또는 NULL이 되도록
               보장함
     check : 해당컬럼에 특정 조건을 항상 만족시키도록함    (컬럼, 테이블)
[참고]  primary key = unique + not null

    ex)       idx                 일련번호            primary key   
               id                 아이디                unique 
               name                이름                  not null 
               phone              전화번호          
               address             주소      
               score               점수                 check
               subject_code       과목코드         
               hire_date           입학일              기본값(오늘날짜)
               marriage            결혼                 check    
             ---------------------------------------------------------------------
- 제약조건확인
    - constraint_name:이름
    - constraint_type:유형
  
          1.  p:primary key 
          2.  u:unique 
          3.  r:reference 
          4.  c:check, not null

    - search_condition :  check조건 내용
    - r_constraint_name : 참조테이블의 primary key 이름
    - delete_rule : 참조테이블의 primary key 컬럼이 삭제될때 적용되는 규칙
                           (no action, set null, cascade등)


    - 삭제 RULE

       1. on delete cascade:대상 데이터를 삭제하고,해당 데이터를 참조하는 데이터도 삭제
       2. on delete set null:대상 데이터를 삭제하고,해당 데이터를 참조하는 데이터는 
                          NULL로 바꿈
       3. on delete restricted:삭제대상 데이터를 참조하는 데이터가 존재하면 삭제할수 
                            없음(기본값)

    
    - 수정 RULE
       on update cascade:대상 데이터를 수정하면,해당 데이터를 참조하는 데이터도 수정
- 예시
```SQL
create table user1(
idx     number  primary key, --식별키(중복데이터X,NULL X)
id      varchar2(10) unique,  -- (중복값X,NULL O)
name    varchar2(10) not null,  --(NULL X)
phone   varchar2(15),
address varchar2(50),
score   number(6,2)  check(score >=0 and score <= 100), --()안에 비교연산식이TRUE인값만출력
subject_code  number(5),
hire_date  date default sysdate, --데이터를 입력하지않앗을시,기본값을 지정한값으로 넣는다
marriage   char(1)  default 'N'  check(marriage in('Y','N')));

※ USER_CONSTRAINTS :제약조건만 들어있는 테이블
 -> DESC USER_CONSTRAINTS; 
 ->ELECT * FROM USER_CONSTRAINTS; C:체크 P:기본키 U:유니크
```       
### 테이블 위치 찾기      
    select TABLESPACE_NAME, TABLE_NAME from all_all_tables where TABLE_NAME LIKE '%찾고싶은 테이블의 단어%';
## Update,삭제 등

- id 컬럼    --->  usr 컬럼으로 변경
    alter table test rename column id to usr;

- test 테이블  --> exam테이블로 변경
    alter table test rename to exam;

- exam테이블을 삭제하고 휴지통비우기 / exam테이블을 휴지통에 넣지 않고 바로 삭제
    drop table exam;
    purge recyclebin;  --휴지통 비우기

### 시퀀스
- 시퀀스:자동번호 넘버링. =은행의 번호표기계같은거.시퀀스는 수정할때 중간만 하지않고 새로쓰는걸 추천
```SQL
--ex19) 시퀀스생성 / 삭제 
create sequence  idx_sql
increment by 2          --증가값 2씩 증가한다
start with 1             --시작값 1부터시작한다   
maxvalue  9   --MAX값 맥스값을 9로지정
cycle nocache;

select  idx_sql.nextval  from dual;    ---> 다음 시퀀스값표시(nextval)
select  idx_sql.currval  from dual;    ---> 현재 시퀀스값표시(currtval)
drop sequence idx_sql;

--시퀀스1
CREATE SEQUENCE ID_NO
INCREMENT BY 5
START WITH 1
MAXVALUE 20
CYCLE NOCACHE;

시퀀스 작동 순서 ↓
--NEXTVAL->CURRVAL->NEXTVAL->NEXTVAL...MAX값을 만나면 초기값으로 돌아간다.

SELECT ID_NO.CURRVAL FROM DUAL; --CURRVAL은 현재 시퀀스값
SELECT ID_NO.NEXTVAL FROM DUAL; --시퀀스명.CURRVAL을 쓰면X. 처음엔 시퀀스명.NEXTVAL을먼저!

INSERT INTO TEST01 VALUES(ID_NO.NEXTVAL, SYSDATE); --NEXT값이기때문에 현재값보다+된값이 삽입됨

--서브쿼리와 INSERT, UPDATE
--Q1)INSERT INTO 테이블명 VALUES(); TEST_EMP
--서브쿼리를 이용해서 INSERT를해보자
--사원번호가 7902사원의 부서번호와 나머지값은 SCOTT사원과 동일한 값으로 입력해보자.
--INSERT로 되지않는다. 조건이 두개라서 사원번호따로 SOCTT따로 구현해야함

--INSERT INTO 문
INSERT INTO TEST_EMP
SELECT * FROM EMP
WHERE ENAME='SCOTT';

--업데이트문 이건 조건두개가다됨. 7902 찾아서 SCOTT사원과 동일한 값으로 입력해보자
UPDATE TEST_EMP
SET
DEPTNO = (select deptno from TEST_EMP where ename='SCOTT')
WHERE
EMPNO='7902';
```
# [4]PL/SQL

```SQL
DECLARE
  "HELLO" varchar2(10) := 'hello'; --변수선언,단 VARCHAR2때문에 싱글쿼터로 값을대입
BEGIN
  DBMS_Output.Put_Line(Hello); --코드 작성부
END;
/

SET SERVEROUTPUT ON --출력을위해 꼭 써야함

BEGIN
DBMS_OUTPUT.PUT_LINE('This string breaks here.');
END;
```
# [5]프로시저/함수

```sql
펑션:모듈이 조금작고, 유저집계함수때쓴다.

CREATE OR REPLACE FUNCTION FUNC01 
(
  A IN VARCHAR2 DEFAULT 100 
) RETURN VARCHAR2 AS 
BEGIN
  RETURN NULL;
END FUNC01;

프로시저:모듈이 펑션보다 크고,어디든쓰인다. 

create or replace PROCEDURE PROC01 AS --생성또는수정하면서 프로시저를 작성하겠다.
BEGIN   --저장하면 프로시저 디렉터리밑에 프로시저가생김
  NULL;
END PROC01;


CREATE OR REPLACE PROCEDURE PROC03 AS 

  i INTEGER :=20;
  
BEGIN
  DBMS_OUTPUT.PUT_LINE('현재 값은?' || i);  --현재값은?20 출력
END PROC03;

--펑션. 매개변수있는것
CREATE OR REPLACE FUNCTION FUNC02 (mydata varchar2) RETURN VARCHAR2 AS --마이데이터라는 매개변수생성
  grade VARCHAR2(30) := mydata;             --펑션을 호출할때 ()안에 a,b,c,d등을넣으면
  res VARCHAR2(30) := NULL;
BEGIN

  CASE grade
    WHEN 'A' THEN res := 'Excellent';   --grade가a면,res에 ''excellent'를넣음
    WHEN 'B' THEN res := 'Very Good';       --매개변수가 받은애로 찾아서 결과를 출력함
    WHEN 'C' THEN res := 'Good';
    WHEN 'D' THEN res := 'Fair';
    WHEN 'F' THEN res := 'Poor';
    ELSE res := 'No such grad';
  END CASE;
  RETURN res; 
END FUNC02;


```
**차이점** :펑션은 **리턴**, 프로시저는 리턴이없다.

### 프로시저의 IN/OUT/INOUT 

- IN : 받기만하겠다
- OUT: 출력만하겠다
- INOUT : in+out. 위의 둘의 기능을합쳐놓은것 받고 출력도 가능

- 함수호출 : 
    -> select 함수명() FROM DUAL(테이블명); 
    펑션을 만들고 저장하고 불러오는데 펑션안에서 부르면 당연히안댐

### for loop

```sql
<<main>>  -- Label block. 여기 mian을 바꾸면 , 아래 main이라고 적혀잇는곳을 다바꿔야함
DECLARE
  i NUMBER := 5; --전역 i =5
BEGIN
  FOR i IN 1..3 LOOP
    DBMS_OUTPUT.PUT_LINE (
      'local: ' || TO_CHAR(i) || ', global: ' ||
      TO_CHAR(main.i)  -- Qualify reference with block label.
    );
  END LOOP;
END main;
  결과: i는 1, 2, 3, 한줄씩나오고 글로벌 main.i=5도 1과같이나옴 1,5 2,5 3,5 이런식으로

--FOR LOOP EXIT WHEN
  DECLARE
  v_employees EMP%ROWTYPE;
  CURSOR c1 is SELECT * FROM EMP;
BEGIN
  OPEN c1;
  -- 전체행을 V_employees라는 레코드로 가져옴
  FOR i IN 1..10 LOOP
    FETCH c1 INTO v_employees;
    EXIT WHEN c1%NOTFOUND;
    -- 여기서 데이터를 처리함 exit when. c1을 열었으니 close도 해줘야함
  END LOOP;
  CLOSE c1;
END;  --결과는 출력문이없어서 아무것도안나옴


--출력문을 썼다. 얘는 ename중 10개만 출력
CREATE OR REPLACE PROCEDURE PROCE04 AS 
  v_employees EMP%ROWTYPE;
  CURSOR c1 is SELECT * FROM EMP;
BEGIN
  OPEN c1;
  
  FOR i IN 1..10 LOOP
    FETCH c1 INTO v_employees;
    EXIT WHEN c1%NOTFOUND;
    
    DBMS_Output.Put_line(v_employees.ENAME || '  ' || v_employees.SAL);
  END LOOP;
  CLOSE c1;
END PROCE04;


--for i in 1..10 loop -> loop로 바꾸면, emp안의ename을 다 가져옴.
CREATE OR REPLACE PROCEDURE PROCE04 AS 
  v_employees EMP%ROWTYPE;
  CURSOR c1 is SELECT * FROM EMP;
BEGIN
  OPEN c1;

  LOOP
    FETCH c1 INTO v_employees;
    EXIT WHEN c1%NOTFOUND;
   
    DBMS_Output.Put_line(v_employees.ENAME || '  ' || v_employees.SAL);
  END LOOP;
  CLOSE c1;
END PROCE04;
```

# [6] Join EXAM풀이

<details>
<summary>EXAM개인풀이</summary>


```SQL
-- 1. 사원들의 이름, 부서번호, 부서이름을 출력하라.
--ORACLE

select ename,e.deptno,dname
from emp e,dept d
where e.deptno = d.deptno;

-- ANSI
select ename,deptno,dname
from emp join dept using(deptno);

-- 2. DALLAS에서 근무하는 사원의 이름, 직위, 부서번호, 부서이름을
-- 출력하라.
--ORACLE

select e.ename,e.job,e.deptno,d.dname,d.loc  --헷갈려서넣음 loc
from emp e, dept d
where e.deptno = d.deptno and d.loc='DALLAS';

--ANSI

select ename,job,deptno,dname,loc
from emp join dept using(deptno)
where loc='DALLAS';           --JOIN을했기때문에,굳이 별칭을 안줘도됨. 다만 이름이같으면 명시해주는편이

-- 3. 이름에 'A'가 들어가는 사원들의 이름과 부서이름을 출력하라.
--ORACLE

select ename,dname
from emp e, dept d
where e.deptno = d.deptno and ename like '%A%';

--ANSI

select ename,dname
from emp join dept using(deptno)
where ename like '%A%';


-- 4. 사원이름과 그 사원이 속한 부서의 부서명, 그리고 월급을 
--출력하는데 월급이 3000이상인 사원을 출력하라.

--ORACLE
select ename,dname,e.sal
from emp e, dept d
where e.deptno = d.deptno and e.sal>=3000;

--ANSI

select ename,dname,sal
from emp join dept using(deptno)
where sal>=3000;

-- 5. 직위가 'SALESMAN'인 사원들의 직위와 그 사원이름, 그리고
-- 그 사원이 속한 부서 이름을 출력하라.
--ORACLE

select ename,job,dname
from emp e, dept d
where e.deptno=d.deptno and job='SALESMAN';

--ANSI

select ename,job,dname
from emp join dept using(deptno)
where job='SALESMAN';


-- 6. 커미션이 책정된 사원들의 사원번호, 이름, 연봉, 연봉+커미션,
-- 급여등급을 출력하되, 각각의 컬럼명을 '사원번호', '사원이름',
-- '연봉','실급여', '급여등급'으로 하여 출력하라.

--ORACLE

select e.empno 사원번호,e.ename 사원이름,e.sal 연봉,sal + nvl(comm,0)실급여,s.grade 급여등급
from emp e, SALGRADE s  --NON-EQUI JOIN(비등가조인),조인할 데이터가 서로 일치하지않을때 사용.
where e.sal between s.LOSAL and s.HISAL and comm is not null;

--ANSI

select  e.empno 사원번호,e.ename 사원이름,e.sal 연봉,sal + nvl(comm,0)실급여,s.grade 급여등급
from emp e join salgrade s on(e.sal between s.losal and s.hisal)
where comm is not null;

-- 7. 부서번호가 10번인 사원들의 부서번호, 부서이름, 사원이름,
-- 월급, 급여등급을 출력하라.

--ORACLE

select e.deptno,d.dname,e.ename,e.sal,s.grade
from emp e, dept d, salgrade s
where e.deptno = d.deptno 
and e.sal between s.losal and s.hisal
and d.deptno =10;

--ANSI

select deptno,d.dname,e.ename,e.sal,s.grade   --e.deptno x ,deptno o :using했기때문에.
from emp e join dept d using(deptno)
join salgrade s on(e.sal between s.losal and s.hisal)
where deptno=10;

-- 8. 부서번호가 10번, 20번인 사원들의 부서번호, 부서이름, 
-- 사원이름, 월급, 급여등급을 출력하라. 그리고 그 출력된 
-- 결과물을 부서번호가 낮은 순으로, 월급이 높은 순으로 
-- 정렬하라.

--ORACLE

select e.deptno,d.dname,e.ename,e.sal,s.grade
from emp e,dept d,salgrade s
where e.deptno = d.deptno 
and e.sal between s.losal and s.hisal
and e.deptno in(10,20)
order by deptno asc , sal desc;

--ANSI

select deptno,dname,ename,sal,grade
from emp join dept using(deptno)
join salgrade on(sal between losal and hisal)
where deptno in(10,20)
order by deptno asc, sal desc;

-- 9. 사원번호와 사원이름, 그리고 그 사원을 관리하는 관리자의 --사원번호,이름은 조건이x다나와야하고
-- 사원번호와 사원이름을 출력하되 각각의 컬럼명을 '사원번호',  --'그사원을관리하는'이라는 조건이붙은mgr이니까
-- '사원이름', '관리자번호', '관리자이름'으로 하여 출력하라.  -- 종테이블이 emp.mg테이블이되야한다.종은(+)붙임.
--ORACLE

select e.empno,e.ename,mg.empno,mg.ename
from emp e, emp mg
where e.mgr = mg.empno(+);

--ANSI
select e.empno,e.ename,mg.empno,mg.ename
from emp e left outer join emp mg on(e.mgr = mg.empno);

--10 -자신의 관리자보다 먼저 입사한, 모든 사원의 이름 및 입사일을 
--해당관리자의 이름 및 입사일과 함게 표시하고 열 이름을 각각 
--EMPLOYEE,EMPHIREDATE,MANAGER,MGRHIREDATE로 저장한다.

--ORACLE

select e.ename EMPLOYEE,e.hiredate EMPHIREDATE,mg.ename MANAGER,mg.hiredate MGRHIREDATE
from emp e, emp mg
where e.hiredate < mg.hiredate and e.mgr = mg.empno; --매니저가 존재하는 사원중에, 매니저보다 먼저입사한 사원


--ANSI
select e.ename EMPLOYEE,e.hiredate EMPHIREDATE,mg.ename MANAGER,mg.hiredate MGRHIREDATE
from emp e left outer join emp mg on(e.mgr = mg.empno)
where e.hiredate < mg.hiredate;

--11)해당 부서의 모든 사원에 대한 부서 이름, 위치, 사원 수 및 평균 급여를 --표시하는 정의를 작성한다. 
--열 이름을 각각 DNAME,LOC,NUMBER OF PEOPLE,SALARY로 한다.

--ORACLE
select d.dname DNAME,d.loc LOC,
COUNT(*) OVER(PARTITION BY e.deptno) as "NUMBER OF PEOPLE",
ROUND(AVG(sal) OVER(PARTITION BY e.deptno),1) SALARY
from emp e ,dept d
where e.deptno = d.deptno(+);

--ANSI

select dname as DNAME,loc as LOC,
COUNT(*) OVER(PARTITION BY deptno) as "NUMBER OF PEOPLE",
ROUND(AVG(sal) OVER(PARTITION BY deptno),1) as SALARY
from emp join dept using(deptno);


```