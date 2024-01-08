#!/usr/local/python/bin/python
# conding=utf-8
import random
import string
import wx


def password(event):
    if lenth.GetValue().isdigit():
        passwd_length = lenth.GetValue()
    else:
        passwd_length = 8
    try:
        passwd = ''.join(random.sample(
            string.digits + string.ascii_letters + string.punctuation,
            int(passwd_length)
        ))
        contents.SetValue(passwd)
    except:
        contents.SetValue('请输入正确的密码长度，最长94位。')


app = wx.App()
win = wx.Frame(None, title="随机密码", size=(700, 350))
bkg = wx.Panel(win)

lenth = wx.TextCtrl(bkg, value='请输入要生成的密码位数，默认8位，长度最长94位', style=wx.TE_CENTER)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
getButton = wx.Button(bkg, label='生成密码')
getButton.Bind(wx.EVT_BUTTON, password)

h_box = wx.BoxSizer()
h_box.Add(lenth, proportion=1, flag=wx.EXPAND)
h_box.Add(getButton, proportion=0, flag=wx.LEFT, border=5)
v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(h_box, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
v_box.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(v_box)
win.Show()

if __name__ == '__main__':
    app.MainLoop()
