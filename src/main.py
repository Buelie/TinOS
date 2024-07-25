import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import os
import sys
import time
import json
import subprocess
import uuid
import socket

class Message:
    __text:str = 'NULL'
    __mode:str = 'info'
    __applyname:str = 'TinOS'
    def __init__(self,text:str = __text,applyname:str = __applyname,mode:str = __mode) -> None:
        self.text = text
        self.applyname = applyname
        self.mode = mode
        return None

    def send(self) -> int:
        try:
            if self.mode == 'i':
                print(f'[{self.applyname} | INFO] $ {self.text}')
                return 200
            elif self.mode == 'w':
                print(f'[{self.applyname} | WARNNING] $ {self.text}')
                return 200
            elif self.mode == 'e':
                print(f'[{self.applyname} | ERROR] $ {self.text}')
                return 200
            else:
                print(f'[TinOS | INFO] $ Error call from {self.applyname}')
                return 400
        except Exception as error:
            print(f'{Fore.RED}[TinOS | ERROR] $ {error}{Fore.WHITE}')
            return 400

class File:
    def __init__(self,filename:str = 'default.py') -> None:
        self.filename = filename
        return None

    def create(self,text:str = 'NULL',encoding:str = 'utf-8') -> int:
        try:
            if os.path.isfile(self.filename) == False:
                with open(self.filename,'w',encoding=encoding) as newfile:
                    newfile.write(text)
                    newfile.close()
                Message(f'The {self.filename} file was created successfully','TinOS','i').send()
                return 200
            else:
                Message(f'Failed to create {self.filename}','TinOS','e').send()
                return 400
        except Exception as error:
            Message(f'Failed to create {self.filename}','TinOS','e').send()

    def readall(self,encoding:str = 'utf-8') -> str:
        with open(self.filename,'r',encoding=encoding) as readfile:
            readtext = readfile.read()
            readfile.close()
        return str(readtext)

    def writefile(self,text:str = 'NULL'):
        with open(self.filename,'w',encoding='utf-8') as writefile:
            writetext = writefile.write(text)
            writefile.close()
        return writetext

class Folder:
    def __init__(self,foldername:str = '') -> None:
        self.foldername = foldername
        return None

    def create(self) -> int:
        try:
            if os.path.isdir(self.foldername) == False:
                os.makedirs(self.foldername)
                Message(f'The {self.foldername} was created successfully','TinOS','i').send()
                return 200
            else:
                Message(f'Failed to create {self.foldername}','TinOS','e').send()
                return 400
        except Exception as error:
            Message(f'Failed to create {self.foldername}','TinOS','e').send()

class JsonFile:
    def __init__(self,path) -> None:
        self.path = path

    def Read(self):
        with open(self.path,'r',encoding='utf-8') as f:
            Data = json.load(f)
            f.close()
        return Data

    def ReadString(self):
        with open(self.path,'r',encoding='utf-8') as f:
            Data = json.loads(f)
            f.close()
        return Data

    def WriteString(self,context):
        with open(self.path,'w',encoding='utf-8') as f:
            Data = json.dumps(f)
            f.close()
        return Data

    def Write(self,context):
        with open(self.path,'w',encoding='utf-8') as f:
            Data = json.dump(f)
            f.close()
        return Data

    def WriteD(self,context):
        with open(self.path, 'w') as write_f:
            write_f.write(json.dumps(context, indent=4, ensure_ascii=False))

class Internet:
    def __init__(self) -> None:
        return None

    def connected(self):
        try:
            # 创建一个用于 TCP 连接的 socket 对象
            socket.create_connection(("www.baidu.com", 80))
            return True
        except OSError:
            return False

class tk_window:
    def __init__(self) -> None:
        return None

    def raise_above_all(self,window):
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)

if Internet().connected() == True:
    Message(f'The system is connected to the internet.The current connection status is {Internet().connected()}',f'TinOS','i').send()
else:
    pass

tinos_version = '0.1.6-Alpha-3'

