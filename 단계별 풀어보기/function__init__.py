'''

def solve(a: list) -> int형
-> a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
-> 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

# 15596번
def solve(a):
    return sum(a)
'''
# 4673번, 셀프넘버
def findSelfNum (num):
    dn = list(num)
    for item in num:
        num += item
    return num




