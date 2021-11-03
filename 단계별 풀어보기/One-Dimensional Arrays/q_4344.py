# 4344번 평군은 넘겠지 (파이참 결과는 맞는데 백준 제출은 틀렸습니다?)
for _ in range(int(input())):
    stu_num = list(map(int, input().split())) #학생들의 점수 입력받기
    sum, avg, cnt = 0, 0, 0
    for i in range(1, len(stu_num)):
        sum += stu_num[i]
    avg = sum/(len(stu_num)-1)
    for item in stu_num:
        if item > avg: cnt+= 1
    print(f'{cnt/(len(stu_num)-1)*100:.3f}%')

# 4344번 간략
for _ in range(int(input())):
    stu_num = list(map(int, input().split()))
    avg = sum(stu_num[1:])/stu_num[0]
    cnt = 0
    for item in stu_num[1:]:
        if item > avg: cnt+= 1
    print(f'{cnt/stu_num[0] * 100:.3f}%')