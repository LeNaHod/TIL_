# TIL DAY 25(2022-11-08)

## Tensorflow Ver 2
- 실행환경: conda python 3.9
- Tensorflow 2.10.0

ver 1과 다르게 실행할때 session을 사용하지않고 굉장히 간편해짐
특히, loss를 작성하는부분이 많이 간단해졌다. 
눈에보이는 특징은 아래와같음.

(ver1)
loss =tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits,labels=y))   

↓↓↓↓↓↓↓↓↓↓↓↓↓↓

(ver2)
model.compile(loss='categorical_crossentropy',optimizer=adam_v2.Adam(learning_rate=0.1))   

모델.컴파일로 쉽게 loss를 지정할 수 있다. optimizer에서 가장 많이쓰는건 Adam.
(from tensorflow.python.keras.optimizers import adam_v2) 필수.

--------
(ver1)
x=tf.placeholder(shape=[None,4],dtype=tf.float32)
y=tf.placeholder(shape=[None,3],dtype=tf.float32)

w=tf.Variable(tf.random_normal([4,3])) 
b=tf.Variable(tf.random_normal([3]))

↓↓↓↓↓↓↓↓↓↓↓↓↓↓

(ver2)
model.add(Dense(units=10,input_dim=4))
model.add(Dense(units=3, input_dim=20, activation='softmax'))
(from tensorflow.python.keras.layers import Dense)

activation:model종류같은것!

verbose:1 or 0  0은 학습과정 생략, 1은 학습과정을 보여줌. 이 기능 또한 ver1에서는 학습과정을 보기위해 코딩을해줘야했는데 간략해졌다.


```python

#tensorflow V2 를사용해보자
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.optimizers import adam_v2
#1
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,6,8,10,12,14,16,18,20]

#2
model=Sequential()

#3
model.add(Dense(units=10, input_dim=1)) #들어오는거 하나,히든레이어는10개
model.add(Dense(units=40, input_dim=10))
model.add(Dense(units=20, input_dim=40))
model.add(Dense(units=1, input_dim=20))#나가는거하나


model.compile(loss='mse',optimizer=adam_v2.Adam(learning_rate=0.1))#=optimizer='adam_v2'

model.fit(x,y, epochs=100,verbose=1) #v1과 다르게 session으로 실행하지않고 sklen처럼 fit을사용. 100번 학습하겟다
#verbose:1이면 출력할때 훈련과정을 출력함 ===1/100 ==2/100..등, 0이면 훈련과정을 출력하지않음

#실행
test_x=[1,3,5,7,9]
predict=model.predict(test_x)
print(predict)


from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.optimizers import adam_v2


#1.
#3번의 쪽지시험 결과를 가지고 실제 시험 점수를 예측하고 싶다.

data_x =[[73,80,75],[93,88,93],[89,91,90],[96,89,100],[73,66,70]]

data_y=[[80],[91],[88],[94],[61]] #x값에대한 라벨개념 [73,80,75]=[80]..이런식으로 매핑


model=Sequential()

model.add(Dense(units=10,input_dim=3))
model.add(Dense(units=20)) #inputdim생략가능 어차피 위의 코드에서 바로들어갈거라, dl부분
model.add(Dense(10)) #dl부분
model.add(Dense(units=1))


model.compile(loss='mse', optimizer=adam_v2.Adam(learning_rate=0.1)) #tf.reduce_mean(tf.sq~)=loss=mse

model.fit(data_x,data_y,epochs=100,verbose=1)

test_x=[[100,80,78]] #x의 데이터의 차원에 맞춰서 test데이터도 넣어줘야함.! 여긴 [][]두개
print(model.predict(test_x))


하지만 ver2에서도 sidmoid와 softmax는 중요

```

# MongoDB

MongoDB는?
가장 큰 특징으로는 세가지가있다.

1. Nosql. 스키마가 제약을 받지않는다=고정되지않은 스키마 이므로 빠르다.
2. 데이터간의 관계가 X(MongoDB는 db->collection->document 구조를 가지고있다.)
3. 분산형구조이므로 큰데이터를 저장하고 처리하는데 용이하다. (클러스터 데이터 상호 복제가능)


|제목|내용|설명
|:---:|:---:|:---:|
|collection|Table이라고 보면된다.|show collections으로 colloection들을 확인
|documnet|필드,값의 개념.데이터를 BSON으로저장 | BSON:바이너리 제이슨의 약자.</br>JSON형태의 문서.바이너리로 인코딩되어서 serialization되어있는것</br>JSON형태의 데이터 저장/전송 용도로이용하고 바이너리데이터를 추가할수있다.|


