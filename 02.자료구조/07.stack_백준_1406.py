import sys

cur_text = list(sys.stdin.readline().rstrip()) ## input() , 현재 편집기에 입력된 문자
order_cnt = int(input()) ## 명령어의 개수

tmp_word =[]

for i in range(order_cnt):
    order_word = sys.stdin.readline().split() ## 명령어 
    if order_word[0] == 'P':
        cur_text.append(order_word[1])
    elif order_word[0] == 'L' and cur_text: ## cur_text 가 null 이 아니고 명령어가 'L' 일 떄 실행 
        tmp_word.append(cur_text.pop())
    elif order_word[0] == 'D' and tmp_word:
        cur_text.append(tmp_word.pop())
    elif order_word[0] == 'B' and cur_text:        
        cur_text.pop(-1)

print("".join(cur_text + list(reversed(tmp_word)))) ## 리스트를 for 문 없이 출력할때 , "".join(리스트) 사용 

# list를 2개 사용해서 임시로 넣고 빼고 하려 했다. 
# 소스가 꽤 복잡져서 인터넷 검색하니 list 2개 사용하지만 마지막에 reversed 로 마무리
# list 가 null 인지 계속 조건절 len(list) 을 추가 했는데 , if list명  ->  null(false)/not null(true) 값 리턴
  