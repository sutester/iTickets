#!/usr/bin/env python
# coding: utf-8
'''
@author: Danny
@contact: kedanlin@hotmail.com
@file: work.py
@time: 2019/5/16 21:51
@desc:
'''

from datetime import datetime, timedelta
import time, os

FilePath = os.path.abspath(os.path.join(os.getcwd(), ".")) + r'/images'


class Work:
    def __init__(self, S, sessionID):
        self.S = S
        self.sessionID = sessionID
        self.date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        self.host = r'https://huaxi2.mobimedical.cn/index.php'

    def get_departments_list(self, dep_name):
        '''
        :param sessionid:
        :param dep_name:
        :return: Department ID by dep_name
        '''
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
            "PHPSESSID={}".format(self.sessionID)
        }
        params = {
            "g": "WapApi",
            "m": "Register",
            "a": "dutyDeptList",
            "ts": "0"
        }
        response = self.S.get(
            self.host, headers=header, params=params, verify=False).json()
        if response.get('state') == 1 and response.get('errorMsg') == '成功':
            dep_list = response.get('data')
            for dep in dep_list:
                if dep_name in dep.values():
                    return dep.get('deptId')
        else:
            raise RuntimeError('Session was invalid.')

    def get_doctor_list(self, deptId, doctorName):
        '''
        :param sessionid:
        :param deptId:
        :param doctorName:
        :return: Doctor ID by doctorName and deptId
        '''
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
            "PHPSESSID={}".format(self.sessionID)
        }
        params = {"g": "WapApi", "m": "Register", "a": "getDoctorList"}
        data = {
            "deptId": deptId,
            "date": self.date,
            "SessionType": "",
            "LabelId": "0",
            "districtCode": "2"
        }
        response = self.S.post(
            self.host, headers=header, params=params, data=data,
            verify=False).json()
        if response.get('state') == 1 and response.get('errorMsg') == '成功':
            doctor_list = response.get('data')
            for doctor in doctor_list:
                if doctor.get('usable') == 1:
                    if doctor.get('docName') == doctorName:
                        return doctor.get('doctorid')
        else:
            raise RuntimeError('Session was invalid.')

    def get_doctor_detail(self, doctorid):
        '''
        :param sessionid:
        :param doctorid:
        :return: multiple schedulids
        '''
        schedulid = []
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
            "PHPSESSID={}".format(self.sessionID)
        }
        params = {"g": "WapApi", "m": "Register", "a": "getDoctorDetail"}
        data = {
            "doctorid": doctorid,
            "date": self.date,
            "LabelId": "0",
            "districtCode": "2"
        }
        response = self.S.post(
            self.host, headers=header, params=params, data=data,
            verify=False).json()
        if response.get('state') == 1 and response.get('errorMsg') == '成功':
            schedul_list = response.get('data').get('schedul')
            for schedul in schedul_list:
                if schedul.get('usable') == 1:
                    if schedul.get('date') == self.date:
                        schedulid.append(schedul.get('schedulid'))
        else:
            raise RuntimeError('Session was invalid.')
        return schedulid

    def get_card_list(self, patientName):
        '''
        :param sessionid:
        :param patientName:
        :return: userid by patientName
        '''
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
            "PHPSESSID={}".format(self.sessionID)
        }
        params = {"g": "WapApi", "m": "Card", "a": "cardList"}
        response = self.S.get(
            self.host, headers=header, params=params, verify=False).json()
        if response.get('state') == 1 and response.get('errorMsg') == '成功':
            card_list = response.get('data').get('cardList')
            for card in card_list:
                if card.get('userName') == patientName:
                    return card.get('userid')
        else:
            raise RuntimeError('Session was invalid.')

    def get_reg_queue_start(self, schedulid):
        '''
        :param sessionid:
        :param schedulid:
        :return: Token for submit_Reg
        '''
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
            "PHPSESSID={}".format(self.sessionID)
        }
        params = {
            "g": "WapApi",
            "m": "Register",
            "a": "getRegQueueStart",
            "schedulid": schedulid
        }
        response = self.S.get(
            self.host, headers=header, params=params, verify=False).json()
        if response.get('state') == 1 and response.get('errorMsg') == '成功':
            return response.get('data').get('tn')

    def create_verify(self):
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
            "PHPSESSID={}".format(self.sessionID)
        }
        params = {
            "g": "WapApi",
            "m": "FeyVerify",
            "a": "createVerify",
            "v": "0.781006613455341"
        }
        response = self.S.get(
            self.host, headers=header, params=params, verify=False)

        times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timeArray = time.strptime(times, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        pic_name = FilePath + 'MathTest' + str(timeStamp) + '.jpg'
        with open(pic_name, 'wb') as f:
            #with open(FilePath + 'Math' + '.jpg', 'wb') as f:
            f.write(response.content)
        return response, pic_name

    '''
    change the name of the funtion to follow the URL parameter. This would be easily to locate from charles
    
    '''

    def submit_Reg(self, location, schedulId, userId, token):
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
            "PHPSESSID={}".format(self.sessionID)
        }
        params = {"g": "WapApi", "m": "Register", "a": "submitReg"}
        data = {
            "tagArray": location,
            "schedulid": schedulId,
            "userid": userId,
            "is_ai": "",
            "token": token
        }
        response = self.S.post(
            self.host, headers=header, params=params, data=data,
            verify=False).json()
        assert response.get('state') == 1
        assert response.get('errorMsg') == '成功'
        return response

    def get_unpaid_list(self):
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
            "PHPSESSID={}".format(self.sessionID)
        }
        params = {"g": "WapApi", "m": "OrderApi", "a": "waitPayList"}
        response = self.S.get(
            self.host, headers=header, params=params, verify=False).json()
        assert response.get('state') == 1
        assert response.get('errorMsg') == '成功'
        return response


if __name__ == '__main__':
    import io, sys
    from requests import session
    s = session()
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
    patientName = '柯骚骚'
    sessionid = '3k8f34hpq996719qjf21lcr8j6'
    W = Work(S=s, sessionID=sessionid)
    deptId = W.get_departments_list('儿科门诊')
    doctorID = W.get_doctor_list(deptId, '陈永秀')
    #Get schedule id here
    #print(W.get_doctor_detail(doctorID))
    for i in range(0, 1000):
        W.create_verify()
        time.sleep(5)
