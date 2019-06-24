#!/usr/local/bin/pyenv/python
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2019-05-24 14:08:10
# @Last Modified by:   Danny
# @Last Modified time: 2019-05-24 14:08:10
import io, sys
from requests import session
from common.work import Work
from helper import cut_img
from helper.image_analysis import ImageAnalysis
from helper.chaojiying import Chaojiying_Client

s = session()
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
patientName = '黄淑华'
sessionid = 'bkfhhpnlrt4eh71uuh0btbvvv6'
W = Work(S=s, sessionID=sessionid)
deptId = W.get_departments_list('麻醉门诊')
doctorID = W.get_doctor_list(deptId, '叶燕熙')
scheduleId = W.get_doctor_detail(doctorID)[0]
tn = W.get_reg_queue_start(scheduleId)
CaptchaFilePath = W.create_verify()[1]
print(deptId)
print(doctorID)
print(scheduleId)
print(tn)
print (CaptchaFilePath)


S = session()
ia = ImageAnalysis(S)
question_type_pic = cut_img.cut_question(CaptchaFilePath, 'MathTest_Question_left.jpg', 'left')

#text = ia.get_question_title(question_type_pic)
#print(text)
#q_type = ia.get_question_type(text)
#print(q_type)



