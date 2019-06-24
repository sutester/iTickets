#!/usr/local/bin/pyenv/python
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2019-05-24 14:05:50
# @Last Modified by:   Danny
# @Last Modified time: 2019-05-24 14:05:50

import cv2, os

answers_location = [(150, 355, 0, 206), (150, 355, 206, 412),
                    (150, 355, 412, 618), (150, 355, 618, 824), (355, 558, 0,
                                                                 206),
                    (355, 558, 206, 412), (355, 558, 412, 618), (355, 558, 618,
                                                                 824)]
FilePath = os.path.abspath(os.path.join(os.getcwd(), ".")) + r'/images/'
print(FilePath)

def cut_question(old_file_name, question_file_name, position):
    img = cv2.imread(FilePath + old_file_name)
    if position == 'right':
        question = img[0:150, 395:824]  # 裁剪坐标为[y0:y1, x0:x1]
    elif position == 'left':
        question = img[0:150, 0:824]  # 裁剪坐标为[y0:y1, x0:x1]
    else:
        raise RuntimeError(
            'Please define the position of the question then try again.')
    cv2.imwrite(FilePath + question_file_name, question)
    return FilePath + question_file_name


def cut_answer(old_file_name):
    img = cv2.imread(FilePath + old_file_name)
    i = 0
    answerNames = []
    for al in answers_location:
        answer = img[al[0]:al[1], al[2]:al[3]]
        cv2.imwrite(FilePath + old_file_name[0:len(old_file_name) - 4] +
                    '_answer_' + str(i) + '.jpg', answer)
        answerNames.append(FilePath + old_file_name[0:len(old_file_name) - 4] +
                           '_answer_' + str(i) + '.jpg')
        i = i + 1
    return answerNames


if __name__ == '__main__':
    #cut_answer('math.jpg')
    #print(cut_question('captchaSource/math.jpg', 'MathTest_right.jpg', 'right'))
    print (cut_question('MathTest1561370213.jpg','questionLeft.jpg','left'))
    #print(cut_answer('captchaSource/math.jpg'))
