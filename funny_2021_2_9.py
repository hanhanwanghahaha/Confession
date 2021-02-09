# coding=utf-8

import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox


def accept():
    accept_root = tk.Toplevel(root)
    accept_root.title("哈哈好开心")
    accept_root.geometry("300x100")
    l4 = tk.Label(accept_root, text="小仙女，咱们谈恋爱吧！", font=("微软雅黑", 20),fg="red",bg="pink")
    l4.pack()
    button3 = tk.Button(accept_root, text="好的", font=("微软雅黑", 15),bg="pink",command=root.destroy)
    button3.pack()

def not_accept():
    not_accept_root = tk.Toplevel(root)
    not_accept_root.title("呜呜好难受")
    not_accept_root.geometry("300x100")
    l4 = tk.Label(not_accept_root, text="给我一次机会嘛嘤嘤嘤", font=("微软雅黑", 20))
    l4.pack()
    button3 = tk.Button(not_accept_root, text="好的", font=("微软雅黑", 15),bg="pink",command=not_accept_root.destroy)
    button3.pack()
    #要是点击不接受的x按钮，就继续调用此函数
    not_accept_root.protocol("WM_DELETE_WINDOW", not_accept)

def not_closing():
    messagebox.showerror(title="难受啊~",message="我保证听你话，再考虑考虑嘛呜呜呜QAQ~")


root = tk.Tk()
root.title("小姐姐，我喜欢你好久了熬！")
root.geometry("366x420+300+300")

l1 = tk.Label(root, text="hello,小姐姐，我想对你表白", font=("微软雅黑", 16), fg="red")
# E S W N 东南西北
l1.grid(row=0, column=0, sticky=tk.W)  # l1.grid()也是可以的，默认行和列为0，表示第一行第一列

l2 = tk.Label(root, text="自从第一次见你我就喜欢上了你！", font=("微软雅黑", 18))
l2.grid(row=1, column=0)  # 第二行第一列

# 上传图片
bgimg = ImageTk.PhotoImage(file='lovebaby.png')
l3 = tk.Label(root, image=bgimg)
l3.grid(row=2, columnspan=2)

root.protocol("WM_DELETE_WINDOW",not_closing)

button1 = tk.Button(root, text="接受", width=9, height=2, font=("微软雅黑", 16), bg="pink", command=accept)
button1.grid(row=3, column=0, sticky=tk.W)

button2 = tk.Button(root, text="不接受", width=5,command=not_accept)
button2.grid(row=3, column=0, sticky=tk.E)

root.mainloop()
