# 가상머신 하둡,스파크설치

1.업데이트&기본설치

sudo apt update

sudo apt upgrade -y

sudo apt install vim -y

sudo apt install openssh-server -y

sudo apt install ssh-askpass -y

ssh-keygen -y rsa -P '' -f ~/.ssh/id_rsa
cat ~/.shh/id_rsa.pub >> ~/.ssh/authorize_keys

2.아마존 corretto설치(11버전설치할것임. 버전은자유)

wegt [tar xvzf amazon-corretto-11-x64-linux-jdk.tar.gz](https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.tar.gz)

- 코레토의 위치가 루트에있으면 편함 
- 루트가아닐경우 mv [이동대상] [이동할경로] (여러대상을 한번게 옮기기가능)
- mv *[이동할경로] :현재위치의 모든파일 이동
  
```python
~/.bashrc 설정
# java
export JAVA_HOME=/home/big/java
export PATH=$PATH:$JAVA_HOME/bin
```

3.python 설치 & 설정

sudo apt install python3-pip -y

```python
~/.bashrc

# python
alias python=python3
```

4.hadoop 설치 & 설정

스파크에 하둡이 같이들어있는 패키지가있는데,
이것은 하둡실행을 위한 **라이브러리** 이므로 하둡을 데이터저장용도로 사용하고싶으면,
하둡을 따로 설치하는것을 권장.


### vim hadoop-env.sh

```python
#exmport hadoop_home
->export hadoop_home=/home/big/java  으로 설정

export hadoop_pid_dir=pids
```

