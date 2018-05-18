def getMax():
    num1 = int(input("请输入第一个数:"))
    num2 = int(input("请输入第二个数:"))
    num3 = int(input("请输入第三个数:"))
    temp = 0
    if num1 > num2:
        temp = num1
    else:
        temp = num2
    if temp > num3:
        return "其中最大值为:" + str(temp)
    else:
        return "其中最大值为:" + str(num3)
maxValue = getMax()
print(maxValue)
