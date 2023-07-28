import json
import time

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
            Data = json.dumps(context,sort_keys=True, indent=4, separators=(',', ':'))
            f.write(Data)
            f.close()

    def FileRead(self):
        with open(self.path,'r',encoding='utf-8') as f:
            Data = f.read()
            f.close()
        return Data

    def FileWrite(self,context):
    	with open(self.path,'w',encoding='utf-8') as f:
    		f.write(context)
    		f.close()

class system:
	def __init__(self,SofName = '') -> None:
		self.SofName = SofName
		return None

	def SysName(self) -> str:
		if self.SofName == '':
			return None
		else:
			SysNamePath =JsonFile("../../../cfg.json").Read()
			print(f'{SofName}查询系统名称:'+SysNamePath["SystemName"])
			return SysNamePath["SystemName"]

	def SysIntroduce(self) -> str:
		if self.SofName == '':
			return None
		else:
			SysNamePath =JsonFile("../../../cfg.json").Read()
			print(f'{SofName}查询系统简介:'+SysNamePath["Introduce"])
			return SysNamePath["Introduce"]

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
