n=int(input())
a1 = list(map(int, input().split()))
a1.insert(0,a1.pop())
print(a1)