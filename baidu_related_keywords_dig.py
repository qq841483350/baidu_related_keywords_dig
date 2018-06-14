#coding:utf8
#百度相关搜索关键词挖掘GUI工具  开发者：李亚涛 wx:841483350
import requests,re,wx,threading,sys,time,os
from lxml import etree
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
headers={"Host":"www.baidu.com","User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}

def get_html(url):
    while True:
        try:
            html=requests.get(url).content
            return html
        except:
            pass
list=[]
def get_word(word):
    list1=[]
    x=word
    list.append(x)
    url='http://www.baidu.com/s?wd=%s'%x
    html=get_html(url)
    # print html
    soup=BeautifulSoup(html,'html.parser')
    data=soup.find_all("div",id="rs")
    if data:
        words=data[0].find_all('a')
        for word in words:
            word=word.text
            if word not in list:
                if '%s'%y in str(word):
                    print word
                    contents2.AppendText(word+'\n')

                    x=threading.Thread(target=get_word,args=(word,))
                    x.start()

                else:
                    continue
            else:
                continue



def get_fist_word(event):
    global y
    del list[:]  #清空列表
    contents2.Clear()  #清空内容
    word=contents0.GetValue()
    word=str(word).strip()
    y=contents1.GetValue()
    y=str(y).strip()
    get_word(word)



def write_word(event):
    name='word'
    data=contents2.GetValue()
    f=open('%s.txt'%name,'w')
    f.write(data)
    f.close()
    os.system('%s.txt'%name)

if __name__=="__main__":
    app = wx.App()
    win = wx.Frame(None,title = "关键词挖掘工具|开发者：李亚涛 wx:841483350（注意：请填入必须包含的关键词，比如:你想挖掘包含seo的关键词，就在第二个输入框填入seo）".decode('utf8'),size=(1200,1000))
    icon = wx.Icon('favicon.ico', wx.BITMAP_TYPE_ICO)   #绑定ico
    win.SetIcon(icon)
    win.Show()

    wx.StaticText(win,label="请输入一个关键词*：",pos=(105,10),size=(120,30))
    contents1 = wx.TextCtrl(win, pos = (230,5),size = (150,30), style = wx.TE_RICH)

    wx.StaticText(win,label="必须要包含的关键词*：",pos=(400,10),size=(150,30))
    contents0 = wx.TextCtrl(win, pos = (550,5),size = (200,30), style =wx.TE_RICH)

    contents2 = wx.TextCtrl(win, pos = (100,40),size = (800,600), style = wx.TE_MULTILINE | wx.TE_RICH)

    loadButton = wx.Button(win, label = '开始挖掘关键词'.decode('utf8'),pos = (780,5),size = (100,30))
    loadButton_daochu = wx.Button(win, label = '导出关键词并打开'.decode('utf8'),pos = (890,5),size = (150,30))

    loadButton_daochu.Bind(wx.EVT_BUTTON,write_word)  #这个按钮绑定 get_source 这个函数
    loadButton.Bind(wx.EVT_BUTTON,get_fist_word)  #这个按钮绑定 get_source 这个函
    app.MainLoop()
    # word="长沙二手房"
    # y=word
    # get_word(word)
