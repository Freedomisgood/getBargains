# -*- coding: utf-8 -*-
# @Time    : 2020/5/23 11:14
# @Author  : Mrli
# @FileName: app.py
# @Blog    : https://nymrli.top/

from appium import webdriver
from time import sleep
from config import desired_caps
from subprocess import call
from selenium.common.exceptions import NoSuchElementException

# #待测试的app的Java package包名称
# desired_caps['appPackage'] ='ca.zgrs.clipper'
# #待测试的app的Activity名字。比如MainActivity、.Settings，原生app的话要在前面加个"."
# desired_caps['appActivity'] ='.Main'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.close_app()
driver.press_keycode(3) # 回退到home

driver.implicitly_wait(8)
# sleep(1)

# 弃用
def startTaobao():
    print("TaobaoCommit", driver.current_activity)
    driver.start_activity('com.taobao.taobao', 'com.taobao.tao.TBMainActivity')
    print("切换app")
    print(driver.current_activity)


def getDiscount():
    '''
    打开淘宝后获得券的操作
    :return:
    '''
    try:
        driver.find_element_by_id("com.taobao.taobao:id/tpd_common_action").click()
        sleep(0.5)

        accept = driver.find_element_by_xpath(
            '//com.uc.webview.export.WebView[@content-desc="WVUCWebView"]/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[5]')
        # print(accept.text)
        accept.click()
        sleep(0.5)
    except NoSuchElementException as e:
        print(e)
    finally:
        driver.press_keycode(3)  # 回退到home


def clipAppnium(text: str):
    # print("clipAppnium", driver.current_activity)
    code = "\\" + text.strip(")") + '\\)'
    # 切换到剪贴板应用
    driver.start_activity('ca.zgrs.clipper', '.Main')
    # print("切换app")
    print(driver.current_activity)
    call('adb shell am broadcast -a clipper.set -e text "{}"'.format(code))  # 获得剪切板内容
    # call('adb shell am force-stop ca.zgrs.clipper')  # 关闭app


def TaobaoCommit():
    """
    通过startTaobao来获得券, startTaobao为重新打开淘宝
    :return:
    """
    startTaobao()
    getDiscount()


def orderCommit(text: str):
    """
    通过切换后台应用打开淘宝
    :param text: 淘口令
    :return: None
    """
    clipAppnium(text)
    driver.press_keycode(82) # 菜单
    # print(driver.current_activity)
    sleep(0.1)
    # 第一个选项
    # driver.tap([(200, 1200)])
    # 第二个选项
    driver.tap([(600, 1200)])
    # 获得券
    getDiscount()


if __name__ == '__main__':
    # TEST
    # driver.start_activity('com.taobao.taobao', 'com.taobao.tao.TBMainActivity')
    # print(driver.current_activity)
    # driver.background_app(2)
    # TaobaoCommit()
    # clipAppnium('test')

    # TEST: 1
    orderCommit('(fn5I1qyruJe)')
    sleep(2)
    # driver.press_keycode(3) # 回退到home
    # print(driver.current_activity)
    # sleep(2)
    # driver.press_keycode(82) # 菜单
    # print(driver.current_activity)
    # sleep(2)






    # desired_cups = {}
    # desired_cups['platformName'] ='Android'
    # # 手机设备版本，直接看手机设置--关于本机信息里就有
    # # desired_cups['platformVersion'] ='10'
    # # 设备名称，adb devices -l 查看(小字l)，model后的名称，不是adb devices出来的设备号哟
    # desired_cups['deviceName'] ='faca3765'
    # #待测试的app的Java package包名称
    # desired_cups['appPackage'] ='com.taobao.taobao'
    # #待测试的app的Activity名字。比如MainActivity、.Settings，原生app的话要在前面加个"."
    # desired_cups['appActivity'] ='com.taobao.taobao.TBMainActivity'
    # #不需要再次签名
    # desired_cups['noSign'] = 'True'
    # #不需要清理数据，避免重新安装的问题
    # desired_cups['noReset'] = 'True'
    # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cups)
    # driver.start_activity('ca.zgrs.clipper', '.Main')
    