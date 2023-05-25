import json
import cv2
# import pytesseract
# from module import black, median, idverify, white, cardverify, identity

def verified(id,name,key):
    with open("data.json", 'r') as f:
        data = json.load(f)
    # img = cv2.imread(filename)
    # img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
    # if '605' in id:
    #     all_pic = cardverify.result(img)
    #     flag = idverify.verify(all_pic, id)
    #     if flag:
    if id not in data['data'].keys() or name not in data['data'][str(id)]:
        data['data'][str(id)]={"name" : name , "password" : key}
        with open('data.json','w',encoding='utF8') as f:
                json.dump(data,f,indent=4)
        return True
    else:
        return False
    #     else:
    #         return False
    # else:
    #     return False


    
