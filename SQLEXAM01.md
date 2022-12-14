# ORACLE SQL EXAM01(2022-11-12~2022-11-13)

## 문제+오답풀이 

```SQL
--사원의 FULL_NAME(FIRST_NAME + LAST_NAME) 과 이메일을 출력하자 
--(이메일@HR.COM 으로 출력하자) 

select FIRST_NAME || LAST_NAME "FULL_NAME",EMAIL||'@HR.COM'
from employees;

--06년 이후에 입사한 사원의 이름(FIRST_NAME) 과 사원번호 (EMPLOYEE_ID)를 출력하자

SELECT FIRST_NAME,EMPLOYEE_ID,HIRE_DATE
FROM EMPLOYEES
WHERE TO_CHAR(HIRE_DATE,'YY')>='06';


--사원의 이름(FIRST_NAME), 부서이름(DEPARTMENT_NAME), 부서가 있는 거리(STREET_ADDRESS), 부서가 있는 나라(COUNTRY_NAME) 를 출력하자

select FIRST_NAME,DEPARTMENT_NAME,STREET_ADDRESS,COUNTRY_NAME
FROM EMPLOYEES E, DEPARTMENTS D, LOCATIONS L, COUNTRIES C;

--↓조인을 안함! 조인을해줘야 올바른 결과를 가져옴

SELECT FIRST_NAME,DEPARTMENT_NAME,STREET_ADDRESS,COUNTRY_NAME
FROM EMPLOYEES E, DEPARTMENTS D, LOCATIONS L, COUNTRIES C
WHERE E.DEPARTMENT_ID = D.DEPARTMENT_ID AND D.LOCATION_ID = L.LOCATION_ID AND L.COUNTRY_ID = C.COUNTRY_ID;

--'부서번호가 90이고, 전화번호가 515로 시작하면서, 끝자리가 4567인 사원'이 관리하는 사원의 사번과 이름을 출력하자

SELECT EMPLOYEE_ID, FIRST_NAME
FROM EMPLOYEES
WHERE MANAGER_ID=(SELECT EMPLOYEE_ID 
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 90 AND PHONE_NUMBER LIKE '515%' AND PHONE_NUMBER LIKE '%4567');

-- ↑PHONE_NUMBER LIKE '515%' AND PHONE_NUMBER LIKE '%4567') ->AND PHONE_NUMBER LIKE '515.%.4567'); 로 하면 좀 더 깔끔

--전화번호가 650.121.8009인 사원의 이름과, 사원이 속한 부서가 위치한 도시, 주소(STREET_ADDRESS + POSTAL_CODE) 를 출력하자

SELECT FIRST_NAME,DEPARTMENT_ID,LOCATION_ID,CITY,STREET_ADDRESS||' '||POSTAL_CODE AS "주소"
FROM EMPLOYEES JOIN DEPARTMENTS USING(DEPARTMENT_ID) JOIN LOCATIONS USING(LOCATION_ID)
WHERE PHONE_NUMBER = '650.121.8009';

--Canada 에서 일하고 있는 사원의 이름과, 도시, 월급을 출력하자
--이래도 저래도 결과는 잘나와서 그냥 조인냅둠
SELECT FIRST_NAME, CITY, SALARY
FROM EMPLOYEES JOIN DEPARTMENTS USING(DEPARTMENT_ID) JOIN LOCATIONS L USING(LOCATION_ID) RIGHT OUTER JOIN COUNTRIES C ON(L.COUNTRY_ID=C.COUNTRY_ID)
WHERE COUNTRY_NAME = 'Canada';

--이름이 Guy 인 사원과 같은 부서에서 일하면서,/ Guy와 직업(JOB_ID)이 다른 사원의 모든 것을 출력하자
SELECT *
FROM EMPLOYEES
WHERE DEPARTMENT_ID =
  (SELECT DEPARTMENT_ID
  FROM EMPLOYEES
  WHERE FIRST_NAME = 'Guy') AND JOB_ID != (SELECT JOB_ID FROM EMPLOYEES WHERE FIRST_NAME = 'Guy' );

--직업이 06년 7월 24일에 변경된 사원의 이름과, 과거 직업, 현재 직업을 출력하자(06년이과거고 01년이..현재..............?)
SELECT FIRST_NAME, J.JOB_ID AS 과거직업, E.JOB_ID AS 현재직업
FROM EMPLOYEES E LEFT OUTER JOIN JOB_HISTORY J ON(E.EMPLOYEE_ID = J.EMPLOYEE_ID) 
WHERE END_DATE = '06/07/24';

--관리자가 없는 부서의 이름과 부서번호를 출력하자

SELECT DEPARTMENT_NAME,DEPARTMENT_ID
FROM DEPARTMENTS
WHERE MANAGER_ID IS NULL;

--IT 부서 관리자의 성(LAST_NAME)과, 월급을 출력하자 (JOIN 사용하지 않고)

SELECT LAST_NAME,SALARY
FROM EMPLOYEES 
WHERE DEPARTMENT_ID =(SELECT DEPARTMENT_ID FROM DEPARTMENTS WHERE DEPARTMENT_NAME='IT');

--↓'관리자'의 정보이여야하니까 서브쿼리를 부서번호가아니라 매니저번호로 해야한다.
SELECT LAST_NAME,SALARY
FROM EMPLOYEES 
WHERE EMPLOYEE_ID =(SELECT MANAGER_ID FROM DEPARTMENTS WHERE DEPARTMENT_NAME='IT');

--관리자가 존재하는 부서의 장소 중 / 관리자가 가장 많은 장소의 도시 이름을 출력하자 (ROWNUM 사용) 
--=관리자..번호가..제일..큰것..?LOCATIONID와 MANAGERID는안겹치는데..?

SELECT ROWNUM,MANAGER_ID,LOCATION_ID,CITY
FROM (SELECT MANAGER_ID,D.LOCATION_ID,CITY
FROM DEPARTMENTS D, LOCATIONS L
WHERE MANAGER_ID IS NOT NULL AND D.LOCATION_ID = L.LOCATION_ID
ORDER BY MANAGER_ID DESC)
WHERE ROWNUM=1;

--↓문제 잘못이해, 가장많이나온 관리자번호의 도시이름을 출력하는것
SELECT ROWNUM,LC.CITY, LC.LCNT
FROM
(SELECT CITY,COUNT(*) AS LCNT
FROM DEPARTMENTS D JOIN LOCATIONS USING(LOCATION_ID)
WHERE MANAGER_ID IS NOT NULL
GROUP BY CITY
ORDER BY LCNT DESC) LC
WHERE ROWNUM=1;

--18년도가 근속 10주년인 사원의 이름과 입사일을 출력하자

SELECT FIRST_NAME,HIRE_DATE
FROM EMPLOYEES
WHERE TRUNC(months_between('18/12/31',HIRE_DATE)/12) = 10;

--사원 이름이 'S'로 시작하는 사원의 이름과 사원번호, 전화번호를 출력하자

SELECT FIRST_NAME,EMPLOYEE_ID,PHONE_NUMBER
FROM EMPLOYEES
WHERE FIRST_NAME LIKE 'S%';

--입사년도가 04년 이후인 사원들중 Seattle 에서 근무중인 사원들의 월급 총 합을 출력하자
--★
SELECT HIRE_DATE
FROM EMPLOYEES
WHERE TO_CHAR(HIRE_DATE,'YY')='04';

--↓시에틀에서 근무중인 사원을 빠트림
SELECT SUM(SALARY)
FROM EMPLOYEES JOIN DEPARTMENTS USING(DEPARTMENT_ID) JOIN LOCATIONS USING(LOCATION_ID)
WHERE CITY ='Seattle' AND TO_CHAR(HIRE_DATE,'YY')>='04';


--전체 평균 월급보다 월급을 많이 받는 사원들 중 9월에 입사한 사원들의 이름과 월급을 출력하자

SELECT FIRST_NAME,SALARY
FROM EMPLOYEES
WHERE SALARY >=
(SELECT AVG(SALARY)
FROM EMPLOYEES) AND TO_CHAR(HIRE_DATE,'MM')='09';

--LAST_NAME 의 세번째 글자가 c인 사원들의 풀네임을 출력하자

SELECT FIRST_NAME||LAST_NAME FULL_NAME
FROM EMPLOYEES
WHERE SUBSTR(LAST_NAME,3,1)='c';

SELECT FIRST_NAME||LAST_NAME FULL_NAME
FROM EMPLOYEES
WHERE LAST_NAME LIKE '__c%';


--부서 번호가 없는 사원의 이름(FIRST_NAME)과 직업(JOB_ID) 입사날(HIRE_DATE)을 출력하자

SELECT FIRST_NAME,JOB_ID,HIRE_DATE
FROM EMPLOYEES
WHERE DEPARTMENT_ID IS NULL;

--Kevin보다 월급을 많이 받고 / Susan 보다 적게 받는 / 사원의 이름과 월급을 출력하자

SELECT FIRST_NAME,SALARY
FROM EMPLOYEES
WHERE SALARY > ALL(SELECT SALARY FROM EMPLOYEES WHERE FIRST_NAME='Kevin')
AND SALARY <(SELECT SALARY FROM EMPLOYEES WHERE FIRST_NAME='Susan');

--Asia에 속해있는 도시이름과 나라 이름을 출력하자
--CON,REG,LOCATION

SELECT L.CITY,C.COUNTRY_NAME
FROM REGIONS R , LOCATIONS L , COUNTRIES C
WHERE R.REGION_NAME='Asia' AND R.REGION_ID = C.REGION_ID AND C.COUNTRY_ID = L.COUNTRY_ID;

SELECT CITY,COUNTRY_NAME
FROM REGIONS JOIN COUNTRIES USING(REGION_ID) JOIN LOCATIONS USING(COUNTRY_ID)
WHERE REGION_NAME='Asia';

--월급이 4000이상인 사원의 이름과 부서명, 월급을 출력하자

SELECT FIRST_NAME,DEPARTMENT_NAME,SALARY
FROM EMPLOYEES, DEPARTMENTS
WHERE SALARY >= 4000;

--↓JOIN을 빼먹음..!

SELECT FIRST_NAME,DEPARTMENT_NAME,SALARY
FROM EMPLOYEES JOIN DEPARTMENTS  USING(DEPARTMENT_ID)
WHERE SALARY >= 4000;

--부서의 평균월급이 / 전체 평균월급보다 높은 /부서의 부서이름과 평균월급을 출력하자
--★

SELECT D.DEPARTMENT_NAME,E.평균
FROM DEPARTMENTS D,
(SELECT DEPARTMENT_ID,AVG(SALARY)AS 평균 FROM EMPLOYEES GROUP BY DEPARTMENT_ID HAVING DEPARTMENT_ID IS NOT NULL) E
WHERE D.DEPARTMENT_ID = E.DEPARTMENT_ID 
AND E.평균 >(SELECT AVG(SALARY)
FROM EMPLOYEES) ;


--월급을 가장 많이 받는 사원의 전화번호를 출력하자

SELECT PHONE_NUMBER
FROM EMPLOYEES
WHERE SALARY = (SELECT MAX(SALARY) FROM EMPLOYEES);

--Seattle 에 근무하는 사원중 이름이 'l' (엘)로 끝나는 사원의 이름과 직업을 출력하자
--뭔가 제대로안나오는거같음

SELECT FIRST_NAME,JOB_TITLE,DEPARTMENT_NAME,CITY
FROM EMPLOYEES E LEFT OUTER JOIN JOBS J ON(E.JOB_ID=J.JOB_ID) LEFT OUTER JOIN DEPARTMENTS D ON(E.DEPARTMENT_ID=D.DEPARTMENT_ID)
LEFT OUTER JOIN LOCATIONS L ON(D.LOCATION_ID = L.LOCATION_ID)
WHERE CITY = 'Seattle' AND FIRST_NAME LIKE '%l';


--입사한 년도(hire_date) 별로 인원수를 출력하자

SELECT TO_CHAR(HIRE_DATE,'YY') AS 입사년도,COUNT(*)
FROM EMPLOYEES
GROUP BY TO_CHAR(HIRE_DATE,'YY')
ORDER BY 입사년도;


--Canada에서 일하는 직원의 수를 출력하자
--1900은안나와야하는게아닌가?
SELECT COUNT(*)
FROM DEPARTMENTS JOIN LOCATIONS USING(LOCATION_ID) JOIN COUNTRIES USING(COUNTRY_ID)
WHERE COUNTRY_NAME ='Canada';

--↓'직원 수'니까 직원테이블을 추가해줘야한다.
SELECT COUNT(*)
FROM EMPLOYEES JOIN DEPARTMENTS USING(DEPARTMENT_ID) JOIN LOCATIONS USING(LOCATION_ID) JOIN COUNTRIES USING(COUNTRY_ID)
WHERE COUNTRY_NAME ='Canada';

--입사 후 직업의 변경이 없는 사원의 사원 번호, 이름, 입사일, 월급, 부서 이름을 출력하자

SELECT EMPLOYEE_ID,FIRST_NAME,HIRE_DATE,SALARY,DEPARTMENT_NAME
FROM EMPLOYEES JOIN DEPARTMENTS USING(DEPARTMENT_ID)
WHERE EMPLOYEE_ID NOT IN(SELECT EMPLOYEE_ID FROM JOB_HISTORY);


--각 *부서 별* 커미션이 책정되지 않은 사원의 수를 출력하자
SELECT COUNT(NVL(COMMISSION_PCT,0))
FROM EMPLOYEES
WHERE COMMISSION_PCT IS NULL;

--↓*부서별*을 깜박함

SELECT DEPARTMENT_NAME,COUNT(NVL(COMMISSION_PCT,0)) 사원수
FROM EMPLOYEES JOIN DEPARTMENTS USING(DEPARTMENT_ID)
WHERE COMMISSION_PCT IS NULL
GROUP BY DEPARTMENT_NAME;

--핸드폰 번호가 011 로 시작하는 사원의 이름, 전화번호, 이메일을 출력하자

SELECT FIRST_NAME,PHONE_NUMBER,EMAIL
FROM EMPLOYEES
WHERE PHONE_NUMBER LIKE '011%';

--이름이 Britney 인 사원과 같은 부서에서 일하면서, Britney와 직업(JOB_ID)도 같은 사원의 모든 것을 출력하라.

SELECT *
FROM EMPLOYEES
WHERE (DEPARTMENT_ID,JOB_ID) IN(SELECT DEPARTMENT_ID,JOB_ID FROM EMPLOYEES WHERE FIRST_NAME='Britney');

--IT 부서의 관리자의 연봉(commission_pct 생각하기) 보다 더 많은 평균 월급을 받는 부서의 부서번호와 부서이름을 출력하자

SELECT D.DEPARTMENT_ID,D.DEPARTMENT_NAME,E.평균
FROM DEPARTMENTS D,
(SELECT DEPARTMENT_ID,AVG(SALARY)AS 평균 FROM EMPLOYEES GROUP BY DEPARTMENT_ID HAVING DEPARTMENT_ID IS NOT NULL) E
WHERE D.DEPARTMENT_ID = E.DEPARTMENT_ID 
AND E.평균 >(SELECT SALARY + NVL(COMMISSION_PCT,0)
FROM EMPLOYEES
WHERE EMPLOYEE_ID='103');

--↓'월급'(SALARY)이 아니라 '연봉'인걸 착각. SALARY*12 + COMMISSION_PCT를 해야함. 그리고 103번도되지만 IT를찾으라고했으니까 부서이름을추가.

SELECT D.DEPARTMENT_ID,D.DEPARTMENT_NAME,E.평균
FROM DEPARTMENTS D,
(SELECT DEPARTMENT_ID,AVG(SALARY)AS 평균 FROM EMPLOYEES GROUP BY DEPARTMENT_ID HAVING DEPARTMENT_ID IS NOT NULL) E
WHERE D.DEPARTMENT_ID = E.DEPARTMENT_ID 
AND E.평균 >ALL(SELECT SALARY*12 + NVL(COMMISSION_PCT,0)
FROM EMPLOYEES , DEPARTMENTS
WHERE DEPARTMENT_NAME='IT');

```