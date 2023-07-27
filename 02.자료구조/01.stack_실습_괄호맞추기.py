# 입력 : 왼쪽, 오른쪽 괄호 문자열 
# 출력 : 괄호가 쌍을 이루어져 있으면 true, 그렇지 않으면 false

# (()()) -> true
# (())( -> false


top = []
def isEmpty():
    return len(top) == 0

def push(item):
    top.append(item)

def pop():
    if not isEmpty(): # 공백이 아닌 경우
        return top.pop(-1) # 맨 뒤에서 1개를 꺼내서 반환

# for i in range(1,6):
#    push(i)

# print('push 5회 : ' , top)
# print('pop() --> ',pop())
# print('pop() --> ',pop())
# print('pop 2번  : ' , top)

a = input("괄호를 띄어쓰기로 구분하여 입력하시오.").split()

for p in range(len(a)):
    if a[p] == '(':
        push(a[p])
    elif a[p]  == ')' :
        pop()
    else :
        print("not allowed sysmbol")

print(top)

if len(top) > 0 :
    print('false')          
else:
    print('true')
    