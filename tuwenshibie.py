#!usr/bin/python
#_*_ coding:utf-8 _*_
from aip import AipOcr
import easygui
import tkFileDialog
import os
import sys

#API使用参考地址：https://ai.baidu.com/docs#/OCR-Python-SDK/top

APP_ID = '14349685'
API_KEY = 'nuvTxjy3xyQcEI1G6GEuWmrg'
SECRET_KEY = 'SMQUd4tnUrRFE7RttNhWb5W7heYLtBId'

client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
#读取文件路径
def get_localfile_path():
    default_dir=r"/Users/gomo2016/Desktop"  #设置默认打开目录
    fname=tkFileDialog.askopenfilename(title=u"选择文件",initialdir=(os.path.expanduser((default_dir))))
    print(fname) #返回全文件路径
    #print(tkinter.filedialog.askdirectory())    #返回目录全路径
    return fname

#读取图片
def get_localfile_content(filepath):
    with open(filepath,'rb') as fp:
        return fp.read()
def get_local_text():
    try:
        image = get_localfile_content(get_localfile_path())
        print("文本识别中，请稍等...")
        #调用通用文字识别，图片参数为本地图片，把图像识别到的文字存储在一个字典里
        #不带可选参数格式
        #message = client.basicGeneral(image)

        #如果有可选参数
        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "true"

        message1 = client.basicGeneral(image,options)
        #print(message1)
        #从字典中只取出文字
        f = open('f.txt','wb')
        message1.get('words_result')
        for wd in message1.get('words_result'):
            #print(wd.get('words'))
            f.write(wd.get('words').encode('utf-8')+b'\n')
        f.close()
        d = open('f.txt','rb').read()
        #print(d.decode('utf-8'))
        print("识别成功！...")
        easygui.msgbox(d.decode('utf-8'))
    except Exception as e:
        print("发生错误："+str(e))



#调用通用文字识别，图片参数为远程url，把图像识别到的文字存储在一个字典里
def get_url_text():
    try:
        #url = "http://ubmcmm.baidustatic.com/media/v1/0f0005rkScKuZ2caKpTjDs.jpg"
        url = sys.argv[1]
        # 如果有可选参数
        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "true"

        message2 = client.basicGeneralUrl(url,options)
        #print(message2)
        message2.get('words_result')
        print('\n'+'\033[1;35m --------------这里是分割线---------- \033[0m'+'\n')
        print("识别到以下文字：")
        for wd in message2.get('words_result'):
            print(wd.get('words'))
    except Exception as e:
        print("未识别到文字！"+str(e))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        get_url_text()
    else:
        get_local_text()
