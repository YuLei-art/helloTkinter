from tkinter import *  # 导入窗口控件
from tkinter import ttk
root=Tk () #创建窗口
root.title("tree表格测试")
root.geometry("600x300+300+100") #小写x代表乘号500x400为窗口大小，+500+300窗口显示位置
root.columnconfigure(0, weight=1)


tree = ttk.Treeview(root, show="headings") #表格第一列不显示
tree.grid(row=0, columnspan=1)
tree["columns"] = ("序号", "企业名称", "详细信息","其他")
# 设置列，不显示
tree.column("序号", width=100)
tree.column("企业名称", width=100)
tree.column("详细信息", width=300)
tree.column("其他", width=300)
# 显示表头
tree.heading("序号", text="序号")
tree.heading("企业名称", text="企业名称")
tree.heading("详细信息", text="详细信息")
tree.heading("其他", text="其他")

# i = 0
ii = 0
name = "辽宁忠旺集团"
addurl = "辽宁省沈阳市铁西区22号"
aa = ".........................................................."

for i in range(30):
    value = (i+1, name, addurl, aa)
    tree.insert("", END, text=i+1, values=value)

# for i in range(30):
#     tree.insert("", END, text="", values=(i+1, "a"+str(i+1), addurl+str(i+1), aa))

"""
    定义滚动条控件
    orient为滚动条的方向，vertical--纵向，horizontal--横向
    command=tree.yview 将滚动条绑定到treeview控件的Y轴
"""
# ----vertical scrollbar------------
vbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
vbar.grid(row=0, column=1, sticky=NS)
tree.configure(yscrollcommand=vbar.set)

# # ----horizontal scrollbar----------
hbar = ttk.Scrollbar(root, orient=HORIZONTAL, command=tree.xview)
hbar.grid(row=1, column=0, sticky=EW)
tree.configure(xscrollcommand=hbar.set)


root.mainloop() #显示窗口  mainloop 消息循环