# 系统文件夹
Folder(f'DISK').create()
Folder(f'DISK/C').create()
Folder(f'DISK/D').create()
Folder(f'DISK/C/Apply').create()
Folder(f'DISK/C/.Appdata').create()
Folder(f'DISK/C/Users').create()
Folder(f'DISK/C/Users/Images').create()
Folder(f'DISK/C/.System').create()
Folder(f'DISK/D/Default').create()
Folder(f'DISK/D/System').create()
Folder(f'DISK/D/Download').create()
Folder(f'DISK/D/Language').create()
Folder(f'DISK/D/System/Apply').create()
Folder(f'DISK/D/Language/Chinese').create()

# 系统文件
File(f'DISK/C/.System/cy_system.txt').create(f'TinOS {tinos_version}')
File(f'DISK/C/.System/cy_system_apply.txt').create(f'DISK/D/System/Apply')
File(f'DISK/C/.System/cy_system_users.txt').create(f'NULL')
File(f'DISK/C/.System/cy_login_user.txt').create(f'NULL')
File(f'DISK/C/.System/cy_system_config.txt').create(f'Alpha')
File(f'DISK/C/.System/cy_system_version.txt').create(f'{tinos_version}')
File(f'DISK/C/.System/cy_system_background.txt').create(f'bg.png')
File(f'DISK/C/.System/cy_system_root.password').create(f'{uuid.uuid4()}')
File(f'DISK/C/Users/cy_root_users.password').create(f'{uuid.uuid4()}')
File(f'DISK/C/Users/cy_id.uuid').create(f'{uuid.uuid4()}')

# 多国语言支持
File(f'DISK/D/Language/Config.txt').create(f'Chinese')
File(f'DISK/D/Language/Chinese/Start.txt').create(f'开始')
File(f'DISK/D/Language/Chinese/TaskManager.txt').create(f'任务管理器')
File(f'DISK/D/Language/Chinese/FileExplorer.txt').create(f'文件资源管理器')

main = tk.Tk()

def oobe():
    oobe = tk.Toplevel()
    oobe.geometry("600x450+374+182")
    oobe.title("系统 设置/安装 向导")
    oobe.transient(main)
    tk_window().raise_above_all(oobe)

    Lable_1 = ttk.Label(oobe,text="用户名：").grid(row=0,column=0)
    Lable_2 = ttk.Label(oobe,text="密码：").grid(row=1,column=0)
    Lable_3 = ttk.Label(oobe,text="更新通道：").grid(row=2,column=0)

    Entr_1 = ttk.Entry(oobe)
    Entr_2 = ttk.Entry(oobe)
    Entr_3 = ttk.Entry(oobe)

    def login(username:str ,password:str ,update:str) -> None:
        JsonFile(f'DISK/C/.System/cy_system_users.txt').WriteD(f'{username}')
        Folder(f'DISK/C/Users/{username}').create()
        Folder(f'DISK/C/Users/{username}/.Date').create()
        File(f'DISK/C/Users/{username}/.Date/password.txt').create(f'{password}')
        File(f'DISK/C/Users/{username}/.Date/update.txt').create(f'{update}')
        return None

    def mesg():
        if Entr_1.get() == '':
            oobe.withdraw()
            msg = tkinter.messagebox.showerror(title="错误",message="用户名不能为空！")
            oobe.lift()
            oobe.focus_force()
            if msg == True:
                oobe.deiconify()
            else:
                oobe.deiconify()
        elif Entr_2.get() == '':
            oobe.withdraw()
            msg = tkinter.messagebox.showerror(title="错误",message="密码不能为空！")
            oobe.lift()
            oobe.focus_force()
            if msg == True:
                oobe.deiconify()
            else:
                oobe.deiconify()
        elif Entr_3.get() == '':
            oobe.withdraw()
            msg = tkinter.messagebox.showerror(title="错误",message="更新通道(Default,Beta,TinDOS任选一个)不能为空！")
            oobe.lift()
            oobe.focus_force()
            if msg == True:
                oobe.deiconify()
            else:
                oobe.deiconify()
        elif Entr_3.get() not in ["Default","Beta","Alpha","TinOS"]: #or Entr_3.get() != "Beta" or Entr_3.get() != "TinDOS":
            oobe.withdraw()
            msg = tkinter.messagebox.showerror(title="错误",message="不是有效的更新通道!")
            oobe.lift()
            oobe.focus_force()
            if msg == True:
                oobe.deiconify()
            else:
                oobe.deiconify()
        else:
            oobe.withdraw()
            msg = tkinter.messagebox.showinfo(title="提示",message="很快就好了\n你知道吗,TinOS的逻辑有部分是参考MayDOS的哦")
            oobe.lift()
            oobe.focus_force()
            if msg == True:
                oobe.deiconify()
            else:
                oobe.deiconify()
            login(Entr_1.get(),Entr_2.get(),Entr_3.get())

    Entr_1.grid(row=0,column=1)
    Entr_2.grid(row=1,column=1)
    Entr_3.grid(row=2,column=1)

    Btn_1 = ttk.Button(oobe,text='确定',command=mesg).grid(row=3,column=1,columnspan=3)

