from flask import Request


def rcv(request: Request):
    print(request.headers)
    return "recv"