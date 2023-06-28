# _*_ coding: utf-8 _*_
__author__ = 'ALi'

from getpass import getpass
from selenium import webdriver
import time
import datetime
import getpass


class XiaoMi():

    def __init__(self):
        self.name = "18655660717" #登陆小米商城用户名
        self.pwd = getpass.getpass() #登陆小米商城密码
        self.buytime = "2022-08-19 20:00:00" # 指定秒杀时间，并且开始等待秒杀
        self.browser = webdriver.Edge(executable_path="D:\Program Files\msedgedriver.exe")


    def login(self):
        self.browser.get( 'https://account.xiaomi.com/')#登录网址
        time.sleep(2)
        self.browser.find_element_by_name("account").send_keys(self.name)
        self.browser.find_element_by_name("password").send_keys(self.pwd)
        self.browser.find_element_by_xpath('//*[@type="checkbox"]').click()
        self.browser.find_element_by_xpath('//*[@type="submit"]').click()

        #如果找不到标签ID，可以使用其他方法来确定元素位置
        time.sleep(3)
        self.browser.get("https://www.mi.com/shop/buy/detail?product_id=16367")#切换到秒杀页面
        self.buy_on_time()
        print('登录成功，正在等待···')


    def buy_on_time(self):
        self.browser.find_element_by_xpath('//div[@class="sale-btn"]').click() # 再次登陆
        while True: #不断刷新时钟
            now = datetime.datetime.now()
            if now.strftime('%Y-%m-%d %H:%M:%S') == self.buytime:
                self.browser.find_element_by_xpath('//div[@class="sale-btn"]').click() # 购买按钮的Xpath
                print('下单成功，请抓紧付款！')
                time.sleep(0.01) # 注意刷新间隔时间要尽量短


if __name__ ==  "__main__":
    MS = XiaoMi()

    # MS.login()
