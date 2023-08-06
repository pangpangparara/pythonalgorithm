# 클래스를 만들어보자
'''
class Person:
    def greeting(self):
        print('Hello')

jame = Person()
jame.greeting()
'''

# 큐를 만들어보자
class Queue:
    def __init__(self):
        self.items =[]
        self.front_index =0
        print("큐 선언")
      
    def enqueue(self,val):
        self.items.append(val)

    def deque(self):
        if self.front_index == len(self.items):
            print('Queue is Empty')
        else:
            x = self.items[self.front_index]
            self.front_index +=1
            return x

que = Queue()
que.enqueue(1)
print(que.deque())
que.enqueue(2)
que.enqueue(3)
print(que.deque())
print(que.deque())
print(que.deque())
