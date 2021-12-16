from tkinter import *


window = Tk()
window.title("ch_3")

msg = "欢迎进入宇阳英语学习系统"
img = PhotoImage(file="2.gif")
logolab = Label(window,image=img,text=msg,compound=BOTTOM)
logolab.pack()





labFrame = LabelFrame(window,text="数据验证")
accountL = Label(labFrame,text="账号：")
accountL.grid(row=0,column=0)
pwdL = Label(labFrame,text="密码：")
pwdL.grid(row=1)

accounE = Entry(labFrame)
accounE.grid(row=0,column=1)
pwdE = Entry(labFrame)
pwdE.grid(row=1,column=1)

labFrame.pack()
window.mainloop()
