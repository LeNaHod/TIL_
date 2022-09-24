# TIL DAY 02(22_09_23)


# [1] .Gitignore 란 무엇인가?

 ![이미지](https://i0.wp.com/www.alphr.com/wp-content/uploads/2020/08/Whats-a-GITIGNORE-File-How-To-Use-One.jpg?fit=577%2C320&ssl=1)

  
  
- .gitignore : 제외하고싶은 폴더/파일을 지정하는것.사이트가 따로있어 만들기가 편하다.
-   Ex)os파일,IDE, 개발언어,패스워드 등등
-   반드시 이름을 .gitignore로 생성해야하고, git 폴더와 위치가 같아야함 

## ignore 를 포함한 파일 생성 추천순서
  > init->제외하고싶은파일을담을 GITIGNORE 생성(touch .GITIGNORE) -> touch를 통해 파일생성 ->  ADD/OR      TOUCH 등등 작업

## gitignore를 조금 더 알아보자
     패턴규칙
        - 디렉터리는 끝에 /가 붙는다./로시작하면 하위 디렉터리에 재귀적으로 적용되지않는다
        - '!'로 시작하는 파일은 무시하지않음
        -  #이나 아무것도 없는 라인은 무시함
        -  정규패턴(*,[],?,[n-n],**)를 사용한다. (**는 디렉터리 내부 디렉터리까지 지정하는것)
- 
------------------------------------------------------------------------------------------------
# [2] Clone과 pull을 알아보자

- Clone
    > 클론(복제).init과 리모트가 필요없다. 굉장히 편리한 기능
      원격 저장소의 커밋 내역을 가져와 로컬 저장소를 생성한다.
      init이 되어있지않은곳에서 하는게 좋다 (바탕화면->git bash이용)
      fork로 가져와서 Clon으로 로컬에 받아올수도있다.

- Pull
    > 클론과 친구. 원본과 싱크를 맞춰준다.Git pull [주소이름] [브랜치이름]
      업데이트 버전을 매번 다운로드받지않아도 위의 명령어로 다른곳에서 업데이트된 내용을 받아올수있다.
      Clone과 Pull은 한 세트.

### 주의사항
- **작업할 때 init되어있는 곳에서 하면 안좋으니까 init이 되어있지 않은곳**
- **다만 pull을하고 수정을하면 꼭 push로 올려줘야함!**

### 작업순서
클론만들고 -> 파일받고-> 수정하고-> push로 올리고 -> pull로 업데이트된 내용을 받아오고 ->push로 올리고   ->pull하고 (remote/local 어디서든 작업가능.)

**EX) remote를 이용해서 작업할경우**  
1. 아래 명령어를 통해 클론받는다.
```bash
git clone URL
```
2. 로컬에서 COMMIT을 하나 더 쌓은 다음에 remote로 psuh한다.
3. 리모트에서 commit을 하나 더 쌓은 다음, local1에서 pull한다.
4. commit을 쌓습니다.
    -리모트에서 commit을 쌓는다.
    -로컬에서 commi을 쌓는다.
5. push를 하려고 하엿더니 rejected가  뜨면?
6. pull을 먼저 함
7. merge commit을 남김.

 
## [2-1] 오류상황/원격 저장소를 공유해보자
 Clone으로 공유된 저장소의 파일을 받아봤으니 반대로 직접 원격 저장소를 공유해보자.

   1. 공유하고싶은 원격저장소를 생성하고, 로컬 저장소와 연결함(**git remote add origin URL**)
   2. 저장소를 생성했으면, 원하는 파일을 생성하거나 저장소에 push를 통해 올린다.
   3. collaborator으로 유저를 추가하면, 유저에게 초대장이 가고 수락해야 권한을 부여받는다.
   4. 이후 권한을 부여받은 유저들은 Clone을 받고 이후 pull,add,commit,push를 통해 협업을할수있다.
