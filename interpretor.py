import tkinter as tk
import requests
import json

def fy(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

    from_date = {
        'type': 'AUTO',
        'i': word,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'ue': 'UTF-8',
        'action': 'FY_BY_CLICKBUTTON',
        'typoResult': 'true'
    }

    res = requests.post(url, data=from_date)
    if res.status_code == 200:
        return res.text
    else:
        return None

def translate():
    word = wo.get()
    response = fy(word)
    result = json.loads(response)
    r.set(result['translateResult'][0][0]['tgt'])



if __name__ == "__main__":
    w = tk.Tk()
    w.title("translator by Jasonker")
    w['width'] = 500;
    w['height'] = 150

    wo = tk.StringVar()

    l1 = tk.Label(w, text='翻译文字:', width=15)
    l1.place(x=1, y=10)
    e1 = tk.Entry(w, width=40, textvariable=wo)
    e1.place(x=110, y=10)

    r = tk.StringVar()

    l2 = tk.Label(w, text='翻译结果:', width=15)
    l2.place(x=1, y=50)
    e2 = tk.Entry(w, width=40, textvariable=r)
    e2.place(x=110, y=50)

    btn1 = tk.Button(w, width=20, text="翻译", command=translate)
    btn1.place(x=150, y=100)

    w.mainloop()
