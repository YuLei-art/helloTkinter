from tkinter import *

def calculate():
    result = eval(equ.get())
    equ.set(equ.get()+"=\n"+str(result))

def show(buttonString):
    content = equ.get()
    if content == "0":
        content = ""
    equ.set(content + buttonString)

def backspace():
    equ.set(str(equ.get()[:-1]))

def clear():
    equ.set("0")

window = Tk()
window.title("ch_3")
equ = StringVar()
equ.set("0")

label = Label(window,width=25,height=2,relief="raised",anchor=SE,textvariable=equ)
label.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

clearButton = Button(window,text="C",fg="blue",width=5,command=clear)
clearButton.grid(row=1,column=0)
Button(window,text="DEL",width=5,command = backspace).grid(row=1,column=1)
Button(window,text="%",width=5,command=lambda :show("%")).grid(row=1,column=2)
Button(window,text="/",width=5,command=lambda :show("/")).grid(row=1,column=3)

Button(window,text="7",width=5,command=lambda :show("7")).grid(row=2,column=0)
Button(window,text="8",width=5,command=lambda :show("8")).grid(row=2,column=1)
Button(window,text="9",width=5,command=lambda :show("9")).grid(row=2,column=2)
Button(window,text="*",width=5,command=lambda :show("*")).grid(row=2,column=3)

Button(window,text="4",width=5,command=lambda :show("4")).grid(row=3,column=0)
Button(window,text="5",width=5,command=lambda :show("5")).grid(row=3,column=1)
Button(window,text="6",width=5,command=lambda :show("6")).grid(row=3,column=2)
Button(window,text="-",width=5,command=lambda :show("-")).grid(row=3,column=3)

Button(window,text="1",width=5,command=lambda :show("1")).grid(row=4,column=0)
Button(window,text="2",width=5,command=lambda :show("2")).grid(row=4,column=1)
Button(window,text="3",width=5,command=lambda :show("3")).grid(row=4,column=2)
Button(window,text="+",width=5,command=lambda :show("+")).grid(row=4,column=3)

Button(window,text="0",width=12,command=lambda :show("0")).grid(row=5,column=0,columnspan=2)
Button(window,text=".",width=5,command=lambda :show(".")).grid(row=5,column=2)
Button(window,text="=",width=5,bg="yellow",command=calculate).grid(row=5,column=3)

window.mainloop()


