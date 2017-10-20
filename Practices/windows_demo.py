#!/usr/local/python/bin/python
# coding=utf-8

import wx


def load(event):
	test_file = open(file_name.GetValue())
	contents.SetValue(test_file.read())
	test_file.close()


def save(event):
	test_file = open(file_name.GetValue(), 'w')
	temp_txt = contents.GetValue().encode('utf-8')
	test_file.write(temp_txt)
	test_file.close()

app = wx.App()
win = wx.Frame(None, title="Simple Editor", size=(410, 335))
bkg = wx.Panel(win)

load_button = wx.Button(bkg, label='Open')
load_button.Bind(wx.EVT_BUTTON, load)

save_button = wx.Button(bkg, label='Save')
save_button.Bind(wx.EVT_BUTTON, save)

file_name = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

h_box = wx.BoxSizer()
h_box.Add(file_name, proportion=1, flag=wx.EXPAND)
h_box.Add(load_button, proportion=0, flag=wx.LEFT, border=5)
h_box.Add(save_button, proportion=0, flag=wx.LEFT, border=5)

v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(h_box, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
v_box.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(v_box)
win.Show()

if __name__ == '__main__':
	app.MainLoop()
