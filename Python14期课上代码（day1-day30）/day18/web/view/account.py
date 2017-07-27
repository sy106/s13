import time
def handle_index():
    # 返回的内容
    v=str(time.time())
    f=open('template/index.html',mode='rb')
    data=f.read()
    f.close()
    data=data.replace(b'@uuuuu',v.encode('utf-8'))
    return [data,]
    # return [bytes('<h1>Hello, index!</h1>', encoding='utf-8'), ]
def handle_date():
    # 返回的内容
    return [bytes('<h1>Hello, date!</h1>', encoding='utf-8'), ]