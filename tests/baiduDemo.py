# encoding:utf-8
import base64,requests,urllib

'''
captcha identify
'''
accessToken = '24.423397567fe9b74a66027545c46ebbb5.2592000.1559198404.282335-16148227'

class captchaIdentifier():
    def __init__(self,filePath):
        self.filePath = filePath

    def base64Encode(self):
        f = open(r'/Users/squallyang/Documents/Python_WorkSpace/aiDemo/3311.png', 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        self.params = urllib.parse.urlencode(params)
        return self.params
    
    def getText(self):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token="+accessToken
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        r = requests.post(url=request_url,data=self.base64Encode,headers=headers)
        print (r.text)



ci = captchaIdentifier('/Users/squallyang/Documents/Python_WorkSpace/aiDemo/3311.png')
ci.getText()
