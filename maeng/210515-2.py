# https://programmers.co.kr/learn/courses/4008/lessons/13323

a, b = map(int, input().strip().split(' '))
print(a//b, a%b)
print(*divmod(a, b))        # 다른 방법