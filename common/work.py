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
        "date": appointmentDate,
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
        "date": appointmentDate,
        "LabelId": "0",
        "districtCode": "2"
    }
    response = S.post(Host, headers=header, params=params, data=data, verify=False).json()

    for i in range (len(response['data']['schedul'])):
        if response['data']['schedul'][i]['date'] == appointmentDate:
            scheduleId = response['data']['schedul'][i]['schedulid']
    '''
    Here now returns only schedule id which is different with others.
    '''
    return scheduleId


def get_card_list(sessionid,patientName):
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
    for i in range (len(response['data']['cardList'])):
        if response['data']['cardList'][i]['userName'] == patientName:
            userid = response['data']['cardList'][i]['userid']
    '''
    Here now returns only user id which is different with others.
    '''

    return userid


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

    #with open(FilePath + 'MathTest' + str(timeStamp) + '.jpg', 'wb') as f:
    with open(FilePath + 'Math' + '.jpg', 'wb') as f:
        f.write(response.content)
        f.close()
    return response
    

'''
change the name of the funtion to follow the URL parameter. This would be easily to locate from charles

'''
def submit_Reg(sessionid):
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
        "schedulid": "41282",
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
    patientName = '柯骚骚'
    appointmentDate = '2019-05-31'
    sessionid = 'ktd65jqcof2fq81gmogmrjdl34'
    #print(get_departments_list(sessionid))
    #print(get_doctor_list(sessionid))
    
    #Get schedule id here
    #print(get_doctor_detail(sessionid))

    #Get user id here
    #print(get_card_list(sessionid,patientName))
    # print(get_reg_queue_start())
    print(create_verify(sessionid))
    # print(get_unpaid_list())
