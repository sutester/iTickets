#!/usr/local/bin/pyenv/python
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2019-05-24 14:09:38
# @Last Modified by:   Danny
# @Last Modified time: 2019-05-24 14:09:38

import cut_img,testIdentifier
FilePath = r'./images/captchaSource/'
cut_img.cut_answer('math.jpg')
cut_img.cut_question('math.jpg', 'math_question.jpg')
ci = testIdentifier.captchaIdentifier(FilePath+'math_question.jpg')
ci.getText()