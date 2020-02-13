import sys
import os, time, json

lib_path = os.path.join(os.path.dirname(__file__))[:-3]
sys.path.append(lib_path)

from selenium import webdriver
from log.logger import logger as log
from PIL import Image

browser = None


def check_shop(url, keywords):
    global browser
    browser.get(url)
    time.sleep(5)
    find_flag = False
    for keyword in keywords:
        if keyword in browser.page_source:
            find_flag = keyword
            break
    if not find_flag and '出错啦' not in browser.title:
        log.warning("FIND!!!")
        log.warning(url)
        log.warning(keywords)
        #     "发现口罩有货!!",
        fo = open("../data.txt", "r")
        lines = fo.readlines()
        fo.close()
        fo = open("../data.txt", "w")
        str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        lines.append(str_time+" "+browser.title+" url："+url+"\n")
        fo.writelines(lines)
        fo.close()
        print("发现口罩有货!!"+url)
        browser.save_screenshot("imgs/" + str_time + ".png")
        time.sleep(5)




def check_all_shops():
    with open(os.path.join(os.path.dirname(__file__),"config","shop.json"), "r", encoding='UTF-8') as f:
        infos = json.loads(f.read())
        for info in infos:
            for shop in info["shop"]:
                log.info("checking {} / {}".format(shop, info.get("keyword")))
                keywords = info.get("key_word").split(",")
                check_shop(shop, keywords)



# 加载 config/shop.json 中的商品，并检查有货状态，如果有货保存在 data.txt 中
if __name__ == "__main__":
    browser = webdriver.Chrome(os.path.join(os.path.dirname(__file__),"src", "chromedriver"))
    while True:
        check_all_shops()
        # browser.quit()