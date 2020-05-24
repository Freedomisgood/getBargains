# -*- coding: utf-8 -*-
# @Time    : 2020/5/23 10:07
# @Author  : Mrli
# @FileName: config.py
# @Blog    : https://nymrli.top/


'''
    appnium模块
'''
# 这里是用来配制服务的，跟appium里是差不多的
desired_caps = {
    # 设备名:iOS, Android, orFirefoxOS等等
    "platformName": "Android",
    # 手机设备版本，直接看手机设置--关于本机信息里就有
    "platformVersion": "10",
    # 设备名称，adb devices -l 查看(小字l)，model后的名称，不是adb devices出来的设备号哟
    "deviceName": "faca3765",
    # 待测试的app的Java package包名称
    "appPackage": "com.taobao.taobao",
    # 待测试的app的Activity名字。比如MainActivity、.Settings，原生app的话要在前面加个"."
    # "appActivity": "com.taobao.tao.TBMainActivity",
    "appActivity": "com.taobao.tao.welcome.Welcome",
    # 不需要再次签名
    "noSign": True,
    # 不需要清理数据，避免重新安装的问题
    "noReset": True,
    # 'stopAppOnReset': False,
    # 如果600s没消息driver会自动退出
    'newCommandTimeout': 1800
}

#
# desired_caps['platformName'] ='Android'
# # 手机设备版本，直接看手机设置--关于本机信息里就有
# # desired_caps['platformVersion'] ='10'
# # 设备名称，adb devices -l 查看(小字l)，model后的名称，不是adb devices出来的设备号哟
# desired_caps['deviceName'] ='faca3765'
# # 待测试的app的Java package包名称
# desired_caps['appPackage'] ='com.taobao.taobao'
# # 待测试的app的Activity名字。比如MainActivity、.Settings，原生app的话要在前面加个"."
# desired_caps['appActivity'] ='com.taobao.tao.TBMainActivity'
# # 不需要再次签名
# desired_caps['noSign'] = 'True'
# # 不需要清理数据，避免重新安装的问题
# desired_caps['noReset'] = 'True'


reporter = [
    '子溪（666）',
    '子溪 发布员（勿加我）',
    '种草君💰补贴发放员',
    '种草君助手👧🏻',
]

dont_need = [
    '手机壳',
    '花洒',
    '脚气',
    '电容',
    '蟑螂',
    '首单'
]

# '''
# itchat模块
# '''
# FromUserNamedict = {
#     # "子溪(666)": '@@1cbed8ce38f3a0b81b1cfe8200af13db90c77295c8d964e4dcfef2d44ab8f93a',
#     "子溪(666)": '@@a561ba93115a8706a94e516c4d7171dbf42944c4b891c2184ebb233ee2600d96',
# }


'''
appnium-Taobao分析过程
'''
# 剪贴板打开控件ID
# 'com.taobao.taobao:id/tpd_common_action'
# 剪贴板打开控件xpath
# '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]'
# 具体商务
# text内容
# 'text	立即领取'
# 只有xpath
# '//com.uc.webview.export.WebView[@content-desc="WVUCWebView"]/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[5]'

'''
PS：说明下怎么获取package名和activity名：
'''
#     a.  cmd命令行打开adb shell
#         adb shell
#     b. 在手机上打开一会想要操作的APP
#     c. 在adb shell中输入以下命令
#         dumpsys activity | grep mFocusedActivity
#     d. 即可看到包名和活动名


