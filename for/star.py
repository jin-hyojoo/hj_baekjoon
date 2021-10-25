# # 2438번
# for dot in range(1, int(input())+1): print('*' * dot)
#
# # 2439번
# n = int(input())
# for dot in range(1,n+1): print(' '*(n-dot) + '*'*dot)
#
# # 2439번 .rjust(n) 활용 => 전체 n중 오른쪽 정렬
#         .center(n) => 전체 n 중 센터 정렬
#         .ljust(n) => 전체 n중 왼쪽 정렬

n = int(input())
for i in range(1, n+1):
    star = '*' * i
    print(star.rjust(n))