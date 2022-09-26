SQL TIL1(22_09_24)

# [1]그룹과 그룹함수,기본 복습


## 예제코드

<details>
<summary>예제코드(오전)</summary>


```SQL

--생성,추가

CREATE  TABLE MY_TABLE(

  KEY1 CHAR(4),
  KEY2 CHAR(4),
  KEY3 CHAR(4),
  KEY4 CHAR(4),
  VAL NUMBER

);

INSERT INTO MY_TABLE VALUES ('AAAA','AAA','AA','A',10); --1:1관계 순차적인 값 매핑
INSERT INTO MY_TABLE(컬럼명) VALUES ('AAAA','AAA','AA','A',10); --컬럼명에 대해 1:1매핑

-- 행 삭제
DELETE FROM MY_TABLE
WHERE VAL = 11;

DELETE FROM MY_TABLE 스키마는그대로 전체삭제

--테이블  삭제
DROP TABLE MY_TABLE;

--ROLLUP,GROUP,GROUPING,CUBE

--Q1) 전체 개수를 출력해보자.

SELECT COUNT(*)
FROM MY_TABLE;

--Q2)  KEY1,KEY2 그룹핑해서 그룹별 개수와 VAL합을 구해보자

SELECT KEY1,KEY2,COUNT(*),SUM(VAL)
FROM MY_TABLE
GROUP BY KEY1,KEY2
ORDER BY 1,2;
--Q3) KEY를 이용한 ROLLUP을 해보자

SELECT KEY1,KEY2,COUNT(*),SUM(VAL)
FROM MY_TABLE
GROUP BY KEY1,ROLLUP(KEY2)
ORDER BY 1,2;

--Q4)KEY1,KEY2,KEY3을 이용한 ROLLUP을 해보자(KEY2,KEY3)만 그룹
SELECT KEY1,KEY2,KEY3,COUNT(*),SUM(VAL)
FROM MY_TABLE
GROUP BY KEY1,ROLLUP(KEY3,KEY2)
ORDER BY 1,3,2;

--Q5)KEY1,KEY2,KEY3,KEY4을 이용한 ROLLUP을 해보자(KEY3,KEY4)만 그룹

SELECT KEY1,KEY2,KEY3,KEY4,COUNT(*),SUM(VAL)
FROM MY_TABLE
GROUP BY KEY1,KEY2, ROLLUP(KEY3,KEY4)
ORDER BY 1,2,3,4;

--Q6)그룹핑을 해보자
SELECT GROUPING(KEY1)AS GP01,
COUNT(*),SUM(VAL)
FROM MY_TABLE
GROUP BY KEY1;

--Q6-1)그룹핑을 해보자2
SELECT GROUPING(KEY1)AS GP01,
GROUPING(KEY2)AS GP02,
GROUPING(KEY3)AS GP03,
COUNT(*),SUM(VAL)
FROM MY_TABLE
GROUP BY KEY1,ROLLUP(KEY2,KEY3);

--Q6-2)그룹핑을 해보자3 집계된열=1 집계되지않은열 = 0
SELECT GROUPING(KEY1)AS GP01,
GROUPING(KEY2)AS GP02,
GROUPING(KEY3)AS GP03,
GROUPING_ID(KEY1,KEY2,KEY3) AS GID,KEY1,KEY2,KEY3,
COUNT(*),SUM(VAL)
FROM MY_TABLE
GROUP BY KEY1,ROLLUP(KEY2,KEY3)
ORDER BY KEY1,KEY2,KEY3;

--Q6-3)CUBE를 이용해서 KEY1,2,3를 그룹핑하자
SELECT GROUPING(KEY1)AS GP01,
GROUPING(KEY2)AS GP02,
GROUPING(KEY3)AS GP03,
GROUPING_ID(KEY1,KEY2,KEY3) AS GID,KEY1,KEY2,KEY3,
COUNT(*),SUM(VAL)
FROM MY_TABLE
GROUP BY CUBE(KEY1,KEY2,KEY3)
ORDER BY KEY1,KEY2,KEY3;


--Q6-4)CUBE를 이용해서 (KEY1,(2,3))를 그룹핑하자
SELECT GROUPING(KEY1)AS GP01,
GROUPING(KEY2)AS GP02,
GROUPING(KEY3)AS GP03,
GROUPING_ID(KEY1,KEY2,KEY3) AS GID,KEY1,KEY2,KEY3,
COUNT(*),SUM(VAL)
FROM MY_TABLE
GROUP BY CUBE(KEY1,(KEY2,KEY3))
ORDER BY KEY1,KEY2,KEY3;

--Q6--5)CUBE를 이용해서 (KEY2,(KEY1,KEY3))을 그룹핑해보자
SELECT GROUPING(KEY1)AS GP01,
GROUPING(KEY2)AS GP02,
GROUPING(KEY3)AS GP03,
GROUPING_ID(KEY1,KEY2,KEY3) AS GID,KEY1,KEY2,KEY3,
COUNT(*),SUM(VAL)
FROM MY_TABLE
GROUP BY CUBE(KEY2,(KEY1,KEY3))
ORDER BY KEY2,KEY1,KEY3;

--Q11)GORUPINF SETS을 이용해보자 (끝에 ()가붙고,주로 정렬용)
SELECT GROUPING(KEY1)AS GP01,
GROUPING(KEY2)AS GP02,
GROUPING(KEY3)AS GP03,
GROUPING_ID(KEY1,KEY2,KEY3) AS GID,KEY1,KEY2,KEY3,
COUNT(*),SUM(VAL)
FROM MY_TABLE
GROUP BY GROUPING SETS(KEY2,(KEY1,KEY3),())
ORDER BY KEY1,KEY2,KEY3;

★자리가같음 = GROUPING SETS 단 ()붙여야함 = ROLLUP =CUBE
SELECT 절 = GROUPING_ID

--HR계정 연습문제 (MY)

--Q1)

SELECT EMPLOYEE_ID,FIRST_NAME,LAST_NAME,SALARY
FROM HR.EMPLOYEES;

--Q2)

SELECT CONCAT(FIRST_NAME,LAST_NAME)AS 사원명,
HIRE_DATE AS 입사일,
SALARY *12||'원' AS 연봉,
DEPARTMENT_ID AS 부서코드
FROM HR.EMPLOYEES
WHERE DEPARTMENT_ID ='90';

--Q3)

SELECT LAST_NAME,JOB_ID,DEPARTMENT_ID
FROM HR.EMPLOYEES
WHERE JOB_ID ='IT_PROG' OR JOB_ID='ST_MAN' OR JOB_ID='SA_REP';

-- JOB_ID IN('IT_PROG','ST_MAN','SA_REP')

--Q4) 

SELECT LAST_NAME,HIRE_DATE,JOB_ID
FROM HR.EMPLOYEES
WHERE EXTRACT(YEAR FROM HIRE_DATE) 
BETWEEN EXTRACT(YEAR FROM TO_DATE('1997-01-01','YYYY-MM-DD'))
AND EXTRACT(YEAR FROM TO_DATE('2000-12-31','YYYY-MM-DD'));  --원래 아무것도안뜸

--Q5)

SELECT LAST_NAME,salary*12,COMMISSION_PCT
FROM HR.EMPLOYEES
WHERE COMMISSION_PCT IS NULL;

--Q6)
SELECT LAST_NAME, JOB_ID
FROM HR.EMPLOYEES
WHERE JOB_ID LIKE('%IT%');


--Q7)
SELECT LAST_NAME AS 사원이름,EMAIL AS 이메일,
PHONE_NUMBER AS전화번호
FROM HR.EMPLOYEES
WHERE SALARY >= 1500 AND SALARY <= 5000 AND JOB_ID IN('IT_PROG');

--Q8)

SELECT DEPARTMENT_ID AS 사원번호, 
CONCAT(FIRST_NAME,LAST_NAME) AS "이 름",
SALARY AS "연 봉"
FROM HR.EMPLOYEES;

--Q9)

SELECT LAST_NAME||' is a '||JOB_ID AS "Employee Detail"
FROM HR.EMPLOYEES;

--Q10)

SELECT CONCAT(FIRST_NAME,LAST_NAME) AS 사원명, '$'||SALARY AS "월 급",
DEPARTMENT_ID AS 부서코드
FROM HR.EMPLOYEES
WHERE DEPARTMENT_ID IN(90) AND SALARY <= 25000 OR SALARY >= 30000;

--Q11)

SELECT LAST_NAME AS 이름, JOB_ID AS 업무ID, SALARY AS "급 여"
FROM HR.EMPLOYEES
WHERE (JOB_ID='SA_REP' OR JOB_ID ='AD_PRES') AND SALARY >15000;

--Q12)

SELECT DISTINCT(JOB_ID)
FROM HR.EMPLOYEES;

--Q13)

SELECT EMPLOYEE_ID, LAST_NAME,HIRE_DATE  --YEAR는 MSSQL
FROM HR.EMPLOYEES
WHERE EXTRACT(YEAR FROM HIRE_DATE) = EXTRACT(YEAR FROM TO_DATE('1997-01-01','RR-MM-DD'));

--Q14)

SELECT LAST_NAME, JOB_ID,DEPARTMENT_ID
FROM HR.EMPLOYEES
WHERE JOB_ID LIKE('%MAN%');

--Q15)

SELECT LAST_NAME, DEPARTMENT_ID,HIRE_DATE
FROM HR.EMPLOYEES
ORDER BY DEPARTMENT_ID DESC;

--Q16)
SELECT EMPLOYEE_ID,CONCAT(FIRST_NAME,LAST_NAME) AS NAME,
LENGTH(CONCAT(FIRST_NAME,LAST_NAME)) AS LENGTH
FROM HR.EMPLOYEES
WHERE SUBSTR(CONCAT(FIRST_NAME,LAST_NAME),LENGTH(CONCAT(FIRST_NAME,LAST_NAME)),1)='n';

--LAST_NAME LIKE('%n');

--Q17)
SELECT LAST_NAME,HIRE_DATE,TO_CHAR(HIRE_DATE,'DD-MON-YYYY')
FROM HR.EMPLOYEES
WHERE HIRE_DATE > TO_DATE('2000-01-01','YYYY-MM-DD');

--Q18)
SELECT EMPLOYEE_ID AS 사원번호,LAST_NAME AS 사원명,
(CASE WHEN SALARY < 10000 THEN '초급'
      WHEN SALARY < 20000 THEN '중급'
      ELSE '고급' END) AS "구 분"
FROM HR.EMPLOYEES
ORDER BY "구 분" ASC,사원명 ASC;


--Q19)
SELECT EMPLOYEE_ID AS 사원번호,LAST_NAME AS 사원이름,SALARY AS 급여,
NVL(COMMISSION_PCT,0) AS 커미션,TO_CHAR(SALARY*12,'$999,999') 연봉
FROM HR.EMPLOYEES;


--Q20)
SELECT EMPLOYEE_ID, LAST_NAME,NVL(MANAGER_ID,'1000') AS MANAGER_ID
FROM HR.EMPLOYEES;

--HR계정(정오표)

--[문제 1]  사원테이블에서 사원번호, 사원명, 급여를 검색하시오
select  employee_id,last_name,salary 
from employees;
--[문제 2]  사원테이블에서 부서가  90번인 사원들의 사원명,입사일,연봉,부서코드를 출력하시오
--         조건1)  제목은  사원명, 입 사 일,연   봉,부서코드로 하시오(as 별명)
--         조건2)  연봉  = 급여 * 12
--         조건3)  연봉 뒤에 화폐단위 "원"을 붙이시오 (|| 연결연산자)
--         조건4)  사원명은  first_name , last_name을 연결 하시오

select first_name || '  ' ||last_name as 사원명,hire_date as "입 사 일", 
          salary*12 || '원' as "연  봉" , department_id as 부서코드
from employees
where department_id=90;
 
--[문제 3]  사원테이블에서  업무ID가  IT_PROG,ST_MAN,SA_REP인 사원을 표시하시오
--        조건1)  사원명, 업무ID, 부서ID만 표시
--        조건2)  or  연산자 이용 ,  in 연산자 이용 둘다 쓰시오
--        or연산자 이용
select last_name,job_id,department_id 
from employees
where job_id='IT_PROG' or  job_id='ST_MAN' or job_id='SA_REP';

--       in연산자 이용
select last_name,job_id,department_id 
from employees
where  job_id  in ('IT_PROG','ST_MAN','SA_REP');

--[문제 4]  입사일이  1997~2000 사이의 입사한 사원들의  사원명,입사일, 업무 ID를 출력하시오 
--(and,  between연산자 모두 표시)
--  and연산자
select last_name,hire_date,job_id 
from HR.employees
where  HIRE_DATE >= '1997/01/01'
            and  HIRE_DATE  <= '2000/12/31';

-- between연산자 (초과,미만이 없다)
select last_name,hire_date,job_id 
from HR.employees
where  hire_date  between '1997/01/01' and '2000/12/31';




--[문제 5]  커미션을 받지 않는 사원들의   이름과 연봉,커미션을 출력하시오
--         (is  null)  
select last_name,salary*12,commission_pct
from employees
where  commission_pct is null;
--[문제 6]   업무ID중  IT가 포함되어있는 사원들의 이름과 업무ID을 구하시오

select last_name,job_id 
from employees
where  job_id like '%IT%'; 
--[문제 7] 급여가  1500이상  5000이하인 사원중  IT_PROG의 업무 ID인 사원을 표시하시오
--조건1) 제목은  사원이름, 이메일,전화번호

select  last_name as 사원이름,email as 이메일,phone_number as 전화번호
from employees
where (salary between 1500 and 5000) and job_id='IT_PROG';

--[문제 8 ]   다음과 같이 사원번호 , 이름, 연봉을 출력하시오 

select employee_id as "사원번호",first_name || '  ' || last_name as "이  름",
       salary * 12 || '달러' as "연  봉"
from  employees;

 
--[문제  9] 사원의 이름과 job_id를 다음과 같이 출력하시오 

 select last_name || ' is a ' || job_id as "Employee Detail" from employees; 
--[문제 10] 급여가 2500이하 이거나 3000이상이면서 90번 부서인 사원의 이름, 급여, 부서ID를 출력하시오.
--      조건1) 제목은 사원명, 월  급, 부서코드로 하시오
--      조건2) 급여앞에 $를 붙이시오
--      조건3) 사원명은 first_name과 last_name을 연결해서 출력하시오

select first_name ||'  ' || last_name as "사원명",
       '$'|| salary as "월  급",department_id as "부서코드"
from employees
where (salary<=2500  or  salary>=3000) and department_id=90;

--[문제 11 ] 업무ID가 'SA_REP' 이거나 'AD_PRES' 이면서 급여가 15000를 
--초과하는 사원들의 이름, 업무ID ,급여를 출력하시오
 
select last_name as "이름",job_id as "업무ID", salary || '원' as "급 여"
from employees
where  (job_id = 'SA_REP' or job_id = 'AD_PRES') and salary > 15000;


--[문제12] Employees테이블의 업무ID가 중복되지 않게 표시하는 질의를 작성하시오
select distinct job_id
from employees;
 
 
--[문제13 ] 입사일이 97년인 사원들의 사원번호,이름,입사일을 표시하시오
select employees_id,last_name,hire_date
from employees
where hire_date like '97%';

  
--
--[문제 14 ] 업무ID에 MAN이 포함되어있는 사원들의 이름,업무ID,부서ID를 출력하시오

 

select last_name,job_id,department_id
from employees
where  job_id  like '%MAN%';


 
--[문제 15 ] 사원명, 부서ID, 입사일을  부서별로 내림차순 정렬하시오
--     같은부서가 있을때는  입사일 순으로 정렬하시오

select last_name,department_id,hire_date 
from employees
order by  department_id  desc,  hire_date asc;


 


--[문제 16] 사원의 레코드를 검색하시오(concat,  length)
--      조건1) 이름과 성을 연결하시오(concat)
--      조건2) 구해진 이름의 길이를 구하시오(length)
--      조건3) 성이 n으로 끝나는 사원(substr)
select  employee_id, concat(first_name,last_name) as name, 
length(concat(first_name,last_name)) as length
from employees
where  substr(last_name,-1,1)='n';

 

 
--[문제 17] 2000년 이후에 고용된 사원을 찾으시오 
select last_name,to_char(hire_date,'dd-mon-yyyy')
from employees
where hire_date>to_char(to_date('2000-01-01','yy-mm-dd'),'yy-mm-dd');
 
--[문제 18] 급여가 10000미만이면 초급, 20000미만이면 중급 그 외면 고급을 출력하시오
--조건1) 컬럼명은  '구분'으로 하시오
--      조건2) 제목은 사원번호, 사원명, 구  분
--      조건3) 구분(오름차순)으로 정렬하고, 같으면 사원명(오름차순)으로 정렬하시오

select employee_id as 사원번호,last_name as 사원명, 
       case 
          when salary<10000 then '초급'
          when salary<20000 then '중급'
          else '고급'
       end "구분"
from employees
order by 3,2;
 

--[문제 19 ] 사원테이블에서 사원번호, 이름, 급여, 커미션, 연봉을 출력하시오
--        조건1) 연봉은 $ 표시와 세자리마다 콤마를 사용하시오
--        조건2) 연봉 = 급여 * 12 + (급여 * 12 * 커미션) 
--        조건3) 커미션을 받지 않는 사원도 포함해서 출력하시오

select employee_id as "사원번호",last_name as "사원이름",
       salary as "급여", nvl(commission_pct,0) as "커미션",
       to_char(to_number((salary*12+(salary*12*nvl(commission_pct,0)))),
        '$9,999,999') as "연봉"
from employees;   

 
 
--[문제 20] 매니저가 없는 사원의 매니저id를, 1000번으로 표시
--        조건1) 제목은 사원번호,이름,매니저ID
--        조건2) 모든 사원을 표시하시오       
 
select employee_id,last_name,nvl(manager_id,1000) as manager_id
from employees;
```
</details>


