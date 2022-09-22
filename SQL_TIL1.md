SQL TIL1(22_09_19~22_09_20)

# [1]DataBase와 SQL

### - DataBase란?
>
    데이터베이스는 구조화된 정보 또는 데이터의 조직화된 모음으로서 일반적으로 컴퓨터 시스템에 전자적으로 저장되는데,데이터베이스는 일반적으로 데이터베이스 관리 시스템(DBMS)에 의해 제어됨.연결된 애플리케이션과 함께 데이터와 DBMS를 하나로 묶어 데이터베이스 시스템이라고 하며 단축하여 데이터베이스라고도 한다.

### - SQL(Structured Query Language)?
>
    SQL은 데이터를 쿼리, 조작 및 정의하고 액세스 제어를 제공하기 위해 거의 모든 관계형 데이터베이스에서 사용되는 프로그래밍 언어. SQL의 시초는 1970년대에 IBM에서 처음 개발되었으며 Oracle의 적극적인 공헌으로 SQL ANSI 표준이 수립되기에 이르게되었다. SQL은 오늘날에도 널리 사용되고 있지만 새로운 프로그래밍 언어가 등장하기 시작했다.

### 데이터 베이스의 유형은 어떤게있을까?

- RDB(Relational Database)/RDBMS(Relational Database Management System)/관계형 :열과 행이있는 테이블의 집합으로 구성. 정형정보에 접근하는 가장효율적인 방법을 제공.
  
- 객체지향 데이터베이스 : 정보를 객체 형태로 표현한다.
- 분산 데이터베이스 : 서로 다른사이트에 위치한 둘 이상의 파일로 구성. 물리적으로 같은위치에 있는 데이터베이스는 다른 네트워크에 분산될수있다.
- 데이터 웨어하우스 : 빠른쿼리 및 분석용
- NoSql 데이터베이스 : 비정형,반정형 데이터를 저장하고 조작할수있다.
- 그래프 데이터베이스 : 엔티티 및 엔티티 간의 관계 측면에서 데이터 저장
- 오픈소스 데이터베이스 : 소스코드가 오픈 소스인시스템임(SQL,Nosql)
- 클라우드 데이터베이스 : 하이브리드 클라우드 컴퓨팅 플랫폼에 상주하는 정형,비정형 데이터 모음.(DBaaS)
- 다중모델 데이터베이스 : 서로 다른유형을 단일 통합 백엔드로 결합.
- 문서/JSON : 행/열 대신 JSON형식으로 데이터를 저장함.문서 지향 정보 를저장,검색,관리
- 자율 운영 데이터베이스 : 클라우드를 기반으로 머신 러닝을 사용하여 데이터베이스 튜닝, 보안 ,백업, 업데이트 등의 관리작업을 자동화시킴

-------------------------------------------------------------------------
# [2]오라클(Oracle Database)

