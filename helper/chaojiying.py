#!/usr/bin/env python
# coding:utf-8

#有积分限制，省着点用

import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    #有积分限制，省着点用

	#用户中心>>软件ID 生成一个替换 96001
    chaojiying = Chaojiying_Client('stone0214', 'Perf1234', '900031')	
	#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    #im = open('questionRight1560695076827.jpg', 'rb').read()
    im = open('demo_answer_1.jpg', 'rb').read()
	#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    print (chaojiying.PostPic(im, 1004))											
    
        #im = open('questionRight1560695076827.jpg', 'rb').read()
    im = open('demo_answer_2.jpg', 'rb').read()
	#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    print (chaojiying.PostPic(im, 1004))	

        #im = open('questionRight1560695076827.jpg', 'rb').read()
    im = open('demo_answer_3.jpg', 'rb').read()
	#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    print (chaojiying.PostPic(im, 1004))	

        #im = open('questionRight1560695076827.jpg', 'rb').read()
    im = open('demo_answer_4.jpg', 'rb').read()
	#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    print (chaojiying.PostPic(im, 1004))	

        #im = open('questionRight1560695076827.jpg', 'rb').read()
    im = open('demo_answer_5.jpg', 'rb').read()
	#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    print (chaojiying.PostPic(im, 1004))	

        #im = open('questionRight1560695076827.jpg', 'rb').read()
    im = open('demo_answer_6.jpg', 'rb').read()
	#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    print (chaojiying.PostPic(im, 1004))	

        #im = open('questionRight1560695076827.jpg', 'rb').read()
    im = open('demo_answer_7.jpg', 'rb').read()
	#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    print (chaojiying.PostPic(im, 1004))	

        #im = open('questionRight1560695076827.jpg', 'rb').read()
    im = open('demo_answer_8.jpg', 'rb').read()
	#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    print (chaojiying.PostPic(im, 1004))	


