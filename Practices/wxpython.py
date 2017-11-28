#!/usr/local/python/bin/python
# coding=utf-8

import wx


def load(event):
	contents.SetValue('test %s' % quary_id.GetValue())


app = wx.App()
win = wx.Frame(None, title="英雄查询", size=(900, 700))
bkg = wx.Panel(win)

load_button = wx.Button(bkg, label='查询')
load_button.Bind(wx.EVT_BUTTON, load)

quary_id = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

h_box = wx.BoxSizer()
h_box.Add(quary_id, proportion=1, flag=wx.EXPAND)
h_box.Add(load_button, proportion=0, flag=wx.LEFT, border=5)
v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(h_box, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
v_box.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(v_box)
win.Show()

if __name__ == '__main__':
	app.MainLoop()
