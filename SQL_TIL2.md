SQL TIL(22_09_24)

# 각종 함수들을 코드를 통해 알아보자

## [1] 숫자,날짜,변환함수

숫자,날짜,변환함수들에 대해알아보자.

|제목|내용|설명|
|:------|:---:|:---:|
|ROUND|자릿수를 지정해서 남기고 반올림|아래 날짜+문자 부분참조|
|TRUNC|자릿수를 지정해서 남기고 버림|아래 날짜+문자 부분 참조|
|MOD|나머지반환|-|
|ABS|절대값으로 만들어준다|-|
|FLOOR|지정된수보다 작거나 같은정수|-|
|CEIL|지정된수 보다 크거나 같은정수값|-|
|SIGN|음수양수판별 음수면 -1, 양수면 1,0이면 0 반환|-|
|POWER|M의N승|-|


아래는 기본활용법이다.

(그외의 예제들은 접어놨다.)
```SQL
--Q1)ROUND 를확인해보자
SELECT ROUND(4567.678)결과1,ROUND(4567.678,0)결과2,ROUND(4567.678,2)결과3,ROUND(4567.678,-2)결과4
FROM DUAL;

--Q2)TRUNC를 확인해보자

SELECT TRUNC(4567.678)결과1,TRUNC(4567.678,0)결과2,TRUNC(4567.678,2)결과3,TRUNC(4567.678,-2)결과4
FROM DUAL;

--Q3)사원테이블에서 급여를 30으로 나눈 나머지를 출력하자. 이름과 급여 결과를 출력해보자

SELECT ENAME, SAL, MOD(SAL,30) "결 과"      "여기안에 공백을넣기위해 ""를썻다"
FROM SCOTT.EMP E;


--Q4)★중요/날짜함수의 서식을 확인해보자
SELECT VALUE 
FROM NLS_SESSION_PARAMETERS          --키밸류값을 초기 데이터 베이스의 포맷을 관리하는 테이블(포맷형식테이블)
WHERE PARAMETER ='NLS_DATE_FORMAT';   --RR/MM/DD(00~49:2000년대), DD/MON/RR(50~99:1900년대)
                                      --RR=2000년대표시             DD=1900년대년도를표시할때
SELECT PARAMETER,VALUE
FROM NLS_SESSION_PARAMETERS;          --파라미터와 밸류만보면 편함. 이름 어떤용도 이렇게나옴

--7BYTES로 내부 표현을 하게된다. 시간,날짜값이 '상수'로 리턴된다.
--국가, 년도, 달, 날, 시간,분,초를 포함한 7바이트! 이런 배치정보를가지고 '상수'로 리턴이된다.

/*
  2011년 6월7일 오전 3시 15분 47초 -> 07-JUN-11리턴
  국가, 년도, 달, 날, 시간, 분,  초
   20   11   06  07   3   15    47   이런식으로 메모리상에 들어가는것.
위와같은 형태로 들어가기때문에 날짜는 산술연산이가능한데 단, 날짜+날짜는X
*/

--Q5)날짜형식은 산술연산이 가능하다. 
--20번부서의 사원이름 입사일 입사일보다 이후3일이후 날짜 출력
SELECT SYSDATE,ADD_MONTHS(SYSDATE,3) --얘는 3개월후
FROM DUAL;

SELECT ENAME,HIREDATE,HIREDATE+3  --얘는Day. 3일후
FROM SCOTT.EMP
WHERE DEPTNO=20;
--얘는 포맷을씀 
SELECT ENAME,TO_CHAR(HIREDATE,'YYYY-MM-DD-dy'),HIREDATE +3  --이거 Dy같은결과.
FROM SCOTT.EMP                                              --DAY OR day는 요일까지 dy Dy는 수 이런식으로
WHERE DEPTNO=20;

--Q6)EXTRACT함수 : 입력날짜 중 년/달/일 을 선택해서 추출한다.

SELECT EXTRACT(YEAR FROM SYSDATE)     --EXTRACT(Y/M/D FROM 날짜)
FROM DUAL;

--입사일의 달만 출력
SELECT ENAME,TO_CHAR(HIREDATE,'YYYY-MM-DD-Dy'),EXTRACT(MONTH FROM HIREDATE)   
FROM SCOTT.EMP;

--Q7)사원T에서 사원의 현재까지의 근무일수가 몇주 몇일인지 조회

/*
MONTHS_BETWEEN(날짜,날짜):날짜와 날짜사이의 개월수를 반환  --단 리턴값이 숫자.밸류임
ADD_MONTHS(날짜,더할값):날짜에 더할 개월을 입력, 더한 개월을 반환 --날짜데이터로반환
NEXT_DAY(기준일자,찾을요일): 기준일자의 다음에오는 찾을요일의 날짜를 구한다. -8하면 이전요일에 해당하는 날짜를 찾을수있다.--날짜데이터로반환
LAST_DAY : 해당월의 마지막 날짜를 리턴 --날짜데이터로반환
*/
--이건 그냥 입사일부터 몇일 일했는지!
SELECT HIREDATE, SYSDATE, TRUNC(SYSDATE - HIREDATE,3) AS "TOTALD"
FROM SCOTT.EMP;

--★입사날부터 오늘까지 일한날짜가 몇'주'인지!!★
SELECT HIREDATE, SYSDATE, TRUNC(SYSDATE - HIREDATE,3) AS "TOTALD", 
TRUNC((SYSDATE -HIREDATE)/7,0)AS WEEKS
FROM SCOTT.EMP;

--★그 주가 몇일인지

SELECT HIREDATE, SYSDATE, TRUNC(SYSDATE - HIREDATE,3) AS "TOTALD", 
TRUNC((SYSDATE -HIREDATE)/7,0)AS WEEKS,
ROUND(MOD((SYSDATE-HIREDATE),7),0)DAYS
FROM SCOTT.EMP
ORDER BY 4 DESC;


--Q8)사원테이블에서 10번 부서의 사원들이 현재까지의 근무 월수를 계산해서 리턴-MONTH_BETWEEN

SELECT ENAME,TO_CHAR(HIREDATE,'YYYY-MM-DD-DAY')AS 원래값,
SYSDATE AS 오늘,TRUNC(MONTHS_BETWEEN(SYSDATE, HIREDATE),3)AS 근무월수,
MONTHS_BETWEEN(TO_DATE(TO_CHAR(SYSDATE,'MM-DD-YYYY')), TO_DATE(HIREDATE,'MM-DD-YYYY')) TODATE테스트 
FROM SCOTT.EMP
WHERE DEPTNO=10
ORDER BY 4 DESC;   날짜1-날짜2 =두 날짜간의 개월수 출력

--Q9)사원테이블에서 10번 30번 부서의 사원들의 입사일로부터 5개월이지난 후 날짜계산
SELECT DEPTNO,ENAME,TO_CHAR(HIREDATE,'YYYY-MM-DD-DAY')AS 원래값,
ADD_MONTHS(HIREDATE,5)
FROM SCOTT.EMP
WHERE DEPTNO IN(10,30)

--*TEST
SELECT MONTHS_BETWEEN(TO_DATE('02-02-1995','MM-DD-YYYY'), TO_DATE('01-01-1995','MM-DD-YYYY') ) 
FROM DUAL; --데이트타입으로 02 02 1955를 MM DD YYYY자리에 맞춰 날짜로변환하겠다.
--결론은 특정서식으로 데이트타입을가져오고싶으면 TO_CHAR ->다시 TO_DATE로

--Q10) 사원테이블에서 10번 부서 사원들의 입사일로 부터 돌아오는 금요일 계산

SELECT ENAME,HIREDATE,NEXT_DAY(HIREDATE,6)  --돌아오는금요일이 언제인지 출력. 
FROM SCOTT.EMP                --일,월,화,수,목,금
WHERE DEPTNO=10;

```


