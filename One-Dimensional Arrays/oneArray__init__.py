
# 2557번 숫자의 개수
# 리스트에는 문자열로 저장되어있기 때문에 count()함수에 str형변환 요함
# 계속 int형으로 count를 했기 때문에 결과값이 0만 나온 거였음...
a, b, c = int(input()), int(input()), int(input())
mList = list(str(a*b*c))
for i in range(10) :
    print(mList.count(str(i)))

# 1546번 평균
subjectNum, subScoreList, modifyScore = int(input()),list(map(int, input().split())), 0
for item in subScoreList:
     modifyScore += item/max(subScoreList)*100
print(modifyScore/subjectNum)