# [2]SubQuery(서브쿼리)

- 서브쿼리 : 기본질의=주쿼리=기본쿼러=외부쿼라 / 서브쿼리 = 부쿼리 로 나뉜다.
            하나의 쿼리를 조건으로 자주 사용.(사용하기나름) 주 쿼리와 서브쿼리로 구현되는
            하나의 구문에서 먼저 서브쿼리가 실행되고 결과를 통해 주쿼리를 연산
            즉,서브먼저 주 나중 서브의 결과로 주를 연산

- SELECT,FROM ,GROUP BY, ORDER BY, UPDATE,HAVING,DELETE,INSERT INTO,WHERE 등에서 **사용할수있다.**
-   ()로 묶어서 사용된다. /비교조건의 오른쪽에 선언된다.
-   ★서브쿼리안에서 **ORDER BY 사용 X**
- 서브쿼리의 결과가 **다중행, 단일행**로 나뉜다.   

### 단일행 연산자
- 주로 >, >=, <, <=,==,!=
  
### 다중행 연산자
- IN, NOT IN, NOT ALY, NOT ALL, ANY, ALL....등
## 정리

다중 행 (Multiple-Row) 서브쿼리 – 하나 이상의 행을 리턴 하는 서브쿼리를 다중 행 서브쿼리라고 한다.

