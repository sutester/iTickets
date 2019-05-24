#!/usr/bin/env python
# coding: utf-8
'''
@author: Danny
@contact: kedanlin@hotmail.com
@file: work.py
@time: 2019/5/16 21:51
@desc:
'''

from requests import session
from datetime import datetime
import os, time

S = session()
FilePath = r'./images/captchaSource/'
Host = r'https://huaxi2.mobimedical.cn/index.php'


def get_departments_list(sessionid):
    header = {
        "Accept":
        "*/*",
        "X-Requested-With":
        "XMLHttpRequest",
        "User-Agent":
        r"Mozilla/5.0 (Linux; Android 9; ONEPLUS A6010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044607 Mobile Safari/537.36 MMWEBID/9309 MicroMessenger/7.0.3.1400(0x2700033C) Process/tools NetType/WIFI Language/zh_CN",
        "Referer":
        r"https://huaxi2.mobimedical.cn/index.php?g=Wap&m=WxView&d=registerAndAppoint&a=index",
        "Cookie":
        "PHPSESSID={}".format(sessionid)
    }
    params = {"g": "WapApi", "m": "Register", "a": "dutyDeptList", "ts": "0"}
    response = S.get(Host, headers=header, params=params, verify=False).json()
    assert response.get('state') == 1
    assert response.get('errorMsg') == '成功'
    return response


def get_doctor_list(sessionid):
    header = {
        "Accept":
        "*/*",
        "Origin":
        "https://huaxi2.mobimedical.cn",
        "X-Requested-With":
        "XMLHttpRequest",
        "User-Agent":
        r"Mozilla/5.0 (Linux; Android 9; ONEPLUS A6010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044607 Mobile Safari/537.36 MMWEBID/9309 MicroMessenger/7.0.3.1400(0x2700033C) Process/tools NetType/WIFI Language/zh_CN",
        "Referer":
        r"https://huaxi2.mobimedical.cn/index.php?g=Wap&m=WxView&d=registerAndAppoint&a=index",
        "Cookie":
        "PHPSESSID={}".format(sessionid)
    }
    params = {"g": "WapApi", "m": "Register", "a": "getDoctorList"}
    data = {
        "deptId": "16",
        "date": "2019-05-31",
        "SessionType": "",
        "LabelId": "0",
        "districtCode": "2"
    }
    response = S.post(
        Host, headers=header, params=params, data=data, verify=False).json()
    return response


def get_doctor_detail(sessionid):
    header = {
        "Accept":
        "*/*",
        "Origin":
        "https://huaxi2.mobimedical.cn",
        "X-Requested-With":
        "XMLHttpRequest",
        "User-Agent":
        r"Mozilla/5.0 (Linux; Android 9; ONEPLUS A6010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044607 Mobile Safari/537.36 MMWEBID/9309 MicroMessenger/7.0.3.1400(0x2700033C) Process/tools NetType/WIFI Language/zh_CN",
        "Referer":
        r"https://huaxi2.mobimedical.cn/index.php?g=Wap&m=WxView&d=registerAndAppoint&a=index",
        "Cookie":
        "PHPSESSID={}".format(sessionid)
    }
    params = {"g": "WapApi", "m": "Register", "a": "getDoctorDetail"}
    data = {
        "doctorid": "3610",
        "date": "2019-05-31",
        "LabelId": "0",
        "districtCode": "2"
    }
    response = S.post(
        Host, headers=header, params=params, data=data, verify=False).json()
    return response


def get_card_list(sessionid):
    header = {
        "Accept":
        "*/*",
        "Origin":
        "https://huaxi2.mobimedical.cn",
        "X-Requested-With":
        "XMLHttpRequest",
        "User-Agent":
        r"Mozilla/5.0 (Linux; Android 9; ONEPLUS A6010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044607 Mobile Safari/537.36 MMWEBID/9309 MicroMessenger/7.0.3.1400(0x2700033C) Process/tools NetType/WIFI Language/zh_CN",
        "Referer":
        r"https://huaxi2.mobimedical.cn/index.php?g=Wap&m=WxView&d=registerAndAppoint&a=index",
        "Cookie":
        "PHPSESSID={}".format(sessionid)
    }
    params = {"g": "WapApi", "m": "Card", "a": "cardList"}
    response = S.get(Host, headers=header, params=params, verify=False).json()
    return response


