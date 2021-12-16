import tkinter as tk
from dataBaseOpr import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import *

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox



class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # 变量定义
        self.opr = MySqlOpr()
        self.list = self.init_data()
        self.item_selection = ''
        self.data = []


        #定义区域，把全局分为上中下三部分
        self.frame_top = tk.Frame(width=600,height=90)
        self.frame_center = tk.Frame(width=600,height=180)
        self.frame_bottom = tk.Frame(width=600,height=90)

        # 定义上部分区域
        self.lb_tip = tk.Label(self.frame_top,text="评议小组")
        self.string = tk.StringVar()
        self.string.set("")
        self.ent_find_name = tk.Entry(self.frame_top,textvariable=self.string)
        self.btn_query = tk.Button(self.frame_top,text="查询",command=self.query)
        self.lb_tip.grid(row=0,column=0,padx=15,pady=30)
        self.ent_find_name.grid(row=0, column=1, padx=60, pady=30)
        self.btn_query.grid(row=0, column=2, padx=30, pady=30)

        # 定义下部分区域
        self.btn_delete = tk.Button(self.frame_bottom, text="删除")
        self.btn_update = tk.Button(self.frame_bottom, text="修改")
        self.btn_add = tk.Button(self.frame_bottom, text="添加",command=self.addGroup)
        self.btn_delete.grid(row=0, column=0, padx=20, pady=30)
        self.btn_update.grid(row=0, column=1, padx=120, pady=30)
        self.btn_add.grid(row=0, column=2, padx=20, pady=30)


        # 定义中心列表区域
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=8, columns=("a", "b", "c", "d"))
        self.vbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)
        # 表格的标题
        self.tree.column("a", width=80, anchor="center")
        self.tree.column("b", width=120, anchor="center")
        self.tree.column("c", width=120, anchor="center")
        self.tree.column("d", width=120, anchor="center")
        self.tree.heading("a", text="小组编号")
        self.tree.heading("b", text="小组名称")
        self.tree.heading("c", text="负责人")
        self.tree.heading("d", text="联系方式")
        # 调用方法获取表格内容插入及树基本属性设置
        self.tree["selectmode"] = "browse"
        self.get_tree()
        self.tree.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)

        # 定义整体区域
        self.frame_top.grid(row=0, column=0, padx=60)
        self.frame_center.grid(row=1, column=0, padx=60, ipady=1)
        self.frame_bottom.grid(row=2, column=0, padx=60)
        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        # 窗体设置
        self.center_window(600, 360)
        self.title('评议小组管理')
        self.resizable(False, False)
        self.mainloop()

    # 窗体居中
    def center_window(self, width, height):
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        # 宽高及宽高的初始点坐标
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(size)

    # 数据初始化获取
    def init_data(self):
        result = self.opr.query()
        if self.opr.queryStatus:
            return 0
        else:
            return result

    # 表格内容插入
    def get_tree(self):
        if self.list == 0:
            tkinter.messagebox.showinfo("错误提示", "数据获取失败")
        else:
            # 删除原节点
            for _ in map(self.tree.delete, self.tree.get_children("")):
                pass
            # 更新插入新节点
            for i in range(len(self.list)):
                group = self.list[i]
                self.tree.insert("",END,values=(group[0],group[1],group[2],group[3]), text=group[0])
            # TODO 此处需解决因主程序自动刷新引起的列表项选中后重置的情况，我采用的折中方法是：把选中时的数据保存下来，作为记录
            # 绑定列表项单击事件

            self.tree.bind("<ButtonRelease-1>", self.tree_item_click)
            self.tree.after(500, self.get_tree)

    # 为解决窗体自动刷新的问题，记录下单击项的内容
    def tree_item_click(self, event):
        try:
            selection = self.tree.selection()[0]
            self.data = self.tree.item(selection, "values")
            self.item_selection = self.data[0]
        except IndexError:
            tkinter.messagebox.showinfo("单击警告", "单击结果范围异常，请重新选择！")

    # 单击查询按钮触发的事件方法
    def query(self):
        query_info = self.ent_find_name.get()
        self.string.set('')
        if query_info is None or query_info == '':
            tkinter.messagebox.showinfo("警告", "查询条件不能为空！")
            self.get_tree()
        else:
            strSql = "where name like '%"+  query_info + "%'"
            result = self.opr.query(queryby=strSql)
            self.get_tree()
            if self.opr.queryStatus:
                tkinter.messagebox.showinfo("警告", "查询出错，请检查数据库服务是否正常")
            elif not result:
                tkinter.messagebox.showinfo("查询结果", "该查询条件没有匹配项！")
            else:
                self.list = result
                # TODO 此处需要解决弹框后代码列表刷新无法执行的问题

    # 调用子窗口，获取子窗口的list数据，进行数据后续处理
    def addGroup(self):
        addWin = AddWindow()
        self.wait_window(addWin)  # 启动子窗口线程
        res = addWin.groupinfo    # 获得子窗口封装后的list数据
        print(res)

    # def addGroup(self):
    #     res = self.ask_groupinfo()   # 接收弹窗的数据
    #     print("回到母窗口了")
    #     print(res)
    #     if res is None: return

    #     # 弹窗
    # def ask_groupinfo(self):
    #     addWin = AddWindow()
    #     self.wait_window(addWin)  # 这一句很重要！！！
    #     return addWin.groupinfo


    # def addGroup(self):
    #     creatWin = tk.Toplevel(master=self)
    #     noLab = Label(creatWin, text="小组编号")
    #     noLab.grid(row=0)
    #     nameLab = Label(creatWin, text="小组名称")
    #     nameLab.grid(row=1)
    #     headerLab = Label(creatWin, text="负责人")
    #     headerLab.grid(row=2)
    #     telLab = Label(creatWin, text="负责人联系电话")
    #     telLab.grid(row=3)
    #     noEnt = Entry(creatWin)
    #     noEnt.grid(row=0,column=1)
    #     nameEnt = Entry(creatWin)
    #     nameEnt.grid(row=1, column=1)
    #     headerEnt = Entry(creatWin)
    #     headerEnt.grid(row=2, column=1)
    #     telEnt = Entry(creatWin)
    #     telEnt.grid(row=3, column=1)
    #     okBtn = Button(creatWin,text="确定",command=self.insert)
    #     okBtn.grid(row=4,column=0, columnspan=2)
    #     width = 600
    #     height = 360
    #     screenwidth = self.winfo_screenwidth()
    #     screenheight = self.winfo_screenheight()
    #     # 宽高及宽高的初始点坐标
    #     size = '%dx%d+%d+%d' % (600, 360, (screenwidth - width) / 2, (screenheight - height) / 2)
    #     creatWin.geometry(size)
    #     creatWin.mainloop()

class AddWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('新增小组')

        # 弹窗界面
        self.setup_UI()

    def setup_UI(self):
        # 第一行（两列）  小组编号
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='小组编号：', width=8).pack(side=tk.LEFT)
        self.num = tk.StringVar()
        tk.Entry(row1, textvariable=self.num, width=20).pack(side=tk.LEFT)

        # 第二行（两列） 小组名称
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='小组名称：', width=8).pack(side=tk.LEFT)
        self.groupName = tk.StringVar()
        tk.Entry(row1, textvariable=self.groupName, width=20).pack(side=tk.LEFT)

        # 第三行（两列） 负责人姓名
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='负责人姓名：', width=8).pack(side=tk.LEFT)
        self.headerName = tk.StringVar()
        tk.Entry(row1, textvariable=self.headerName, width=20).pack(side=tk.LEFT)

        # 第四行  负联系电话
        row2 = tk.Frame(self)
        row2.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row2, text='联系电话：', width=8).pack(side=tk.LEFT)
        self.tel = tk.IntVar()
        tk.Entry(row2, textvariable=self.tel, width=20).pack(side=tk.LEFT)

        # 第五行
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Button(row3, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row3, text="确定", command=self.ok).pack(side=tk.RIGHT)
        self.center_window(600, 360)

        # 窗体居中
    def center_window(self, width, height):
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        # 宽高及宽高的初始点坐标
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(size)

        # 确定键，将文本框值组装成一个list数据
    def ok(self):
        self.groupinfo = [self.num.get(), self.groupName.get(),self.headerName.get(),self.tel.get()]  # 设置数据

        self.destroy()  # 销毁窗口


        # 取消键，销毁窗口
    def cancel(self):
        self.groupinfo = None  # 空！
        self.destroy()




