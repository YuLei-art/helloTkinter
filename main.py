# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys,tkinter

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 创建主窗口
    root = tkinter.Tk()
    root.title("title:HelloWorld")
    root.minsize(1000, 500)
    # 创建标签
    tkinter.Label(root, text="HelloWorld").pack()
    # 创建按钮并把命令绑定到退出
    tkinter.Button(root, text="Exit", command=sys.exit).pack()
    # 启动主循环
    root.mainloop()
    print_hi('in tkinter')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
