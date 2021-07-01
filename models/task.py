'''
負責與db溝通
save_user(user:User) :新增資料時，若有重複資料，則採更新
get_user(user_id:str):取用資料，開放以user_id的方式尋找
'''
from __future__ import annotations
import time

class Task(object):

    # 物件基礎建構式
    def __init__(self, style_id, content_pic_url, status, timestamp=str(time.time())):
        self.style_id = style_id
        self.content_pic_url = content_pic_url
        self.status = status
        self.timestamp = timestamp

    # source的欄位係以 資料庫欄位做為預設命名
    @staticmethod
    def from_dict(source: dict) -> Task:
        task = Task(
            style_id=source.get(u'style_id'),
            content_pic_url=source.get(u'content_pic_url'),
            status=source.get(u'status'),
            timestamp=source.get(u'timestamp'),
        )

        return task

    def to_dict(self):
        user_dict = {
            "style_id": self.style_id,
            "content_pic_url": self.content_pic_url,
            "status": self.status,
            "timestamp": self.timestamp,
        }
        return user_dict

    def __repr__(self):
        return (f'''User(
            style_id={self.style_id},
            content_pic_url={self.content_pic_url},
            status={self.status},
            timestamp={self.timestamp},
            )'''
                )