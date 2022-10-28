##함수

from collections import deque


# def isQueueFull():#큐 꽉찼는지 확인
#     global SIZE,queue,front,rear
#     if (rear == SIZE-1): #>=도가능
#         return True  #넣을자리가없다
#     else:
#         return False #넣을자리가있다

#자리를만들어주기(당겨주기)

def isQueueFull():#큐 꽉찼는지 확인
    global SIZE,queue,front,rear
    if (rear != (SIZE-1)): #>=도가능
        return False 
    elif (rear == SIZE-1 and front == -1) :
        return True
    else:#자리를당기는 문
        for i in range(front+1,SIZE,1): #front+1부터 size까지 당김
            queue[i-1] = queue[i]
            queue[i]=None
        front -=1
        rear -=1
        return False
        

def enQueue(data):
    global SIZE,queue,front,rear
    if(isQueueFull()): #꽉찼으면 그냥 돌아가게구현
        print('큐가 꽉찼음')
        return 
    rear += 1
    queue[rear]=data

def isQueueEmpty():
    global SIZE,queue,front,rear

    if(front == rear): #큐가 비어있는지 확인
        return True
    else:
        return False #안비었으면 계속들어옴

def deQueue():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print("큐가없어")
        return None
    front +=1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE,queue,front,rear
    if(isQueueEmpty()): #큐가 비있을때
        print('큐가비어있어')
        return None
    return queue[front +1] #큐가비어잇지않을때 내보냄
##선언

SIZE=5
queue= [None for _ in range(SIZE)]
front = rear = -1

##메인
enQueue('화사')
enQueue('솔라')
# enQueue('문별')
# enQueue('휘인')
# enQueue('선미')

print('<--출구',queue,'<---입구')

# enQueue('재남')#꽉차서 못들어감
# print('<----출구',queue,'<----입구')

print('식사손님:',deQueue())
print('*준비하세요:',peek())
print('식사손님:',deQueue())
print('<----출구',queue,'<----입구')

print('식사손님:',deQueue())
#자리가비었지만 None가들어가잇어서 못들어감.당겨주거나 삭제하거나

enQueue('재남')
print('<----출구',queue,'<----입구')

enQueue('길동')
print('출구<---', queue, '<---입구')
enQueue('철수')
