# ************** 다른사람 소스 확인 후 재 작성, 스택 문제니깐 append랑 pop은 써야지 **************
import sys

cmdList = list(sys.stdin.readline().rstrip()) ## 입력 값

tmpList = [] # 막대기 임시보관함

totCnt = 0 # 절단된 막대기 개수 
prev = '' # 이전 입력 값 
for command in cmdList:
    if command == '(':
        tmpList.append('(')
        prev = '('
    elif command == ')':
        if prev == '(': ## '()' 레이저 절단
            tmpList.pop(-1) # 절단한거니깐 이전 막대기로 입력한 값 취소
            totCnt += len(tmpList)
        else:
            tmpList.pop(-1)
            totCnt += 1
        prev = ')'
print(totCnt) # 최종 막대기 갯수 
# ************** 제출은 성공했지만 stack 문제에 맞지 않는 풀이같아서 찝찝  **************
# import sys

# totNum = 0 # 절단된 쇠막대기 갯수 
# tmpNum = 0 # 쇠막대기 개수

# cmdList = list(sys.stdin.readline().rstrip()) ## input() , 현재 편집기에 입력된 문자

# cnt = 0 # cmdList 인덱스 
# for command in cmdList:
#     if command == '(':
#         tmpNum += 1
#     elif command == ')':
#         if cmdList[cnt-1] == '(':  ## '()' 일때 실행:
#             tmpNum -=1 # 앞에 작업 취소
#             totNum += tmpNum
#         else:    
#             tmpNum -=1 # 앞에 작업 취소
#             totNum += 1 
#     cnt +=1

# print(totNum) ## 스택문제인데 이거 맞아?ㅋㅋㅋㅋㅋㅋㅋ


# ************** 메모리초과로 제출 실패  **************  
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