MongoDB는 사용도 편리하고 빨라서 자주이용한다.

db.콜렉션명(테이블명).명령어 구조로 되어있다.

## INSERT문

```
아래 insert문을보면 db.tset<콜렉션명.insertOne<추가명령문 이다. find도마찬가지

db.test.insertOne({"name":"test","age":100,"class":"multi"}); 

db.test.insertOne({"name":"test","age":100,"class":"multi"}); 
->이러면 test테이블에 추가는 되지만, 오브젝트아이디라고해서 자동으로 특정값을 만들어 프라이머리키를 생성한다.


db.test.find(); 
->test내용물 출력

show dbs
->db의 저장현황?이라고해야하나 저장현황이나옴
admin 0.000GB
config 0.000GB
local 0.000GB
test 0.000GB
...이런식

show collections
->collections 리스트를보여줌


db.mulit.insert({"name":"hong-gd","class":"multi","midterm":{"kor":100,"eng":60,"math":80}});
->위 처럼 {}안에 {}를 쓸수있다

또, 변수를선언해서 insertone(변수명) 이런식으로 사용 가능

db.multi.insertMany([{"name":"you-js","kor":100,"eng":90,"math":85},{"name":"shin-dy","kor":90,"eng":85,"math":100}]);
->두개이므로 insertedIds. 복수형으로 프라이머리키가 두개 만들어진다.
[]로 묶고 {}로 나눔!


EX1)
db.mulit.insertOne({"name":"kang-hd","kor":80,"eng":90,"math":95});
== insert into multi(name,kor,eng,math)values('kang-hd',80,90,95);

```
중요:**insertedId를 추가하지않으면 자동으로 프라이머리키가 생성된다는것!**

## 조건을 걸어서 조회해보자

EQ,AND,OR등 여러조건으로 필터링해서 find로 조회 할 수있다.
다만 앞에 $가붙고 크게{}가붙고 안에 []붙는경우도있다.
find에서 사용할때 위치가 제각각이므로 공식문서를 참조하는게 좋다.