def sign():
    sign = tk.Toplevel()
    sign.geometry("600x450+374+182")
    sign.title("用户账户登录")
    sign.transient(main)
    tk_window().raise_above_all(sign)

    Lable_1 = ttk.Label(sign,text="用户名：")
    Lable_2 = ttk.Label(sign,text="密码：")
    Entr_1 = ttk.Entry(sign)
    Entr_2 = ttk.Entry(sign)

    def sign_c():
        if Entr_1.get() == File('DISK/C/.System/cy_system_users.txt').readall():
            if Entr_2.get() == File(f'DISK/C/Users/{Entr_1.get()}/.Date/password.txt').readall():
                sign.withdraw()
                msg = tkinter.messagebox.showinfo(title="登陆成功",message=f'欢迎回来，{File(f'DISK/C/.System/cy_system_users.txt').readall()}')
                File(f'DISK/C/.System/cy_login_user.txt').writefile(f'{Entr_1.get()}')
                sign.lift()
                sign.focus_force()
                if msg == True:
                    sign.deiconify()
                else:
                    sign.deiconify()
                sign.destroy()
            else:
                sign.withdraw()
                msg = tkinter.messagebox.showerror(title="登陆失败",message=f'{Entr_1.get()}用户账户的密码不正确！！！')
                sign.lift()
                sign.focus_force()
                if msg == True:
                    sign.deiconify()
                else:
                    sign.deiconify()
        else:
            sign.withdraw()
            msg = tkinter.messagebox.showerror(title="登陆失败",message="用户账户不存在!")
            sign.lift()
            sign.focus_force()
            if msg == True:
                sign.deiconify()
            else:
                sign.deiconify()

    Btn_1 = ttk.Button(sign,text='确定',command=sign_c).grid(row=3,column=1,columnspan=3)

    Lable_1.grid(row=0,column=0)
    Lable_2.grid(row=1,column=0)
    Entr_1.grid(row=0,column=1)
    Entr_2.grid(row=1,column=1)

#UsersName = File(f'').readall()
if File('DISK/C/.System/cy_system_users.txt').readall() == 'NULL':
    oobe()
else:
    sign()

ApplyID = tk.StringVar()

