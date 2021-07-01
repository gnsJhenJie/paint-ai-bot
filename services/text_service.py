from models.user import User
from flask import Request
from linebot import (
    LineBotApi
)

import os
from daos.user_dao import UserDAO
from linebot.models import (
    TextSendMessage
)

import line_messages.general as lmsg
import line_messages.chat as cmsg

class TextService:
    line_bot_api = LineBotApi(channel_access_token=os.environ["LINE_CHANNEL_ACCESS_TOKEN"])

    
    @classmethod
    def handle_text_message(cls,event):
        user = UserDAO.get_user(event.source.user_id)
        nickname = user.line_user_nickname
        message = event.message.text
        msg = cmsg.transform_messsage(message)
        if message == "開始使用" or message == "再來一張":
            cls.line_bot_api.reply_message(
                event.reply_token,
                lmsg.s01_choose_artist()
            )
        elif cmsg.is_hello(msg):
            cls.line_bot_api.reply_message(
                event.reply_token,
                cmsg.hello(nickname)
            )
        elif cmsg.is_scissors(msg):
            cls.line_bot_api.reply_message(
                event.reply_token,
                cmsg.scissors(nickname, user)
            )
        elif cmsg.is_stone(msg):
            cls.line_bot_api.reply_message(
                event.reply_token,
                cmsg.stone(nickname, user)
            )
        elif cmsg.is_paper(msg):
            cls.line_bot_api.reply_message(
                event.reply_token,
                cmsg.paper(nickname, user)
            )
        elif cmsg.is_pss_report(msg):
            cls.line_bot_api.reply_message(
                event.reply_token,
                cmsg.pss_report(nickname, user)
            )
        else:
            cls.line_bot_api.reply_message(
                event.reply_token,
                cmsg.cannot_recongnized(message, user)
            )
