# TIL DAY26(2022-11-09)

# MongoDB2(PyMongo)

## Python에서 MongoDB를 사용해보자(pymongo)

python에서도 mongodb를 쉽게 사용할 수 있다.
어떻게 사용하는지 알아보자.

```python

python에서 mongodb를 불러와보자(기본)

from pymongo import MongoClient

#client=MongoClient('localhost',27017)
client = MongoClient('mongodb://localhost:27017') #이렇게도가능

#db=client.test
db=client['test'] #주석처리된애들도 모두 사용가능

#collention = db.score
collention=db['score']

documents=collention.find() #이게 커서로가져오기때문
#print(documents) #그냥 프린트로가져오면 커서객체만 반환

for documents in documents: #for문으로가져와야함!
    print(documents)

inventory = db.inventory.find() #monodb형태로 써도 동작하도록 pymongo가 되어있어서 쓰고싶은대로 선택해서쓰면됨!
for item in inventory: #다만 이것도 가져올땐 for
    print(item)

#client,db,collention부분은 설정부분이고
#documents부분은 mongodb의 문법을 따른다. .find(), .count_documnets 등등

↓find()를해볼것임

from pymongo import MongoClient
import pprint

#pprint 프리티프린트 출력을 좀 보기편하게해줌

client = MongoClient('localhost', 27017)
db=client['test'] #db=client.test도 가능 솔직히 이게편함
score =db.score

cursor=score.find()

for doc in cursor:
    pprint.pprint(doc)

print('---------')
pprint.pprint(score.find_one({'name':'이순신'})) #몽고디비는 한글도 가능하다!

print(f'documnet의 촛 갯수: {score.count_documents({})}') #이건 7개나옴 말그대로 score컬렉션안의 도큐먼트갯수가져옴
#count_documents
print("국어점수가 60점 이상인 학생들 출력")

ks=score.find({'kor':{'$gte':60}}) #앞에 db.score해도되고 안해도되고

for doc in ks:
    pprint.pprint(doc)

↓Insert도 가능

from pymongo import MongoClient


client=MongoClient('localhost',27017)
db=client.test
score=db.score

'''
추가문 1회성임.계속들어가면 곤란
#res01=score.insert_one({'name':'아이유','kor':100,'eng': 100 , 'math':100})
#print(res01.inserted_id) 아이디출력

'''
yoon={'name':'윤하','kor':100,'eng':100,'math':100}

res02=score.insert_many([ yoon,{'name':'뷔',"kor":100, 'eng': 100, 'math':100}])
#yoon이라는 변수를 만들어서 many안에 길게안쓰고 변수로 사용했고, 반면 뷔 데이터는 변수안쓰고 바로씀. 그리고 many이므로
#[] 배열로 넣어줌. 딕셔너리형태로 도큐먼트를 만들었다.
print(res02.inserted_ids)


↓update도 할수있다.

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db=client.test
score=db['score'] #=db.score

#유재석의 국어점수를 100으로 수정

res01=score.update_one(
    {'name':'유재석'},
    {'$set':{'kor':'100'}}) #그냥 cmd창에선 $eq 등 연산자에 ''안붙여도됐지만 파이몽고에선 붙여야함!유의!!

print(res01.matched_count) #찾은거
print(res01.modified_count) #바꾼거 같은거 두번실행하면 0나옴

res02=score.update_many(
    {"eng":{'$lt':80}},
    {'$set':{'eng':100}}

)
print(res02.matched_count)
print(res02.modified_count)

↓삭제가능! delete 

from pymongo import MongoClient


client = MongoClient('localhost',27017)
db=client.test
score=db.score

# cc=score.find()
# 확인용 조회문
# for doc in cc:
#     print(doc)

res01=score.delete_one({'name':'유재석'})
print(res01.deleted_count)

#국어 점수가 100, 수학점수도 100인 학생모두삭제
res02=score.delete_many({'$and':[{'kor':100},{'math':100}]})
print(res02.deleted_count)

#★drop도 가능한데 드롭은 컬렉션을 통째로날려버림


from pymongo import MongoClient


client=MongoClient('localhost',27017)
db=client.test
score=db.score

#aggregate(집계)를 해보자. 국어점수가 50점이상인애들의 국어점수 평균
aggr=score.aggregate([
    {'$match':{'kor':{'$gte':50}}},
    {'$group':{'_id':'kor','avg':{'$avg':'$kor'}}} #group할때 그룹할 id와 표시할것은 필수!
    ])

print(aggr)
print(list(aggr))


↓ aggregate(집계)도 해보자

from pymongo import MongoClient

client=MongoClient('localhost',27017)
db=client.test
score=db.score

#aggregate(집계)를 해보자. 국어점수가 50점이상인애들의 국어점수 평균
aggr=score.aggregate([
    {'$match':{'kor':{'$gte':50}}},
    {'$group':{'_id':'kor','avg':{'$avg':'$kor'}}} #group할때 그룹할 id와 표시할것은 필수!
    ])

print(aggr)
print(list(aggr))

↓ ★★스타벅스js(예전에작업해둔것)을 가지고 위치를 검색해보자/(저장파트)

from pymongo import MongoClient
import json
from pprint import  pprint

#예전에 작업한 스타벅스json파일을(매장위치파일임)이용해보자
#json파일을 일단 열고
with open('starbucks.json','r',encoding='utf8') as file:
    starbucks=file.readline() #.readline():파일의 첫번째줄을 읽어서 출력함. 여러줄을 출력하고싶으면 for문으로돌리면됨

#열어서 딕셔너리타입으로 가져올거임. ※json.loads(변수명)! 꼭 쓰기
starbucks_dict=json.loads(starbucks)
print(starbucks_dict)

#dict데이터를 몽고디비에 저장하자

client=MongoClient('localhost',27017)
db=client.test

#upsert(지정한내용이있으면 수정,없으면 만들어주는거)써도될거같고,insertmany써도될듯
#test.update({"이름":"정길동"}, {"$set":{"별명" :"의적"}},upsert =True, multi = True) 형태.
# res=db.starbucks.insert_many(starbucks_dict['list']) #스타벅스_딕트의 name이 list인친구의 '값'을 모두 추가.
#(json열어보면 list:[{'네임1':'값1'},{'네임2':'값2'}...] 로 이루어져있음
# print(res.inserted_ids) 하지만 생성문이라 한번만 실행할거니까 주석처리
for doc in db.starbucks.find():
    pprint(doc)


↓ ★★스타벅스js(예전에작업해둔것)을 가지고 위치를 검색해보자/(검색파트)

import json
from pymongo import MongoClient
from pprint import pprint

with open('starbucks.json','r',encoding='utf8') as file:
    json_data=file.readline()

dict_data=json.loads(json_data)
#pprint(dict_data)

#★geo스페셜쿼리 사용!
#기본형태 = 필드: [longitude, latitude ] / [x,y]도 가능 / 필드 :{필드1:x or lot, 필드2: y or lat}
geo_list=list()
for data in dict_data['list']:
    #dict이부분은 s_name(매장이름)을 넣음. s_name엔 data s_name을, 도로명엔 도로명을
    geo_dict = dict()
    geo_dict['s_name']=data['s_name']
    geo_dict['doro_address']=data['doro_address']
    #여기부턴 lot,lat나누고 location:type,point,coordinates :[lot,lat]형태로 만들었다
    coordinates=[float(data['lot']),float(data['lat'])] #각 lot,lat의 데이터를 가져오고 데이터 타입선언
    geo_dict['location']={'type':'Point','coordinates':coordinates} #그러면 coordinates는 각각 lat,lot의 데이터를 가지고있겟지(127.11,36.11~)

    geo_list.append(geo_dict) #그리고 list에 geo_dict에 어팬드(추가)했다
print(geo_list)

#그리고 저 위에서만든 geo_list를 mongodb에 저장할것임!!
client= MongoClient('localhost',27017)
db=client.test
starbucks=db.starbucks
#res=starbucks.insert_many(geo_list)
# pprint(res.inserted_ids)

#제대로 생성되었는지 확인
all=starbucks.find()
for doc in all:
    pprint(doc)


↓ 스타벅스js를 가지고 특정거리안에 있는 매장을 검색해보자

실행환경:mongo. (pyhon x)

#일단 index를생성해줘야한다. 기본형태는 아래와 같음.
db.collection.createIndex( { <location field> : "2dsphere" } )

#스타벅스 index생성(미리 location으로 이름을 지정해놨기때문에, 그대로사용)
db.starbucks.createIndex( { 'location' : "2dsphere" } )

#선릉역위치를 중심으로 넣었기때문에, 선릉역을 기준으로 가까운순으로 매장을찾아줌.
db.starbucks.find(
{location: {
$near:{
$geometry:{
type:'Point', coordinates: [127.04891744662912, 37.50466836387415]#선릉역 위치
}
}
}
}
)

#MaxDistance를 사용해서 원하는 범위내에서 매장을 찾자
# $maxDistance : 단위는 m(미터), 최대거리. 위의경우 최대거리 500미터 안.
#최대거리500미터 안에서 매장을찾음
db.starbucks.find(
{location: {
$near:{
$geometry:{
type:'Point', coordinates: [127.04891744662912, 37.50466836387415]
},
$maxDistance:500
}
}
}
)

(lot,lat 순서)
# 강남역 : 127.02758390096662, 37.498208718241884
# 신반포역 : 126.9960576848932, 37.50361063865503
# 잠원역 : 127.01155735420919, 37.51313018512163

#원을그려서 원반경내에서 매장찾기 
db.starbucks.find({
	location:{
		$geoWithin:{
			$centerSphere:[
				[127.04891744662912, 37.50466836387415],
				0.5/3963.2
			]
		}
	}
})

위와같이 mongo가 위치찾는건 잘되어있어서 위치찾을땐 편하다.

```

