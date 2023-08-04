import sys

n = int(input()) # 피연산자의 개수 
posfix = list(input()) # 후위표기식 입력:  ABC*+DE/- 출력 : ['A', 'B', 'C', '*', '+', 'D', 'E', '/', '-'] 

expn = []
for i in range(n):
    expn.append(int(input()))
numstk = []
for token in posfix:
    if 'A' <= token <= 'Z':
        numstk.append(expn[ord(token) - ord('A')]) # 문자열이랑 숫자 매핑 해야하는데 몰라서 검색 아래 사항 
                                             # 만약 문자인 경우 ord() > 아스키 코드값으로 변환 후 배열 인덱스를 구해 추가
    else:
        a = numstk.pop()
        b = numstk.pop()
        if token == '+':
            numstk.append(b + a)
        elif token == '-':
            numstk.append(b - a)
        elif token == '*':
            numstk.append(b * a)
        elif token == '/':
            numstk.append(b / a)
print(format(*numstk, ".2f")) ## 포맷은 이렇게 주는 구나. 인터넷 검색 