# section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time

words = [] # 영어 단어 리스트(1000개 로드)

n =  1  # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip()) # 양쪽 공백 제거해주는 strip 함수

# print(words) 단어 리스트 확인

print()

input("Ready? Press Enter Key") # Enter Game Start!

start = time.time()

while n <= 5:
    random.shuffle(words)   # words 순서 알아서 섞어줌
    q = random.choice(words)    # 랜덤으로 하나 뽑아오기

    print()

    print("*Question # {}".format(n))
    print(q)    # 문제 출력

    x = input() # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip():    # 입력 확인(공백 제거). 내가 입력한 값이랑 입력해야 하는 값이랑 동일한지 확인함
        print("Pass!")
        cor_cnt += 1
    else:
        print("Wrong!")

    n += 1  # 다음 문제 전환

end = time.time()   # End time 기록
et = end - start    # 소요시간 계산
et = format(et, ".3f")  # 소수점 자릿수 지정

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

# 수행 시간 출력
print("게임 시간 : ", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작 시점
if __name__ == '__main__':  # 이게 main에서 실행될 때에만 코드 돌아가도록 함
    pass