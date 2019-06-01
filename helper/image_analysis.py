#!/usr/local/bin/pyenv/python
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2019-05-24 14:09:38
# @Last Modified by:   Danny
# @Last Modified time: 2019-05-24 14:09:38

from . import cut_img
from .BD_Identifier import captchaIdentifier
from .BD_Identifier import objIdentifier
import base64

class ImageAnalysis:
    def __init__(self,session):
        self.session = session
        self.ci = captchaIdentifier(self.session)
        self.oi = objIdentifier(self.session)

    def get_image(self,file_path):
        with open(file_path,'rb') as f:
            return base64.b64encode(f.read())

    def get_question_title(self,file_path):
        '''
        To get the text of the question
        :param file_path:
        :return: question text
        '''
        return self.ci.getText(self.get_image(file_path))

    def get_question_type(self,question):
        if '计算' in question:
            return 1
        elif '对应' in question:
            return 2
        else:
            return 0

    def get_answer(self,question):
        question = question.replace('?','')
        if self.get_question_type(question):
            if self.get_question_type(question) == 1:
                question = question.split('结果')[1]
                if '加' in question:
                    m,n = question.split('加')
                    return int(m) + int(n)
                elif '减' in question:
                    m,n = question.split('减')
                    return int(m) - int(n)
                elif '乘' in question:
                    m,n = question.split('乘')
                    return int(m) * int(n)
                elif '除' in question:
                    m,n = question.split('除')
                    return int(m) / int(n)
                else:
                    raise SystemError
            else:
                question = question.split('图片')[1]

if __name__ == '__main__':
    FilePath = r'../images/'
    from requests import session
    s = session()
