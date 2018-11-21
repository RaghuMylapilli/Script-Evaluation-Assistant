num1, num2 = list(map(int, input().split()))
if num1%num2==0:
    print(num1,"is divisible by",num2)
else:
    print(num1,"is not divisible by",num2)