def start_menu():
    start_menu = tk.Toplevel()
    start_menu.geometry("600x450+374+182")
    start_menu.title(f"开始 - 当前登录用户:{File(f'DISK/C/.System/cy_login_user.txt').readall()}")
    tk_window().raise_above_all(start_menu)

    w = start_menu.winfo_screenwidth()
    h = start_menu.winfo_screenheight()

    tcl = ttk.Button(start_menu,text='TinOS Command Line',width=30).grid(row=1,column=0,columnspan=3,sticky=tk.W)

    def shut():
        os.system('shutdown -s -t 3')
    def dor():
        os.system('powercfg.exe /hibernate on')
        os.system('shutdown -h')

    Shuot = ttk.Button(start_menu,text='关机',command=shut).grid(row=0,column=0)
    Shuot = ttk.Button(start_menu,text='休眠',command=dor).grid(row=0,column=1)

    ApplyVar = tk.StringVar()
    ApplyList = tk.StringVar()
    ApplyList = os.listdir(File(f'DISK/C/.System/cy_system_apply.txt').readall())
    ApplyTwo = tuple(ApplyList)
    AppList = ttk.Combobox(start_menu,textvariable=ApplyVar,value=ApplyTwo)

    def sofE():
        ApplyID = 7
        OS_Cmd = AppList.get()
        #exec(open(f'disk\\C\\apply\\{OS_Cmd}',encoding='utf-8').read())
        runexe = subprocess.Popen(['python', f'{File(f'DISK/C/.System/cy_system_apply.txt').readall()}/{OS_Cmd}'])
        runpid = runexe.pid
        print(runpid)
        btn = ttk.Button(main,text=f'{OS_Cmd[0:5]}').grid(row=0,column=ApplyID)
        ApplyID += 1
        main.update()

    AppList.grid(row=0,column=2)
    AppGetBtn = ttk.Button(start_menu,text="运行",command=sofE).grid(row=0,column=3)

def Setting():
    Setting = tk.Toplevel()
    Setting.geometry("600x450+374+182")
    Setting.title(f"设置 - 当前登录用户:{File(f'DISK/C/.System/cy_login_user.txt').readall()}")
    tk_window().raise_above_all(Setting)

    Lable_1 = ttk.Label(Setting,text="背景图片：")
    Lable_2 = ttk.Label(Setting,text="权限密码：")
    Entr_1 = ttk.Entry(Setting,width=62)
    Entr_2 = ttk.Entry(Setting,width=62)

    def image_back():
        path = Entr_1.get()
        File(f'DISK/C/.System/cy_system_background.txt').writefile(str(path))
        msg = tkinter.messagebox.showinfo(title="提示",message=f"更改完成\n重启系统以使用自定义背景\n路径：{Entr_1.get()}")
        Setting.lift()
        Setting.focus_force()
        if msg == True:
            Setting.deiconify()
        else:
            Setting.deiconify()

    def quanxian():
        pass

    Btn_1 = ttk.Button(Setting,text=f'更改',command=image_back)
    Btn_2 = ttk.Button(Setting,text=f'确定')

    Entr_1.insert(0,f'{File(f'DISK/C/.System/cy_system_background.txt').readall()}')

    Lable_1.grid(row=0,column=0)
    Lable_2.grid(row=1,column=0)
    Entr_1.grid(row=0,column=1,columnspan=3)
    Entr_2.grid(row=1,column=1,columnspan=3)
    Btn_1.grid(row=0,column=4)
    Btn_2.grid(row=1,column=4)

width = main.winfo_screenwidth()
height = main.winfo_screenheight()
BackgroundImage = tk.PhotoImage(file=File(f'DISK/C/.System/cy_system_background.txt').readall())

StartButton = ttk.Button(text=f'开始',command=start_menu)
SettingButton = ttk.Button(text=f'设置',command=Setting)
LoginButton = ttk.Button(text=f'注册',command=oobe)
SignButton = ttk.Button(text=f'登录',command=sign)
TaskManagerButton = ttk.Button(text=f'任务管理器')
FileExplorerButton = ttk.Button(text=f'文件资源管理器')
Background = tk.Label(main)

Background.config(image=BackgroundImage)
Background.grid(row=1,column=0,columnspan=height,rowspan=width,sticky=tk.W)
StartButton.grid(row=0,column=0)
SettingButton.grid(row=0,column=1)
LoginButton.grid(row=0,column=2)
SignButton.grid(row=0,column=3)
TaskManagerButton.grid(row=0,column=4)
FileExplorerButton.grid(row=0,column=5)

main.overrideredirect(True)
main.geometry("%dx%d" %(width, height))
main.mainloop()
