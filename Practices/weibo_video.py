#!/usr/local/python/bin/python
# coding=utf-8
"""
下载给定微博视频页面的短视频。
"""
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import wx


def get_url(event):
    eme_dir = {}
    # head = {
    #     'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) '
    #                   'AppleWebKit/535.19 (KHTML, like Gecko) '
    #                   'Chrome/63.0.3239.84  '
    #                   'Safari/535.19'}
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.84 Safari/537.36',
        'Cookie': 'SINAGLOBAL=5509313659804.092.1509697025382; UOR=mdba.cn,widget.weibo.com,login.sina.com.cn; login_sid_t=b6f151e63308684a4b9baedc6cd6327b; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; YF-V5-G0=46bd339a785d24c3e8d7cfb275d14258; _s_tentry=-; Apache=3883694632513.3237.1513042638971; ULV=1513042638982:11:8:2:3883694632513.3237.1513042638971:1512970437951; cross_origin_proto=SSL; YF-Page-G0=d30fd7265234f674761ebc75febc3a9f; WBtopGlobal_register_version=49306022eb5a5f0b; WBStorage=81fd372985034324|undefined; wb_cusLike_2947521064=N; SCF=Ap5e3jhqTVJ8XF3Y3nsQP6DhO49CFhrf5zGPC1lV6eYrIbJzswQYO6GUMosJa-3suwnuQadIvYaKbjKNk3ykcqk.; SUB=_2A253KwfeDeRhGeRH71UU8i_MzTiIHXVUQX4WrDV8PUNbmtBeLVejkW9NTcxSbQMoXBJ-_jymVy66qUGZyyGaGOM_; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhkGPUrzyPaec5jEZWJ4Vow5JpX5KzhUgL.Foz4ShMfeo27SoB2dJLoI79C9gfLK27t; SUHB=0BLYcxMgSWCNGq; ALF=1544596238; SSOLoginState=1513060238'
    }
    req = request.Request(video_url.GetValue(), headers=head)
    response = request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    soup_text = soup.find('div', class_='weibo_player_fa', id='playerRoom')('div')[0]

    for eme in soup_text.attrs['action-data'].split('&'):
        if ("video_src" in eme) | ("cover_img" in eme):
            eme_dir[eme.split('=', 1)[0]] = "http:" + parse.unquote(eme.split('=', 1)[1])

    contents.SetValue(eme_dir['video_src'])


app = wx.App()
win = wx.Frame(None, title="新浪微博短视频下载", size=(1200, 300))
bkg = wx.Panel(win)

video_url = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
check_button = wx.Button(bkg, label='解析视频url')
check_button.Bind(wx.EVT_BUTTON, get_url)

h_box = wx.BoxSizer()
h_box.Add(video_url, proportion=1, flag=wx.EXPAND)
h_box.Add(check_button, proportion=0, flag=wx.LEFT, border=5)
v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(h_box, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
v_box.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(v_box)
win.Show()


if __name__ == '__main__':
    app.MainLoop()
