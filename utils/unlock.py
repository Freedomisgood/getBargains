# -*- coding: utf-8 -*-
# @Time    : 2020/5/23 15:19
# @Author  : Mrli
# @FileName: unlock.py
# @Blog    : https://nymrli.top/

# from appium.webdriver.common.touch_action import TouchAction
from subprocess import call


def unlock():
    # TODO: 无法解锁九宫格, 因为swipe之间无法保持按住
    # 亮屏幕
    call('adb shell input keyevent  26')
    # 上滑切换到九宫格解锁
    call('adb shell input touchscreen swipe 545 2100 530 1385 200')
    # 横
    call('adb shell input touchscreen swipe 240 1084 815 1084 100')
    # call('adb shell input flick swipe 240 1084 815 1084 100')
    # 竖
    call('adb shell input swipe 815 1084 825 1690 100')

unlock()