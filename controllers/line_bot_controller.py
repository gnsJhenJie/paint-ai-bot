'''
當用戶關注時，必須取用照片，並存放至指定bucket位置，而後生成User物件，存回db
當用戶取消關注時，
    從資料庫提取用戶數據，修改用戶的封鎖狀態後，存回資料庫
'''

from linebot import (
    LineBotApi, WebhookHandler
)
import os

# 載入Follow事件
from linebot.models.events import (
    FollowEvent, UnfollowEvent
)

from services.image_service import ImageService
from services.user_service import UserService
from services.video_service import VideoService
from services.audio_service import AudioService
from services.text_service import TextService
from services.postback_service import PostbackService

from urllib.parse import parse_qs


class LineBotController:

    # 將消息交給用戶服務處理
    @classmethod
    def follow_event(cls, event):
        # print(event)
        UserService.line_user_follow(event)

    @classmethod
    def unfollow_event(cls, event):
        UserService.line_user_unfollow(event)

    # 未來可能會判斷用戶快取狀態
    @classmethod
    def handle_text_message(cls, event):
        TextService.handle_text_message(event)
        return "OK"

    # 用戶收到照片時的處理辦法
    @classmethod
    def handle_image_message(cls, event):
        ImageService.line_user_upload_image(event)
        return "OK"

    # 用戶收到照片時的處理辦法
    @classmethod
    def handle_video_message(cls, event):
        VideoService.line_user_upload_video(event)
        return "OK"

    @classmethod
    def handle_audio_message(cls, event):
        AudioService.line_user_upload_video(event)
        return "OK"

    # 擷取event的data欄位，並依照function_name，丟入不同的方法
    @classmethod
    def handle_postback_event(cls, event):

        '''
        # query string 拆解 event.postback.data
        query_string_dict = parse_qs(event.postback.data)

        # 擷取功能
        detect_function_name = query_string_dict.get('function_name')[0]
        '''

        data_dict = event.postback.data.split('_')
        
        if data_dict[0] == 's1':
            PostbackService.handle_choose_artist(event)
        elif data_dict[0] == 's2':
            PostbackService.handle_choose_artwork(event)

        # Postbakc function 功能對應轉發


        return "OK"