import requests


# 使用 Server酱 发送电量数据至微信
def send(url: str, data: list):
    # 处理数据
    data = handle(data)
    # post请求
    requests.post(url, data=data)


def handle(data):
    # 计算昨日用电与剩余电量
    yesterday_rest = data[-2][1]
    today_rest = data[-1][1]
    used = float(yesterday_rest) - float(today_rest)
    # 标题
    text = '昨日用电{}度，今日剩余{}度'.format(used, today_rest)
    # 详细内容
    desp = '| 日期 | 剩余电量 | 总用电量 | 总购电量 |\n' + \
           '| --- | ------- | ------- | ------ |\n'
    for line in data:
        for datum in line:
            desp += '| {}　 '.format(datum)  # 出于Sever酱的markdown表格样式问题，尾随全角空格一个
        desp += '|\n'
    # print(desp)  # 测试用
    data = {
        'text': text,
        'desp': desp
    }
    return data
