# 8958번 OX퀴즈
caseCnt = int(input())
for i in range (caseCnt):
    oxList = list(input()) ## OX 문자열 입력받기

    ## O 개수 판별해서 점수 계산
    score, sumScore = 0,0
    for item in oxList:
        if item == 'O': score += 1
        else: score=0 ## X가 나오면 증가되는 score 초기화
        sumScore += score
    print(sumScore)


## 8958번 간략
for _ in range (int(input())):
    sumScore , score = 0,0
    for item in list(input()):
        if item == 'O': score+= 1
        else : score = 0
        sumScore += score
    print(sumScore)