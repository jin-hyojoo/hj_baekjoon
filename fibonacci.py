#피보나치 수열 구하기 함수
#Fn = Fn-1 + Fn-2
def fibonacci_test(n):
    if n < 2: return
    first, next = 0, 1
    for i in range(n):
        fist, next = next, first + next
    print(f'입력한 피보나치 수열의 값은 {first}입니다')

#fibonacci_test(int(input("")))
fibonacci_test(int(input("피보나치 수열 입력: ")))



