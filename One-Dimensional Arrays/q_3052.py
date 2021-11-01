'''
(파이썬 리스트 중복 제거 방법 3가지,,,, 읽어보기)
https://blockdmask.tistory.com/543
'''

# 3052번 나머지
remainList, cnt= [], 0
for _ in range(1,11):
    remainList.append(int((input()))%42) #나머지값 담기
## print(remainList)

##나머지 카운트(0값 포함, 중복 제거 위해 set 자료구조 이용)
for item in set(remainList):
    if item in remainList :
        cnt += 1
print(cnt)


# 3052번 => 나머지 값 담기/카운트 나누지 않고 한 번에
remainList, cnt= [], 0
for _ in range(1,11):
    num = int(input()) % 42
    if num not in remainList:
        remainList.append(num)
        cnt += 1
print(cnt)