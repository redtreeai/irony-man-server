# -*- coding: utf-8 -*-
# @Time    : 19-6-3 下午4:53
# @Author  : Redtree
# @File    : s.py
# @Desc :


import asyncio
import json
import logging
import websockets

logging.basicConfig()

USERS = set()

#说话事件
def talk_event(msg,head_img):
    return json.dumps({'type': 'talk', 'text':msg,'head_img':head_img})

#用户数据，进入房间或退出房间后广播
def users_event():
    return json.dumps({'type': 'users', 'count': len(USERS)})

#房间人数超过100后，提示满员
def overflow_event():
    return json.dumps({'type': 'users_over', 'count': len(USERS)})

async def notify_talk(msg,head_img):
    if USERS:       # asyncio.wait doesn't accept an empty list
        message = talk_event(msg,head_img)
        await asyncio.wait([user.send(message) for user in USERS])

async def notify_users():
    if USERS:       # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])

async def register(websocket):
    USERS.add(websocket)
    await notify_users()

async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()

async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    #房间目前支持100个人
    if len(USERS)>=2:
        await websocket.send(overflow_event())
    else:
        await register(websocket)
        try:
            async for message in websocket:
                data = json.loads(message)
                if data['action'] == 'talk':
                    msg = data['text']
                    head_img = data['head_img']
                    await notify_talk(msg,head_img)
                else:
                    logging.error(
                        "unsupported event: {}", data)
        finally:
            await unregister(websocket)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(counter, '0.0.0.0',6789))
asyncio.get_event_loop().run_forever()