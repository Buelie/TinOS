import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import os
import json
import time
import sys

# 确认系统文件
app = 'disk/C/apply'
if os.path.isdir('disk/C') == False:
    os.makedirs('disk/C')

if os.path.isdir(app) == False:
    os.makedirs(app)

if os.path.isdir('disk/C/user') == False:
    os.makedirs('disk/C/user')

if os.path.isdir('disk/C/user/root') == False:
    os.makedirs('disk/C/user/root')

if os.path.isdir('disk/C/lang') == False:
    os.makedirs('disk/C/lang')

if os.path.isfile('disk/C/lang/lang.json') == False:
    with open('disk/C/lang/lang.json','w') as f:
        f.write("false")
        f.close()

if os.path.isfile('disk/C/user/cfg.txt') == False:
    with open('disk/C/user/cfg.txt','w') as f:
        f.write("false")
        f.close()

if os.path.isfile('disk/C/user/code.txt') == False:
    with open('disk/C/user/code.txt','w') as f:
        f.write("0")
        f.close()

# 打开JSON(语言)文件
with open("disk/C/lang/lang.json","r",encoding="utf-8") as file:
    # 加载JSON数据到Python对象
    lang_data = json.load(file)

INFO_RET = {}

class JsonFile:
    """
    读取/写入JSON文件的类
    Read方法是读写JSON文件
    Write方法是写入JSON文件
    """
    def __init__(self,path) -> None:
        self.path = path

    def Read(self):
        with open(self.path,'r',encoding='utf-8') as f:
            Data = json.load(f)
            f.close()
        return Data

    def Write(self,context):
        with open(self.path,'w',encoding='utf-8') as f:
            Data = json.dumps(f)
            f.close()
        return Data

    def FileRead(self):
        with open(self.path,'r',encoding='utf-8') as f:
            Data = f.read()
            f.close()
        return Data
    def FileWrite(self,context):
        with open(self.path,'r',encoding='utf-8') as f:
            f.write(context)
            f.close()
        return Data

root = tk.Tk()

def oobe():
	oobe = tk.Toplevel()
	oobe.geometry("600x450+374+182")
	oobe.title("系统 设置/安装 向导")
	oobe.transient(root)
	oobe.wm_attributes('-topmost',1)

	Lable_1 = ttk.Label(oobe,text=lang_data["zh_CN"]["1"]).grid(row=0,column=0)
	Lable_2 = ttk.Label(oobe,text=lang_data["zh_CN"]["2"]).grid(row=1,column=0)
	Lable_3 = ttk.Label(oobe,text=lang_data["zh_CN"]["3"]).grid(row=2,column=0)

	Entr_1 = ttk.Entry(oobe)
	Entr_2 = ttk.Entry(oobe)
	Entr_3 = ttk.Entry(oobe)

	def mesg():
		if Entr_1.get() == '':
			oobe.withdraw()
			msg = tkinter.messagebox.askquestion("错误", "用户名不能为空！")#showerror(title="错误",message="用户名不能为空！")
			oobe.lift()
			oobe.focus_force()
			if msg == True:
				oobe.deiconify()
			else:
				oobe.deiconify()
		elif Entr_2.get() == '':
			oobe.withdraw()
			msg = tkinter.messagebox.askquestion("错误", "密码不能为空！")#tkinter.messagebox.showerror(title="错误",message="密码不能为空！")
			oobe.lift()
			oobe.focus_force()
			if msg == True:
				oobe.deiconify()
			else:
				oobe.deiconify()
		elif Entr_3.get() == '':
			oobe.withdraw()
			msg = tkinter.messagebox.askquestion("错误", "更新通道(Default,Beta,TinDOS任选一个)不能为空！")#tkinter.messagebox.showerror(title="错误",message="更新通道(Default,Beta,TinDOS任选一个)不能为空！")
			oobe.lift()
			oobe.focus_force()
			if msg == True:
				oobe.deiconify()
			else:
				oobe.deiconify()
		elif Entr_3.get() != "Default" or Entr_3.get() != "Beta" or Entr_3.get() != "TinDOS":
			oobe.withdraw()
			msg = tkinter.messagebox.askquestion("错误", "不是有效的更新通道!")#tkinter.messagebox.showerror(title="错误",message="不是有效的更新通道!")
			oobe.lift()
			oobe.focus_force()
			if msg == True:
				oobe.deiconify()
			else:
				oobe.deiconify()
		else:
			tkinter.messagebox.showinfo(title="提示",message="很快就好了\n你知道吗,TinOS的逻辑有部分是参考MayDOS的哦")

	Entr_1.grid(row=0,column=1)
	Entr_2.grid(row=1,column=1)
	Entr_3.grid(row=2,column=1)

	Btn_1 = ttk.Button(oobe,text='确定',command=mesg).grid(row=3,column=0)

if JsonFile('disk/C/user/cfg.txt').FileRead() == 'false':
	oobe()

def sof_list():
	SofList = tk.Toplevel()
	SofList.geometry("600x450+374+182")
	SofList.title("开始")
	SofList.wm_attributes('-topmost',1)

	

	def shut():
		os.system('shutdown -s -t 3')
	def dor():
		os.system('shutdown -h')
		
	Shuot = ttk.Button(SofList,text='关机',command=shut).grid(row=0,column=0)
	Shuot = ttk.Button(SofList,text='休眠',command=dor).grid(row=0,column=1)

	AppVarAir = tk.StringVar()
	AppVarList = tk.StringVar()
	AppVarList = os.listdir(app)
	AppVarListTwo = tuple(AppVarList)
	AppList = ttk.Combobox(SofList,textvariable=AppVarAir,value=AppVarListTwo)

	def sofE():
		OS_Cmd = AppList.get()
		os.system(f'disk\\C\\apply\\{OS_Cmd}')

	AppList.grid(row=0,column=2)
	AppGetBtn = ttk.Button(SofList,text="运行",command=sofE).grid(row=0,column=3)

Background = tk.Label(root)
BG = tk.PhotoImage(file="img/bg.png")
Background.config(image=BG)
Background.pack(fill='both',expand=True)
Start = ttk.Button(root,text='开始',command=sof_list).pack(side='bottom',anchor='sw',before=Background)

root.overrideredirect(True)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("%dx%d" %(w, h))
#root.geometry("600x450+374+182")
root.mainloop()

"""
cfg.json
{
	"SystemName":"TinOS", //系统名称
	"Introduce":"一个基于py 图形库制作的操作系统", //系统简介
	"Version":["0.1.3","正式版"], //系统版本 [版本号,版本类型] (版本类型:正式版,测试版,阿尔法)
	"en_us":{ //英文配置
		"SystemName":"TinOS", //系统名称
		"Introduce":"An operating system based on the py graphics library", //系统简介
		"Version":["0.1.3","release"] //系统版本 [版本号,版本类型] (版本类型:release,beta,alpha)
	}
}
"""
