##함수
#스택이 꽉 찼는지 확인이 꼭필요함! 스택오버플로우가일어나면 프로그램 사망

def isStackFull():
    global size,stack,top
    if(top == size -1):   #top이 위에있으니 0부터시작해서 -1인값이면 꽉찼다는소리
        return True
    else :
        return False
def push(data):
    global size,stack,top
    if (isStackFull() == True):
        print('스택 꽉찼어!!')
        return
    top += 1
    stack[top] =data #스택이 다 안찼을시 찰때까지 추가

#스택이 비었는지 확인

def isStackEmpty():
    global size,stack,top
    if(top == -1):
        return True
    else:
        return False

def pop():
    global size,stack,top
    if(isStackEmpty()):   #자체가 t/f값이니까 굳이 ==true/false를안썼음
        print('스택 없어')
        return None

    data =stack[top] #스택이있으면 없을때까지 꺼냄
    stack[top]=None
    top =-1
    return data
def peek(): #peek=미리보기 진짜꺼내는건아님
    global size,stack,top
    if(isStackEmpty()):
        print('스택이 없어')
        return None
    return stack[top]
##전역

size = 5
stack = [None for_in range(size)] #=stack = [None,None,None,None,None]
top = -1 #0으로해놓으면 0의 1번쨰부터쌓여서 1부터쌓여짐 -1은 0부터시작하겟다는의미?

##메인
push('커피')
push('녹차')
# push('꿀물')
# push('콜라')
# push('환타')

print('바닥:',stack)

#여기서부턴 넣어지지않음!
# push('사이다')
# print('바닥:',stack)

# print('팝-->',pop())
# print('팝-->',pop())
# print('팝-->',pop()) #계속꺼냄
# print('바닥:-->',stack) #현재스택출력

print('팝-->',pop())
print('다음후보:',peek())
print('팝-->',pop())
print('다음후보:',peek())
print('바닥-->',stack)
