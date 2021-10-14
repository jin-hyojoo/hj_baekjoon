# 백준 10430
"""
# ver1

A,B,C = input().split()
A,B,C = int(A),int(B),int(C)
print((A+B)%C, ((A%C)+(B%C))%C,(A*B)%C, ((A%C)*(B%C))%C, sep='\n')
"""

# ver2 => map 함수 활용
A, B, C = map(int, input().split())
print((A+B)%C, ((A%C)+(B%C))%C,(A*B)%C, ((A%C)*(B%C))%C, sep='\n')

