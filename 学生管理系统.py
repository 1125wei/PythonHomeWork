# 学生信息列表，用来存储所有学生的信息
student_info = []


# 显示学生信息
def show_student():
    print("————" * 10)
    print("学生信息如下:")
    print("————" * 10)
    print("序号\t学号\t姓名\t性别\t")  # 打印表头
    i = 1
    for tempinfo in student_info:  # 遍历学生信息列表
        # 打印每个学生的信息，格式化输出
        print("%d\t%s\t%s\t%s\t" % (i, tempinfo['num'], tempinfo['name'], tempinfo['sex']))
        i += 1  # 序号递增


# 打印菜单
def print_menu():
    print("————" * 10)
    print("学生信息管理系统v1.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.显示所有学生信息")
    print("0.退出系统")
    print("————" * 10)


# 添加学生信息的函数
def add_student():
    newNum = input("请输入学号：")  # 提示用户输入学号
    newName = input("请输入学生姓名：")  # 提示用户输入姓名
    newSex = input("请输入学生性别：")  # 提示用户输入性别
    newInfo = {'num': newNum, 'name': newName, 'sex': newSex}  # 创建一个新的字典来存储学生信息
    student_info.append(newInfo)  # 将新学生的信息添加到学生信息列表


# 删除学生信息
def delStudentInfo(student):
    del_num = input("请输入要删除的学生的学号：")  # 输入要删除的学生的学号
    for stu in student:  # 遍历学生信息列表
        if stu['num'] == del_num:  # 如果找到匹配的学号
            student.remove(stu)  # 从列表中删除该学生的信息
            break


# 程序入口
if __name__ == '__main__':
    while True:  # 无限循环来持续运行程序
        print_menu()  # 打印菜单
        key = input("输入对应功能的字符：")
        if key == '1':  # 添加学生信息
            add_student()
        elif key == '2':  # 删除学生信息
            delStudentInfo(student_info)
        elif key == '3':  # 显示所有学生信息
            show_student()
        elif key == '0':  # 退出系统
            quit_con = input("确认退出吗？yes/No")  # 提示用户确认退出
            if quit_con == 'Yes' or quit_con == 'yes':
                break
