import os, time
import cut_img
import BD_Identifier
from requests import session

FilePath = r'../images/'


def cut_all_right_part(prefix):
    for root, dirs, files in os.walk(FilePath):
        for file in files:
            if file[0:len(prefix)] == prefix:
                cut_img.cut_question(file, 'questionRight' + str(generate_timestamp()) + '.jpg', 'right')


def generate_timestamp():
    timeStamp = int(round(time.time() * 1000))
    return timeStamp


def identify_all(prefix):
    s = session()
    ci = BD_Identifier.captchaIdentifier(s)
    for root, dirs, files in os.walk(FilePath):
        for file in files:
            if file[0:len(prefix)] == prefix:
                time.sleep(1)
                resultWord = ci.getText(BD_Identifier.get_image(FilePath + file))['words_result']
                if len(resultWord) == 0:
                    print('the file name is ' + file + ' and the file can not be identify')
                    os.rename(FilePath + file, FilePath + 'none.jpg')
                else:
                    print('the file name is ' + file + ' and the value is ' + resultWord[0]['words'])
                    os.rename(FilePath + file, FilePath + resultWord[0]['words'] + '.jpg')


def check_success_rate():
    for root, dirs, files in os.walk(FilePath):
        for file in files:
            if file[0:len('MathTest')] == 'MathTest':
                pass
            else:
                print(file)


if __name__ == '__main__':
    import warnings

    warnings.filterwarnings("ignore")
    # print(generate_timestamp())
    cut_all_right_part('demo')
    # identify_all('questionRight')
    # check_success_rate()
    cut_img.cut_answer('demo.jpg')
    #identify_all('demo_answer')