- 복수 행 연산자(IN, ANY, ALL)를 사용한다.

- IN : 목록에 있는 임의의 값과 동일하면 참  
- ANY : 서브쿼리에서 리턴된 각각의 값과 비교하여 하나라도 참이면 참 ( '=ANY'는IN과 동일) 
        EX) < ANY  = 최대값보다 적음   ,   >ANY  최소값보다 큼 /= 애니보다 크다 =최솟값보다크다
- ALL : 서브쿼리에서 리턴된 모든 값과 비교하여 모두 참이어야 참 
       EX) < ALL = 최소값보다 적음   ,   >ALL  최대값 보다 큼
- ★NOT 연산자는 IN, ANY, ALL 연산자와 함께 사용될 수 있다.
- 연산자 ANY() = OR, OR, OR 고 연산자 ALL() = AND, AND,AND   IN도 OR,OR,OR

### ★상호 연관(Correlated Subquery)서브쿼리
상의 질의 즉  주쿼리에 있는 테이블의 열을 참조하는 것을 말함.

### ★상호 연관(Correlated Subquery)서브쿼리가 시간이 오래걸리는이유
1. 메인쿼리의 하나의 row에서 서브쿼리가 한번씩 실행된다.
2. 테이블에서 행을 먼저 읽어서 각 행의 값을관련된 데이터와 비교한다.
3. 주 쿼리에서 각 서브쿼리의 행에 대해 다른결과를 리턴할 때 사용한다.
4. 각 행의 값에 따라 응답이 달라지는 다중 질의의 값을 리턴받을 때 사용한다.
5. 서브쿼리에서 메인쿼리의 컬럼명을 사용할 수 있지만 메인에서 는 서브쿼리의 컬럼명을
   사용할수없다.

