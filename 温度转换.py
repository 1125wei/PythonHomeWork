"""
打印hello world
温度转换
"""
print("hello world!")
select = input("1:摄氏度->华氏度；2:华氏度->摄氏度；请输入1或2选择：")  # 输入1 or 2 选择相应功能
data = float(input("请输入数据:"))
if select == "1":
    print("转换后的华氏温度为："+str(data * 9 / 5 + 32))  # 如果输入"1" 则进行 摄氏温度->华氏温度
elif select == "2":
    print("转换后的摄氏温度为："+str((data - 32) * 5 / 9))  # 如果输入"2" 则进行 华氏温度->摄氏温度
else:  # 如果输入除 1或者2的数据判断为非法
    print("输入非法！")
