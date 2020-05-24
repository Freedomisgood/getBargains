# -*- coding: utf-8 -*-
# @Time    : 2020/5/23 9:37
# @Author  : Mrli
# @FileName: getGroupMessage.py
# @Blog    : https://nymrli.top/

import itchat
import re
from datetime import datetime

# from utils.app import TaobaoCommit, clipAppnium
# from utils.clipboard import writeToClipboard
from utils.app import orderCommit
from utils.config import dont_need, reporter


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    print('--------------收到群消息--------------')
    # print(msg['FromUserName'])
    # if msg['FromUserName'] == FromUserNamedict.get('子溪(666)'):
    print("发送消息的人为: ", msg['ActualNickName'] )
    for p in reporter:
        if msg['ActualNickName'] == p:
            # get the msg
            content = msg['Content']
            print(content)

            # filter things that we don't need
            for word in dont_need:
                if word in content:
                    print("*********过滤信息*********")
                    return

            # pick up the key code
            res = re.search("\((.*?)\)|\$(.*?)\$|￥(.*?)￥", content)
            if not res:
                return
            code = res.group()
            print("淘口令为:", code)

            # writeToClipboard(code)

            # 该方法组合了下面两个步骤
            orderCommit(code)

            # # paste to the clipboard
            # writeToClipboard(code)
            #
            # # 换用appnium切换应用的clipAppnium
            # # clipAppnium(code)
            # time.sleep(.5)
            #
            # # use app: taoBao to get the discount
            # TaobaoCommit()

            # reflect
            print("{}已抢到{}".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S"), content))
            with open('discount.log', 'a+', encoding='UTF8') as f:
                f.writelines("{} 已抢到\n{}".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S"), content))
                f.writelines("-"*10)


itchat.auto_login(True)
itchat.run(True)
