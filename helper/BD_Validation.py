import os,time
import cut_img
import BD_Identifier
from requests import session
FilePath = r'../images/'

def cutAllRightPart(prefix):
    for root, dirs, files in os.walk(FilePath):
        for file in files:
            if file[0:len(prefix)] == prefix:
                cut_img.cut_question(file,'questionRight'+str(generateTS())+'.jpg','right')

def generateTS():
    timeStamp = int(round(time.time() * 1000))
    return timeStamp

def identifyAll(prefix):
    s = session()
    ci = BD_Identifier.captchaIdentifier(s)
    for root, dirs, files in os.walk(FilePath):
        for file in files:
            if file[0:len(prefix)] == prefix:
                time.sleep(1)
                if len(ci.getText(BD_Identifier.get_image(FilePath + file))['words_result'])==0:
                    os.rename(FilePath+file,FilePath+'none.jpg')
                else:
                    os.rename(FilePath+file,FilePath+ci.getText(BD_Identifier.get_image(FilePath + file))['words_result'][0]['words']+'.jpg')

def checkSuccessRate():
    for root, dirs, files in os.walk(FilePath):
        for file in files:
            if file[0:len('MathTest')] == 'MathTest':
                pass
            else:
                print (file)



if __name__ == '__main__':
    #print(generateTS())
    #cutAllRightPart('MathTest')
    #identifyAll('questionRight')
    #checkSuccessRate()
    cut_img.cut_answer('demp.jpg')

