import pytesseract


def verify(all_pic, id):
    for pic in all_pic:
        text = pytesseract.image_to_string(
            pic, lang='eng')
        text = text.split('\n')
        for ele in text:
            word = ele.replace(" ", "")
            word = word.replace("|", "1")
            word = word.replace("o", "0")
            # print(word)
            if '605' in word and id == word:
                # print(word)
                return True
    else:
        return False