def get_reg_queue_start(sessionid):
    header = {
        "Accept":
        "*/*",
        "Origin":
        "https://huaxi2.mobimedical.cn",
        "X-Requested-With":
        "XMLHttpRequest",
        "User-Agent":
        r"Mozilla/5.0 (Linux; Android 9; ONEPLUS A6010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044607 Mobile Safari/537.36 MMWEBID/9309 MicroMessenger/7.0.3.1400(0x2700033C) Process/tools NetType/WIFI Language/zh_CN",
        "Referer":
        r"https://huaxi2.mobimedical.cn/index.php?g=Wap&m=WxView&d=registerAndAppoint&a=index",
        "Cookie":
        "PHPSESSID={}".format(sessionid)
    }
    params = {
        "g": "WapApi",
        "m": "Register",
        "a": "getRegQueueStart",
        "schedulid": "40517"
    }
    response = S.get(Host, headers=header, params=params, verify=False).json()
    return response


def create_verify(sessionid):
    header = {
        "Accept":
        "*/*",
        "Origin":
        "https://huaxi2.mobimedical.cn",
        "X-Requested-With":
        "XMLHttpRequest",
        "User-Agent":
        r"Mozilla/5.0 (Linux; Android 9; ONEPLUS A6010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044607 Mobile Safari/537.36 MMWEBID/9309 MicroMessenger/7.0.3.1400(0x2700033C) Process/tools NetType/WIFI Language/zh_CN",
        "Referer":
        r"https://huaxi2.mobimedical.cn/index.php?g=Wap&m=WxView&d=registerAndAppoint&a=index",
        "Cookie":
        "PHPSESSID={}".format(sessionid)
    }
    params = {
        "g": "WapApi",
        "m": "FeyVerify",
        "a": "createVerify",
        "v": "0.781006613455341"
    }
    response = S.get(Host, headers=header, params=params, verify=False)

    times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timeArray = time.strptime(times, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))

    with open(FilePath + 'MathTest' + str(timeStamp) + '.jpg', 'wb') as f:
        f.write(response.content)
        f.close()
    #return response.text


def submit_order(sessionid):
    header = {
        "Accept":
            "*/*",
        "Origin":
            "https://huaxi2.mobimedical.cn",
        "X-Requested-With":
            "XMLHttpRequest",
        "User-Agent":
            r"Mozilla/5.0 (Linux; Android 9; ONEPLUS A6010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044607 Mobile Safari/537.36 MMWEBID/9309 MicroMessenger/7.0.3.1400(0x2700033C) Process/tools NetType/WIFI Language/zh_CN",
        "Referer":
            r"https://huaxi2.mobimedical.cn/index.php?g=Wap&m=WxView&d=registerAndAppoint&a=index",
        "Cookie":
            "PHPSESSID={}".format(sessionid)
    }
    params = {"g": "WapApi", "m": "Register", "a": "submitReg"}
    data = {
        "tagArray": "90,496",
        "schedulid": "39789",
        "userid": "2201256",
        "is_ai": "",
        "token":"wx155869757230528"
    }
    response = S.post(
        Host, headers=header, params=params, data=data, verify=False).json()
    assert response.get('state') == 1
    assert response.get('errorMsg') == '成功'
    return response

def get_unpaid_list(sessionid):
    header = {
        "Accept":
            "*/*",
        "Origin":
            "https://huaxi2.mobimedical.cn",
        "X-Requested-With":
            "XMLHttpRequest",
        "User-Agent":
            r"Mozilla/5.0 (Linux; Android 9; ONEPLUS A6010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044607 Mobile Safari/537.36 MMWEBID/9309 MicroMessenger/7.0.3.1400(0x2700033C) Process/tools NetType/WIFI Language/zh_CN",
        "Referer":
            r"https://huaxi2.mobimedical.cn/index.php?g=Wap&m=WxView&d=registerAndAppoint&a=index",
        "Cookie":
            "PHPSESSID={}".format(sessionid)
    }
    params = {"g": "WapApi", "m": "OrderApi", "a": "waitPayList"}
    response = S.get(
        Host, headers=header, params=params, verify=False).json()
    assert response.get('state') == 1
    assert response.get('errorMsg') == '成功'
    return response

if __name__ == '__main__':
    import io, sys
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
    sessionid = 'qra14valb8b4c7r4oq08l265g4'
    print(get_departments_list(sessionid))
    # print(get_doctor_detail())
    # print(get_doctor_list())
    # print(get_card_list())
    # print(get_reg_queue_start())
    # print(create_verify())
    # print(get_unpaid_list())