<details>
<summary>날짜+문자함수/CASE,DECODE</summary>

## [2] 날짜+문자,Case,Decode 혼합
```SQL
/*
ROUND : 일을 반올림 할때 정오를 넘으면 다음날 자정을 리턴하고, 넘지 않으면 그날 자정을 리턴한다. 
        월 : 15일 이상이면 다음달 1을 출력 / 넘지 않으면  현재 달 1을 리턴
        년도: 6월을 넘으면 다음해 1월1일 리턴 / 넘지 않으면 현재 1월 1일 리턴
        
TRUNC : 일을 절삭하면 그날 자정출력, 월을 절삭 그 달 1을출력, 년도를 절삭하면 금년 1월1일 리턴          

현재를 기점으로하고싶다 =TRUNC
년,월,일 의 반을 기점으로하고싶다 =ROUND
*/
SELECT   to_char(sysdate, 'YY/MM/DD HH24:MI:SS') normal, 
          to_char(trunc(sysdate), 'YY/MM/DD HH24:MI:SS') trunc, 
          to_char(round(sysdate), 'YY/MM/DD HH24:MI:SS') round 
          FROM  dual;

SELECT to_char(hiredate, 'YY/MM/DD HH24:MI:SS') hiredate, 
to_char(round(hiredate,'dd'), 'YY/MM/DD') round_dd, 
to_char(round(hiredate,'MM'), 'YY/MM/DD') round_mm, 
to_char(round(hiredate,'YY'), 'YY/MM/DD') round_yy
FROM  SCOTT.EMP     
WHERE  ENAME='SCOTT';

--RR/MM/DD(00-49:2000년대),DD/MON/RR(50-99:1900년대)

SELECT TO_CHAR(TO_DATE('98','RR'),'YYYY') test1, 
TO_CHAR(TO_DATE('05','RR'),'YYYY') test2, --RR이 2000년대니까 2000년대+05 +YYYY =2005
TO_CHAR(TO_DATE('98','YY'),'YYYY') test3, 
TO_CHAR(TO_DATE('05','YY'),'YYYY') test4 
FROM  dual;

SELECT   '000123',  to_number('000123')  FROM  dual; --숫자형은0이표시안됨

--Q12)  다음 문장의 실행 결과를 알아보자.
SELECT   to_timestamp_tz ('2004-8-20 1:30:00 -3:00', 'YYYY-MM-DD HH:MI:SS TZH:TZM')
FROM dual;-- CHAR, VARCHAR2 데이터 타입을 TIMESTAMP WITH TIME ZONE 데이터 타입으로 리턴  
--데이터 형식, 포맷을 타임존타입으로 만들어준다는것.아래 타임스탬프도같음

SELECT to_timestamp('2004-8-20 1:30:00', 'YYYY-MM-DD HH:MI:SS') 
FROM dual;-- CHAR, VARCHAR2 데이터 타입을 TIMESTAMP데이터 타입으로 리턴 

SELECT sysdate, sysdate+to_yminterval('01-03') "15Months later" 
FROM  dual;  ---- CHAR, VARCHAR2 데이터 타입을 INTERVAL YEAR TO MONTH 데이터 타입으로 리턴 

SELECT  sysdate, sysdate+to_dsinterval('003 17:00:00') as "3days 17hours later" 
FROM dual; ---- CHAR, VARCHAR2 데이터 타입을 INTERVAL DAY TO SECOND 데이터 타입으로 리턴 

--Q13)  다음 문장의 실행 결과를 알아보자.
 --EMP 테이블의 사원이름,  매니저 번호, 매니저번호가 null이면 ‘대표’ 로 표시하고, 매니저번호가 있으면 '프로'으로 표시. 
 SELECT ename, mgr, NVL2(mgr, mgr||'프로','대표') 
 FROM SCOTT.EMP;  --NULL일경우 FALSE / TRUE


--Q14) EMP 테이블의 사원이름 , 업무, 업무가 'CLERK‘ 인 경우 NULL로 나오도록 리턴.
SELECT  ename, job, NULLIF(job,'CLERK') AS result 
FROM  SCOTT.EMP; --NULLIF(컬럼,조건)-> 조건에 맞는 컬럼안의 데이터를 NULL로출력


--Q15)EMP테이블에서 이름, 보너스,연봉, 보너스가 null 아닌 경우 COMM를, COMM null인 경우엔 연봉을,
--모두 null인 경우엔 50으로 리턴.
SELECT ename, comm,sal, COALESCE(comm,sal,50) result --NLV2를 편하게 쓰기위한 함수 NLV2는 조건이 두가지밖에안되니까
FROM SCOTT.EMP;                                     --COALESCE(TRUE,FALSE,ELSE)값


--Q16) decode함수를 이용하여 급여가 1000보다 작으면 ‘A’, 1000이상 2500미만이면 ‘B’, 2500이상이면 ‘C’로 표시하라.
SELECT  ename, sal, DECODE(SIGN(sal-1000),-1,'A', DECODE(SIGN(sal-2500),-1,'B','C')) grade 
FROM  SCOTT.EMP;

--DECORDE==IF ELSE와 똑같음

--Q17)case 함수를 이용하여 급여가 1000보다 작으면 ‘A’, 1000이상 2500미만이면 ‘B’, 2500이상이면 ‘C’로 표시하라. 
SELECT ename,sal, 
        CASE WHEN sal < 1000 THEN 'A' 
             WHEN sal>=1000 AND sal<2500 THEN 'B' 
             ELSE 'C' END  AS grade 
FROM SCOTT.EMP ORDER BY grade;

★CASE WHEN 조건1 THEN 결과1 WHEN 조건2 THEN 결과2..ELSE 결과N END  CASE함수의 기본.

```
</details>

