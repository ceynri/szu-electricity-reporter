import requests
import datetime
import re


# 返回一个7*4的二维数组，分别是日期、剩余电量、总用电量、总购电量
def crawlData(client: str, room_name: str, room_id: str, interval: int = 7) -> list:
    # 爬取网页，应该一般不会变动
    url = 'http://192.168.84.3:9090/cgcSims/selectList.do'

    # 计算今天与六天前
    today = datetime.date.today()
    days_before = str(today - datetime.timedelta(days=interval - 1))
    today = str(today)

    # 设置 post 请求参数
    params = {
        'hiddenType': '',
        'isHost': '0',
        'beginTime': days_before,
        'endTime': today,
        'type': '2',
        'client': client,
        'roomId': room_id,
        'roomName': room_name,
        'building': ''
    }

    # 发送 post 请求，获得返回 html 文本
    response = requests.post(url, data=params)
    html = response.text
    # print('\n--- HTML ---\n', html, '\n--- HTML ---\n')  # 调试用

    # 匹配需要的表格块
    raw_electricity_data = re.findall(r'<td width="13%" align="center">(.*?)</td>', html, re.S)
    raw_date_data = re.findall(r'<td width="22%" align="center">(.*?)</td>', html, re.S)
    # 清洗数据
    electricity_data = []
    count, i = 0, -1
    for datum in raw_electricity_data:
        if count % 5 != 0 and count % 5 != 1:
            electricity_data[i].append(datum.strip())
        elif count % 5 != 1:
            i += 1
            electricity_data.append([])
            electricity_data[i].append(raw_date_data[i].strip()[:10])
        count += 1

    # print(electricity_data)  # 调试用

    return electricity_data
