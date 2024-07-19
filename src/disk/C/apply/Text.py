import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import *
import tkinter.colorchooser
import sys
import os

import json
class parse:
    __parse = None

    def __init__(self,path : str) -> None:
        self.path = path

    def json(self) -> str:
        try:
            with open(self.path, 'r') as f:
                __data = json.load(f)
            return __data
        except Exception as __e:
            print(__e)
            return __e
    
    def yaml(self):
        pass

    def xml(self):
        pass

app = tk.Tk()

textPad = ScrolledText(bg='white', height=10)
textPad.pack(fill=tk.BOTH, expand=1)
textPad.focus_set()

def no():
    answer = tk.messagebox.showinfo(title="提示",message="该功能还未开放哦！")

def yhxy():
    winNew = tk.Toplevel()
    winNew.geometry('600x450+374+182')
    winNew.title("用户协议")
    f = "The MIT License (MIT)\
\nCopyright (c) 2023  |  yydshmcl@outlook.com\
\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”),\n to deal in the Software without restriction, \nincluding without limitation the rights to use, \ncopy, modify, merge, publish, distribute, sublicense, \nand/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\
\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\
\nThe Software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability,\n fitness for a particular purpose and noninfringement. \nIn no event shall the authors or copyright \nholders be liable for any claim, damages or other liability, \nwhether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the Software."
    lable = tk.Label(winNew,text=f).pack()

def ConfigWind():
    winNew = tk.Toplevel()
    winNew.geometry('600x450+374+182')
    winNew.title('参数设置')
    def dbxm():
        def dbxm_file(path : str,main_file : str,mode : str,image : str) -> None:
            if image != None or image != "" or image != '':
                if mode == 'F':
                    os.system('cd '+path+'&& '+path[0:1]+'&&pyinstaller -F -w '+main_file+" -i "+image)
                elif mode == 'D':
                    os.system('cd '+path+'&& '+path[0:1]+'&&pyinstaller -w '+main_file+" -i "+image)
                else:
                    print(Exception)
            else:
                if mode == 'F':
                    os.system('cd '+path+'&& '+path[0:1]+'&&pyinstaller -F -w '+main_file)
                elif mode == 'D':
                    os.system('cd '+path+'&& '+path[0:1]+'&&pyinstaller -w '+main_file)
                else:
                    print(Exception)
            return None

        WinM = tk.Toplevel()
        WinM.geometry('600x450+374+182')
        WinM.title('打包项目')
        try:
            a = ""
            Vsa = tk.BooleanVar()
            PathLab = ttk.Label(WinM,text="项目路径:",width=10).grid(row=0,column=0)
            PathInp = ttk.Entry(WinM,width=40,textvariable=a).grid(row=0,column=1)

            b = ""
            MainLab = ttk.Label(WinM,text="主文件路径:",width=10).grid(row=1,column=0)
            MainInp = ttk.Entry(WinM,width=40,textvariable=b).grid(row=1,column=1)
            
            dxF = ttk.Radiobutton(WinM,text="打包单个文件",value="F").grid(row=2,column=0)
            dxD = ttk.Radiobutton(WinM,text="打包整个项目",value="D").grid(row=2,column=1)

            c = ""
            imags = ""
            ImageL = ttk.Label(WinM,text="图标路径:",textvariable=c,width=10).grid(row=4,column=0)
            Image = ttk.Entry(WinM,width=40,textvariable=c).grid(row=4,column=1)

            OK_Btn = ttk.Button(WinM,text="打包项目",command=lambda:dbxm_file(a,b,c)).grid(row=5,column=0)
        except Exception as e:
            WarLable = tk.Label(WinM,text="使用此功能，需要安装pyinstaller库!!!").grid(row=0,column=0)
            ErrLable = tk.Label(WinM,text=e).grid(row=0,column=0)
            print(e)

    hj_path = ""
    PathLab = ttk.Label(winNew,text=sys.path[5]+"\\python.exe",relief='solid').grid(row=0,column=1,columnspan=2)
    PathBtn = ttk.Button(winNew,text="更改解释器路径").grid(padx=0,row=0,column=0)
    DabaoBtn = ttk.Button(winNew,text="打包项目",command=dbxm).grid(padx=0,row=1,column=0)

