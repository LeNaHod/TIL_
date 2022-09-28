TIL_DAY06(22_09_28)


# 시퀀스 리뷰

- 은행처리같은거 =루프
- Basic LOOP : 무한루프
- FOR LOOP : 초기값,조건값,증가값 루프
- Curost For LOOP 
- While LOOP 입력객체 반복루프
- EXIT
- EXIT WHEN %인자로 인한 상수값으로 탈출조건을 지정한다.

### 오류처리 원형
```SQL
ALTER SESSION SET PLSQL_WARNINGS='ENABLE:ALL'; --에러처리 총 3가지 경우가있다.

EXCEPTION
  WHEN ex_name_1 THEN statements_1                
  WHEN ex_name_2 OR ex_name_3 THEN statements_2 Exception handler
  WHEN OTHERS THEN statements_3                      
END;

CREATE OR REPLACE PROCEDURE select_item (
  t_column VARCHAR2,
  t_name   VARCHAR2
) AUTHID DEFINER
IS
  temp VARCHAR2(30);
BEGIN
  temp := t_column;  -- For error message if next SELECT fails
 
  -- Fails if table t_name does not have column t_column:
 
  SELECT COLUMN_NAME INTO temp
  FROM USER_TAB_COLS 
  WHERE TABLE_NAME = UPPER(t_name)
  AND COLUMN_NAME = UPPER(t_column);
 
  temp := t_name;  -- For error message if next SELECT fails
 
  -- Fails if there is no table named t_name:
 
  SELECT OBJECT_NAME INTO temp
  FROM USER_OBJECTS
  WHERE OBJECT_NAME = UPPER(t_name)
  AND OBJECT_TYPE = 'TABLE';

 ★ 이쪽이중요한부분!
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE ('No Data found for SELECT on ' || temp);
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE ('Unexpected error');
    RAISE;
END;
★
```

### 프로시저 리뷰

-목록과 펑션목록

    SELECT * FROM SYS.USER_PROCEDURES; --생성된 펑션과 프로시저가같이나온다. TYPE,NAME등등

-소스도 확인해보자

    SELECT * FROM USER_SOURCE;

-프로시저ex01

```sql
create or replace PROCEDURE EX01 
(
  V_EMPNO IN EMP.EMPNO%TYPE  --EMPNO의 타입을가져온다.
, V_ENAME IN EMP.ENAME%TYPE 
, V_DEPTNO IN EMP.DEPTNO%TYPE
) 

AS 

R_EMPNO EMP.EMPNO%TYPE;
R_ENAME EMP.ENAME%TYPE;
R_SAL EMP.SAL%TYPE;

CURSOR EMP_CURSOR IS     --1.커서 선언 :하나이상의 ROW를 담을수 있는 객체
SELECT EMPNO,ENAME,SAL   --EMPNO에 INTO 뒤의 EMPNO,ENAME...
FROM EMP        --번호 OR 컬럼을받아서 처리할것임
WHERE DEPTNO=V_DEPTNO;

BEGIN --2.실제코드
   OPEN EMP_CURSOR;        --3.커서오픈
    LOOP                    --이름을 줘도되고 안줘도되고
    
      FETCH EMP_CURSOR INTO R_EMPNO, R_ENAME,R_SAL; --변수대입
      EXIT WHEN EMP_CURSOR%ROWCOUNT > 5 OR EMP_CURSOR%NOTFOUND;
      DBMS_OUTPUT.PUT_LINE(R_EMPNO || ' ' || R_ENAME || ' ' ||R_SAL);
   END LOOP;
   CLOSE EMP_CURSOR;
END EX01;

var 변수명 타입 --변수선언
EXEC 프로시저명(값, :매개인자) -->PL/SQL실행
PRINT 매개인자  -->매개인자에 담아온걸 출력
```
### 펑션리뷰

