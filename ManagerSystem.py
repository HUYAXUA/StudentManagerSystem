# 添加学员函数内部需要创建学员对象，导入student模块
import student

from student import *


class MangerSystem():
    def __init__(self):
        # 存储学员数据列表
        self.student_list = []

    # 1，程序入口函数，启动程序后执行的函数
    def run(self):
        # 加载学员信息
        self.load_student()

        while True:
            # 显示功能菜单
            self.show_menu()

            # 用户输入功能序号
            menu_num = int(input('请输入您需要的功能序号：'))

            # 根据用户输入的功能序号执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()

            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()

            elif menu_num == 4:
                # 查询学员信息
                self.search_student()

            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()

            elif menu_num == 6:
                # 保存学员信息
                self.save_student()

            elif menu_num == 7:
                # 退出系统
                break
            else:
                print('无效果指令，请重新输入')

    # 2，定义功能函数
    # 显示功能菜单
    @staticmethod
    def show_menu():
        print('------------请选择如下功能------------')
        print('\t1：添加学员')
        print('\t2：删除学员')
        print('\t3：修改学员信息')
        print('\t4：查询学员信息')
        print('\t5：显示所有学员信息')
        print('\t6：保存学员信息')
        print('\t7：退出系统')
        print('------------------------------------')

    # 添加学员
    def add_student(self):
        # 用户输入姓名、性别、手机号
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的手机号：')
        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    # 删除学员
    def del_student(self):
        # 用户输入目标学员姓名
        del_name = input('请输入要删除学员的姓名：')
        # 判断该学员是否存在
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                print("该学员已经删除")
                break
        else:
            print("查无此人！")
        # 打印学员列表，验证删除功能
        # print(self.student_list)

    # 修改学员信息
    def modify_student(self):
        # ⽤户输⼊⽬标学员姓名
        modify_name = input('请输⼊要修改的学员的姓名：')
        # 如果⽤户输⼊的⽬标学员存在则修改姓名、性别、⼿机号等数据，否则提示学员不存在

        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输⼊学员姓名：')
                i.gender = input('请输⼊学员性别：')
                i.tel = input('请输⼊学员⼿机号：')
                print(f'修改该学员信息成功，姓名{i.name},性别{i.gender}, ⼿机号{i.tel}')
                break
            else:
                print('查⽆此⼈！')

    # 查询学员信息
    def search_student(self):
        # 用户输入目标学员姓名
        search_name = input('请输入要查询的学员姓名：')

        # 判断学员是否存在
        for i in self.student_list:
            if i.name == search_name:
                print(f'姓名：{i.name},性别：{i.gender},手机号：{i.tel}')
                break
            else:
                print("查无此人！")

    # 显示所有学员信息
    def show_student(self):
        print("\t姓名\t\t性别\t\t手机号")
        for i in self.student_list:
            print(f"\t{i.name}\t\t{i.gender}\t\t{i.tel}")

    # 保存学员信息
    def save_student(self):
        # 打开文件
        f = open('student.data', 'w')

        # 文件写入学员数据
        # 注意1：⽂件写⼊的数据不能是学员对象的内存地址，需要把学员数据转换成列表字典数据再做存储?
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        # 注意2：⽂件内数据要求为字符串类型，故需要先转换数据类型为字符串才能⽂件写⼊数据
        f.write(str(new_list))

        # 关闭文件
        f.close()

    # 加载学员信息
    def load_student(self):
        # 尝试以"r"模式打开数据⽂件，⽂件不存在则提示⽤户；⽂件存在（没有异常）则读取数据
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 读取数据
            data = f.read()
            # ⽂件中读取的数据都是字符串且字符串内部为字典数据，故需要转换数据类型再转换字典为对象后存储到学员列表
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            # 关闭文件
            f.close()
