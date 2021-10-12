#팩토리얼 구하기 함수
def fac_test(num):
    startNum = 1
    for numbers in range(1, num+1):
        startNum *= numbers
    print(f'{num}!의 결과값은 {startNum}입니다')

fac_test(int(input("팩토리얼 구할 양수 입력")))