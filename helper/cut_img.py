#!/usr/local/bin/pyenv/python
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2019-05-24 14:05:50
# @Last Modified by:   Danny
# @Last Modified time: 2019-05-24 14:05:50

import cv2

answers_location = [(150, 355, 0, 206), (150, 355, 206, 412),
                    (150, 355, 412, 618), (150, 355, 618, 824), (355, 558, 0,
                                                                 206),
                    (355, 558, 206, 412), (355, 558, 412, 618), (355, 558, 618,
                                                                 824)]
FilePath = r'./images/captchaSource/'


def cut_question(old_file_name, question_file_name):
    img = cv2.imread(FilePath + old_file_name)
    question = img[0:150, 0:824]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(FilePath + question_file_name, question)


def cut_answer(old_file_name):
    img = cv2.imread(FilePath + old_file_name)
    i = 1
    for al in answers_location:
        answer = img[al[0]:al[1], al[2]:al[3]]
        cv2.imwrite(FilePath + str(i) + '_' + old_file_name, answer)
        i = i + 1


if __name__ == '__main__':
    cut_answer('math.jpg')
    cut_question('math.jpg', 'math_question.jpg')
