"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

http_application = get_asgi_application()


async def websocket_application(scope, receive, send):
    while True:
        event = await receive()
        print('[event]',event)

        # 收到建立websocket连接的消息
        if event['type'] == 'websocket.connect':
            await send({'type': 'websocket.accept'})
        # 收到中断websocket连接的消息
        elif event['type'] == 'websocket.disconnect':
            break
        # 其他情况，正常的websocket消息
        elif event['type'] =='websocket.receive':
            if event['text'] == 'ping':
                await send({
                    'type': 'websocket.send',
                    'text': 'pong'
                })
        else:
            pass
    print('[disconnect]')


async def application(scope, receive, send):
    print('scope:',scope)
    if scope['type'] == 'http':
        await http_application(scope, receive, send)
    elif scope['type'] == 'websocket':
        await websocket_application(scope, receive, send)
    else:
        raise Exception('unkown scope type, ',scope['type'])