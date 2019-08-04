def encode_(text):
    '''加密汉字和英文字母部分
    '''
    new_text = ''
    new_key = []
    global key
    if isinstance(text, str):
        text_list = list(text)
    else:
        return text
    for i, char in enumerate(text_list):
        if is_eng(char) or is_zh(char):
            text_list[i] = chr(ord(char) + 900000)
    for i in text_list:
        new_text += i
    return new_text


def decode_(text):
    '''解密
    '''
    new_text = ''
    text_list = list(text)
    for i, char in enumerate(text_list):
        if ord(char) > 900000:
            text_list[i] = chr(ord(char)-900000)
    for i in text_list:
        new_text += i
    return new_text


def is_zh(uchar):
    '''判断是否是中文汉字
    args:
        uchar: unicode编码的字符
    '''
    if uchar >= u'\u4E00' and uchar <= u'\u9FA5':
        return True
    else:
        return False


def is_eng(uchar):
    '''判断是否是英文字母
    args：
        uchar:unicode编码的字符
    '''
    if (uchar >= u'\u0041' and uchar <= u'\u005A'):
        return True
    elif (uchar >= u'\u0061' and uchar <= u'\u007A'):
        return True
    else:
        return False


if __name__ == '__main__':
    a = encode_(u'你好，a A bZ！z')
    print(a)
    a = decode_(a)
    print(a)