<details>
<summary>CUBE,ROLLUP,Grouping Set</summary>

## [3] CUBE,ROLLUP,Grouping Set

```SQL
--Q18)ROLLUP,CUBE(그룹 특수함수이고 엑셀의 부분합 총합이랑똑같은기능) 
/*
사용의의: 그룹핑한 결과를 상호참조열에 따라 상위집계를 내는 작업

ROLLUP: 정규 그룹화 행, 하위총합 포함해서 결과를 리턴. 그룹모아서 하나, 그룹모아서 하나, 맨밑에 총계를낸다.

        -데이터 보고서 작성,집합에서 통계 및 요약정보를 추출하는데 사용
        -GROUP BY 절에 ()이용해서 지정된 열 목록을 따라 오른쪽에서 왼쪽 방향으로 하나씩 그룹을만든다.
        -그다음 그룹함수를 생성한 그룹에 적용한다.
        -총계를 산출하려면 N+1 개의 SELECT문을 UNION ALL로 지정한다.

CUBE:   ROLLUP결과를 교차 도표화 행을 포함 하는 결과 집합을 리턴
        --GROUP BY 확장기능이다.
        -집계함수를사용하게되면 결과집합에 추가 행이 만들어짐
        --GROUP BY절에 N개의 절이 있을경우 '상위집계조합'수는 2N승 개이다.

★중요 : ROLLUP은 하위 총합의 조합중에 일부를 합을 내지만,큐브는 다..
        모든 그룹의 합과 총계!

*/

--사원테이블에서 부서별 급여의 합 조회시 롤업을이용해 총 집계를 내보자

SELECT DEPTNO,COUNT(*),SUM(SAL) --부서번호별 총 몇명인데 그 총몇명의 봉급을 더한값이 한줄씩나오고
FROM SCOTT.EMP                  --저 위의 결과를 다 더해서 전체결과를 리턴해줌 =ROLLUP
GROUP BY ROLLUP(DEPTNO);        --내부 그룹정렬도 좀 해준다 . 정렬은 덤..?

--Q19)사원테이블에서 부서별,직업별 급여의 합 조회시 롤업집계를 내보자.

SELECT DEPTNO,JOB,COUNT(*),SUM(SAL)
FROM SCOTT.EMP
GROUP BY ROLLUP(DEPTNO,JOB);    --두개쓸땐 순서도 지켜줘야한다.두개면 조금 보고서다워짐
                            
                                
--3개

SELECT DEPTNO,JOB,MGR,SUM(SAL)
FROM SCOTT.EMP
GROUP BY ROLLUP(DEPTNO,JOB,MGR);  --세개짜리는 정렬이 뭔가 더 깨끗하게된다. 더 보고서스러워짐

--ROLLUP->CUBE

SELECT DEPTNO,COUNT(*),SUM(SAL)     --ROLLUP은 오름차순느낌이라면CUBE는 내림차순느낌
FROM SCOTT.EMP                  
GROUP BY CUBE(DEPTNO);       

SELECT DEPTNO,JOB,COUNT(*),SUM(SAL)     --이건두개짜리인데 롤업을 뒤집어놓은것같다.
FROM SCOTT.EMP                          --큐브는 위에 목록(합계)들을보여주고 내려온다.
GROUP BY CUBE(DEPTNO,JOB);    
                                
                                
SELECT DEPTNO,JOB,MGR,SUM(SAL)      --명령문은 2*2*2, 8개의 그룹화를계산함
FROM SCOTT.EMP                      
GROUP BY CUBE(DEPTNO,JOB,MGR);

--Q21)그룹핑함수는 롤업, 큐브와 함께사용한다
/*
  -하나의 열을인수로갖는다
  -인수는 그룹바이절에 컬럼과 같아야한다.=표현식중하나가 일치하여야한다
  -0또는 1을반환한다.
  -0 : 해당열(인수로갖는값)을 그대로 사용하여 집계값을 계산했거나 해당 열에 나오는 NULL값이 저장된것을 의미한다.
  -1:해당열을 사용하지 않고 집계값을 계산했거나 NULL값이 그룹화의 결과로 ROLLUP이나
    CUBE에 리턴값으로 구현된 것을 말한다.
  - 이 행이 큐브와 롤업으로 생성된건지, 또 이 NULL값이 원래 들어있던값인지
   '구분'하기위해 책갈피껴놓는거랑 비슷함.
★ GROUPING은 '셀렉트문' 뒤에 지정한다. 

*/

SELECT DEPTNO,JOB,SUM(SAL),GROUPING(DEPTNO),GROUPING(JOB)
FROM SCOTT.EMP
GROUP BY ROLLUP(DEPTNO,JOB);  --롤업이나 큐브로 도출된값 =1. 아닌값 =0


SELECT DEPTNO,JOB,SUM(SAL),GROUPING(DEPTNO),GROUPING(JOB)
FROM SCOTT.EMP
GROUP BY CUBE(DEPTNO,JOB);

--GROUPING SETS = 여러개의 그룹핑쿼리를 UNION ALL한것과 비슷함 단,셀렉절이아니라 그룹바이절 뒤에
--어떨때쓸까?(DEPTNO,JOB,MGR) (DEPTNO,MGR) , (JOB,MGR) ->한번에 쓰고싶을때

★ UNION을 이용해보자!
--UNIONALL을 이용해 합치는법. 컬럼 갯수와 데이터 타입이 일치해야 합칠수 있으므로 맞춰주기위해 NULL이들어감
--UNION : 각 쿼리의 결과 합을 반환하는 합집합 (중복제거)
--UNION ALL : 각 쿼리의 모든 결과를 포함한 합집합 (중복제거 안함)

SELECT DEPTNO,JOB,MGR,AVG(SAL)  
FROM SCOTT.EMP
GROUP BY DEPTNO,JOB,MGR
UNION ALL
SELECT DEPTNO,NULL,MGR,AVG(SAL) 
FROM SCOTT.EMP
GROUP BY DEPTNO,MGR
UNION ALL
SELECT NULL,JOB,MGR,AVG(SAL) 
FROM SCOTT.EMP
GROUP BY JOB,MGR;

--GROUPING SETS써보자

SELECT DEPTNO,JOB,MGR,AVG(SAL)
FROM SCOTT.EMP
GROUP BY GROUPING SETS(DEPTNO,JOB,MGR);
---↑↓두 코드 결과 다름.
--아래는 널값이 아래로감. 
SELECT DEPTNO,JOB,MGR,AVG(SAL)
FROM SCOTT.EMP
GROUP BY GROUPING SETS((DEPTNO,JOB,MGR),(DEPTNO,MGR) ,(JOB,MGR));

--Q22)롤업안에 그룹을 만들자!
SELECT DEPTNO,JOB,MGR,SUM(SAL)
FROM SCOTT.EMP
GROUP BY ROLLUP(DEPTNO,(JOB,MGR));

/*
    1)GROUP BY  GROUPING SETS(A,B,C)  =  GROUP BY  A  UNION ALL     
                                         GROUP BY  B  UNION ALL 
                                         GROUP BY  C  UNION ALL 
                                         
    2)GROUP BY  GROUPING SETS(A,B,(B,C))=  GROUP BY  A  UNION ALL   
                                           GROUP BY  B  UNION ALL 
                                           GROUP BY  B,C
                                           
    3)GROUP BY  GROUPING SETS((A,B,C))=  GROUP BY A,B,C 
    
    4)GROUP BY  GROUPING SETS(A,(B),()) =  GROUP BY A   UNION ALL   
                                           GROUP BY B   UNION ALL   
                                           GROUP BY ()
*/

+) 기타

/*
    GROUPING_ID
    ROLLUP 또는 CUBE 함수로 연산할 때 특정 열이 그룹화되었는지 출력
    그룹화 비트 벡터 값으로 나타남!

    LISTAGG([나열할 열], [구분자(,이면 데이터사이에 ,)])
    그룹에 속해 있는 데이터를 가로로 나열할 때 사용

    PIVOT, UNPIVOT
    테이블의 행을 열로(PIVOT), 열을 행으로(UNPIVOT) 변환
*/

```
</details>

