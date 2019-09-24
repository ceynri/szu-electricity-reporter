import crawler
import serverChanSender


# 格式化输出爬虫获得的数据
def printData(data: list):
    print('日期'.ljust(10, ' '), '剩余电量'.ljust(8, ' '), '总用电量'.ljust(8, ' '), '总购电量'.ljust(8, ' '))
    for row in data:
        for datum in row:
            print(datum.ljust(12, ' '), end='')
        print()
    return


if __name__ == '__main__':
    # [需修改] 相关参数
    client = '192.168.84.xxx'
    room_name = '101'
    room_id = '0001'
    # 需要获取的日期范围（默认最近7天）
    interval_day = 7

    # 获得数据
    tabular_data = crawler.crawlData(client, room_name, room_id, interval_day)
    print('爬取数据结束')

    # 格式化输出爬虫获得的数据
    printData(tabular_data)

    # 以下内容如无需发送至微信则无需修改，直接注释掉

    # [需修改] Server酱SCKEY
    sc_key = 'https://sc.ftqq.com/xxxxxxxxxxxxxxxxxxxx.send'

    # 通过 server酱 处理与发送数据
    # describe参数内容会添加到内容详情最前端
    describe = '{}电量查询 ᶘ ᵒᴥᵒᶅ'.format(room_name)
    serverChanSender.send(
        url=sc_key,
        data=tabular_data,
        describe=describe
    )
    print('已发送至微信')
