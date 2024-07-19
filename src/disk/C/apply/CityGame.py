import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import os
import json
import webbrowser
import requests
import wget
import time
import sys
import random

if os.path.isdir('config/cfg') == False:
    os.makedirs('config/cfg')
if os.path.isdir('config/game') == False:
    os.makedirs('config/game')
if os.path.isdir('config/game/date') == False:
    os.makedirs('config/game/date')
if os.path.isdir('config/game/user') == False:
    os.makedirs('config/game/user')
if os.path.isfile('config/cfg/cfg.json') == False:
    Test = {"language":"zh-cn","quality":"0","FPS":"30"}
    with open('config/cfg/cfg.json','w') as f:
        fe = json.dumps(Test,sort_keys=True, indent=4, separators=(',', ':'))
        f.write(fe)
        f.close()
if os.path.isfile('config/game/date/money.txt') == False:
    with open('config/game/date/money.txt','w') as f:
        f.write("350")
        f.close()
if os.path.isfile('config/game/date/favorability.txt') == False:
    with open('config/game/date/favorability.txt','w') as f:
        f.write("20")
        f.close()
if os.path.isfile('config/game/date/happiness.txt') == False:
    with open('config/game/date/happiness.txt','w') as f:
        f.write("30")
        f.close()
if os.path.isfile('config/game/date/employment.txt') == False:
    with open('config/game/date/employment.txt','w') as f:
        f.write("15")
        f.close()
if os.path.isfile('config/game/date/school_attendance.txt') == False:
    with open('config/game/date/school_attendance.txt','w') as f:
        f.write("15")
        f.close()
if os.path.isfile('config/game/date/jobless_rate.txt') == False:
    with open('config/game/date/jobless_rate.txt','w') as f:
        f.write("5")
        f.close()
if os.path.isfile('config/game/date/electricity.txt') == False:
    with open('config/game/date/electricity.txt','w') as f:
        f.write("0")
        f.close()
if os.path.isfile('config/game/date/water.txt') == False:
    with open('config/game/date/water.txt','w') as f:
        f.write("0")
        f.close()
if os.path.isfile('config/game/date/highway.txt') == False:
    with open('config/game/date/highway.txt','w') as f:
        f.write("0")
        f.close()
if os.path.isfile('config/game/date/dipi.txt') == False:
    with open('config/game/date/dipi.txt','w') as f:
        f.write("450")
        f.close()

tkinter.messagebox.showinfo(title="市长CUI模拟器",message="由 清澈之云工作室©2023 出品\n未经许可，不得盗用，版权所有，侵权必究\n游戏分级:8+游戏")
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
            Data = json.dumps(context)
            f.write(Data)
            f.close()
        return Data

    def FileRead(self):
        with open(self.path,'r',encoding='utf-8') as f:
            Data = f.read()
            f.close()
        return Data

    def FileWrite(self,context):
    	with open(self.path,'w',encoding='utf-8') as f:
    		f.write(context)
    		f.close()

rate = 50
enco = 0
dipi = 450

root = tk.Tk()
FrameText = tk.Frame(root).grid()
money = tk.Label(FrameText,text=f'城市资金:￥{JsonFile("config/game/date/money.txt").FileRead()}',font=('楷体',16))
favorability = tk.Label(FrameText,text=f'市民好感度:{JsonFile("config/game/date/favorability.txt").FileRead()}',font=('楷体',16))
happiness = tk.Label(FrameText,text=f'市民幸福度:{JsonFile("config/game/date/happiness.txt").FileRead()}',font=('楷体',16))

employment = tk.Label(FrameText,text=f'就业率:{JsonFile("config/game/date/employment.txt").FileRead()}%',font=('楷体',16))
school_attendance = tk.Label(FrameText,text=f'就学率:{JsonFile("config/game/date/school_attendance.txt").FileRead()}%',font=('楷体',16))
jobless_rate = tk.Label(FrameText,text=f'失业率:{JsonFile("config/game/date/jobless_rate.txt").FileRead()}%',font=('楷体',16))

electricity = tk.Label(FrameText,text=f'电力覆盖:{JsonFile("config/game/date/water.txt").FileRead()}%',font=('楷体',16))
water = tk.Label(FrameText,text=f'水资源覆盖:{JsonFile("config/game/date/water.txt").FileRead()}%',font=('楷体',16))