def FileSetWind():
    winNew = tk.Toplevel()
    winNew.geometry('600x450+374+182')
    winNew.title('文件设置')

def NewFile():  #新文件
    textPad.delete(1.0,tk.END)

def GetFile(): #读取文件
    filename = askopenfilename(defaultextension='.py')
    if filename != '':
        textPad.delete(1.0,tk.END)#delete all
        f = open(filename,'r',encoding='utf-8',errors='ignore')
        textPad.insert(1.0,f.read())
        f.close()

def SaveFile(**kages): #另存文件
    filename = asksaveasfilename(initialfile = 'new',defaultextension ='.txt')
    if filename != '':
        fh = open(filename,'w',encoding='utf-8',errors='ignore')
        msg = textPad.get(1.0,tk.END)
        fh.write(msg)
        fh.close()

def EXEInfo():
    winNew = tk.Toplevel()
    winNew.geometry('600x450+374+182')
    winNew.title('软件信息')
    lb = tk.Label(winNew,text=f'软件版本 : {ver["ExeVer"]}',relief='solid').pack()
    lb2 = tk.Label(winNew,text=f'核心版本 : {ver["version"]}',relief='solid').pack()
    lb3 = tk.Label(winNew,text=f'当前主题 : {ver["topic"]}',relief='solid').pack()
    lb4 = tk.Label(winNew,text=f'贡献者 : {ver["contributors"]}',relief='solid').pack()
    lb5 = tk.Label(winNew,text=f'源码托管平台 : {ver["platform"]}',relief='solid').pack()

def showPopoutMenu(w, menu):
    def popout(event):
        menu.post(event.x + root.winfo_rootx(), event.y + root.winfo_rooty()) 
        root.update() 
    root.bind('<Button-3>', popout) 

#菜单栏
MenuBar = tk.Menu(app,relief='solid')

# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = tk.Menu(MenuBar, tearoff=False,relief='solid')
filemenu.add_command(label="打开", command=GetFile)
filemenu.add_command(label="保存", command=SaveFile)
filemenu.add_command(label="新建", command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="退出", command=app.quit)
MenuBar.add_cascade(label="文件", menu=filemenu)
 
# 创建另一个“编辑”下拉菜单，然后将它添加到顶级菜单中
EditMenu = tk.Menu(MenuBar, tearoff=False,relief='solid')
EditMenu.add_command(label="剪切", command=no)
EditMenu.add_command(label="拷贝", command=no)
EditMenu.add_command(label="粘贴", command=no)
MenuBar.add_cascade(label="编辑", menu=EditMenu)
 
# 创建另一个“设置”下拉菜单，然后将它添加到顶级菜单中
settingmenu = tk.Menu(MenuBar, tearoff=False,relief='solid')
settingmenu.add_command(label="参数设置", command=ConfigWind)
settingmenu.add_command(label="文件设置", command=FileSetWind)
MenuBar.add_cascade(label="设置", menu=settingmenu)

# 创建另一个“帮助”下拉菜单，然后将它添加到顶级菜单中
helptmenu = tk.Menu(MenuBar,tearoff=False,relief='solid')
helptmenu.add_command(label="关于我们", command=no)
helptmenu.add_command(label="获取帮助", command=no)
helptmenu.add_command(label="软件信息", command=EXEInfo)
helptmenu.add_command(label="用户协议",command=yhxy)
MenuBar.add_cascade(label="帮助", menu=helptmenu)

app.title("文本编辑器")
app.config(menu=MenuBar)
app.geometry("600x450+374+182")
app.lift()
app.focus_force()
app.mainloop()