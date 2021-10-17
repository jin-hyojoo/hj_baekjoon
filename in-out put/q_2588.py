# 변수 a를 변수 b 일,십,백의 자리와 각각 곱한 값을 출력해야 하니 문자열로 받기
a, b = int(input()), input()

# 문자열로 받은 값은 형변환을 통해 계산
print(a*int(b[2]), a*int(b[1]), a*int(b[0]), a*int(b), sep="\n")

# 다른사람 답 => print(a*(b%10),a*((b//10)%10),a*(b//100),a*b,sep="\n")