FrameGUI = tk.Frame(root).grid()

def Settings():

    SetTov = tk.Toplevel()
    SetTov.transient(root)
    SetTov.geometry("600x450+374+182")
    SetTov.title("设置")

    TitleLable_0 = tk.Label(SetTov,text='系统设置',font=('楷体',10)).grid(row=0,column=0)
    FPS = ttk.Checkbutton(SetTov,text="开启高帧率(开启60FPS)").grid(row=1,column=0)
    Label_0 = tk.Label(SetTov,text='画质:',font=('楷体',10)).grid(row=1,column=1)

    VerVarAir = tk.StringVar()
    VerVarList = tkinter.StringVar()
    VerVarAir.set('中')
    VerVarList = ('低','中','高')
    VerList = ttk.Combobox(SetTov,textvariable=VerVarAir,value=VerVarList).grid(row=1,column=2)

    QuitBtn = ttk.Button(SetTov,text='退出游戏',command=root.quit).grid(row=1,column=3)

def ConstructionDef():
    ConDef = tk.Toplevel()
    ConDef.transient(root)
    ConDef.geometry("600x450+374+182")
    ConDef.title("建设")

    label_A_0 = ttk.Label(ConDef,text=f'当前可建筑面积:{JsonFile("config/game/date/dipi.txt").FileRead()}㎡')

    def Road():
        __a0 = ["陆","露","花","蕾","芳","花","花","梅","竹","孙","中","山","石","东","西","南","北","大道","地","中山","神","漠","泊","湖","水","大","金","木","水","火","土","古","聚","龙","里","接","德","新","华"]
        __a1 = random.choice(__a0)
        __a2 = random.choice(__a0)
        __a01 = int(JsonFile("config/game/date/dipi.txt").FileRead())
        __a02 = int(JsonFile("config/game/date/money.txt").FileRead())
        __a05 = int(JsonFile("config/game/date/favorability.txt").FileRead())
        if __a02 > 20:
            tkinter.messagebox.showinfo(title="市长CUI模拟器",message="建造成功\n花费20万元修建了一条公路\n名称:"+__a1+__a2+"路")
            __a03 = __a02 - 20
            __a04 = __a01 - 80
            __a06 = __a05 + random.randint(1,15)
            JsonFile("config/game/date/money.txt").FileWrite(str(__a03))
            JsonFile("config/game/date/dipi.txt").FileWrite(str(__a04))
            JsonFile("config/game/date/favorability.txt").FileWrite(str(__a06))
            money.config(text=f'城市资金:￥{JsonFile("config/game/date/money.txt").FileRead()}')
            favorability.config(text=f'市民好感度:{JsonFile("config/game/date/favorability.txt").FileRead()}')
            label_A_0.config(text=f'当前可建筑面积:{JsonFile("config/game/date/dipi.txt").FileRead()}㎡')
        else:
            tkinter.messagebox.showerror(title="市长CUI模拟器",message="建造失败\n资金不足")

    def GetDipi():
        __a01 = random.randint(250,1500)
        __a02 = random.randint(150,25000)
        __a03 = int(JsonFile("config/game/date/dipi.txt").FileRead())
        dipi = __a02
        __a03 += dipi
        __a04 = int(JsonFile("config/game/date/money.txt").FileRead())

        if __a04 > dipi:
            tkinter.messagebox.showinfo(title="市长CUI模拟器",message="购买成功\n你以"+str(__a01)+"万元的价格购买了"+str(__a02)+"平米的地皮")
            JsonFile("config/game/date/dipi.txt").FileWrite(str(__a03))
            __a05 = __a04 - dipi
            JsonFile("config/game/date/money.txt").FileWrite(str(__a05))
            money.config(text=f'城市资金:￥{JsonFile("config/game/date/money.txt").FileRead()}')
        elif __a04 < dipi:
            tkinter.messagebox.showerror(title="市长CUI模拟器",message="购买失败\n资金不足，请拥有足够钱财后再购买!")
        else:
            pass
        label_A_0.config(text=f'当前可建筑面积:{JsonFile("config/game/date/dipi.txt").FileRead()}㎡')

    def School():
        __a1 = ["小学","中学","大学","师范"]
        __a0 = ["清","华","理工","陆","露","花","蕾","芳","花","花","梅","竹","孙","中","山","石","东","西","南","北","大道","地","中山","神","漠","泊","湖","水","大","金","木","水","火","土","古","聚","龙","里","接","德","新","华"]
        __a01 = random.randint(10,25)
        __a02 = random.randint(150,2500)
        __a03 = int(JsonFile("config/game/date/school_attendance.txt").FileRead()) #就学率
        __a04 = int(JsonFile("config/game/date/money.txt").FileRead()) #城市资金
        __a05 = int(JsonFile("config/game/date/dipi.txt").FileRead()) #当前可建筑面积
        __a06 = int(JsonFile("config/game/date/happiness.txt").FileRead()) #市民幸福度:
        __a07 = int(JsonFile("config/game/date/favorability.txt").FileRead()) #市民好感度

        if __a07 > 35 and __a04 > 145 and __a05 > 45:
            tkinter.messagebox.showinfo(title='市长CUI模拟器',message=f'建造成功\n学校名称:{random.choice(__a0)}{random.choice(__a0)}{random.choice(__a1)}')
            __a08 = __a03 + __a01 #就学率
            __a09 = __a04 - 145 #城市资金
            __a10 = __a05 - 45 #当前可建筑面积
            __a11 = __a06 + __a02 #市民幸福度:
            __a12 = __a07 + __a01 #市民好感度

            JsonFile("config/game/date/school_attendance.txt").FileWrite(str(__a08)) #就学率
            JsonFile("config/game/date/money.txt").FileWrite(str(__a09)) #城市资金 
            JsonFile("config/game/date/dipi.txt").FileWrite(str(__a10)) #当前可建筑面积
            JsonFile("config/game/date/happiness.txt").FileWrite(str(__a11)) #市民幸福度:
            JsonFile("config/game/date/favorability.txt").FileWrite(str(__a12)) #市民好感度

            money.config(text=f'城市资金:￥{JsonFile("config/game/date/money.txt").FileRead()}')
            school_attendance.config(text=f'就学率:{JsonFile("config/game/date/school_attendance.txt").FileRead()}%')
            label_A_0.config(text=f'当前可建筑面积:{JsonFile("config/game/date/dipi.txt").FileRead()}')
            happiness.config(text=f'市民幸福度:{JsonFile("config/game/date/happiness.txt").FileRead()}')
            favorability.config(text=f'市民好感度:{JsonFile("config/game/date/favorability.txt").FileRead()}')

        elif __a07 > 35 and __a04 > 145 and __a05 < 45:
            tkinter.messagebox.showwarning(title='市长CUI模拟器',message=f'建筑面积不足')
        elif __a07 > 35 and __a04 < 145 and __a05 < 45:
            tkinter.messagebox.showwarning(title='市长CUI模拟器',message=f'建筑面积及资金不足')
        elif __a07 < 35 and __a04 < 145 and __a05 < 45:
            tkinter.messagebox.showwarning(title='市长CUI模拟器',message=f'建筑面积、市民好感度及资金不足')
        else:
            tkinter.messagebox.showwarning(title='市长CUI模拟器',message=f'不满足条件:\n1.资金>145\n2.可建筑面积>35㎡\n3.市民好感度>35')

    label_A_0.grid(sticky='W')

    Btn_A_0 = ttk.Button(ConDef,text='建筑公路',command=Road).grid(row=1,sticky='W')
    Btn_A_1 = ttk.Button(ConDef,text='建筑学校',command=School).grid(row=2,sticky='W')
    Btn_A_2 = ttk.Button(ConDef,text='火车线路',command=Road).grid(row=3,sticky='W')
    Btn_A_3 = ttk.Button(ConDef,text='地铁线路',command=Road).grid(row=4,sticky='W')
    Btn_A_4 = ttk.Button(ConDef,text='公交线路',command=Road).grid(row=5,sticky='W')
    Btn_A_5 = ttk.Button(ConDef,text='轮船线路',command=Road).grid(row=6,sticky='W')
    Btn_A_6 = ttk.Button(ConDef,text='航空线路',command=Road).grid(row=7,sticky='W')
    Btn_A_7 = ttk.Button(ConDef,text='电网线路',command=Road).grid(row=8,sticky='W')
    Btn_A_8 = ttk.Button(ConDef,text='水源线路',command=Road).grid(row=9,sticky='W')
    Btn_B_0 = ttk.Button(ConDef,text='购买地皮',command=GetDipi).grid(row=1,column=1)
    Btn_B_1 = ttk.Button(ConDef,text='收购企业',command=GetDipi).grid(row=2,column=1)
    Btn_B_2 = ttk.Button(ConDef,text='收购学校',command=GetDipi).grid(row=3,column=1)
    Btn_B_3 = ttk.Button(ConDef,text='城市政府',command=GetDipi).grid(row=4,column=1)
    Btn_B_4 = ttk.Button(ConDef,text='教育机构',command=GetDipi).grid(row=5,column=1)
    Btn_B_5 = ttk.Button(ConDef,text='民警机构',command=GetDipi).grid(row=6,column=1)
    Btn_B_6 = ttk.Button(ConDef,text='消防机构',command=GetDipi).grid(row=7,column=1)
    Btn_B_7 = ttk.Button(ConDef,text='卫生机构',command=GetDipi).grid(row=8,column=1)
    Btn_C_0 = ttk.Button(ConDef,text='建设医院',command=GetDipi).grid(row=1,column=2)
    Btn_C_1 = ttk.Button(ConDef,text='建太平间',command=GetDipi).grid(row=2,column=2)
    Btn_C_2 = ttk.Button(ConDef,text='建立社区',command=GetDipi).grid(row=3,column=2)

