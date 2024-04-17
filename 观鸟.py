# 2024/3/9 17:03
import execjs
import requests

import gene_useragent


def func(page):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://birdreport.cn",
        "Referer": "http://birdreport.cn/",
        "User-Agent": gene_useragent.get_ua()
    }
    url = "https://api.birdreport.cn/front/activity/search"
    params = '{"limit":"20","page":"%s"}' % page
    print(params)
    js = execjs.compile(open('观鸟.js', 'r', encoding='utf-8').read())
    key = js.call('beforeSend', params)
    headers['sign'] = key['sign']
    headers['requestId'] = key['requestId']
    headers['timestamp'] = str(key['timestamp'])
    response = requests.post(url, headers=headers, data=key['data'])

    # print(response.json())
    # print(response)

    res = js.call('decode', response.json()['data'])
    print(res)


if __name__ == '__main__':
    for i in range(1, 11):
        func(i)
