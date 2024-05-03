from typing import Any
from flask import Request


def rcv(request: Request) -> Any:
    return "recv"

def sendToStream(body: dict[str, str]) -> None:
    """ Goocle cloud のpub/subにbodyを送信する
    """
    
    # メッセージを送信する
    message = body["message"]
    
    if not isinstance(message, str):
        return
    
    print("Sending to stream: {}".format(message))
    
