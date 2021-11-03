
# 2739번 구구단 출력
num = int(input())
for i in range(1,10):
    print(f'{num} * {i} = {num*i}' )
    
# 10950번
testcnt = int(input())
for i in range(1,testcnt+1):
    a,b = map(int, input().split())
    print(a+b)

# 8393번
n, sum = int(input()), 0
for i in range(1, n+1):
    sum += i
print(sum)


# 15552번 빠른 A+B
# 빠른 I/O 방식을 통해 시간초과를 방지 => python의 경우 input 대신 sys.stdin.readline 사용
# 이때 맨 끝 개행문자까지 입력받기 떄문에 문자열 저장하고 싶은 경우엔 .rstrip()
import sys
T = int(input())
for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)


# 2741번
num = int(input())
for i in range(1,num+1): print(i)

# 2741번 한 줄.ver
for i in range(1, int(input())+1): print(i)

# 2742번
for i in range(int(input()), 0, -1): print(i)

# 11021번
testcnt = int(input())
for i in range(1,testcnt+1):
    a,b = map(int, input().split())
    print(f'Case #{i}: {a+b}')

# 11022번
testcnt = int(input())
for i in range(1,testcnt+1):
    a,b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')








