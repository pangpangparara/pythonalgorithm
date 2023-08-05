import sys

totNum = 0 # 절단된 쇠막대기 갯수 
tmpNum = 0 # 쇠막대기 개수

cmdList = list(sys.stdin.readline().rstrip()) ## input() , 현재 편집기에 입력된 문자

cnt = 0 # cmdList 인덱스 
for command in cmdList:
    if command == '(':
        tmpNum += 1
    elif command == ')':
        if cmdList[cnt-1] == '(':  ## '()' 일때 실행:
            tmpNum -=1 # 앞에 작업 취소
            totNum += tmpNum
        else:    
            tmpNum -=1 # 앞에 작업 취소
            totNum += 1 
    cnt +=1

print(totNum) ## 스택문제인데 이거 맞아?ㅋㅋㅋㅋㅋㅋㅋ


# 메모리초과로 제출 실패 
# import sys

# totList = [] # 절단된 쇠막대기를 모아두는 list
# tmpList = [] # 절단에 사용되는 막대기 임시 list

# cmdList = list(sys.stdin.readline().rstrip()) ## input() , 현재 편집기에 입력된 문자

# cnt = 0 # cmdList 인덱스 
# for command in cmdList:
#     if command == '(':
#         tmpList.append('1')
#     elif command == ')':
#         if cmdList[cnt-1] == '(':  ## '()' 일때 실행:
#             tmpList.pop(-1) # 앞에 작업 취소
#             for add in tmpList:
#                 totList.append(add)
#         else:    
#             tmpList.pop(-1)
#             totList.append('1') 
#     cnt +=1

# print(len(totList) )

