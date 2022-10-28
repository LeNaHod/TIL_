##함수

def addNumber(num): #10이라고 가정하면 10에서 -1씩해서 num이1이될때까지 반복한다
    if (num ==  1): #for와 같음 대신 코드가 더 간결함. 단점:헷갈림
        return 1    #1+2+3+4+5+6+7+8+9+10 를 반복해서 55가  출력
    return num+addNumber(num-1)




##전역
print(addNumber(10))
