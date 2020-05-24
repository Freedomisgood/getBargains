# -*- coding: utf-8 -*-
# @Time    : 2020/5/23 9:48
# @Author  : Mrli
# @FileName: formatJson.py
# @Blog    : https://nymrli.top/
import subprocess
from time import sleep


def writeToClipboard(text: str):
    code = "\\" + text.strip(")") + '\\)'
    subprocess.call('adb shell am start ca.zgrs.clipper/.Main')  # 开启app
    sleep(0.2)
    subprocess.call('adb shell am broadcast -a clipper.set -e text "{}"'.format(code))  # 获得剪切板内容
    # subprocess.call('adb shell am broadcast -a clipper.set -e text "\(fn5I1qyruJe\)"')  # 获得剪切板内容
    # subprocess.call('adb shell am broadcast -a clipper.get')  # 获得剪切板内容
    sleep(0.2)
    # subprocess.call('adb shell am force-stop ca.zgrs.clipper')  # 关闭app


if __name__ == '__main__':
    import re
    # writeToClipboard("(fn5I1qyruJe)")
    # writeToClipboard("$ntmZ1qzHavb$")
    # content = '淘口令:(fn5I1qyruJe)'
    content = '(BQu51J0m7BB)'
    res = re.search("\((.*?)\)|\$(.*?)\$|￥(.*?)￥", content)
    print(res)
