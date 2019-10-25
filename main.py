import crawler
import scsender


# main函数
def main():
    # 【需修改】相关参数
    # 已填写示例以风槐201（非本人宿舍）为例
    client = '192.168.84.87'
    room_name = '201'
    room_id = '7141'
    # 需要获取的日期范围（默认最近14天）
    interval_day = 14

    # 获得数据
    table_data = crawler.crawlData(client, room_name, room_id, interval_day)
    if len(table_data) == 0:
        print('[爬取数据失败，请检查是否能访问电费查询网站"http://192.168.84.3:9090/cgcSims/"]')
        return
    print('[爬取数据结束]')

    # 处理数据
    data = processingData(table_data)
    print('[数据处理结束]')
    # 在控制台格式化输出爬虫获得的数据
    printData(data)

    # 以下内容如无需发送至微信则无需修改，直接注释掉 #########################

    # # 【需修改】填写Server酱SCKEY
    # sc_key = 'https://sc.ftqq.com/xxxxxxxxxxxxxxxxxxxx.send'

    # # describe参数内容会添加到内容详情最前端
    # describe = 'ᶘ ᵒᴥᵒᶅ {}电量查询'.format(room_name)

    # # 处理数据为要发送的表格格式信息
    # send_msg = scsender.handle(data, describe)

    # # 发送信息
    # scsender.send(
    #     key_url=sc_key,
    #     data=send_msg,
    # )

    # print('[已发送至微信]')
    return


# 加工数据获得想要的数据格式
def processingData(table_data: list):
    data = []
    day_num = len(table_data)

    # 日期 | 当日用电量
    for i in range(day_num - 1):
        charge = table_data[i + 1][3] - table_data[i][3]
        data.append({
            'date': table_data[i][0],
            'cost': table_data[i][1] - table_data[i + 1][1],
            'rest': table_data[i][1],
            'charge': charge
        })
        if charge != 0:
            data[-1]['cost'] += charge  # 充了电，则需要修正耗电计算公式问题
        else:
            data[-1]['charge'] = '-'  # 没充电费

    # 最后一天需要单独赋值
    data.append({
        'date': table_data[day_num - 1][0],
        'cost': '-',
        'rest': table_data[day_num - 1][1],
        'charge': '-'
    })

    return data


# 格式化输出爬虫获得的数据
def printData(data: list):
    print('日期'.ljust(8, ' '), '当日用电'.ljust(8, ' '),
          '可用电量'.ljust(8, ' '), '当日充电'.ljust(8, ' '))
    for row in data:
        for datum in row:
            value = row[datum]
            # float型要转换为str才可以使用ljust函数
            if isinstance(value, float):
                value = '{:.2f}'.format(value)
            print(value.ljust(12, ' '), end='')  # 每个数据的长度为12字符宽
        print()
    return


if __name__ == '__main__':
    main()
