def sum(n):
    res = 0
    while n >= 1:
        if n % 2 == 0:
            res -= 1.0/(n*(n+1))
        else:
            res += 1.0/(n*(n+1))
        n -= 1
    return res
num = int(input("请输入一个整数:"))
print(sum(num))
