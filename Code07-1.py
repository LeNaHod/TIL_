##함수




##전역

import queue


size=5
queue= [None for _ in range(size)]
front = rear = -1

##메인

#삽입(enqueue)은 꼬리를하나 증가시킨다.

rear += 1
queue[rear]='화사' 

rear += 1
queue[rear]='솔라' 

rear += 1
queue[rear]='문별' 

print('출구<---' ,queue,'<---입구')

#dequeue() 추출

front += 1
data = queue[front]
queue[front]=None #나가면 자리를 None로 채워준다.
print('식사 손님:', data)

front += 1
data = queue[front]
queue[front]=None
print('식사 손님:', data)

front += 1
data = queue[front]
queue[front]=None
print('식사 손님:', data)