### 인라인 뷰(inline): from 절에 서브쿼리
- 상호연관 쿼리보다 속도면에서 **빠르다**.

### 스칼라(Scalar) 서브쿼리
- 하나의 행에서 하나의 열 값만 리턴하는 서브 쿼리를 스칼라 서브쿼리
- select문에서 하나의 컬럼처럼 사용하기위해씀
- 스칼라 서브쿼리의 값은 서브 쿼리의 select 목록에 있는 항목 값이다.
- 서브쿼리가 0개의 행을 리턴하면 스칼라 서브쿼리의 값은 null
- 서브쿼리가 2개 이상의 행을 리턴하면 오류가 리턴된다.
- select(group by는 제외),insert의 values목록 ,decode의 case조건문,update set문

## ★서브쿼리 예제코드

<details>
<summary>서브,스칼라,인라인뷰 등등</summary>

```SQL

--Q1)JONES보다 월급을 많이 받는 사원의 이름과 봉급출력
SELECT SAL
FROM EMP
WHERE ENAME='JONES';    --2975

SELECT ENAME,SAL
FROM EMP
WHERE SAL>2975;

SELECT ENAME,SAL              --서브쿼리1 = JON+SAL>2975
FROM EMP
WHERE SAL > (SELECT SAL
              FROM EMP
              WHERE ENAME='JONES');
              
--Q2) 사원번호가 7839인 사원과 /'같은(동일한)' 직업을 가진 사원들의 이름과 직업을 출력하자

SELECT ENAME,JOB
FROM EMP
WHERE JOB = (SELECT JOB
            FROM EMP
            WHERE EMPNO=7839);
            
--Q3)7566사원보다 급여를 많이받는 사원의 이름, 급여를  출력해보자          
SELECT ENAME,SAL
FROM EMP
WHERE SAL > (SELECT SAL
              FROM EMP
              WHERE EMPNO=7566);
              
--Q4)사원T에서 사원의 봉급의 평균보다 적은 사원의 사원번호, 이름, 직업,부서번호

SELECT EMPNO,ENAME,JOB,DEPTNO,SAL
FROM EMP
WHERE SAL < (SELECT AVG(SAL)
                  FROM EMP);
                  
--Q5)사원번호가 7521인 사원과 직업이 같고/ 봉급이 7934인 사원보다 많은
--사원의 이름 직업 입사일 봉급 (조건이 두개일땐 AND를 사용해서 서브쿼리를 이어줄수잇다)

SELECT ENAME, JOB, HIREDATE,SAL
FROM EMP
WHERE JOB = (SELECT JOB
            FROM EMP
            WHERE EMPNO=7521)
AND SAL>(SELECT SAL FROM EMP WHERE EMPNO=7934);


--Q6)직업중에서 가장 작은 평균급여를 받는 직업을 출력하자

SELECT JOB,AVG(SAL)
FROM EMP
GROUP BY JOB
HAVING AVG(SAL) = (SELECT MIN(AVG(SAL))
             FROM EMP GROUP BY JOB);
          

--Q7)(서)사원의 봉급이 20번 부서번호의 최소 봉급/(주)보다 많은 부서번호를 출력하자.

SELECT DEPTNO,MIN(SAL)
FROM EMP
GROUP BY DEPTNO
HAVING MIN(SAL) > (SELECT MIN(SAL) FROM EMP WHERE DEPTNO=20);


--Q8)(서)부서별 최소 봉급과/ (주)같은 월급을받는 사원의 부서번호와 이름을 출력하자

SELECT DEPTNO,ENAME
FROM EMP
WHERE SAL IN (SELECT MIN(SAL)   --IN을쓴이유 서브쿼리가 하나이상의 행을 리턴해서.
                    FROM EMP        --IN은 (1 OR 2 OR 3 OR...)같은원리
                    GROUP BY DEPTNO);
  
 SELECT DEPTNO,ENAME    -- 중요 =ANY가 같다는거지 그냥ANY 같다는게아님
FROM EMP
WHERE SAL =ANY (SELECT MIN(SAL)   --IN을쓴이유 서브쿼리가 하나이상의 행을 리턴해서.
                    FROM EMP        --IN은 (1 OR 2 OR 3 OR...)같은원리
                    GROUP BY DEPTNO); 
                    
--Q9)업무가 SALESMAN인 사원의 최소값보다 급여를 많이 받는 사원의 이름,급여,직업출력

SELECT ENAME,SAL,JOB
FROM EMP
WHERE SAL >  ANY (SELECT SAL
             FROM EMP
             WHERE JOB = 'SALESMAN');  -- 컬럼 >ANY는 최소값보다 큼 즉 ANY는 OROR
                                      -- ALL은 AND, AND(다만족해야함)
                              
--Q10)FORD,BLAKE 와 매니저 및 부서번호가 /같은 사원의 정보를 출력해보자.

SELECT ENAME,MGR,DEPTNO
FROM EMP
WHERE (MGR,DEPTNO) IN
(SELECT MGR,DEPTNO FROM EMP WHERE ENAME IN ('FORD','BLAKE'));

--Q11)소속된 부서번호의 평균봉급보다 많은 봉급을 받는 사원의 이름,급여,부서번호,입사일
--직업을 출력하자

SELECT ENAME,SAL,DEPTNO,HIREDATE,JOB 
FROM EMP E
WHERE  SAL>  (SELECT AVG(SAL)
              FROM EMP
              WHERE DEPTNO = E.DEPTNO);   --밖의 EMP테이블과 별칭을 통해 연결하여
                                          --밖의 EMP테이블 안의 DEPTNO를 가져온다.

--아래가 11번문제를 인라인뷰로 바꾼것.(추가좀했음)
 
SELECT E.ENAME, E.SAL, E.DEPTNO, E.HIREDATE, D.AVGSAL
FROM EMP E,   (SELECT DEPTNO , AVG(SAL)  AVGSAL FROM EMP E GROUP BY DEPTNO) D
WHERE E.DEPTNO = D.DEPTNO AND E.SAL  > D.AVGSAL;

SELECT E.ENAME,E.DEPTNO,E.JOB             --아래에서 세개만 받아오게되어있으니 이쪽도 세개
FROM (SELECT ENAME,JOB,DEPTNO 
      FROM EMP WHERE JOB = 'MANAGER')E,DEPT D   
WHERE  E.DEPTNO = D.DEPTNO;

--Q12)
--CASE 1:
 SELECT E.ENAME, E.SAL, E.DEPTNO, E.HIREDATE, D.AVGSAL
 FROM EMP E,   (SELECT DEPTNO , AVG(SAL)  AVGSAL FROM EMP E GROUP BY DEPTNO) D
 WHERE E.DEPTNO = D.DEPTNO AND E.SAL  > D.AVGSAL;

--CASE 2: 
 SELECT E.ENAME, E.SAL, E.DEPTNO, E.HIREDATE, E.JOB, D.AVGSAL
 FROM EMP E,   (SELECT DEPTNO , AVG(SAL)  AVGSAL FROM EMP E GROUP BY DEPTNO) D
 WHERE E.DEPTNO = D.DEPTNO AND E.SAL  > D.AVGSAL;

--CASE 3: 
 SELECT E.ENAME, E.SAL, E.DEPTNO, E.HIREDATE, E.JOB
 FROM EMP E,   (SELECT DEPTNO , AVG(SAL)  AVGSAL FROM EMP E GROUP BY DEPTNO) D
 WHERE E.DEPTNO = D.DEPTNO AND E.SAL  > D.AVGSAL;


--Q13)사원번호,이름,부서번호, 사원이 속한 부서의 평균 급여를 출력하자.

SELECT EMPNO,ENAME,DEPTNO,SAL,
ROUND((SELECT AVG(SAL) FROM EMP WHERE DEPTNO= E.DEPTNO)) AS M_SAL
FROM EMP E;

--Q14)사원번호,이름,부서번호, 사원이 속한 부서를 출력하자
--ORDER BY 절 뒤에 '부서명' 별로 '정렬'하자. (ORDER BY 뒤에 같은 코드를 붙였다)
--즉 집계하자 =  SELECT절 뒤 일반 스칼라절쓰듯이
--정렬하자 = ORDER BY 뒤

SELECT EMPNO,ENAME,DEPTNO,SAL
FROM EMP E
ORDER BY (SELECT DNAME FROM DEPT WHERE DEPTNO = E.DEPTNO);

--Q15)★EXISTS연산자★
--부하 사원을 가지고 있는[EMPNO=MGR] 사원의 사원번호, 이름, 직업, 입사일,봉급을 출력하자

SELECT EMPNO,ENAME,JOB,HIREDATE,SAL
FROM EMP E
WHERE  EXISTS (SELECT 1        --EMPNO
                FROM EMP
                WHERE E.EMPNO=MGR     --EMPNO가 매니저번호에도있는 자료만출력
                )                     --즉 매니저번호에EMPNO가없으면 말단이라는소리
ORDER BY 1;
 
--Q16)부하사원이없는, 즉 말단 =  ![EMPNO=MGR]< 같지않다
SELECT EMPNO,ENAME,JOB,HIREDATE,SAL
FROM EMP E
WHERE NOT EXISTS (SELECT 1        --EMPNO
                FROM EMP
                WHERE E.EMPNO=MGR     --EMPNO가 매니저번호에도있는 자료만출력
                )                     --즉 매니저번호에EMPNO가없으면 말단이라는소리
ORDER BY 1;
 
 
 --서브쿼리 개인문제
 
-- Q1)'SMITH'보다 월급을 많이 받는 사원들의 이름과 월급을 출력하라.
SELECT ENAME,SAL 
FROM EMP
WHERE SAL > (SELECT SAL
             FROM EMP
             WHERE ENAME='SMITH');
             
--Q2) 10번 부서의 사원들과 같은 월급을 받는 사원들의 이름, 월급,부서번호를 출력하라.

SELECT ENAME,SAL,DEPTNO
FROM EMP
WHERE SAL IN(SELECT SAL FROM EMP WHERE DEPTNO=10);

--Q3)'BLAKE'와 같은 부서에 있는 사원들의 이름과 고용일을 뽑는데
--   'BLAKE'는 빼고 출력하라.

SELECT ENAME,HIREDATE
FROM EMP 
WHERE DEPTNO IN(SELECT DEPTNO
              FROM EMP
              WHERE ENAME='BLAKE') AND ENAME<>'BLAKE';
 
--Q4.평균급여보다 많은 급여를 받는 사원들의 사원번호, 이름, 월급을
-- 출력하되, 월급이 높은 사람 순으로 출력하라.         

SELECT EMPNO,ENAME,SAL
FROM EMP
WHERE SAL > (SELECT AVG(SAL)
              FROM EMP)
ORDER BY SAL DESC;


--Q5)이름에 'T'를 포함하고 있는 사원들과 같은 부서에서 근무하고
--   있는 사원의 사원번호와 이름을 출력하라.

SELECT EMPNO,ENAME,E.DEPTNO
FROM EMP 
WHERE DEPTNO IN(SELECT DEPTNO FORM WHERE ENAME LIKE'%7%');    --11명

DEPTNO IN (SELECT DEPTNO FROM EMP WHERE ENNAME LIKE %7%)

--Q6)자신의 급여가 평균급여보다 많고,이름에 S자가 들어가는 사원과 동일한
--  부서에서 근무하는 모든 사원의 사원번호,이름 및 급여를 출력하시오
--4명
SELECT EMPNO,ENAME,SAL
FROM EMP E
WHERE SAL >(SELECT AVG(SAL)
                      FROM EMP) AND
                      DEPTNO IN(SELECT DEPTNO FROM EMP WHERE ENAME LIKE ('%S%'))
                
 
--Q7)30번 부서에 있는 사원들 중에서 가장 많은 월급을 받는 사원보다
--   많은 월급을 받는 사원들의 이름, 부서번호, 월급을 출력하라.
--   (단, ALL 또는 ANY 연산자를 사용할 것)
SELECT ENAME,DEPTNO,SAL
FROM EMP
WHERE SAL >ALL (SELECT SAL
              FROM EMP
              WHERE DEPTNO=30);

--MAX+ANY
SELECT ENAME, DEPTNO, SAL 
FROM EMP e
WHERE SAL > ANY (
SELECT MAX(SAL) 
FROM EMP e
WHERE DEPTNO = 30
);

--Q8. 'DALLAS'에서 근무하고 있는 사원과 같은 부서에서 일하는 사원의
--   이름, 부서번호, 직업을 출력하라.

SELECT ENAME,DEPTNO,JOB
FROM EMP
WHERE DEPTNO IN(SELECT DEPTNO
FROM DEPT
WHERE LOC='DALLAS');


--Q9. SALES 부서에서 일하는 사원들의 부서번호, 이름, 직업을 출력하라.
SELECT DEPTNO,ENAME,JOB
FROM EMP
WHERE DEPTNO IN(SELECT DEPTNO FROM DEPT WHERE DNAME='SALES');


--Q10. 'KING'에게 보고하는 모든 사원의 이름과 급여를 출력하라.
--     (KING에게 보고하는 사원이란 mgr이 KING인 사원을 의미함)

SELECT ENAME,SAL
FROM EMP
WHERE MGR = (SELECT EMPNO FROM EMP WHERE ENAME='KING');

--Q11. 커미션을 받는 사원과 부서번호, 월급이 같은 사원의
--    이름, 월급, 부서번호를 출력하라.

SELECT ENAME,SAL,DEPTNO
FROM EMP
WHERE DEPTNO IN(SELECT DEPTNO FROM EMP WHERE COMM IS NOT NULL)
AND
SAL IN(SELECT SAL FROM EMP WHERE COMM IS NOT NULL);


--Q12. 30번 부서 사원들과 월급과 커미션이 같지 않은
--    사원들의 이름, 월급, 커미션을 출력하라.(30번 부서 제외) *단골시험문제*

SELECT ENAME,SAL,COMM
FROM EMP
WHERE SAL NOT IN(SELECT SAL FROM EMP WHERE DEPTNO=30)
AND 
COMM NOT IN(SELECT NVL(COMM,0) FROM EMP WHERE DEPTNO=30);

--Q13. 사원번호, 이름, 월급, 그리고 월급누적을 출력하라.

SELECT E.EMPNO, E.ENAME,E.SAL,SUM(D.SAL)
FROM EMP E,(SELECT EMPNO,SAL FROM EMP)D
WHERE E.EMPNO >= D.EMPNO
GROUP BY E.EMPNO,E.ENAME,E.SAL
ORDER BY 1;

```
</details>



