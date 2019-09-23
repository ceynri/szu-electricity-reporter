# 微信提醒宿舍电量情况

[更新于2019-09-23]

## 简介

使用 python 简单爬取深圳大学特定的宿舍电量情况，将其简单处理后借助 [Server酱](http://sc.ftqq.com) 将电量情况发送至微信上。可配合定时任务完成每日电量提醒功能。

## 项目结构

- main.py  
  主程序，需要手动修改参数，可选是否发送到微信

- crawler.py  
  爬虫代码，一般不用修改

- serverChanSender.py  
  通过 Server酱 进行微信提醒，不用修改

- responsed-html-sample.html
  一个 POST 请求响应返回的 HTML 文本，可供参考（没什么用）

## 使用方法

    环境：Anaconda、深大校内网

1. 修改 `main.py` 代码内容，将指定的参数修改为你对应的参数值

    参数值获取途径（以 Chrome浏览器 为例）：

    校内网环境，点击<kbd>F12</kbd>键或空白处`右键-检查`打开开发者工具，选择 Network 选项卡，登录深大[SIMS电控网上查询系统](http://192.168.84.3:9090/cgcSims/)，填写宿舍信息后，随便选择开始时间、结束时间、查询类型，点击查询，在开发者工具中选择 `selectList.do` 文件，查看它的 POST 请求参数（如果没有则刷新页面）。

    ![network.jpg](https://ftp.bmp.ovh/imgs/2019/09/2021ada6023d5368.jpg)

    将 `main.py` 文件内的参数对应地替换为图中红框所包含的 `client`、`roomId`、`roomName` 参数即可。

2. 注册 Server酱 账号，绑定微信并获得 SCKEY 完成设置

    （为避免日后版本更新，以官网教程为准。）
    
    ![serverChan.jpg](https://ftp.bmp.ovh/imgs/2019/09/274ff356c8a14998.jpg)
    
    打开 [Server酱](http://sc.ftqq.com/) 官网，选择`登入`，自动 github 账号授权登录。

    然后选择`微信推送`，扫码绑定微信，关注公众号。

    然后复制`发送信息`的 `SCKEY` 码，替换 `main.py` 中的 `sc_key` 参数即可。

3. 运行 `main.py` 程序即可收到微信提醒，控制台亦有相关信息输出

    ![msg.jpg](https://ftp.bmp.ovh/imgs/2019/09/57f81d7b37df2f90.jpg)

4. Windows 系统可以设置 `计划任务` 定时运行该脚本，达到每日提醒的效果~（具体方法略）

## 其他

有问题欢迎提交 issue

python新手见谅