[끝말잇기 게임 참여자료](https://github.com/cyctal/word-relay.git) 

★ **git non-fast-forward 오류 해결하기**

    Clone으로 받아오지않은 로컬의 md파일을(Branch는 master1개) 원격에서(Git Hub)에서 수정했을때,
    로컬에있는 파일을 pull로 업데이트해줘야한다. Clone으로 받아왔을땐 git pull만 쓰면 됐었는데
    그건 Clone의경우고 이 상황이랑은 다르므로, pull을 하지않고 push를 시도하면 
    ★non-fast-forward★ 오류가 발생하게된다.
        해결방법: git pull <reomote> <branch>인데, git pull origin(remote했을때 쓴 이름) master하면된다. 


# [3]Branch(분기)

![브랜치이미지](https://git-scm.com/book/en/v2/images/advance-master.png)

(Branch의 구조를 이미지로 나타내보았다.)

### Branch, 무엇이고 왜쓰는가?

- 완전히 독립된공간, 평행세계 같은 걸 만들어준다. 마스터에서 파생된 공간인 **Branch** 에서 작업을한다.
- 작업을할때 분업으로 하는 경우가 더 많기때문에 각 목적에 맞는 Branch를 생성해 사용자들에게 할당해준다.
    또한,마스터(=서비스의 공간을 의미) 에서 작업하다가 오류나면 서비스가 아예 멈춰버리기 때문에 더더욱 
   Branch에서 작업하고 merge(병합)작업을 해준다.
------------------------------
### Branch 사용 예제
- 다음은 브랜치의 기본 명령어에 대해 표를만들어봤다.
    표의 내용중 switch 명령어가있는데, 사용전,**반드시 COMMIT** 을 하고 이동해야한다!

**브랜치 기본 명령어**

|제목|내용|설명|
|:---|:---:|:---:|
|git Branch [Branch명]|새로운 Branch를 생성한다|=git checkout -b 와비슷|
|git Branch|Branch조회|만들어진 Branch와 헤더를 확인할수있다.|
|git Branch -r|원격 저장소의 Branch 목록 확인|다르지만 git log --all로도 조회할수있다. |
|git Branch -[Branch명][커밋ID]|특정 커밋기준으로 Branch생성|-|
|git Branch **-D** [Branch명]|특정 Branch삭제|강제삭제,**병합되지않은** Branch도삭제된다.|
|git Branch **-d** [Branch명]|특정 Branch삭제|**병합된**Branch만 삭제.|
|git switch [다른 Branch명]|다른 Branch로 이동 |-|
|git switch -c [Branch명]|생성과 동시에 이동한다|-|
|git switch -c [Branch명][커밋ID]|특정 커밋 기준으로 생성과 동시에 이동|-|

---------------------------
## [3-1] Merge를 알아보자
**Branch Merge 작업이란?** 
    각 다른 Branch에서 작업한내용을 master에 반영을 하기위해 병합하는 작업을 말한다.
    **git merge [Branch명]** 을 이용해서 병합할수있다. 
    다만, switch를 통해 marster로 바꿔준 다음, 병합을 진행해야한다.
   
### Merge의 세가지 종류

- Fast-Forward : Branch가 가리키는 커밋을 앞으로 이동시킨다.(별도의 merge과정 없이 포인터가 이동.)
               git merge [Branch명]

- 3-Wa Merge :  병합할 때 각 Branch 의 커밋 두개와 공통조상 하나를 사용하여 병합을한다.
              -> 어느때사용? 두 Branch에서 다른파일 / 같은파일의 **다른부분을 수정**했을시 사용한다.
              
    ```bash
        $ git merge iss53
        Merge made by the 'ort' strategy
    ```

-Merge Conflict : 3way와 다르게 두 Branch에서 **같은파일의 같은부분을 수정** 했을시 발생한다.
                  충돌나는 부분을 어느쪽으로 수정할건지 하나의 수정내용만 선택하여 적용시킨다.
                  Merge branch [Branch명]

# [4] 그 외의 기능
    
위의 **Clon,Pull,Branch,Merge** 등의 기능을 통해 Git Hub에서 협업하기가 수월해졌다.

그럼 Hub내에서 무엇을할수있는지 조금 알아보자.

- Fork & Pull Model:(오픈 소스 프로젝트와 같이, 자신의 소유가 아닌 원격 저장소인 경우 사용합니다.) 
> 
    1.원본 원격 저장소를 내 원격 저장소에 복제하여 로컬에 Clon으로 다운받아 사용할 수 있게된다.=fork
    2.다운받은 Clon파일을 수정하고 커밋한 후, push를 통해 내 원격 저장소에 저장한다.
    3.이후 Pull Request(PR)를 통해 원본 원격 저장소에 반영될 수 있게 요청한다.

- fork로 떠와서 -> Clon로 다운받고 -> 수정 add, commit하고 ->push로 원격에 올린다음 ->pull request를 요청

# [5] Git명령어 정리 

<details>
<summary>기본</summary>

## 기본Git명령어

```bash
# 작성자 이름, 메일 등록 (최초 1번만 실행)
git config --global user.name "github username"
git config --global user.email "github email"

# config 정보 출력
git config --global --list

# 일반 폴더 -> 로컬 저장소
git init

# 버전 상태 출력
git status

# Working Directory -> Staging Area
git add [File]
git add .  # 모든 파일 add

# Staging Area -> Commits
git commit -m "commit message"

# commits 목록 출력
git log
git log --oneline  # 한줄로 보기 옵션
git log -p  # 커밋마다 차이 보기 옵션

```
</details>

<details>
<summary>리모트</summary>

## 리모트명령어

```bash
# 로컬 저장소와 원격 저장소를 연결
git remote add origin [Github repository URL]

# 연결된 원격 저장소 목록 조회
git remote -v

# 원격 저장소 연결 삭제
git remote rm origin
git remote remove origin

# 로컬 저장소의 commits을 원격 저장소에 반영
git push origin master
git push -u origin master  # -u 옵션을 했다면 이후 push할 때는 git push만으로도 가능

# 원격 저장소를 로컬에 복제
git clone [Github repository URL]

# 원격 저장소의 변경 사항 로컬에 받아오기 (동기화)
git pull origin master
```
</details>

<details>
<summary>reset, revert</summary>

## reset, revert

```bash
# 특정 커밋 상태로 되돌리기 (soft, mixed, hard 세 가지 옵션)
git reset --soft [commit ID]
git reset --mixed [commit ID]
git reset --hard [commit ID]

# 커밋을 취소하는 커밋을 새로 생성하여 특정 커밋을 되돌리기
git revert [commit ID]

# 이전 커밋 목록 모두 출력
git reflog
```
</details>


<details>
<summary>Branch,Merge</summary>

## Branch,Merge

```bash
# 브랜치 목록 확인
git branch

# 새 브랜치 생성
git branch [branch name]

# 특정 브랜치 삭제
git branch -d [branch name]
git branch -D [branch name]  # 강제 삭제(병합되지 않은 브랜치도 삭제)

git switch [branch name]  # 다른 브랜치로 이동
git switch -c [branch name]  # 브랜치를 생성함과 동시에 이동

# 한 줄로, 모든 브랜치의, 그래프를 포함하여 커밋 목록 출력
git log --oneline --all --graph

# 브랜치 병합
git merge [branch name]

```
</details>

