##함수

##전역
size=5
stack = [None for_in range(size)] #=stack = [None,None,None,None,None]
top = -1

##메인

#push
top +=1
stack[top]='커피'
top +=1
stack[top]='녹차'
top +=1
stack[top]='꿀물'

print('바닥:',stack)

#pop
data=stack[top]
stack[top]=None
top -= 1
print('팝->',data)
data=stack[top]
stack[top]=None
top -= 1
print('팝->',data)
data=stack[top]
stack[top]=None
top -= 1
print('팝->',data) #꿀물이 제일먼저 출력. 마지막에 넣었기때문에. 넣은순서와 반대로출력

