import os
import tinify
import json
from urllib.request import Request, urlopen
import time
import requests
import sys
import random
from PIL import Image
from selenium import webdriver

# 导入模块
basedir = os.path.abspath(os.path.dirname(__file__))
from wxpy import *
import itchat


def login():
    # bot = Bot(cache_path=True)
    bot = Bot()
    groups = bot.groups()
    group1 = bot.groups().search(keywords='口罩消毒液放货监控群')
    group = bot.groups().search(keywords='口罩消毒液放货监控群')[0]
    print(group)
    while True:
        group.send('有货啦')
    return bot


def get_bot():
    bot = Bot('bot.pkl', qr_path=os.path.join(
        basedir, 'QR.png'), console_qr=None)
    # bot.enable_puid()
    # bot.messages.max_history = 0
    return bot


# bot = get_bot()

def save_jd_url(url):
    try:
        fo = open("jdurl.txt", "r")
        lines = fo.readlines()
        fo.close()
        fo = open("jdurl.txt", "w")
        lines.append("\"" + url + "\",\n")
        fo.writelines(lines)
        fo.close()
    except Exception:
        print("读取data失败")


def save_tm_url(url):
    try:
        fo = open("tmurl.txt", "r")
        lines = fo.readlines()
        fo.close()
        fo = open("tmurl.txt", "w")
        lines.append("\"" + url + "\",\n")
        fo.writelines(lines)
        fo.close()
    except Exception:
        print("读取data失败")






def get_outfile(infile, outfile):
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir, suffix)
    return outfile





def resize_image(infile, outfile='', x_s=1124):
    """修改图片尺寸
    :param infile: 图片源文件
    :param outfile: 重设尺寸文件保存地址
    :param x_s: 设置的宽度
    :return:
    """
    im = Image.open(infile)
    x, y = im.size
    y_s = int(y * x_s / x)
    out = im.resize((x_s, y_s), Image.ANTIALIAS)
    outfile = get_outfile(infile, outfile)
    out.save(outfile)

#
# if __name__ == '__main__':
#         file = open("data.txt")
#         for line in file:
#             # 压缩图片到500k以下
#             file_name = "src/imgs/" + line[:19]
#             resize_image(file_name + ".png", file_name + "_copy.png")
#             # group.send("发现有货!!!\n" + line)
#         print("读取data.txt结束")
#         file.close()


if __name__ == '__main__':
    browser = webdriver.Chrome(os.path.join(os.path.dirname(__file__) + "/src", "chromedriver"))
    bot = Bot()
    # 修改群名
    group = bot.groups().search(keywords='口罩消毒液放货监控群')[0]
    group2 = bot.groups().search(keywords='口罩消毒液监控群')[0]
    # url = "http://invoice.pinhai.com.cn:8090/index/maskloglist"
    url = "http://invoice.pinhai.com.cn/index/maskloglist"
    # 包装头部
    firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # 构建请求
    pre_time = ""
    i = 0
    data_map = {}
    while (1):
        if (i + 1) % 5 == 0:
            print("已为您成功您监控" + str(i + 1) + "次")
        try:
            file = open("data.txt")
            try:
                for line in file:
                    if line not in data_map:
                        group2.send("发现有货!!!\n" + line)
                        # 压缩图片到500k以下
                        file_name = "src/imgs/"+line[:19]
                        try:
                            resize_image(file_name + ".png", file_name + "_copy.png")
                            group2.send_image(file_name+"_copy.png", media_id=None)
                            group.send("发现有货!!!\n" + line)
                            group.send_image(file_name+"_copy.png", media_id=None)
                        except Exception:
                            continue
                        data_map[line] = line
                print("读取data.txt结束")
            except Exception:
                print("读取data失败")
            finally:
                file.close()
            # 注释开始
            request = Request(url, headers=firefox_headers)
            html = urlopen(request)
            data = html.read()
            strs = str(data, 'UTF-8')
            list = json.loads(strs)['data']['maskloglists']
            data_json = list[-1]
            title = data_json["title"]

            if pre_time != data_json["ctime"] and data_json["title"] not in data_map:
                print(data_json)
                data_map[data_json["title"]] = data_json['url']
                data = "商品名：【" + data_json["title"] + "】\n" + data_json["card_text"] + "\n购买链接：" + data_json[
                    'url']
                print(data)
                # 再次检查
                browser.get(data_json['url'])
                time.sleep(3)
                find_flag = False
                for keyword in ['无货', '下柜', '已下架', '不支持销售', '售完', '卖光']:
                    if keyword in browser.page_source:
                        find_flag = keyword
                        break
                if find_flag is not False:
                    continue
                # 发送微信信息
                img_name = "imgs/" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                browser.save_screenshot(img_name+ "B.png")
                group2.send(data)
                resize_image(img_name + "B.png", img_name + "B_copy.png")
                group2.send_image(img_name + "B_copy.png", media_id=None)
                # time.sleep(1)
                group.send(data)
                url_save = data_json['url']
                if "jd" in url_save:
                    save_jd_url(url_save)
                elif "tmall" in url_save:
                    save_tm_url(url_save)
                print("推送成功")
        except Exception:
            print("第" + str(i + 1) + "次推送挂掉了")
            i = i - 1
        sleep_time = 10 + int(random.random() * 10)
        time.sleep(sleep_time)
        i = i + 1
