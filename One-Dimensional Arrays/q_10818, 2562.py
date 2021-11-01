''' min/max '''

# 10818번
n = int(input())
numList = list(map(int, input().split()))
numList.sort()
print(numList[0], numList[-1])

# 2562번 (파이참 결과는 맞는데 백준 제출은 틀렸습니다?)
numList, max= [], 0
for i in range(10):
    numList.append(int(input()))
    if numList[i-1] < numList[i]:
        max = numList[i]
print(max, numList.index(max)+1, sep="\n") #인덱스 0부터 시작하기 때문에 +1

# 2562번 => max함수 사용
numList=[]
for i in range(9):
    numList.append(int(input()))
print(max(numList), numList.index(max(numList))+1, sep="\n")
