# encoding:utf-8
import base64,requests

'''
captcha identify
'''
#Define access token. once the token been issued it would be validated for 30 mins.
accessToken = '24.423397567fe9b74a66027545c46ebbb5.2592000.1559198404.282335-16148227'

class captchaIdentifier():
    def __init__(self,filePath):
        self.filePath = filePath
    
    def getText(self):
        #load pic and encode with base 64
        f = open(self.filePath, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token="+accessToken
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        #send the request wit header and body to get response
        r = requests.post(url=request_url,data=params,headers=headers)
        print (r.text)


class objIdentifier():
    def __init__(self,filePath):
        self.filePath = filePath
    
    def getText(self):
        #load pic and encode with base 64
        f = open(self.filePath, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general?access_token="+accessToken
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        #send the request wit header and body to get response
        r = requests.post(url=request_url,data=params,headers=headers)
        print (r.text)


#ci = captchaIdentifier('/Users/squallyang/Documents/Python_WorkSpace/aiDemo/3311.png')
#ci.getText()
FilePath = r'./images/captchaSource/'
#oi = objIdentifier(FilePath+'math_question.jpg')
#oi.getText()
if __name__ == '__main__':
    ci = captchaIdentifier(FilePath+'question.png')
    ci.getText()
