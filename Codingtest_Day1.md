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