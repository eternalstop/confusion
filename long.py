#!/usr/local/python3/bin/python
# coding=utf-8
from aip import AipOcr
import wx
import os
import pandas as pd


# 百度ocr-python文档：https://cloud.baidu.com/doc/OCR/OCR-Python-SDK.html


class SiteLog(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='转换', size=(1280, 960))

        self.SelBtn = wx.Button(self, label='选择目录', pos=(1065, 5), size=(80, 25))
        self.SelBtn.Bind(wx.EVT_BUTTON, self.open_file)

        self.OkBtn = wx.Button(self, label='开始转换', pos=(1150, 5), size=(80, 25))
        self.OkBtn.Bind(wx.EVT_BUTTON, self.get_contents)

        self.FileName = wx.TextCtrl(self, pos=(5, 5), size=(1055, 25))
        self.FileContent = wx.TextCtrl(self, pos=(5, 35), size=(1250, 960), style=(wx.TE_MULTILINE))

    def open_file(self, event):
        wildcard = "xlsx files(*.xlsx)|*.xlsx|All files (*.*)|*.*"
        dialog = wx.FileDialog(None, 'select', os.getcwd(), '', wildcard, wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            path_name = "\\".join(dialog.GetPath().split('\\')[:-1])
            # print(path_name)
            self.FileName.SetValue(path_name)
            if os.path.isdir(path_name):
                self.FileContent.SetValue("目录下文件：\n" + "\n".join(os.listdir(path_name)))
            dialog.Destroy

    def get_contents(self, event):
        path_name = self.FileName.GetValue()
        try:
            if os.path.isdir(path_name):
                file_list = os.listdir(path_name)
                for one_file in file_list:
                    # xlsx to csv
                    # print(path_name + "\\" + one_file)
                    data_xls = pd.read_excel(path_name + "\\" + one_file, index_col=0)
                    csv_name = path_name + "\\" + one_file.split(".")[0] + ".csv"
                    # print(csv_name)
                    data_xls.to_csv(csv_name, encoding='utf-8')
                    # rename
                    new_name = one_file.split(".")[0][0:13] + ".csv"
                    os.renames(csv_name, path_name + "\\" + new_name)
            content = "转换后文件：\n" + "\n".join(os.listdir(path_name))
            self.FileContent.SetValue(content)
            # with open(self.FileName.GetValue(), 'rb') as fp:
            #     result = my_client.basicAccurate(fp.read(), options)
            # content = '\t'.join([i['words'] for i in result['words_result']])
            # self.FileContent.SetValue(content)
        except:
            content = "选择正确的目录"
            self.FileContent.SetValue(content)


if __name__ == '__main__':
    app = wx.App()
    SiteFrame = SiteLog()
    SiteFrame.Show()
    app.MainLoop()
