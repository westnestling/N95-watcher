# N95-watcher
 🏷️监控京东、天猫、苏宁等商城口罩、消毒液、护目镜等物资有货信息，并推送微信提醒。抗击疫情！中国加油🇨🇳！
 请不要用于非法用途！请不要倒卖口罩！此项目是为了学习技术，不对代码用途负责！

## 已有功能
- 推送微信消息
- 根据商品列表监控商品
- 最新：推送商品页面截图，方便甄别有效信息
- 根据已有接口查询商品并检查，然后推送
- 发现需要抢购的商品，输入url自动下单抢购（支持天猫淘宝）tmall_order.py 
- 京东监控扫码一键登陆功能 jd_auto_order.py
<img src="http://i1.fuimg.com/673525/70a1e32512ff0875.jpg" width="250" align=center>
<img src="http://i1.fuimg.com/673525/14707fe5414940b5.jpg" width="250" align=center>
<img src="http://i1.fuimg.com/673525/399b61427ad9bef4.jpg" width="250" align=center>


### 如果对您有帮助 欢迎点亮 🌟star🌟
# 加入已有交流群
<img src="http://i2.tiimg.com/673525/362cd540e3ba52f5.jpg" width="250" align=center>

[群二维码不显示点击这里](http://i2.tiimg.com/673525/362cd540e3ba52f5.jpg)
#### ！！！为防止人恶意刷单，京东扫码登陆功能已经删除，如有需要请加微信群获取

## 加群失败 请关注以下二维码 获得最新消息
<img src="http://chuantu.xyz/t6/715/1581144518x2728303411.jpg" width="250" align=center>

[二维码不显示点击这里](http://chuantu.xyz/t6/715/1581144518x2728303411.jpg)


## 自行微信推送使用方式
- 请自行安装python 3，如果已安装版本是python 2，推荐使用版本管理工具。
```buildoutcfg
python3：https://www.python.org/downloads/
```
- 安装所需依赖
```buildoutcfg
pip install wxpy
pip install selenium
pip install pillow
如果还有其他缺失 请根据提示 pip install 安装
```
- 运行watcher.py
- 运行wechat_push.py
- 修改程序内的要推送用户名
- 扫码登陆
- 开始推送

## 天猫、淘宝、天猫商城抢购功能
### 使用方法
1. 设置url
2. 设置天猫还是淘宝
3. 设置开抢时间
4. 运行程序
5. 扫码登录
6. 选中要购买商品以及相应种类等（必须选中！！！）
7. 自动下单

## 京东监控扫码一键登陆功能
### 使用方法
1. 设置skuidsString：需要抢购的商品id ，逗号 ',' 分割 （已有默认口罩id）
2. 设置modelType：抢购模式 ，默认快速模式
3. 设置支付密码 payment_pwd
4. 启动程序,扫码登录京东，程序即可自动运行
#### ！！！注意，需要设置默认收货地址，下单地址即为默认收货地址，监测有货也是以此地址监测。
#### ！！！为防止人恶意刷单，京东扫码登陆功能已经删除，如有需要请加微信群获取


## 欢迎关注公众号：后端开发技术
<img src="http://chuantu.xyz/t6/715/1581144518x2728303411.jpg" width="250" align=center>

[二维码不显示点击这里](http://chuantu.xyz/t6/715/1581144518x2728303411.jpg)
