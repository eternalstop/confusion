#!/usr/local/python3/bin/python
# coding=utf-8
from aip import AipOcr
import wx
import os

# 百度ocr-python文档：https://cloud.baidu.com/doc/OCR/OCR-Python-SDK.html


class SiteLog(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='图文转换', size=(1280, 960))

        self.SelBtn = wx.Button(self, label='选择文件', pos=(1065, 5), size=(80, 25))
        self.SelBtn.Bind(wx.EVT_BUTTON, self.open_file)

        self.OkBtn = wx.Button(self, label='开始转换', pos=(1150, 5), size=(80, 25))
        self.OkBtn.Bind(wx.EVT_BUTTON, self.get_contents)

        self.FileName = wx.TextCtrl(self, pos=(5, 5), size=(1055, 25))
        self.FileContent = wx.TextCtrl(self, pos=(5, 35), size=(1250, 960), style=(wx.TE_MULTILINE))

    def open_file(self, event):
        wildcard = "PNG files(*.png)|*.png|All files (*.*)|*.*"
        dialog = wx.FileDialog(None, 'select', os.getcwd(), '', wildcard, wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.FileName.SetValue(dialog.GetPath())
            dialog.Destroy

    def get_contents(self, event):
        APP_ID = '11678143'
        API_KEY = 'HdFOqrkZGddbKAshqprIyGgp'
        SECRET_KEY = '5l5WuwO18xwzvhGTdh26HCDNaXIXShI3'
        my_client = AipOcr(appId=APP_ID, apiKey=API_KEY, secretKey=SECRET_KEY)
        options = {"detect_direction": "true", "probability": "false"}
        try:
            with open(self.FileName.GetValue(), 'rb') as fp:
                result = my_client.basicAccurate(fp.read(), options)
            content = '\t'.join([i['words'] for i in result['words_result']])
            self.FileContent.SetValue(content)
        except:
            content = "该文件无法解析，请确认是否为图片文件（png、jpg）！"
            self.FileContent.SetValue(content)


if __name__ == '__main__':
    app = wx.App()
    SiteFrame = SiteLog()
    SiteFrame.Show()
    app.MainLoop()