# [3]JOIN

## JOIN(조인)

- 여러개의 테이블의 데이터가 필요한 경우 사용
- 관계형 데이터 베이스에서 기본
- 기준테이블에서 다른테이블의 있는 ROW를  찾아 오는 것
- RACLE 조인:EQUI,NON-EQUI,SELF,OUTER
- ★ANSI 조인:CROSS,INNER JOIN,NATURAL,OUTER(레프트 라이트 풀)

- JOIN =INNER JOIN =두개의 테이블에서 TRUE값만 출력,**FALSE,NULL은 추출되지않음**
    일반적인 JOIN=같은값만 추출된다

**문법이 조금씩 다름**
  ```SQL
    ORCLE : 
    FROM 테이블1,테이블2
    WHERE 테이블1.컬럼1 = 테이블2.컬럼2(컬럼1과 이름이 동일하다고 가정)

    ANSI:
    FROM 테이블1 JOIN 테이블2 USING(컬럼1) ★USING은 동일한 컬럼을 지정할때
                                          ★ON은 서로 다른 컬럼을 지정할때 ON(컬럼1=컬럼2)  
```

## JOIN예제코드

```SQL

--Q1.INNER JOIN 을 해보자
--SALESMAN의 사원번호, 이름,봉급,부서명,근무지(LOC)

--oracle join ver
SELECT EMPNO,ENAME,SAL,DNAME,LOC
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO;

--ansi ver 

SELECT EMPNO,ENAME,SAL,DNAME,LOC
FROM EMP JOIN DEPT USING(DEPTNO);   --같은 DEPNO를 지정하고싶으니까 USING이다.

--결과는 위와 동일하다 기본이 INNER JOIN
SELECT EMPNO,ENAME,SAL,DNAME,LOC    
FROM EMP INNER JOIN DEPT USING(DEPTNO);

--Q2)M,S 두 테이블의 M1,S1컬럼을 조인해보자
--ORCLE JOIN

SELECT *    
FROM M,S 
WHERE M1=S1;

--ANSI JOIN
SELECT *
FROM M JOIN S ON(M1=S1);

```
