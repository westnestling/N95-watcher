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
    elif mall == '2':
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
    elif mall == '3':
        btn_buy = '#J_Go'
        btn_order = '#submitOrderPC_1 > div > a'
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
        tmp_time = time.time()
        if tmp_time >= timeStamp or (timeStamp - tmp_time) < 0.01:
            try:
                # 找到“立即购买”，点击
                selector = driver.find_element_by_css_selector(btn_buy)
                if selector:
                    selector.click()
                    break
                # time.sleep(0.1)
            except:
                pass
    while True:
        try:
            # 找到“立即下单”，点击，
            # print("尝试提交订单")
            order_selector = driver.find_elements_by_css_selector(btn_order)
            if order_selector:
                order_selector[-1].click()
                # 下单成功，跳转至支付页面
                print("购买成功")
                break
            driver.refresh()
        except:
            driver.refresh()
            time.sleep(0.01)


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
    # url = "https://chaoshi.detail.tmall.com/item.htm?id=611911893371&sourceType=item&sourceType=item&price=126&suid=8d12be3f-0542-43be-a763-9822c43d5565&ut_sk=1.XbCIz/bFF4ADALGCBoZRXQj7_23181017_1581584224037.Copy.tm_detail&un=91e19e41e6228caa0a62cb2c046d31df&share_crt_v=1&spm=a2159r.13376460.0.0&sp_tk=77%20lNnA0YzFWM2FGWDfvv6U=&cpp=1&shareurl=true&short_name=h.VXpAOsV&sm=4a6d85&app=chrome"
    url = "https://cart.tmall.com/cart.htm?from=bmini&tpId=725677994"
    # 请选择商城（淘宝 1  天猫 2  3 天猫超市 输入数字：
    mall = '3'
    # 输入开售时间
    bt = "2020-02-13 00:00:00"
    login(url, mall)
    buy(bt, mall)
    # driver.quit()