<details>
<summary>분석함수</summary>

## [4]분석함수

```SQL
/* 집계함수:여러행 또는 테이블 전체 행으로부터 그룹별로 집계하여 결과를 반환한다
   분석함수:집계 결과를 각 행마다 보여준다 =그룹별 계산결과를 각 행마다보여줌
   차이점:그룹별 최대, 최소, 합계, 평균, 건수 등을 구할 때 사용되며, 그룹별 1개의 행을 반환 VS
          그룹마다가 아니라 결과Set의 각 행마다 집계결과를 반환

--Q24)max min count lag,lead,rank,ratio_to_report,row_number 등등
    argument(전달인자) : 0~3개 까지만 줄수있다.
  [형식] 테이블에서 몇줄에서 몇줄까지 그룹핑 해서 정렬한 다음 분석함수의 결과를 리턴하는 함수
        테이블->선택행 ->그룹핑->정렬 ->집계 리턴
    SELECT 
      분석함수(ARGS) OVER(총 3개/선택
        [partition by] 쿼리 결과를 그룹으로 묶는다.
        [order by]각 그룹의 정렬. 행의 검색순서 partition by 한 내용을 정렬함.기본두개/null+first|last  
                    ex)desc null first | asc null last =NULL값들을 처음으로/끝으로 어디로보낼건지
        [windowing절] rows | range [between n and m ] 몇행까지 가져올건지?
                          )
      
      FROM 테이블명;
*/

--사원번호 사원이름 부서번호 봉급 부서내에서 급여가 많은 사원부터 순위를내자

SELECT EMPNO,ENAME,DEPTNO, SAL,
      RANK()OVER(PARTITION BY DEPTNO ORDER BY SAL DESC) --이부분이 분석함수들어가는자리.
FROM SCOTT.EMP;           
--위와같이하면 부서번호별 급여의 순위가 나오게된다. (Partition by 부서번호, Order by 급여많은순의랭크)
--★OVER안의 파티션이 어떤걸로 그룹핑할건지, Order by가 정렬할건지를 정하는것!

--RNAK앞에 DENSE를쓰면 동일순위처리를 어떻게할건지 선택적으로 처리할수있음
--DENSE쓰면 6등이없어지고 5등이생김(위의결과기준임)
SELECT EMPNO,ENAME,DEPTNO, SAL,
      DENSE_RANK()OVER(PARTITION BY DEPTNO ORDER BY SAL DESC)
FROM SCOTT.EMP;

--Q25)CUME_DIST():누적된 분산정도를 출력 분산값출력
  --누적분산도 출력과정: 1.그룹핑 - > 2.정렬 -> 3.그룹별 상대적인 위치(계산해서출력한다)(누적된 분산정도)출력
  --그룹내 상대적위치: 구하고자하는 값보다 작거나 같은 값을 가진 ROW(행)수를 그룹의 전체 ROW수로나눈것.
  -- 상대적위치의값은 0~1 사이의 값만나온다.

--20번 사원의 이름,봉급, 누적분산을 출력해보자.
SELECT DEPTNO,ENAME,SAL,
        CUME_DIST()OVER(ORDER BY SAL) "누적 분산"
FROM SCOTT.EMP
WHERE DEPTNO=20;

--Q26)NTILE(N):버킷분할
--사원의 봉급을 기준으로 4등분을하자.

SELECT ENAME,SAL,NTILE(4)OVER(ORDER BY SAL) 
FROM SCOTT.EMP;

--Q27)사원이름, 부서번호, 봉급,전체봉급의 합계, 부서별 봉급합계를 출력해보자.
--별도의 Group by 절 없이 셀렉절에 집계함수 OVER()넣으면 알아서 계산해준다..!!
--아래코드는 전체봉급만 나옴.
SELECT ENAME,SAL,SUM(SAL) OVER() TOTAL
FROM SCOTT.EMP;

--전체봉급의 합계와 부서별봉급합계 출력이된다.
SELECT ENAME,SAL,
SUM(SAL) OVER() TOTAL,
SUM(SAL) OVER(PARTITION BY DEPTNO) DEPTNO
FROM SCOTT.EMP;

--Q28)사원이름,직업,봉급,직업별 봉급 평균, 직업중 최대급여출력

SELECT ENAME,JOB,SAL,
ROUND(AVG(SAL) OVER(PARTITION BY JOB),2) "직업별 봉급 평균",
MAX(SAL) OVER(PARTITION BY JOB)"직업별 최대급여"
FROM SCOTT.EMP;


--Q29)사원 이름,부서번호,봉급의 합계 3줄씩 더한 결과 및 누적합계를 출력하자

SELECT ENAME,DEPTNO,SAL,
SUM(SAL) OVER (ORDER BY SAL ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) "SUM1",
SUM(SAL) OVER (ORDER BY SAL ROWS UNBOUNDED PRECEDING )"SUM2"
FROM SCOTT.EMP;

--SUM1은 SAL을 두개씩더해서 SUM1의 행한개를 출력(BETWEEN 1 PRECEDING AND 1 FOLLWING)
--SUM2은 계속그냥 1+1+1+처럼 누적데이터임 SAL의1행+SAL+2행..-누적 이런식.
--          (UNBOUNDED PRECEING)

--Q30)RATIO_TO_REPORT를 이용해서 해당 구간을차지하는 비율을 리턴해보자.
--사원의 전체 월급을 5만원으로 증가했을때 기존비율을 적용했을 경우 각 사원은 얼마를받을까
SELECT ENAME,SAL,RATIO_TO_REPORT(SAL) OVER ()AS "비율출력",--OVER안에 구간넣는데일단안줌
       TRUNC(RATIO_TO_REPORT(SAL) OVER ()* 50000) "받게될 봉급"
FROM SCOTT.EMP;
--위는 5만원을주되 비율에따라주겠다는것
--스미스는 전체를1로봤을때 0.027을 차지하고있으니,0.027만큼받을수 있다.
--즉, 5만원을 인상할시 스미스는 5만원의 0.027만큼(비율)받는다.50000*0.0275


--Q31)LAG:이전값을 참조한다.
--상대적으로 상위에 위치한 로우(오름차순의 경우 기준 로우의 정렬 컬럼의 값보다 작은값을 갖는로우)
--내림차순의 경우 기준 로우의 정렬 컬럼 값보다 큰 값을 갖는 로우를 참조하기 위해 사용된다.
--LAG의 기본값은 1
SELECT ENAME,DEPTNO,SAL,LAG(SAL,1,0)OVER(ORDER BY SAL) AS NEXT_SAL,
      LAG(SAL,1,SAL) OVER(PARTITION BY DEPTNO ORDER BY SAL) AS NEXT_SAL03
FROM SCOTT.EMP;
--LAG SAL을(현재행)을 기준으로 ,1 =첫번째'이전'값을 출력,0=가져올값이없으면0을반환
--즉,NEXT_SAL의 기본은 행을기준으로 이전값을가져오는거고 
--NEXT_SAL03은 파티션 DEPTNO를줬으니 같은DEPTNO끼리의 이전값을참조한다.

SELECT ENAME,DEPTNO,SAL,
      LEAD(SAL,1,0)OVER(ORDER BY SAL) AS NEXT_SAL,
      LEAD(SAL,1,SAL) OVER(ORDER BY SAL) AS NEXT_SAL02
FROM SCOTT.EMP;

--LAG반대. 다음값을반환
```
</details>




