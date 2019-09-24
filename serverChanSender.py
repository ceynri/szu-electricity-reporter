import requests


# 使用 Server酱 发送电量数据至微信
def send(url: str, data: list, describe: str):
    # 处理数据
    data = handle(data, describe)
    # post请求
    requests.post(url, data=data)
    return



def handle(data: list, describe: str):
    # 计算昨日用电与剩余电量
    yesterday_rest = float(data[-2][1])
    today_rest = float(data[-1][1])
    used = yesterday_rest - today_rest

    # 判断是否充了电
    charge = 0
    if used < 0:
        charge = float(data[-1][3]) - float(data[-2][3])
        used += charge

    # 标题
    text = '昨日用电{:.2f}度，今日剩余{:.2f}度'.format(used, today_rest)

    # 详细内容
    desp = describe + '\n\n'
    desp += '| 日期 | 剩余电量 | 总用电量 | 总购电量 |\n' + \
            '| --- | ------- | ------- | ------ |\n'
    for line in data:
        for datum in line:
            desp += '| {}　 '.format(datum)  # 出于Sever酱的markdown表格样式问题，尾随全角空格一个
        desp += '|\n'

    desp += '\n昨日充电{}度\n'.format(charge)
    # print(desp)  # 测试用

    data = {
        'text': text,
        'desp': desp
    }

    return data
