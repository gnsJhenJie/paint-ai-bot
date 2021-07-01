'''

用戶上傳照片時，將照片從Line取回，放入CloudStorage

瀏覽用戶目前擁有多少張照片（未）

'''

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


# 圖片下載與上傳專用
import urllib.request
from google.cloud import storage

# 圖像辨識
import time

import os

from utils.reply_send_message import detect_json_array_to_new_message_array

#model = tensorflow.keras.models.load_model('converted_savedmodel/model.savedmodel')

from google.cloud import firestore
from models.task import Task
from daos.user_dao import UserDAO

import line_messages.general as lmsg

class ImageService:
    line_bot_api = LineBotApi(channel_access_token=os.environ["LINE_CHANNEL_ACCESS_TOKEN"])

    '''
    用戶上傳照片
    將照片取回
    將照片存入CloudStorage內
    '''
    @classmethod
    def line_user_upload_image(cls,event):

        # 取出照片
        image_blob = cls.line_bot_api.get_message_content(event.message.id)
        temp_file_path=f"""{event.message.id}.png"""

        #
        with open(temp_file_path, 'wb') as fd:
            for chunk in image_blob.iter_content():
                fd.write(chunk)

        # 上傳至bucket
        storage_client = storage.Client()
        bucket_name = os.environ['USER_INFO_GS_BUCKET_NAME']
        destination_blob_name = f'{event.source.user_id}/image/{event.message.id}.png'
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(temp_file_path)

        # 建立客戶端
        db = firestore.Client()
        tasks_ref = db.collection(u'tasks')
        task_ref = tasks_ref.document(event.source.user_id)
        task_doc = task_ref.get()

        # 若已在tasks中,不再加入
        if task_doc.exists:
            cls.line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"""你已經有一張圖片正在產生囉~啾啾正在努力幫你畫""")
            )
        else:
            task = Task(
                style_id=UserDAO.get_user(event.source.user_id).selected_style_id,
                content_pic_url=destination_blob_name,
                status=0
            )
            if task.style_id == 0:
                cls.line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"""請先選擇想要啾啾幫你畫的畫風喔~""")
                )
            else:
                tasks_ref.add(document_data=task.to_dict(), document_id=event.source.user_id)
                cls.line_bot_api.reply_message(
                    event.reply_token,
                    lmsg.s04_drawing()
                )
        

        # 回覆消息
        # cls.line_bot_api.reply_message(
        #     event.reply_token,
        #     TextSendMessage(f"""圖片已上傳，請期待未來的AI服務！""")
        # )