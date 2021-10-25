'''
# 10952번
import sys
while True:
    # a,b = map(int, input().split())
    a,b = map(int, sys.stdin.readline().split())
    # 입력의 마지막에는 0 2개가 들어오므로 if문 추가
    if (a == 0 and b == 0): break
    else : print(a+b)

#10951번
# 테스트 케이스가 정해지지 않아 무한반복 되는 while문은 오류처리 요함
while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except: break
'''
# 1110번
N, cycleCnt, tmpN = int(input()), 0, 0
tmpN = N
while True:
    tmp1 = tmpN // 10 #몫(정수 부분만, 두자리수 중 앞자리 수)
    tmp2 = tmpN % 10 #나머지 (두자리수 중 뒷자리 수)
    tmp3 = (tmp1 + tmp2) % 10 #앞,뒷자리 더한 결과값의 뒷자리 수
    tmpN = (tmp2 * 10) + tmp3 #tmp2, tmp3 값 각각 첫-뒷자리 수

    cycleCnt+= 1
    if tmpN == N: break
print(cycleCnt)

