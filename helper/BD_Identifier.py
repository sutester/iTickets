# encoding:utf-8
'''
captcha identify
'''
#Define access token. once the token been issued it would be validated for 30 mins.
accessToken = '24.8603abe537c4061b66b3dbe1875299f0.2592000.1561554145.282335-16148227'


class captchaIdentifier():
    def __init__(self, s):
        self.api_url = r'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'
        self.S = s
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def getText(self, img):
        params = {"access_token": accessToken}
        data = {"image": img}
        r = self.S.post(
            url=self.api_url,
            params=params,
            data=data,
            headers=self.headers,
            verify=False).json()
        return r
        # return r.get('words_result')[0].get(
        #     'words') if r.get('words_result_num') > 0 else None


class objIdentifier():
    def __init__(self, s):
        self.S = s
        self.api_url = r'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general'
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def getText(self, img):
        data = {"image": img}
        params = {"access_token": accessToken}
        r = self.S.post(
            url=self.api_url,
            params=params,
            data=data,
            headers=self.headers,
            verify=False).json()
        return r.get('result')[0].get(
            'keyword') if r.get('result_num') > 0 else None


if __name__ == '__main__':
    FilePath = r'./images/'
    from requests import session
    s = session()
    import base64
    import io, sys
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

    def get_image(file_path):
        with open(file_path, 'rb') as f:
            return base64.b64encode(f.read())

    ci = captchaIdentifier(s)
    print(ci.getText(get_image(FilePath + 'test1.png')))

    # oid = objIdentifier(s)
    # print(oid.getText(get_image(FilePath+'banana.jpg')))