```sql

CREATE OR REPLACE FUNCTION GETDEPT 
(
  P_EMPNO IN EMP.EMPNO%TYPE

) RETURN VARCHAR2 AS 
   v_res varchar2(60);
   v_deptno emp.deptno%type;      
   begin   
   select deptno   into v_deptno   from emp
   where empno = p_empno;      
   
   if v_deptno = 10 then
   	v_res := 'ACCOUNTING 부서 사원입니다';
   elsif v_deptno = 20 then
	   v_res :='RESEACH 부서 사원입니다';
   elsif v_deptno = 30 then
	   v_res :='SALES 부서 사원입니다';
   elsif v_deptno = 40 then
   v_res :='OPERATIONS 부서 사원입니다'; 
   END IF; 
  RETURN v_res;
END GETDEPT;


이후 ↓입력시
select ename, empno,sal,getdept(empno) from emp;
RESEACH 부서 사원입니다 등 펑션에 입력(?)한대로나온다.

--Q4)사번을 입력받아 연봉을 리턴하는 getsal()함수를 만들어보자.

CREATE OR REPLACE FUNCTION GETSAL (v_empno in emp.empno%type)
 RETURN number is
   v_tot number := 0;
   v_sal emp.sal%type := 0;      
   begin   
   select sal   into v_sal   from emp
   where empno = v_empno;      
   v_tot := v_sal*12;
   return v_tot;
END GETSAL;

execute :sal :=getsal(값(empno를입력)) --sal에getsal(값(empno를입력))에서 계산한값을 넣고

print sal --출력

--Q5)사번을 입력받아 봉급을 리턴하는 getbong()함수를 만들어보자
--봉급 =연봉+커미션
select empno,ename,sal,getbong(empno) from emp;

--Q5의펑션부분
create or replace FUNCTION GETBONG(v_empno in emp.empno%type) --괄호안은입력받을값을선언
RETURN NUMBER IS  --입력받을값의 리턴타입
   v_tot number := 0;   --입력값x 계산용 변수 선언. 타입은 테이블%타입
   v_sal emp.sal%type := 0;
   v_comm emp.comm%type := 0;
BEGIN   --실행부
   select sal,comm into v_sal,v_comm from emp 
   where empno = v_empno;    --empno는 v_empno에서 받은값이다.대입  
   v_tot := (v_sal*12)+nvl(v_comm,0);
   return v_tot;
END GETBONG;

```

## 뷰(VIEW)
- 가상의 테이블. 원본데이터를 보여주는것이지 실제 데이터를 조작하는게 아님.실제 데이터가 없다고 생각하면된다.
   - 자체적으로 데이터를 포함하지 않는다
   - 베이스테이블(Base table) : 뷰를 통해 보여지는 실제테이블(원본테이블)창문같은
   - 선택적인 정보만 제공 가능
```sql 
create [or  replace] [force | noforce ] view  뷰이름 [(alias [,alias,.....)]
as 서브쿼리
[with check option [constraint 제약조건이름]]
[with read only [constraint 제약조건이름]]
```
  - create or replace : 지정한 이름의 뷰가 없으면 새로생성,동일이름이 있으면 수정
  - force | noforce
  
          force   : 베이스테이블이 존재하는 경우에만 뷰생성가능
          noforce : 베이스테이블이 존재하지 않아도 뷰생성가능
  - alias : 
        뷰에서 생성할 표현식 이름(테이블의 컬럼이름의미)
        생략하면 서브쿼리의 이름적용
        alias의 갯수는 서브쿼리의 갯수와 동일해야함

  - 서브쿼리 : 뷰에서 표현하는 데이터를 생성하는 select구문
  - 제약조건 
  
        with check option : 뷰를 통해 접근가능한 데이터에 대해서만 DML작업가능
        with read only : 뷰를 통해 DML작업안됨
        제약조건으로 간주되므로 별도의 이름지정가능


뷰 - 인라인(inline)개념 : 별칭을 사용하는 서브쿼리 (일반적으로 from절에서 사용)

### 뷰 - Top N분석

  Top N분석 : 조건에 맞는 최상위(최하위) 레코드를 N개 식별해야 하는 경우에 사용
   예) 최상위 소득자3명
         최근 6개월동안 가장 많이 팔린 제품3가지
         실적이 가장 좋은 영업사원 5명
   

   오라클에서 Top N분석원리

      1 원하는 순서대로 정렬
      2 rownum 이라는 가상의컬럼을 이용하여 순서대로 순번부여
      3 부여된 순번을 이용하여 필요한수만큼 식별
      4 rownum값으로 특정행을 선택할수 없음
        (단, Result Set  1st  행(rownum=1)은 선택가능)

### 뷰 예제코드
```SQL 

--Q6)VIEW확인/아래에서 정길동을 업데이트했으니 view에도 반영
SELECT * FROM MY_VIEW;

--VIEW에도 INSERT INTO가될까?
INSERT INTO MY_VIEW VALUES(9000,'홍길동',300); --VIEW 컬럼3개니까 3개만

--원본확인
SELECT * FROM EMP;

--VIEW에 없는 컬럼도 추가가될까?
INSERT INTO MY_VIEW(EMPNO,ENAME,SAL,DEPTNO) --VIEW를통해서는 3개만있으니까 4개는안됨
VALUES(9999,'정길동02',3000,20);

--그럼 원본을 업데이트해보자. VIEW결과도 업데이트된다.
INSERT INTO EMP(EMPNO,ENAME,SAL,DEPTNO) --VIEW를통해서는 3개만있으니까 4개는안됨
VALUES(9999,'정길동',3000,20);

```