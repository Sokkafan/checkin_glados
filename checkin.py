import requests
import json
import os

def start():
    # 从 GitHub Secrets 中读取 Cookie
    cookie = os.environ.get("GLADOS_COOKIE")
    if not cookie:
        print("未获取到 COOKIE，请检查 Secrets 配置")
        return

    url = "https://glados.cloud/api/user/checkin"
    url2 = "https://glados.cloud/api/user/status"
    origin = "https://glados.cloud"
    referer = "https://glados.cloud/console/checkin"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    
    # 签到负载
    payload = {'token': 'glados.one'}
    
    checkin = requests.post(url, headers={
        'cookie': cookie,
        'referer': referer,
        'origin': origin,
        'user-agent': user_agent,
        'content-type': 'application/json;charset=UTF-8'
    }, data=json.dumps(payload))

    state = requests.get(url2, headers={
        'cookie': cookie,
        'referer': referer,
        'origin': origin,
        'user-agent': user_agent
    })

    # 输出结果
    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        print(f"签到状态: {mess}")
        print(f"剩余天数: {int(float(time))} 天")
    else:
        print("签到失败，请检查 Cookie 是否过期")

if __name__ == '__main__':
    start()
