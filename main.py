import random
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

# def treeSelect(event):
#     widgetObj = event.widget
#     itemSelected = widgetObj.selection()[0]
#     col1 = widgetObj.item(itemSelected,"text")
#     col2 = widgetObj.item(itemSelected, "values")[0]
#
#     str = "{0}:{1}".format(col1,col2)
#     # str = "{0}".format(col1)
#     var.set(str)

def doubleClick(event):
    e = event.widget;
    iid = e.identify("item",event.x,event.y)
    state = e.item(iid,"text")
    city  = e.item(iid,"values")[0]
    str = "{0}:{1}".format(state,city)
    messagebox.showinfo(title='提示', message=str)

def removeItem():
    lids = tree.selection()
    for lid in lids:
        tree.delete(lid)

def insertItem():
    state = stateEntry.get()
    city = cityEntry.get()
    if(len(state.strip())==0 or len(city.strip())==0):
        messagebox.showinfo(title='提示', message='请输入')

    tree.insert("",END,text=state,values=(city))
    stateEntry.delete(0,END)
    cityEntry.delete(0,END)


asia = {"中国":"北京","日本":"东京","泰国":"曼谷","韩国":"首尔","英国":"伦敦","法国":"巴黎","德国":"柏林","挪威":"奥斯陆","英国1":"伦敦1","法国1":"巴黎","德国1":"柏林","挪威1":"奥斯陆"}
euro = {"英国":"伦敦","法国":"巴黎","德国":"柏林","挪威":"奥斯陆"}

# fruits = {"Banana","Watermelon","Pineapple","Orange","Grapes","Mango"}

window = Tk()
window.title("ch_3")
window.rowconfigure(1,weight=1)
window.columnconfigure(0,weight=1)

# window.geometry("300x180")

stateLab = Label(window,text="State:")
stateLab.grid(row=0,column=0,padx=5,pady=3,sticky=W)
stateEntry = Entry()
stateEntry.grid(row=0,column=1,padx=5,pady=3,sticky=W+E)
cityLab = Label(window,text="City:")
cityLab.grid(row=0,column=2,padx=5,pady=3,sticky=W)
cityEntry = Entry()
cityEntry.grid(row=0,column=3,padx=5,pady=3,sticky=W+E)

inBtn = Button(window,text="插入",command=insertItem)
inBtn.grid(row=0,column=4,padx=5,pady=3)

tree = Treeview(window,columns=("capital"),selectmode=EXTENDED)


tree.heading("#0",text="国家")
tree.heading("capital",text="首都")

# idAsia = tree.insert("",index=END,text="Asia")
# idEuro = tree.insert("",index=END,text="Euro")

for country in asia.keys():
    tree.insert("",index=END,text=country,values=asia[country])
# for country in euro.keys():
#     tree.insert(idEuro,index=END,text=country,values=euro[country])
tree.bind("<Double-1>",doubleClick)
tree.grid(row=1,column=0,columnspan=5,padx=5,sticky=W+E+N+S)

# ----vertical scrollbar------------
vbar = Scrollbar(window, orient=VERTICAL, command=tree.yview)
vbar.grid(row=1, column=5, sticky=NS)
tree.configure(yscrollcommand=vbar.set)


# var = StringVar()
# label = Label(window,textvariable=var,relief="groove" )
# label.pack(fill=BOTH,expand=True)

btn = Button(window,text="删除",command=removeItem)
btn.grid(row=2,column=2,columnspan=5,padx=3,sticky=W)

window.mainloop()


# def printInfo():
#     selection = ""
#     for i in checkboxes:
#         if checkboxes[i].get() == True:
#             selection = selection + sports[i] + "\t"
#     print(selection)
#
# window = Tk()
# window.title("ch_3")
# window.geometry("500x300")
# labFrame = LabelFrame(window,text="选择喜欢的运动")
# sports = {0:"美式足球",1:"棒球",2:"篮球",3:"网球"}
# checkboxes = {}
# for i in range(len(sports)):
#     checkboxes[i] = BooleanVar()
#     Checkbutton(labFrame,text=sports[i],variable=checkboxes[i]).grid(row=i+1,sticky=W)
# labFrame.pack(ipadx=5,ipady=5,pady=10)
# btn= Button(window,text="确定",width=10,command=printInfo)
# btn.pack()
# window.mainloop()