```
(find({},{$eq~})이렇게 들어갈수도있고, find({$and:[{~}]})이렇게 들어갈수도 있다는것)

db.inventory.find( { $or: [ { status: "A" }, { qty: { $lt: 30 } } ] } )
==SELECT * FROM inventory WHERE status = "A" OR qty < 30 
 
db.multi.find({},{name:1}); find를 이렇게도 쓸 수 있다.0은 표시안함 1는 표시함
만약 name이 나오는게싫다면, name:0,id:1이런식으로 쓸 수있다.

조건을 걸고싶다면, 첫번째 {}안에 조건을 넣는다 
db.multi.find({"class":"multi"}); 이런식으로. == SELECT * FROM mulit where class=multi


db.multi.find({"midterm":{$exists:true}});

$exists = t/f 만존재. 일치하는 값을 매칭해서 출력
$gt: >와 같음 특정값보다 초과하는 값만 출력
$lte: <= 이하. ~e는 이상이하임

SELECT NAME,KOR,ENG FROM multi WHERE KOR < 100 AND MATH >=70;
==db.multi.find({},{"_id":0,"name":1,"kor":1."eng":1},{$and:[{"kor":{$lt:100},"math":{$gte:70}}]});

and가 여기선 $and:[{and로걸어줄조건}] 이다.

★ db.inventory.find( { $or: [ { "qty": 25 }, { "qty": 45 } ] } ); 이렇게쓰는게 위보다 보기 편함.

예제3
midterm field안에 있는 kor에 조건을 걸고싶다.

db.mulit.find({"midterm.kor":{$gte:50}}); (midterm.kor=미드텀필드안의 kor에)

db.multi.find({"name":/k/}); ==like임. name like %k% 와 동일하다. name이 k를포함하는것을 출력

db.multi.find({"name":{$regex:'k'}}); 으 로도 쓸 수있다.

$regex : 값이 지정된 정규식과 일치하는것을 찾아준다.

★$regex를 이용해서 ~로시작하는, ~로끝나는 조건을 작성하고싶다면, 아래와 같이 작성

1. db.inventory.find({"item":{$regex:/r$/}}); =r로끝나는

2. db.inventory.find({"item":{$regex:/^p/}}); =r로시작하는

3. db.inventory.find({"item":{$regex:/r/}}); or $regex:'r' = r을 포함하는

정렬해보자!
db.multi.find().sort({"name":1 or -1 }); 1:오름 -1:내림 

단, 정렬의 유의사항:오름이면 해당하는 필드가 없는애들이 나중에. -1면 없는애들이 먼저

$eq는 해당값과 일치하는 값을가진필드를 찾음! == {필드:값} 과 같긴함..

db.inventory.find({ "item": { $eq: "notebook" } }, {"itme":1,"status":1})

$ne:지정한 한개만 제외 / $nin:여러개 제외! $nin[{}]
db.inventory.find( { $and: [ { "size.w": {$ne:11} }, { "size.w": {$ne:21} } ] } );


정렬(sort)와 find를 같이 사용할수있다.

db.multi.find().sort({"kor":-1}).limit(3); 
->sort+ limit을 같이사용할수있다.(국어점수 상위3명 출력)

db.mulit.find().skip(1); 
->skip은 위에서부터 입력한 값갯수 만큼 스킵하고(빼고)보여줌

```
비교
|제목|내용|설명
|:---:|:---:|:---:|
|$gt| 초과값을찾음 > 이다.|{필드:{$gt:값}}|
|$lt|미만. < |{ 필드: { $lt: 값 } }|
|$gte|이상! >= |{ 필드: { $gte: 값 } }|
|$lte|이하. <=|{ 필드: { $lte: 값 } } |
|$eq|해당값과 일치하는값을 찾는다.| { 필드: { $eq: 값 } }|
|$ne|해당값과 일치하지 '않는 값' 을가진 필드를 찾는다.단수|{ 필드: { $ne: 값 } } |
|$in|in안에 들어있는 값들 중 하나인필드를 찾음|{ 필드: { $in: [ 값1, 값2..]}|
|$nin|필드값이 해당값들이 아닌 필드를 찾음.복수|{ 필드: { $nin: [ 값1, 값2,..] }|

논리

|제목|내용|설명
|:---:|:---:|:---:|
|$or|말그대로 or. ~이거나|{ $or: [{ 조건1 }, { 조건2 }, ...] }|
|$and|말그대로 and. ~이면서,이고.사용은 or와같지만,</br>and와 or섞어쓸때 유용 |{ $and: [{ 조건1 }, { 조건2 }, ...] }|
|$nor|'여러개의조건'을 '모두만족x'도큐먼트를찾음|{ $nor: [{ 조건1 }, {</br> 조건2 }, ...] }|
|$not| $nor의 단수버전.조건을 만족하지않는 필드를 찾음|{ $not: { 조건 } }|




## Update를해보자

update할때 $set은 세트라고 생각하자
{$set:{필드1:값1,필드2:값2}} <업데이트부분에 들어감. 업데이트를'할' 내용에 set을붙임.

**replaceOne과 update는 다름**

각 updateOne/ updateMany 가 있고, (필터,업데이트,옵션)으로 구성되어있다
```

예제4

sql:update multi set name='홍길동' where name= 'hong-gd';
mongo: db.multi.updateOne({"name":"hong-gd"},{$set:{"name":"홍길동"}}) 

예제5
midterm필드가 존재하는 학생들의! 클래스를 "graduated"로 바꾸자.
db.multi.updateMany({"midterm",{$exists:true}},{$set:{"class":"graduated"}})


replaceOne:document를 변경한다.== id(프라이머리키)는 그대로지만, 그 뒤에 문서의내용 뭐 name이나 컬럼과 값에 속하는것들이 '입력한대로'통째로 바뀌어버림! 그리고 리플레이스원은 변경내용에 $set을안붙여도된다는 특징이있다. 중요한건 id는 바뀌지않는다.

예제 6
db.multi.replaceOne({"final":{$exists:true}},{"name":"lee-ss","kor":67,"eng":90,"math":100});

function으로 만들어서 사용도 가능하다.

function updateKor(){
	var tmp=db.multi.updateMany({"kor":{$lte:70}},{$set:{"kor":0}});
	return tmp;
}
 updateKor();
->업데이트가 실행된다. { "acknowledged" : true, "matchedCount" : 0, "modifiedCount" : 0 }
			     실행결과            찾은것                 바꾼것


리플레이스는 오라클로보면 
컬럼을 변경(데이터 타입,길이) 할 경우 ALTER TABLE를 사용하며,  컬럼의 데이터 타입, 길이를 수정할 때는 MODIFY, 컬럼명을 수정할 때는 RENAME COLUMN을 사용하면 된다.이므로 여러개써야함

```

## 삭제(delete)문

delete from multi where name ='홍길동';
== db.multi.deleteOne({"name":"홍길동"});

deleteMany는 무조건 필터(첫번째자리)를 넣어줘야한다.아니면 오류남!


# 배열 추가,삭제,필드이름 바꾸기
```
필드이름 바꾸기=$rename (name->이름)이렇게 바꿀수있다.


배열에 '값' 추가하기

db.myfriends.updateOne({"name":"아이언맨"},{$push:{"buddy":{$each:['캡틴아메리카','블랙위도우']}}});

기본문법:{ $push: { <field1>: <value1>, ... } }
지정된 값을 '배열'에 추가한다.

push+each를 같이사용하면, 아래과 같은형태가되고 '한개의 필드에 여러값'을 넣을수있음.
{ $push: { <field>: { $each: [ <value1>, <value2> ... ] } } }


$addToSet은  '값이 존재하지 않는'경우 추가하려고사용.

{$addToSet: { <field>: { $each: [ <value1>, <value2> ... ] } } } 

배열에서 '특정값' 빼기

db.myfriends.updateOne({"name":"슈퍼맨"},{$pop:{"buddy":1}}); (pop:1,-1로 구성되어있음)

기본문법:{$pop: { <field>: <-1 | 1> }}

-1:배열의 첫번째 요소. 1은 마지막요소를 제거함. 위는 1이므로 buddy의 마지막요소가제거됨
```

## ※pipline이란?
pipline(파이프라인):★이전 단계의 결과를 다음 단계의 입력으로 사용★
정말 중요!!

---------------------
## aggreagate(집계)와 Mapreduce

aggregate : 쉽게말하면 집계해주는 친구인데,스테이지를 거쳐 하나씩 집계가된다고 생각하면됨.

**스테이지의 순서는 굉장히중요함.**

sql과 대응해보자면 아래 표와 같다.

|제목|내용|
|:---:|:---:|
|where|= $match|
|having|= $group|
|select|= $project|
|order by|= $sort|
|limit|= $limit|
|sum,count|= $sum|

Mapreduce : aggregation freamowork가 처리못하는 '복잡한집계에'사용.

query->map->reduce->out 순인데 각각 살펴보면

|제목|내용|
|:---:|:---:|
|query|입력될 도큐먼트이다.|
|map|데이터를 매핑,그룹핑해줌|
|reduce|집계 연산을 실행한다.|
|out|collection 이나 도큐먼트 출력|


$project:셀렉트문이랑 똑같음. 조회/출력문 이라고 생각하면됨.

db.score.aggregate({$project:{"_id":0,"name":1,"kor":1,"eng":1,"math":1}});

->이러면 셀렉트된 결과만 aggreate된다. 서브쿼리쓸때 주쿼리에 안쓴건 사용못하는 원리와같음

```

db.score.aggregate({$match:{"kor":{$gte:80}}});

필드앞에 $붙이면 그룹핑하는거랑 같아짐. 아래는 kor별 평균
db.score.aggregate({$group:{"_id":"$test","average":{$avg:"$kor"}}});


test가 final인 도큐먼트들의 이름과 수학과 영어만 출력 == 스테이지가두개

db.score.aggregate([
	{$match:{"test":"final"}},
	{$project:{"_id":0,"name":1,"math":1,"eng":1}}]); ==출력이니까 project(조회문)

※대괄호 생략가능


test가 midterm인 documnet들의 영어 평균을 구하자

db.score.aggregate(
	{$match:{"test":"midterm"}},
	{$project:{"eng":1}},  <<굳이안써도 되긴함. 편의상함
	{$group:{"_id":"test","average":{$avg:"$eng"}}}
);

잘못된풀이 ↓ 순서의 중요성.
db.score.aggregate({$project:{"eng":1}},{$match:{"test":"midterm"}});



함수를 만들어서 결과값을 myreduce에 넣어보자!

함수를 두개만듦. 

function myMap() {
	emit(this.score, {name: this.name, kor: this.kor, eng: this.eng, test: this.test});
} 맵리듀스에 사용되는 emit. 무엇을가져올지 명시.

function myReduce(key, values) {
	var result = {name: new Array(), kor: new Array(), eng: new Array(), total: new Array()};
	values.forEach(function(val){ 파이널 테스트의 점수만 가져올거임
		if (val.test == "final") {
			result.total += val.kor + val.eng + " ";
			result.name += val.name + " ";
			result.kor += val.kor + " ";
			result.eng += val.eng + " ";
		} 	
	});
	return result;
}

db.score.mapReduce(myMap, myReduce, {out: {replace: "myRes"}}); myRes 컬렉션을만들거임. 만약잇으면 myRes로 리플레이스 해줘 라는의미.
db.myRes.find();

```





