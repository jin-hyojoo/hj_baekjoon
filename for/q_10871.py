# 10871번 (틀림)
# list 사용이 포인트

num,standardNum = map(int, input().split())
A = list(map(int,input().split()))
for i in range(num):
    if A[i] < standardNum : print(A[i], end=" ")