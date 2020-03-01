# python3.6.5
# coding:utf-8
# 天猫淘宝自动下单 用于定时抢购
import os
from selenium import webdriver
import requests
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


def buy(buy_time, mall, time_dif):
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
    print("开始准备购买")

    while True:
        # 现在时间大于预设时间则开售抢购
        tmp_time = time.time()
        if tmp_time >= (timeStamp - time_dif):
            try:
                print("开始购买" + str(time.time()))
                # 找到“立即购买”，点击
                if selector:
                    print("点击" + str(time.time()))
                    selector.click()
                    break
            except:
                pass
    while True:
        try:
            # 找到“立即下单”，点击，
            # print("尝试提交订单")
            order_selector = driver.find_elements_by_css_selector(btn_order)
            if order_selector:
                print("购买" + str(time.time()))
                order_selector[-1].click()
                # 下单成功，跳转至支付页面
                print("购买成功" + str(time.time() - tmp_time))
                break
            driver.refresh()
        except:
            driver.refresh()
            time.sleep(0.01)


def get_server_time():
    time_start = time.time()
    r1 = requests.get(url='http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp',
                      headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'})
    x = eval(r1.text)
    tmp = time.time() - time_start
    timeNum = int(x['data']['t'])

    timeStamp = float(timeNum / 1000)
    print(tmp)
    # timeArray = time.localtime(timeStamp)
    # otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return timeStamp, tmp


# 使用方法
# 1 设置url
# 2 设置天猫还是淘宝
# 3 设置开抢时间
# 4 运行程序
# 5 扫码登录
# 6 选中要购买商品以及相应种类等（必须选中！！！）
# 7 自动下单
#

if __name__ == "__main__":
    # 输入要购买物品 url
    # 如果是天猫超市的抢购 请先加入购物车 此处为购物车链接
    url = "https://cart.taobao.com/cart.htm"
    # 请选择商城（淘宝 1  天猫 2  3 通过购物车 输入数字：
    mall = '3'
    # 输入开售时间
    bt = "2020-03-01 15:00:00"
    server_time, tmp = get_server_time()
    time_dif = time.time() - server_time + tmp + tmp
    login(url, mall)
    buy(bt, mall, 2 * time_dif + 0.5)
    # driver.quit()
