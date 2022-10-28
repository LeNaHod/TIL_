
## 함수
def isQueueFull() :  # %5를 쓰면 원형이된다.일반애들은 다돌아가지만,
    global SIZE, queue, front, rear #마지막을 최대크기로나누면 0이되니까 0으로돌아감(원이됨)
    if ( (rear+1) % SIZE == front) :
        return True
    else :
        return False

def enQueue(data) : 
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return None
    return queue[ (front+1) % SIZE]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
print('출구<---', queue, '<---입구')

enQueue('선미')
print('출구<---', queue, '<---입구')

print('식사 손님:', deQueue())
print('식사 손님:', deQueue())
print('출구<---', queue, '<---입구')
#
enQueue('재남')
print('출구<---', queue, '<---입구')
enQueue('길동')
print('출구<---', queue, '<---입구')
enQueue('철수')
