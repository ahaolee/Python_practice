## 打印功能提示
def print_menu():
    print("="*30)
    print("捕获异常系统")
    print("1.未声明变量")
    print("2.除数不能为零")
    print("3.索引错误")
    print("4.键错误")
    print("5.文件未发现")
    print("6.未知对象属性")
    print("7.退出系统")
    print("="*30)

print_menu()
while True:
    key = input("请输入功能选项:")
    if key == '1':
        try:
            print(a)
        except Exception as result:
            print("捕获到异常:%s"%result)
    elif key == '2':
        try:
            first_number = input("请输入第1个数:")
            second_number = input("请输入第2个数：")
            print(int(first_number)/int(second_number))
        except Exception as result:
            print("捕捉到异常：%s"%result)
    elif key == '3':
        try:
            demo_list = []
            print(demo_list[0])
        except Exception as result:
            print("捕捉到异常:%s"%result)
    elif key == '4':
        try:
            dictionary = {'host':'earth','port':80}
            print(dictionary['server'])
        except Exception as result:
            print("捕捉到异常:%s"%result)
    elif key == '5':
        try:
            file = open("test.txt")
        except Exception as result:
            print("捕捉到异常:%s"%result)
    elif key == '6':
        try:
            class Car(object):
                pass
            car = Car()
            car.color = "黑色"
            print(car.color)
            print(car.name)
        except Exception as result:
            print("捕捉到异常:%s"%result)
    elif key == '7':
        break
