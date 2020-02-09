# python3.6.5
# coding:utf-8
# 天猫淘宝自动下单
import os
from selenium import webdriver
import datetime
import time


# 创建浏览器对象
driver = webdriver.Chrome(os.path.join(os.path.dirname(__file__) + "/src", "chromedriver"))
# 窗口最大化显示
driver.maximize_window()


def login(url, mall):
    '''
    登陆函数

    url:商品的链接
    mall：商城类别
    '''
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)
    # 淘宝和天猫的登陆链接文字不同
    if mall == '1':
        # 找到并点击淘宝的登陆按钮
        driver.find_element_by_link_text("亲，请登录").click()
    else:
        # 找到并点击天猫的登陆按钮
        driver.find_element_by_link_text("请登录").click()
    print("请在30秒内完成登录")
    # 用户扫码登陆
    time.sleep(30)


def buy(buy_time, mall):
    '''
    购买函数

    buy_time:购买时间
    mall:商城类别
    '''
    if mall == '1':
        # "立即购买"的css_selector
        btn_buy = '#J_juValid > div.tb-btn-buy > a'
        # "立即下单"的css_selector
        btn_order = '#submitOrder_1 > div.wrapper > a'
    else:
        btn_buy = '#J_LinkBuy'
        btn_order = '#submitOrderPC_1 > div > a'

    while True:
        # 现在时间大于预设时间则开售抢购
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > buy_time:
            try:
                # 找到“立即购买”，点击
                if driver.find_element_by_css_selector(btn_buy):
                    driver.find_element_by_css_selector(btn_buy).click()
                    break
                time.sleep(0.1)
            except:
                time.sleep(0.3)

    while True:
        try:
            # 找到“立即下单”，点击，
            if driver.find_element_by_css_selector(btn_order):
                driver.find_element_by_css_selector(btn_order).click()
                # 下单成功，跳转至支付页面
                print("购买成功")
                break
        except:
            time.sleep(0.5)


if __name__ == "__main__":
    # 输入要购买物品 url
    url = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.5db97de7nIagyn&id=560599203455&skuId=3737496318597&areaId=320500&user_id=2261244963&cat_id=2&is_b=1&rn=45b3402ed4736ad0cd8928eafe32d986"
    mall = input("请选择商城（淘宝 1  天猫 2  输入数字： ")
    # 输入开售时间
    bt = "2019-02-09 22:00:00"
    login(url, mall)
    buy(bt, mall)

