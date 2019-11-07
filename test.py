import tkinter as tk
import os
import requests
from bs4 import BeautifulSoup
from tkinter.filedialog import askdirectory

def selectPath():
    path_ = askdirectory()
    path.set(path_)

def check_null():
    #获取输入值
    save_path = path.get()
    img_path_a = img_path.get()
    #判断输入是否为空
    if save_path.strip() =="" or img_path_a.strip() == "":
        l3.config(text="输入框不能为空")
        return;
    #判断存储路径是否正确和存在
    elif not os.path.isdir(save_path) or not os.path.exists(save_path):
        l3.config(text="存储路径不正确")
        return;
    #判断网址格式是否输入正确
    # elif not os.path.isdir(save_path) or not os.path.exists(save_path):
    #     l3.config(text="the save_path is error")
    #     return;
    else:
        download_img(save_path, img_path_a);

def download_img(sv_path, wb_path):
    try:
        string = ""
        root = sv_path
        res = requests.get(wb_path)
        soup = BeautifulSoup(res.content, "lxml")
        for pa_web in soup.find_all('img'):
            if "https:" in pa_web.get("src") or "http:" in pa_web.get("src"):
                im_path = pa_web.get("src")
            else:
                im_path = wb_path + "/" + pa_web.get("src")
            # print(im_path)
            url = im_path    # 图片地址
            path = root + "/" + url.split("/")[-1]
            if not path.endswith(".jpg"):
                path += ".jpg"
            if not os.path.exists(root):  # 目录不存在创建目录
                os.mkdir(root)
            if not os.path.exists(path):  # 文件不存在则下载
                r = requests.get(url)
                r.raise_for_status
                f = open(path, "wb")
                f.write(r.content)
                f.close()
                string += im_path + "下载成功 \n"
                l3.config(text=string)
            else:
                string += im_path + "文件已经存在 \n"
                l3.config(text=string)
        string += r"下载完成"
        l3.config(text=string)
    except:
        l3.config(text="获取失败")


w = tk.Tk()
w.title("网页图片抓取工具")
w.geometry("500x500")
w.resizable(0,0)
path = tk.StringVar()

img_path = tk.StringVar()
l1 = tk.Label(w, text="图片网络路径:")
l1.grid(row=0, column=0)
e1 = tk.Entry(w, textvariable=img_path, width=34)
e1.grid(row=0, column=1, columnspan=2)

l2 = tk.Label(w, text="存储路径:")
l2.grid(row=1, column=0)
e2 = tk.Entry(w, textvariable=path).grid(row=1, column=1)
b1 = tk.Button(w, text="路径选择", command=selectPath).grid(row=1, column=2)

b2 = tk.Button(w, text="抓取", command=check_null, width=10).grid(row=2, column=1)


l3 = tk.Label(w, text="empty", width=55, height=20, bg="yellow")
l3.grid(row=3, columnspan=3)

w.mainloop()
