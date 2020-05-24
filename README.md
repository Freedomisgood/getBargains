# 自动拿券

Python 3.6、Appnium、Adb

> 通过别人发的口令, 打开淘宝APP进行抢券


### 1.itchat接收群消息


### 2.将口令复制到剪贴板


### 3.打开淘宝APP点击抢券


## 碰到的问题:
1. 出现如下警告:`Warning: Activity not started, its current task has been brought to the front` or `Warning: Activity not started, intent has been delivered to currently running top-most instance.`
    - A: 不用管他就行, 只是个警告, 提示你有应用切到了顶层

2. 出现提示: `/system/bin/sh: adb: inaccessible or not found`
    - A: 已经在adb shell中输入的命令不需要再加上`adb shell`前缀
e.g.`umi:/ $ adb shell am start ca.zgrs.clipper/.Main` (umi:/)提示已经在adb shell中了

3. 查找app包名和Activity活动页面(Andriod 10)
    - A: 原本的`adb shell dumpsys activity | find  "mFocusedActivity"`在andriod 10上好像检测不出来
```shell
# 查看包名
$ adb shell pm list packages
# 查看Activity
# $ adb shell dumpsys activity com.taobao.taobao | grep ACTIVITY
```

4. adb打开应用的命令?
  
- A: `adb shell am start -n package/launch activity`
  
5. appnium声明driver的时候是打开指定app程序, 但如果每次都是重新打开, 那么加载淘宝的速度会很慢。应该使用切换后台
    - A: 使用`driver.start_activity('com.taobao.taobao', 'com.taobao.tao.TBMainActivity')`
    
    [appium：一个手机运行两个APP，APP之间相互切换](https://blog.csdn.net/jianglianye21/article/details/89850033)
    
6. ADB滑动解锁问题: 在一个位置按住
  
    - A: 暂时还没解决, appnium可以, 但ADB好像没有找到解决方案
    
7. 桌面的activity:
  
    - A: `.launcher.Launcher`
    
8. 报错`selenium.common.exceptions.InvalidSessionIdException: Message: A session is either terminated or not started`

    - A: 原因是driver长时间没收到command自动关闭了, 与使用`driver.quit()`后再用driver执行操作报相同的错误。
    - ->解决方案: 在desirable_caps中将`newCommandTimeout`设置大一点: `'newCommandTimeout': 1800`

附录：
- [python3使用appnium运行手机上的APP](https://blog.csdn.net/lollipop666/article/details/82480403)

- [clipper - Broken on Android 10 (Android Q) #9](https://github.com/majido/clipper/issues/9)

- [Appium Python API 中文版 By-HZJ](https://testerhome.com/topics/3711)

- [Appium配置desired_capability详解](https://blog.csdn.net/u012002125/article/details/80870549)

- 查看包名和activity

  ```shell
  # 在米6(Andriod 10)上尝试可行
  $ adb shell dumpsys window windows | findstr mFocusedApp
  $ adb shell dumpsys window windows | findstr "Current"
  
# 下失效
  $ adb shell dumpsys activity | find  mFocusedActivity
```
  
  - 如果在有apk的情况下, `aapt dump badging d:\\test.apk`
  
  - 打开APP->` adb logcat > D:/log.txt`  -> 胡乱的对APP做一些操作->Ctrl+c 结束adb命令->打开log.txt文件，搜索：Displayed 

