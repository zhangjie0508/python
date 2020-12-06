import os

filename = 'student.txt'


def main():
    while True:
        menum()
        choice = int(input('请选择'))
        if choice in [0, 1, 2, 3, 4, 5]:
            if choice == 0:
                answer = input('你确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢你的使用！')
                    break  # 结束循环，退出系统
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()  # 查找学生信息
            elif choice == 3:
                delete()  # 删除学生信息
            elif choice == 4:
                modify()  # 修改学生信息
            elif choice == 5:
                show()  # 显示学生信息
#主菜单


def menum():
    print("----------宿舍管理系统----------")
    print("----------功能菜单-------------")
    print("         1.录入学生信息         ")
    print("         2.查找学生信息         ")
    print("         3.删除学生信息         ")
    print("         4.修改学生信息         ")
    print("         5.显示学生信息         ")
    print("         0.退出系统            ")
    print("-----------------------------")
#录入学生信息功能


def insert():
        student_list = []
        while True:
            id = input('请输入学号（如201806041101）：')
            if not id:
                break  # 如果学号为空字符串就退出循环
            name = input('请输入姓名：')
            if not name:
                break  # 如果姓名为空字符串就退出循环
            sex = input('请输入性别：')
            if not sex:
                break  # 如果性别为空字符串就退出循环

            try:
                age = int(input('请输入年龄：'))
                dorm = int(input('请数输入宿舍号：'))
            except:
                print('输入无效，不是整数类型，请重新输入')
                continue
            student = {'学号': id, '姓名': name, '性别': sex,
                       '年龄': age, '宿舍号': dorm}  # 将录入的学生信息保存到字典
            student_list.append(student)  # 将学生字典添加到列表中
            answer = input('是否继续添加？y/n\n')
            if answer == 'y'or answer == 'Y':
                continue
            else:
                break
        save(student_list)  # 调用save方法存储学生信息
        print('学生信息录入完毕')


def save(lst):
    try:
        sut_txt = open(filename, 'a', encoding='utf-8')  # 打开文件，a追加模式
    # 如果打开文件不存在就进入写入模式
    except:
        sut_txt = open(filename, 'w', encoding='utf-8')  # 打开文件，w写入模式
    for item in lst:  # 遍历列表
        sut_txt.write(str(item)+'\n')  # 将列表中每一行数据都转换成字符串类型
    sut_txt.close()  # 关闭文件
#查找学生信息


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按学号查找请输入1，按姓名查找请输入2：')
            if mode == '1':
                id = input('请输入学生学号：')
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('你的输入有误，请重新输入！')
                search()
            with open(filename, 'r', encoding='utf-8')as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    # print('--', d)
                    if id != '':
                        if d['学号'] == id:
                            student_query.append(d)
                    elif name != '':
                        if name['name'] == name:
                            student_query.append(d)
            # print(student_query)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            anser = input('是否要继续查询？y/n\n')
            if anser == 'y' or anser == 'Y':
                continue
            else:
                break
        else:
            print('暂为保存学生信息')
            return


def show_student(lst):
    # print('lst', lst)
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示')
        return
    format_title = '{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}'
    print(format_title.format('学号', '姓名', '性别', "年龄", '宿舍号'))
    #定义内容的显示格式
    format_date = '{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}'
    for item in lst:
        print(format_date.format(item.get('学号'),
                                 item.get('姓名'),
                                 item.get('性别'),
                                 item.get('年龄'),
                                 item.get('宿舍号')))
#删除学生信息


def delete():
        while True:
            student_id = input('请输入要删除的学生的学号:')
            if student_id != '':  # 如果输入的学号不为空
                if os.path.exists(filename):  # 判断文件是否存在
                    with open(filename, 'r', encoding='utf-8')as file:  # 以只读模式打开文件
                        student_old = file.readlines()  # 读取所有学生信息添加到列表中
                #文件不存在
                else:
                    student_old = []  # 列表为空
                flag = False  # 标记是否被删除
                if student_old:  # 判断列表
                    with open(filename, 'w', encoding='utf-8') as wfile:  # 以写入模式打开文件
                        d = {}  # 定义空字典
                        for item in student_old:  # 遍历列表
                            d = dict(eval(item))  # 把列表中字符串转字典
                            # 判断要删除的学生信息在字典中存不存在
                            if d['学号'] != student_id:  # 要删除的学生信息在字典中不存在
                                wfile.write(str(d)+'\n')  # 将一条学生信息写入文件
                            else:  # 要删除的学生信息在字典中存在
                                flag = True  # 已删除
                        #判断flag的值
                        if flag:
                            print(f'学号为{student_id}的学生信息已被删除')
                        else:
                            print(f'没有找到学号为{student_id}的学生信息')
                else:
                    print('无该学生信息')
                    break  # 退出循环
                show()  # 删除后要重新显示所有学生信息
                answer = input('是否继续删除？y/n\n')
                if answer == 'y' or answer == 'Y':
                    continue  # 继续删除信息
                else:
                    break  # 退出循环
#修改学生信息


def modify():
    show()  # 显示所有学生信息
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r', encoding='utf-8')as rfile:  # 以只读模式打开文件
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学生学号')
    with open(filename, 'w', encoding='utf-8')as wfile:  # 以写入模式打开文件
        for item in student_old:  # 遍历列表
            d = dict(eval(item))  # 字符串转成字典类型
            if d['学号'] == student_id:  # 是否为要修改的学生
                print('找到该学生信息，可以修改该学生的相关信息了')
                while True:
                    try:
                        d['id'] = input('请输入学号：')
                        d['name'] = input('请输入姓名：')
                        d['sex'] = input('请输入性别：')
                        d['age'] = input('请输入年龄：')
                        d['dorm'] = input('请输入宿舍：')
                    except:
                        print('你的输入有错误，请重新输入！')
                    else:
                        break  # 退出循环
                wfile.write(str(d)+'\n')  # 将修改的信息写入文件
                print('修改成功！')
            else:
                wfile.write(str(d)+'\n')  # 将未修改的信息写入文件
        answer = input('是否继续修改其他学生信息？y/n')
        if answer == 'y' or answer == 'Y':
            modify()
#显示学生信息


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂无学生信息数据')


if __name__ == '__main__':  # 以主函数方式运行
    main()  # 调用main
