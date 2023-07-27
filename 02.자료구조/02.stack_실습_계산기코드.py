# infix 수식 -> postfix 수식
# '2+3*5' -> 235*+

# postfix 수식 -> 계산

outstack = [] 
opstack = []

def isEmpty():
    return len(opstack) == 0

def push(item):
    opstack.append(item)

def pop(item):
    opstack.pop(-1)

def tokenRnk(item): 
    ## token 의 우선순위 설정
    if(item in('+','-')):
        rnk = '1'
    elif(item in('*','/')):
        rnk = '2'
    return int(rnk)


instack = input("infix 수식을 입력 : ").split() # 2+3*5 
print(instack)


for token in instack:
    if token in ('1','2','3','4','5','6','7','8','9'): 
        outstack.append(token)
    if token == '(':
        opstack.append(token)
    if token == ')':    
        tmp = opstack.pop()
        while tmp != '(' :  # '(가 나올떄 까지 pop
            outstack.append(tmp)
            tmp = opstack.pop()              
    if token in ('+','*','-','/'):
        if len(opstack) == 0:
            opstack.append(token)
        else:
            tmp = opstack.pop()
            if tmp == '(':
                opstack.append(tmp)
                opstack.append(token)
            else:
                if tokenRnk(token) >= tokenRnk(tmp):
                    outstack.append(token)
                    opstack.append(tmp)
                else:
                    outstack.append(tmp)
                    opstack.append(token)

print("outstack >>")
print(outstack)