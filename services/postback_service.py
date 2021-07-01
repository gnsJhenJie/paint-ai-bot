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

class PostbackService:
    line_bot_api = LineBotApi(channel_access_token=os.environ["LINE_CHANNEL_ACCESS_TOKEN"])

    
    @classmethod
    def handle_choose_artist(cls,event):
        data_dict = event.postback.data.split('_')
        if data_dict[1]=='1':
           cls.line_bot_api.reply_message(
                event.reply_token,
                lmsg.s02_choose_artwork_01()
            )
        elif data_dict[1]=='2':
            cls.line_bot_api.reply_message(
                event.reply_token,
                lmsg.s02_choose_artwork_02()
            )
        elif data_dict[1]=='3':
            cls.line_bot_api.reply_message(
                event.reply_token,
                lmsg.s02_choose_artwork_03()
            )
        elif data_dict[1]=='4':
            cls.line_bot_api.reply_message(
                event.reply_token,
                lmsg.s02_choose_artwork_04()
            )
        elif data_dict[1]=='5':
            cls.line_bot_api.reply_message(
                event.reply_token,
                lmsg.s02_choose_artwork_05()
            )
                

    
    @classmethod
    def handle_choose_artwork(cls,event):
        user = UserDAO.get_user(event.source.user_id)
        user.selected_style_id = int(event.postback.data.split('_')[2])
        UserDAO.save_user(user)

        cls.line_bot_api.reply_message(
            event.reply_token,
            lmsg.s03_artwork_selected()
        )
