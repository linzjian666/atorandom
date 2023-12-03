# -*- coding: UTF-8 -*-
'''
Author: Linzjian666
Date: 2023-11-18 11:45:14
LastEditors: Linzjian666
LastEditTime: 2023-12-03 11:04:36
'''

from tkinter import *
from tkinter import messagebox
import random

def 获取小数位数(number):
    # 将输入数字转换为字符串并按小数点分割
    decimal_str = str(number).split('.')
    # 判断是否有小数部分并返回小数位数
    if len(decimal_str) == 2 and len(decimal_str[1]) != 0:
        return len(decimal_str[1])
    else:
        return 0

def 生成随机数():
    before = before_var.get()
    after = after_var.get()
    filter_str = filter_var.get()
    # exclude = 获取排除数()
    try:
        # 检查起始数是否大于终止数
        if float(before) > float(after):
            messagebox.showerror("错误", "起始数应小于终止数!")
            return
        # 判断是否包含小数部分
        if 获取小数位数(before) == 0 and 获取小数位数(after) == 0:
            # 不包含，整数模式生成
            random_num = random.randint(int(before), int(after))
        else:
            # 包含，小数模式生成
            decimal_places = max(获取小数位数(before), 获取小数位数(after))
            before = float(before) * 10 ** decimal_places
            after = float(after) * 10 ** decimal_places
            random_num = random.randint(int(before), int(after))
            random_num /= 10 ** decimal_places
        # 将要排除的数字转换为列表
        filter_list = [float(exclude) for exclude in filter_str.split(',') if exclude.strip()]
        # 检查生成的随机数是否在排除列表中，如果是，则重新生成
        while random_num in filter_list:
            random_num = random.randint(int(before), int(after))
            if 获取小数位数(before) > 0 or 获取小数位数(after) > 0:
                random_num /= 10 ** decimal_places
        # 显示生成结果
        print(random_num)
        # result['text'] = str(random_num)
        result.config(state=NORMAL)
        result.delete(0, END)
        result.insert(0, str(random_num))
        result.config(state=DISABLED)
    
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数据!")

def 大输入框(title,var):
    messagebox.showinfo("功能暂未开放", "此功能仍在开发中,敬请期待!")

if __name__ == '__main__':
    # 创建主窗口
    window = Tk()
    window.geometry("400x400")
    window.configure(background="#ffffff")
    window.title("随机数生成器")
    window.resizable(width=False, height=False)

    # 标题
    lable = Label(window, bg="#ffffff", fg="#000000", text="欢迎使用随机数生成器", font=("Helvetica", 15, "bold"), pady=10)
    lable.place(x=90, y=0)

    # 范围起始数输入框
    before_lable = Label(window, bg="#ffffff", text="输入范围起始数:", bd=6,
                   font=("Helvetica", 13, "bold"), pady=5)
    before_lable.place(x=55, y=60)
    before_var = StringVar()
    before_entry = Entry(window, bd=8, width=10, font="Roboto 11", textvariable=before_var)
    before_entry.place(x=240, y=60)
    before_button = Button(window, text="...", command=lambda: 大输入框("输入范围起始数",before_var))
    before_button.place(x=330, y=60)

    # 范围终止数输入框
    after_lable = Label(window, bg="#ffffff", text="输入范围终止数:", bd=6,
                   font=("Helvetica", 13, "bold"), pady=5)
    after_lable.place(x=55, y=105)
    after_var = StringVar()
    after_entry = Entry(window, bd=8, width=10, font="Roboto 11", textvariable=after_var)
    after_entry.place(x=240, y=105)
    after_button = Button(window, text="...", command=lambda: 大输入框("输入范围终止数",after_var))
    after_button.place(x=330, y=105)

    #范围排除数输入框，多个排除数以英文逗号分隔
    filter_lable = Label(window, bg="#ffffff", text="输入排除数:", bd=6,
                    font=("Helvetica", 13, "bold"), pady=5)
    filter_lable.place(x=55, y=150)
    filter_var = StringVar()
    filter_entry = Entry(window, bd=8, width=10, font="Roboto 11", textvariable=filter_var)
    filter_entry.place(x=240, y=150)

    # 生成结果框
    result_lable = Label(window, bg="#ffffff", text="生成结果:", bd=6,
                   font=("Helvetica", 15, "bold"), pady=5)
    result_lable.place(x=55, y=200)
    result = Entry(window, bd=10, width=10, font=("Roboto 11", 12, "bold"), state=DISABLED)
    # result = Label(window, relief=SUNKEN, bg="#ffffff", text="", bd=8, width=10,
    #                 font=("Roboto 11", 12, "bold"), pady=5, anchor="w")
    result.place(x=240, y=200)

    # 生成按钮
    button = Button(bg="#000000", fg='#ffffff', bd=12, text="生成", padx=33, pady=10, command=生成随机数,
                    font=("Helvetica", 20, "bold"))
    button.grid(row=5, column=0, sticky=W)
    button.place(x=115, y=265)



    window.mainloop()