![오라클](https://cdn.digitaltoday.co.kr/news/photo/202106/406162_403436_326.jpg)
>
    미국 오라클(Oracle)사의 관계형 데이터베이스 관리 시스템의 이름이다. 현재 유닉스 환경에서 가장 널리 사용되는 RDBMS이다. 검색이나 업데이트용 언어로는 국제표준화기구의 표준 구조화 조회 언어와 PL/SQL을 지원한다.
    버전



### 오라클 말고 어떤 종류가있을까?

대표적으로 아래와 같은 종류들이있다. 종류마다 조금씩 문법이 다르다.
1. Mysql [MySql홈페이지](https://www.mysql.com/)
2. MariaDB [MariaDB홈페이지](https://mariadb.org/)
3. SQL Server [SQL Server홈페이지](https://www.microsoft.com/ko-kr/sql-server/)


# [3] 실습과 예제코드

기본테이블 조회문과 실행순서를 대표로 이하 실습코드들은 분류별로 나눠서 접어놨으니 펼쳐보자.

### SQL문의 실행 순서
> 
    1   FROM     -> JOIN을 통해서 테이블을 생성
    2   WHERE   ->하나의 ROW씩 읽어서 조건을 만족하는 결과를 추출한다
    3   GROUP BY  -> 원하는 행들을 그룹핑한다.
    4   HAVING  ->  조건을 만족하는 그룹을 남긴다
    5   ORDER BY  -> 조건에 따라 정렬한다
    6   SELECCT    -> 원하는 결과만 SELECT한다.

### 기본 테이블 조회
```SQL
select * from all_tables; 모든테이블을 출력
select * from all_tab_comments where table_name='테이블명' 테이블 코멘트 조회

select * from cols where table_name ='테이블명'; 지정한 테이블이름 컬럼

select * from tabs; / select * from user_objects where object_type='table' 접속한 계정의 테이블 목록 조회
```
<details>
<summary>계정생성/권한/세션변경</summary>

### 계정생성과 권한부여, 세션변경
```SQL
alter session set "_ORACLE_SCRIPT"=TRUE; #C ##CC 등을 세션을바꿔줌으로써 편하게사용할수있다.

create user big22 identified by ****;  big22라는 계정생성
grant connect,resource, dba to big22;  connet,resource,dba 권한을 big22에게부여

~SQL디벨로퍼로 보면~
- USER SQL
ALTER USER "BIG21"
DEFAULT TABLESPACE "USERS"
TEMPORARY TABLESPACE "TEMP"
ACCOUNT UNLOCK ;

-- QUOTAS

-- ROLES
GRANT "DBA" TO "BIG21" ;
GRANT "CONNECT" TO "BIG21" ;
GRANT "RESOURCE" TO "BIG21" ;
```
</details>


<details>
<summary>별칭 AS /연산 펼치기</summary>

### 별칭과 AS / 연산

```SQL
SELECT * 
FROM SCOTT.EMP, SCOTT.DEPT; -- CROSS JOIN (=전체출력) / ANSI QUERY


--Q1)테이블에 별칭을줘서 DEPTNO를주자
SELECT E.ENAME, D.DEPTNO
FROM SCOTT.EMP E,SCOTT.DEPT D; 
                              
--Q2-1)별칭X테이블명으로도가능 명시해주는 방법도있다.
SELECT ENAME, SCOTT.DEPT.DEPTNO
FROM SCOTT.EMP,SCOTT.DEPT;

--Q2-2)한쪽에만 테이블에만 명시.
SELECT ENAME, D.DEPTNO
FROM SCOTT.EMP,SCOTT.DEPT D;

--Q2-3)별칭에 ""를 주는 케이스. 이거 오류안남. 컬럼에는 "" 데이터값에는''
SELECT ENAME, "D".DEPTNO
FROM SCOTT.EMP,SCOTT.DEPT "D";      한쪽에만 "D"를줘도 오류나지않는다.

--Q3)사원의 테이블에서 사원이름과 봉급을 출력하되 봉급은 연봉으로 출력하자

SELECT ENAME, SAL *12 연봉
FROM SCOTT.EMP;

--Q4) 사원의 테이블에서 이름과 봉급을 출력하되 "ㅇㅇ의 봉급은 ㅇㅇ이다"
SELECT ENAME||'의 봉급은'|| SAL ||'이다' 봉급내역 
FROM SCOTT.EMP;
```

</details>


<details>
<summary>WHERE/NVL/NVL2</summary>

## WHERE/NVL/NVL2

```SQL
--Q11)사원테이블에서 사원이름,봉급,봉급+커미션 한 값을 월급으로 출력
SELECT ENAME, SAL,COMM, SAL+NVL(COMM,0) 월급
FROM SCOTT.EMP;
  --NULL의 키워드는 null
  --NULL은 문자 0은 숫자
  --NULL은 공백의 문자이다.
  --NULL의 연산결과는 NULL이다
  --NULL을 하나라도 포함한 데이터의 연산결과는 NULL/ 한행의 열에 데이터가없으면 NULL

--Q12)NVL(컬럼명,초기값)을 이용하여 NULL값처리.
SELECT ENAME, SAL,COMM, SAL+NVL(COMM,'0') 월급 NULL이면 초기값,아니면 컬럼값
FROM SCOTT.EMP;        

--Q13)커미션값이 측정되지않은 친구들은 SAL같으로 채움

SELECT ENAME, SAL, COMM, NVL(COMM,SAL)널값봉급
FROM SCOTT.EMP;

--Q14)ENAME과 MGR사이에 'ABCD'를 컬럼으로 출력하자
SELECT ENAME,'ABCD',MGR --값도'ABCD'로채워짐
FROM SCOTT.EMP;

--Q15)사원이름(사원), 관리자(관리자)로 출력해보자 
SELECT ENAME||'(사원)', MGR||'(관리자)',"D".LOC||'(위치)'  
FROM SCOTT.EMP, SCOTT.DEPT D;

--Q16)NVL2(컬럼,NULL이아닐때,NULL일때)
SELECT ENAME,DEPTNO,COMM,NVL2(COMM,'X','O')
FROM SCOTT.EMP;

```
</details>

<details>
<summary>중복제거/의사열/이상이하/Between/In</summary>

## 중복제거/의사열/>=,<=/Between

```SQL
--Q17)부서별(DEPTNO) 담당하는 업무(JOB)를 한번씩만 조회한다.
SELECT DISTINCT DEPTNO ,JOB 
FROM SCOTT.EMP;

--Q18)의사열 : 테이블과 유사한 쿼리가능한 열.
--  ROWNUM:SELECT 문으로 검색하게 되면 로우수를 리턴한다(로우갯수리턴)
    /* -> 검색된 행의 일련번호. 12345678등 안겹치는 '일련번호'.
    ORDER BY 에 의한 정렬전에 부여된다.
--  ROWID:테이블내에 특정한 행을 구별할수 있는 ID 말그대로 로우의아이디
      ->즉 검색된 행에게 절대 중복되지않는 ID를 부여해주는거임.
*/
SELECT ROWNUM,ROWID,ENAME
FROM SCOTT.EMP;

--Q20)급여가 3000이상인 사원의번호,이름,봉급출력

SELECT EMPNO,ENAME,SAL
FROM SCOTT.EMP
WHERE SAL>=3000;

--Q21)BETWEEN을 사용해보자. WHERE 대상컬럼 BETWEEN 최소값 AND 최댓값 = 이상이하값

SELECT ENAME,SAL
FROM SCOTT.EMP
WHERE SAL BETWEEN 1300 AND 1700; -- SAL >= 1300 AND SAL<=1700

--Q22)비트윈앞에 NOT을써보자
SELECT ENAME,SAL
FROM SCOTT.EMP
WHERE SAL NOT BETWEEN 1300 AND 1700; --비트윈앞에 NOT쓰면 1300~1700을제외한값가져옴

SELECT ENAME,SAL
FROM SCOTT.EMP
WHERE SAL < 1300 OR SAL >1700;

--Q23)BETWEEN 기출변형. 최소 최댓값의 위치를 바꿔보자.
SELECT ENAME ,SAL
FROM SCOTT.EMP
WHERE SAL BETWEEN 1700 AND 1300;  --오류는안나는데 결과는나온다.

--Q24)IN 여러값 중에 일치하는 값 WHERE 대상컬럼 IN (3,4,5) 

  /* IN안에 들어있는값이랑 일치하는 결과를 가져옴. 컬럼값이 3,4,5인값출력.
     IN=ANY연산자와 같다.
     NOT IN != ALL . IN = ALL
     NOT IN(목록)은 목록에있는애를 가져오지 않는거니까 목록을 피해감
     */
--사원번호가 7920,7788,7566 인 사원의 이름과 사원번호 입사일

SELECT ENAME,EMPNO,TO_CHAR(HIREDATE,'YYYY"년"-MM"월"-DD"일" DAY')AS 문자포맷 --AS써도되고..안써도되고..
FROM SCOTT.EMP                     --EMPNO가 7902 7799 7566인 친구를 다불러옴
WHERE EMPNO IN(7902,7788,7566);   --TO캐릭터 지정된포맷으로 문자열로바꿔줌
                                  --TO시리즈 중 가장 많이쓰는것 캐릭터,데이트,넘버
SELECT ENAME,EMPNO,HIREDATE
FROM SCOTT.EMP
WHERE EMPNO NOT IN(7902,7788,7566); --위의 결과 세명이 제외된결과가나온다.

```
</details>

<details>
<summary>Like/문자열/IsNull/Order By</summary>

## Like와 각종문자열,IsNull/Order By

```SQL
--Q25)LIKE(문자의 패턴이 같은 값)
/*
    특정 패턴에 속하는 문자열을 추출하는 키워드
    %:임의의 길이 문자열(공백포함) ->LIKE %문자열~ OR 문자열% 등 ~로끝나고 ~로시작하는
    _:한글자
    ESCAPE:검색할 문자에 %,_ 문자 대응.
*/
--사원의 이름이 S로 시작하는 사원의 이름 봉급을 출력하자
SELECT ENAME,SAL
FROM SCOTT.EMP
WHERE ENAME LIKE 'S%';

--두번째글짜가L로 시작하는
SELECT ENAME,SAL
FROM SCOTT.EMP
WHERE ENAME LIKE '_L%';       

--PLAYER_T테이블(가상)에서 영문이름이 _문자가 들어있는 선수의 정보를 출력하자
SELECT PNAME
FROM PLAYER_T
WHERE PNAME LIKE '%#_%' ESCAPE '#'; --__ 대신에 #으로 구분을하겟다.
--즉 이스케이프 뒤에오는 구분자를가지고 앞에있는 친구를 대신하겠다라는 뜻.
--위의 예제를보면 #을 가지고 _(언더바)를 대신함.
--데이터 _(언더바)가들어오면 #으로 간주하겠다는것

--Q26)커미션이 측정되지 않은 사원을 출력해보자
SELECT *
FROM SCOTT.EMP
WHERE COMM IS NULL;

--이건 커미션측정된사람
SELECT *
FROM SCOTT.EMP
WHERE COMM = NVL(COMM,0); --null이면 0으로대신한다.

SELECT *
FROM SCOTT.EMP
WHERE COMM IS NOT NULL; -- COMM이 NULL이 아닌값을 출력한다.

--Q30)order by절 얘 는늘 절의 맨마지막에.
/*
  SELECT
  FROM
  WHERE
  ORDER BY ASC|DESC 컬럼명: SELECT 문장의 마지막에 명시한다.
  
  -ASC 오름차순
  -DESC 내림차순
  NULL값은? 오름차순시 마지막에 표시된다.
            *오름차순 내림차순 판단은 아스키코드값

*/


--★데이터를 찾을떄,전체 데이터를 반으로 쪼개고 그걸 다시 나누고 나누고 나눠진 구조이므로 찾아갈때도 위에서부터 찾아내려온다

SELECT ROWNUM,ROWID,ENAME,EMPNO,SAL,DEPTNO,TO_CHAR(HIREDATE,'YY"년"-MM"월"-DD"일"')입사일
FROM SCOTT.EMP
ORDER BY 5;  --컬럼명대신 숫자로표시할수도있다. 다섯번째는 SAL.

--Q30)부서별로 담당하는 업무를 한번씩 조회하자, 업무기준으로 정렬.

SELECT DISTINCT DEPTNO,JOB  --부서별로 담당하는 업무를하나씩조회
FROM SCOTT.EMP      --이러면 부서번호1개당 JOB1개인데 번호와 JOB이 서로겹치지않게나옴
ORDER BY JOB;   
```
</details>

<details>
<summary>문자,숫자,날짜,변환,기타함수</summary>

## 문자,숫자,날짜,변환,기타(분석,윈도우)함수

```SQL
SELECT INITCAP('the soap') "Capitals"--첫글자를 대문자로.
FROM DUAL; 

--Q32)SCOTT의 직업을 전체소문자로출력
SELECT EMPNO, ENAME, LOWER(JOB) 소문자출력
FROM SCOTT.EMP
WHERE ENAME=UPPER('scott');      --UPPER로 scott를 대문자로바꿔준다.

--Q33)EMPNO와ENAME을 붙여서출력하자 단 CONCAT이용

SELECT ENAME,EMPNO,CONCAT(ENAME,EMPNO)  --안에들어있는 데이터들을 이어준다.
FROM SCOTT.EMP;                           

--Q34)DEPT 테이블에서 컬럼의 첫 글자들만 대문자로 변화하여 모든 정보를 출력하여라. 
SELECT INITCAP(DEPTNO),INITCAP(DNAME),INITCAP(LOC)
FROM SCOTT.DEPT;
  
 --Q35)EMP 테이블에서 이름의 첫글자가 'K'보고 크고 'Y'보다 작은 사원의 사원번호, 이름, 업무, 급여, 부서번호를 조회한다. 
        --단, 이름순으로 정렬하여라. 
SELECT EMPNO,ENAME,JOB,SAL,DEPTNO
FROM SCOTT.EMP
WHERE SUBSTR(ENAME,1,1) >'K' AND SUBSTR(ENAME,1,1) <'Y'
ORDER BY 2;

--Q36)EMP 테이블에서 부서가 20번인 사원의 사원번호, 이름, 이름의 자릿수, 급여, 급여의 자릿수를 조회한다.LENGTH사용

SELECT EMPNO,ENAME,LENGTH(ENAME) "이름의 자릿수", SAL,LENGTH(SAL) "급여의 자릿수"
FROM SCOTT.EMP
WHERE DEPTNO='20';

--Q37)EMP 테이블에서 이름 중 'L'자의 위치를 조회한다.
      --EX) ALLEN	2	2	3	0
SELECT ENAME,INSTR(ENAME,'L',1,1)
FROM SCOTT.EMP;
 
--Q38)EMP 테이블에서 10번 부서의 사원에 대하여 담당 업무 중 좌측에 'A'를 삭제하고
       --급여 중 좌측의 1을 삭제하여 출력하여라. LTIRM사용

SELECT DEPTNO,JOB,TRIM(TRAILING 'A' FROM JOB),SAL,LTRIM(SAL,'1')
FROM SCOTT.EMP
WHERE DEPTNO = '10';   그냥 TRIM은 실패
--LTRIM
SELECT DEPTNO,JOB,LTRIM(JOB,'MA'),SAL,LTRIM(SAL,'1')
FROM SCOTT.EMP
WHERE DEPTNO = '10'

--REPACE사용
SELECT JOB,replace(job,'A','')
FROM SCOTT.EMP
WHERE DEPTNO='10';


--Q39)REPACE함수를 사용하여 사원이름에 SC문자열을 *?로 변경해서 조회. 

SELECT ENAME,REPLACE(ENAME,'SC','*?')
FROM SCOTT.EMP;

--Q40)TRANSLATE함수를 사용하여 사원이름에 SC문자열을 *?로 변경해서 조회한다

SELECT ENAME,TRANSLATE(ENAME,'SC','*?')
FROM SCOTT.EMP;

```
</details>


<details>
<summary>GROUP,HAVING,집계함수</summary>

## GROUP과 조건HAVING,집계함수

```SQL
/* 
  그룹함수 : GROUP BY와 함께 사용한다.
  SELECT
  FROM
  WHERE
  GROUP BY
  HAVING 
  ORDER BY +ROLL UP(), CUBE() 
  ,GROUPING은 SELECT절. GROUPING(컬럼명)
  
  다중 행 함수는 조건연산을 할때는 HAVING을 사용한다.
  */

 --Q41)집계함수1

SELECT MIN(HIREDATE),MAX(HIREDATE),MEDIAN(HIREDATE),COUNT(HIREDATE)
FROM SCOTT.EMP;

--Q42)집계함수2
SELECT MAX(SAL),MIN(SAL),MEDIAN(SAL),ROUND(AVG(SAL),2),SUM(SAL)
FROM SCOTT.EMP;

--Q43)직업별로 직원수
SELECT JOB,COUNT(JOB)     
FROM SCOTT.EMP              
GROUP BY JOB;

SELECT COUNT(*),COUNT(COMM),COUNT(ENAME)  --NULL값처리안되고 COUNT는*사용가능
FROM SCOTT.EMP;

--Q44)사원테이블에서 부서별로 봉급,가장큰값,작은값,중간값,평균,합계출력
SELECT DEPTNO, MAX(SAL),MIN(SAL),MEDIAN(SAL),ROUND(AVG(SAL),0)
FROM SCOTT.EMP
GROUP BY DEPTNO;

--Q45)급여의 합이 많은 순으로 정렬하자.
SELECT DEPTNO, MAX(SAL),MIN(SAL),MEDIAN(SAL),ROUND(AVG(SAL),0),SUM(SAL)
FROM SCOTT.EMP
GROUP BY DEPTNO
ORDER BY SUM(SAL) DESC;       --OR ORDER BY 6.

--Q46)두개씩 그루핑하자. 부서별,직업별 봉급합출력

SELECT JOB,DEPTNO,SUM(SAL)
FROM SCOTT.EMP
GROUP BY JOB, DEPTNO;

--Q47)사원 테이블에서 부서인원이 4명 보다 많은 부서의 부서번호,인원수,급여의합

SELECT DEPTNO,COUNT(*),SUM(SAL) 합계             
FROM SCOTT.EMP                                
GROUP BY DEPTNO
HAVING COUNT(*)>4;
/*
  WHERE는 집계함수이전,HAVING은 집계함수이후에 필터링작업
  HAVING 을 이용해서 집계함수결과로 그룹을 제한한다. 
  그룹이 형성(행 분류) -> 그룹함수 계산 -> HAVING절 필터링
  HAVING절은 반드시 그룹바이에 선언한 컬럼이나 집계함수 비교시 사용
  =헤빙절에 그룹안한 컬럼이나 집계함수 아닌거 넣으면 X
  
★그룹은 두번까지만 가능.
*/
--Q48)사원테이블에서 급여가 최대2900 이상인 부서에 대해서 부서번호,평균,급여합계를 구하자

SELECT DEPTNO,ROUND(AVG(SAL),1) 평균급여,SUM(SAL) 급여합계
FROM SCOTT.EMP
GROUP BY DEPTNO
HAVING MAX(SAL) >=2900;

--Q49) 업무별 급여의 평균이 3000 이상인 업무에 대해서 평균급여, 급여의 합계를 구하자

SELECT JOB,AVG(SAL),SUM(SAL)
FROM SCOTT.EMP
GROUP BY JOB
HAVING AVG(SAL)>=3000;

--Q50) 부서별 평균 급여 중 최대값을 조회해보자
SELECT ROUND(MAX(AVG(SAL)),1)
FROM SCOTT.EMP
GROUP BY DEPTNO;
```
</details>


## [4]참고문서
오라클 데이터베이스:https://www.oracle.com/kr/database/what-is-database/

오라클:https://www.oracle.com/kr/