def EconomyDef():
    EcoDef = tk.Toplevel()
    EcoDef.transient(root)
    EcoDef.geometry("600x450+374+182")
    EcoDef.title("经济")

    Label_0 = ttk.Label(EcoDef,text=f'当前剩余经济:{JsonFile("config/game/date/money.txt").FileRead()}').grid(sticky='E')
    Label_1 = ttk.Label(EcoDef,text=f'税率:').grid(row=1,column=0,sticky='E')
    EcoScale = ttk.Scale(EcoDef)
    Label_2 = ttk.Label(EcoDef,text=f'{str(rate)}')
    def tax(*args):
        __a = EcoScale.get()
        __b = str(__a)
        __c = __b[3:5]
        try:
            rate = int(__c)
            Label_2.config(text=f'{str(rate)}%')
            __d = JsonFile("config/game/date/money.txt").FileRead()
            __e = int(__d) * int(__c )
            if __e >= 1000000:
                tkinter.messagebox.showinfo(title="市长CUI模拟器",message="已超出上限，无法继续调整")
            else:
                JsonFile("config/game/date/money.txt").FileWrite(str(__e))
            money = tk.Label(FrameText,text=f'城市资金:￥{JsonFile("config/game/date/money.txt").FileRead()}',font=('楷体',16)).grid(row=0,column=0,sticky='W')
        except Exception as e:
            tkinter.messagebox.showerror(title="市长CUI模拟器",message="税率不能为0!")

    EcoScale.bind('<ButtonRelease>',tax)
    EcoScale.grid(row=1,column=1,sticky='E')
    Label_2.grid(row=1,column=2,sticky='E')

favorability.grid(row=1,column=0,sticky='W')
money.grid(row=0,column=0,sticky='W')
happiness.grid(row=2,column=0,sticky='W')

employment.grid(row=3,column=0,sticky='W')
school_attendance.grid(row=4,column=0,sticky='W')
jobless_rate.grid(row=5,column=0,sticky='W')

electricity.grid(row=6,column=0,sticky='W')
water.grid(row=7,column=0,sticky='W')

SettingBtn = ttk.Button(FrameGUI,text='设置',command=Settings).grid(columnspan=1,sticky='W')
Construction = ttk.Button(FrameGUI,text='建设',command=ConstructionDef).grid(sticky='W',padx=(0,30))
Economy = ttk.Button(FrameGUI,text='经济',command=EconomyDef).grid(sticky='W',padx=(0,30))

root.overrideredirect(True)
white = root.winfo_screenwidth()
hight = root.winfo_screenheight()
root.geometry("%dx%d" %(white, hight))#root.geometry("600x450+374+182")
#root.transient()
root.wm_attributes('-topmost',1)
root.mainloop()