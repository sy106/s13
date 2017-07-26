# -*- coding :utf-8 -*-
from wsgiref.simple_server import make_server
from controler import account


URL_DICT={

    "/index":account.handle_index,
    "/date":account.handle_date,
}

def RunServer(environ, start_response):
    # environ客户端发来的所有的数据
    # start_response封装要返回给用户的数据，响应头状态
    start_response('200 OK', [('Content-Type', 'text/html')])
    current_url=environ['PATH_INFO']
    if current_url in URL_DICT:
            func=URL_DICT[current_url]
            if func:
                    return func()
            else:
                    return [bytes('<h1>404!</h1>', encoding='utf-8'), ]
    # if current_url=='/index':
    #     return handle_index()
    # elif current_url =='/date':
    #    return handle_date()
    # else:
    # # 返回的内容
    #     return [bytes('<h1>404!</h1>', encoding='utf-8'), ]


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()