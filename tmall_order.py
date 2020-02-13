# python3.6.5
# coding:utf-8
# 天猫淘宝自动下单 用于定时抢购
import os
from selenium import webdriver
import datetime
import time
from selenium.webdriver.chrome.options import Options

# 创建浏览器对象
chrome_options = Options()
# 关闭使用 ChromeDriver 打开浏览器时上部提示语 "Chrome正在受到自动软件的控制"
chrome_options.add_argument("disable-infobars")
# 允许浏览器重定向，Framebusting requires same-origin or a user gesture
chrome_options.add_argument("disable-web-security")
driver = webdriver.Chrome(os.path.join(os.path.dirname(__file__) + "/src", "chromedriver"),
                          chrome_options=chrome_options)
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
    print("开始购买")
    if mall == '1':
        # "立即购买"的css_selector
        btn_buy = '#J_juValid > div.tb-btn-buy > a'
        # "立即下单"的css_selector
        btn_order = '#submitOrder_1 > div.wrapper > a'
    else:
        btn_buy = '#J_LinkBuy'
        btn_order = '#submitOrderPC_1 > div > a'
    timeArray = time.strptime(buy_time, "%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    print(timeStamp)
    print(time.time())

    while True:
        # 现在时间大于预设时间则开售抢购
        if time.time() > timeStamp:
            try:
                print("尝试下单")
                # 找到“立即购买”，点击
                if driver.find_element_by_css_selector(btn_buy):
                    driver.find_element_by_css_selector(btn_buy).click()
                    break
                # time.sleep(0.1)
            except:
                pass

    print("下单成功")
    while True:
        try:
            # 找到“立即下单”，点击，
            print("尝试提交订单")
            if driver.find_element_by_css_selector(btn_order):
                driver.find_element_by_css_selector(btn_order).click()
                # 下单成功，跳转至支付页面
                print("购买成功")
                break
        except:
            time.sleep(0.5)


# 使用方法
# 1 设置url
# 2 设置天猫还是淘宝
# 3 设置开抢时间
# 4 运行程序
# 5 扫码登录
# 6 选中要购买商品以及相应种类等（必须选中！！！）
# 7 自动下单

if __name__ == "__main__":
    # 输入要购买物品 url
    url = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.449d5ee8L0oNmL&id=15839960304&areaId=320500&standard=1&user_id=101450072&cat_id=2&is_b=1&rn=baf2eb3ad6e052562ab3c4728367cfd3"
    # 请选择商城（淘宝 1  天猫 2  输入数字：
    mall = '2'
    # 输入开售时间
    bt = "2020-02-13 11:23:59"
    login(url, mall)
    buy(bt, mall)
    driver.quit()
