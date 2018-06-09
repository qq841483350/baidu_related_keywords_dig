#coding:utf8
#百度相关搜索关键词挖掘GUI工具  开发者：李亚涛 wx:841483350
import requests,re,wx,threading
headers={"Host":"www.baidu.com","User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}

list=[]
def get_html2(word):
    keyword=word
    list.append(keyword)
    url='http://www.baidu.com/s?wd=%s'%word
    html=requests.get(url).content
    html=re.findall('<div id="rs">([\s\S]*?)<div id="page" >',html)[0]
    words=re.findall('<a href="[\s\S]*?">([\s\S]*?)</a>',html)
    for word in words:
        if word not in list:
            if '%s'%text1 in str(word):   #text1为 挖掘出的关键词必需要包含的关键词。
                print word.decode('utf8')
                contents2.AppendText(word+'\n')   #添加contents里的内容
                y=threading.Thread(target=get_html2,args=(word,))
                y.start()
                # get_html2(word)
            else:
                pass
        else:
            continue


def get_html1(event):
    global text1,text
    contents2.Clear()  #清空内容
    text1=contents0.GetValue()
    text1=''.join(text1.split()).encode('utf8')
    text=contents1.GetValue()  #获取contents1里的内容
    text=''.join(text.split()).encode('utf8')    #去除中间的空格与回车
    print text
    keyword=text
    list.append(keyword)
    get_html2(keyword)

if __name__=="__main__":
    app = wx.App()
    win = wx.Frame(None,title = "关键词挖掘工具|开发者：李亚涛 wx:841483350（注意：请填入必须包含的关键词，比如:你想挖掘包含seo的关键词，就在第二个输入框填入seo）".decode('utf8'),size=(1200,1000))

    win.Show()

    wx.StaticText(win,label="请输入一个关键词*：",pos=(105,10),size=(120,30))
    contents1 = wx.TextCtrl(win, pos = (230,5),size = (150,30), style = wx.TE_MULTILINE | wx.TE_RICH)

    wx.StaticText(win,label="必须要包含的关键词*：",pos=(400,10),size=(150,30))
    contents0 = wx.TextCtrl(win, pos = (550,5),size = (200,30), style = wx.TE_MULTILINE | wx.TE_RICH)

    contents2 = wx.TextCtrl(win, pos = (100,40),size = (800,600), style = wx.TE_MULTILINE | wx.TE_RICH)

    loadButton = wx.Button(win, label = '开始挖掘关键词'.decode('utf8'),pos = (780,5),size = (100,30))
    loadButton.Bind(wx.EVT_BUTTON,get_html1)  #这个按钮绑定 get_source 这个函数
    app.MainLoop()
    get_html1(text)
