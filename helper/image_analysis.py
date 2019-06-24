#!/usr/local/bin/pyenv/python
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2019-05-24 14:09:38
# @Last Modified by:   Danny
# @Last Modified time: 2019-05-24 14:09:38
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helper.BD_Identifier import captchaIdentifier
from helper.BD_Identifier import objIdentifier
import base64


class ImageAnalysis:
    def __init__(self, session):
        self.session = session
        self.ci = captchaIdentifier(self.session)
        self.oi = objIdentifier(self.session)

    def get_question_title(self, file_path):
        '''
        To get the text of the question
        :param file_path:
        :return: question text
        '''
        return self.ci.getText(get_image(file_path, 'base64'))

    def get_question_type(self, question):
        if u'计算' in question:
            return 1
        elif u'应用' in question:
            return 2
        else:
            return 0


def get_image(file_path, _type='None'):
    with open(file_path, 'rb') as f:
        if _type == 'base64':
            return base64.b64encode(f.read())
        else:
            return f.read()


def match_answer(expectationResult, actuallyResultList):
    if expectationResult in actuallyResultList:
        return actuallyResultList.index(expectationResult)
    else:
        return None


def getExpectationResult(CC, filename):
    expectationResult = CC.PostPic(get_image(filename), 6003)
    print(expectationResult)
    if expectationResult.get('err_no') == 0 and expectationResult.get(
            'err_str') == 'OK':
        return expectationResult.get('pic_str')


def getActuallyResultList(CC, fileNames):
    actuallyResultList = []
    for filename in fileNames:
        actuallyResult = CC.PostPic(get_image(filename), 1004)
        if actuallyResult.get('err_no') == 0 and actuallyResult.get(
                'err_str') == 'OK':
            actuallyResultList.append(actuallyResult.get('pic_str'))
        else:
            actuallyResultList.append('Error')
    return actuallyResultList


if __name__ == '__main__':
    import io, sys, os, time
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
    _path = os.path.abspath(os.path.join(os.getcwd(), "."))
    from helper.chaojiying import Chaojiying_Client as CC
    from helper import cut_img
    from datas.get_location import get_location
    FilePath = _path + r'/images/'
    # 判断问题类型
    import requests
    S = requests.session()
    ia = ImageAnalysis(S)
    question_type_pic = cut_img.cut_question(
        'captchaSource/math.jpg', 'captchaSource/MathTest_left.jpg', 'left')
    #im = get_image(question_type_pic, 'base64')
    text = ia.get_question_title(question_type_pic)
    print(text)
    q_type = ia.get_question_type(text)
    print(q_type)
    if q_type == 1:
        answers = cut_img.cut_answer('captchaSource/math.jpg')
        question = cut_img.cut_question('captchaSource/math.jpg',
                                        'captchaSource/MathTest_right.jpg',
                                        'right')
        cc = CC('stone0214', '12345678', '90031')
        e = getExpectationResult(cc, question)
        a = getActuallyResultList(cc, answers)
        print(e, a)
        print(match_answer(e, a))
        print(get_location(match_answer(e, a)))