# Oracle

실행계정:scott계정(관리자x)

```sql

view를하나 새로 생성할건데, emp테이블 카피해오자.

create or replace view v_emp as select * from emp;

select * from v_emp; #뷰확인. 


시퀀스도 생성해보자(은행 번호표기계같은 원리)

create sequence sequence_test;

확인
select sequence_test.nextval, sequence_test.currval from dual;
각각 1 1 나옴

currval은 nextval을 한 이후에 사용.

기본형태: 시퀀스명.nextval(1씩증가), 시퀀스명.currval


기존에있는 테이블을 복제하려면?

as select * from 테이블

create table 생성할테이블명 as select * from 기존테이블명
( 단 ,이건 *니까 다복사해옴,필요한것만 선택해서 가져오면된다.)

컬럼을 복사(컬럼+데이터)

create table 생셩할 테이블명 as select 컬럼1,컬럼2,컬럼3...from 기존테이블명

※'컬럼구조'만 복사! 데이터 복사 X. 

create table 생성할 테이블명 as select * from emp where 1=2;

★notnull= 설정레벨:컬럼

->무슨말이냐면, 테이블을 생성할때 컬럼의 옵션으로 not null을 지정할수는 있찌만,
 **제약조건**으로 컬럼에 not null을 설정할수없다는것

★not null만!!!!!! 컬럼 제약조건으로 걸수없다. 다른거는 다 가능. 아래처럼 프라이머리키나 유니크 등등 가능

constraint 제약조건 제약조건(컬럼) == constraint tp02_id_pk primary key(id) 


ex)
SQL> create table table_notnull01(
  2  Id char(3) not null,
  3  Name varchar2(20)
  4  );

위와같이 생성을하였다면,

insert into table_notnull01 values(null,'test');

이러면 ORA-01400: NULL을 ("SCOTT"."TABLE_NOTNULL01"."ID") 안에 삽입할 수 없습니다.
라는 오류가발생하고,

SQL> create table talbe_notnull02(
  2  Id char(3),
  3  Nmae varchar2(20),
  4  constraint tn02_id_nn not null(id)
  5  );

이렇게한다면, 부적합한 식별자라고 오류난다.

컬럼에 not null을 설정하고싶다면, 테이블 생성단계에서

옵션으로만줄수있다는점.( create table test_table2(Id char(3) not null)) <<이렇게

tn02_id_nn가 무엇인가?
제약조건 이름을 내가준것. 제약조건이름을 주지않으면,자동으로 만들어준다.
제약조건이름을 설정해주면 좋은건 나중에 찾기가 편하다는 장점이있다.


※예외

SQL> create table table_unique03(
  2  Id char(3),
  3  Name varchar2(20),
  4  constraint tu03_id_unq unique(id,name));

위와같이 제약조건을걸면 id와 name '둘 다 중복되어야' 위배되었다고 오류난다.


만약 name과 id가 각각 중복되지않게 하고싶으면 ↓

create table table_unique04(
Id char(3),
Name varchar2(20),
constraint tu04_id_unq unique(id),
constraint tu04_name_unq unique(name)
);



SQL> create table table_pk02(
  2  Id char(3),
  3  Name varchar2(20),
  4  constraint tp02_id_pk primary key(id)
  5  );

디스크립션(desc)로 확인하면 중간에 컬럼 중간에 null?이라고뜨는데 널이니? 라는의미이다.


슈퍼키에대하여

create table table_pk03(
Id char(3),
Name varchar2(20),
constraint tp03_id_name_pk primary key(id,name) ); ->슈퍼키/복합키 이다 id,name을 묶어서 프라이머리키로 쓴다. 즉 저 두개가 하나의 프라이머리키가 되는것이므로 둘중하나가 null이거나/둘 다 겹치거나하면 안된다.

insert into table_pk03 values('1','oracle');
insert into table_pk03 values('2','oracle');
insert into table_pk03 values(null,'oracle'); ->이녀석은 오류

외부키(fk)

References:참조하겠다.
다른테이블의 기본키를 참조하는경우=forginket(외부키=fk)


create table table_fk01(
Id char(3),
Name varchar(20),
pkid char(3) references table_pk01(id)); ->pkid컬럼은 table_pk01의 id를 참조한다는의미이지만..

insert into table_fk01 values('1','oracle','1');
insert into table_fk01 values('2','mongo','2'); 

table_pk01안에 id값이 2가없기때문에 오류가난다. (1만있음)
부모키가 없다고 나옴

참조하는쪽:자식테이블
참조를 제공하는쪽:부모테이블
당연히 삭제는 '자식테이블'부터해야한다.


check제약조건

create table table_check01(
Id char(3),
Name varchar(20),
Marriage char(1) check(marriage in ('y','n')) );

insert into table_check01 values('1','oracle','y');
insert into table_check01 values('2','mongo','n');
insert into table_check01 values('3','java','s');

check제약조건은 입력되는값을 검사하는 역할을한다. check(컬럼명 in (받을값));
★키워드는 대소문자 크게 상관안하지만, 들어가는 실제값은 대소문자를 구분한다

delete문

delete from 테이블명 where 조건
(drop과 다르게,롤백가능)

```

