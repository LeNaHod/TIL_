# 코딩테스트 공부

서비스보완 및 배포매뉴얼 갱신과 동시에 틈틈히 코딩테스트 공부를 기록.


- 1번문제

    주어진 배열의 각 요소들을 최대 한번씩만 사용하여 조합하고, 입력값에서 각 요소들이 몇번나오는지 구하시오

    word=["aya", "ye", "woo", "ma"] #주어진 배열

```python

    def Test1(input_r):
        word = ["aya", "ye", "woo", "ma"]
        count = 0
        for input_rs in input_r:
            for words in word:
                input_rs = input_rs.replace(words, " ")
            if not input_rs.strip():
                count += 1
        return count

```

- 2번문제

    문자열로 입력된 매개변수의 값을 수식으로 계산하여 결과값을 리턴해라.

    -문자열의 시작과 끝에는 공백이없고, 0으로 시작하는 숫자는 주어지지않음.

    -연산자는 +,-만 사용할것

```python

def word_num(num_string):
    answer = 0
    for num in num_string.replace("-","+ -").split("+"):
        answer += int(num)
    return answer
```

- 3번문제

    X {연산자} Y =Z 형태의 문자열 배열이 매개변수로 주어지게되면,
    매개변수로 입력된 수식이 옳은 수식이면 "O"를 출력, 틀린수식이면 "X"을 반환하라.

    -X,Y,Z는 각각 0~9로 이루어진 정수를 의미하며, 앞에 "-"(마이너스)기호가 하나 존재할수있다. 이것은 음수의 의미이다.

    -X,Y,Z는 0으로 시작하지않는다.

```python

# [5+8=3, 10+2=12, -5+(-3)=-10]과 같이 배열로 quiz가 입력되면, 수식과 함께들어온 결과와 실제 연산결과를 비교하여, 결과가 일치하면 "O"출력, 다르면 "X"출력.

def Operatings(quiz):
    result = []
    for quu in quiz:
        left,right =quu.split("=")  # =를 기준으로 결과와 수식을 나눠 수식은 left에 결과는 right에 저장
        num1,opr,num2=left.split() # 나눠진 3 + 5 는 사이사이에 공백이 존재하기때문에 공백을 기준으로 3,+,5로 나눠 차례대로 각 num1,opr,num2에 할당
        
        # 만약 opr가 +면 더하기연산 진행
        if opr == "+":
            left=int(num1)+int(num2)
        elif opr == "-": # 이곳엔 그냥 else: 도 가능.
            left=int(num1)-int(num2)
        
        #result.append("O" if left==int(right) else "X") 도 가능.
        if left == int(right):
            result.append("O")
        else:
            result.append("X")
            
    return result
```