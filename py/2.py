a = []
while True:
    s = input("请输入一个整数（输入q结束）：")
    if s == "q":
        break
    try:
        n = int(s)
        a.append(n)
    except ValueError:
        print("输入的不是整数，请重新输入。")
if a:
    avg = sum(a) / len(a)
    print("平均值为：", avg)
else:
    print("没有输入任何整数。")
