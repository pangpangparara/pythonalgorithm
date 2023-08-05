n = int(input()) # 명령어의 수 

queue = []
first_index = 0

for i in range(n): # 명령어 n 만큼 실행
    command = input().split() # 명령어
    if command[0] == 'push':
        queue.append(command[1])
    if command[0] == 'pop':
        if queue:
            first_num = queue[first_index]
            print(first_num)
          #  queue.remove[first_num]
        else:
            print(-1)
    if command[0] == 'size':
        print(len(queue))
    if command[0] == 'empty':
        if queue :
            print(0)
        else:
            print(1)
    if command[0] == 'front':
        if queue :
            print(queue[0])
        else:
            print(-1)
    if command[0] == 'back':
        if queue :
            print(queue[len(queue)-1])
        else:
            print(-1)

            # 아놔 출력값 이해가 안가는데 손으로 계산한거랑 달라
            # 