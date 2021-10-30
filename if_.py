
# 1330번
a,b = map(int, input().split())
if a > b :
    print('>')
elif a < b :
    print('<')
elif a == b:
    print('==')


# 9498번
score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else : print('F')


# 2753번 윤년문제 => 4의 배수 && 100의 배수 아닐 때 || 400의 배수일 때
year = int(input())
if (year%4==0 and year%100!=0) or (year%400==0):
    print(1)
else: print(0)


# 14681번
num1, num2 = int(input()), int(input())
if (num1 > 0) and (num2 > 0): print(1)
elif (num1 < 0) and (num2 > 0) : print(2)
elif (num1 < 0) and (num2 < 0) : print(3)
elif (num1 > 0) and (num2 < 0) : print(4)


# 2884번 (틀림)
H, M = map(int, input().split())
if M < 45:
    if H == 0: H = 24
    print(H-1, (60-45+M), sep=' ' )

# 참고 1
H, M = map(int, input().split())
if M > 44:
    print(H, M-45)
elif M < 45 and H > 0:
    print(H-1, M+15)
elif H == 0:
    H = 24
    print(H-1, M+15)


# 참고 2
H, M = map(int, input().split())
if M - 45 < 0:
    if H - 1 < 0:
        print(H + 24 - 1, M + 60 - 45)
    else:
        print(H - 1, M + 60 - 45)
else:
    print(H, M - 45)