'''
基於Line給的用戶屬性，定義用戶類別
並提供 to_dict,  from_dict方法，使能在object與dict間快速轉換
提供 __repr__ 快速打印參數
'''
from __future__ import annotations


class User(object):

    # 物件基礎建構式
    def __init__(self, line_user_id, line_user_pic_url, line_user_nickname, line_user_status, line_user_system_language,
                selected_style_id=0, blocked=False, pss_win=0, pss_draw=0, pss_lose=0):
        self.line_user_id = line_user_id
        self.line_user_pic_url = line_user_pic_url
        self.line_user_nickname = line_user_nickname
        self.line_user_status = line_user_status
        self.line_user_system_language = line_user_system_language
        self.selected_style_id = selected_style_id
        self.blocked = blocked
        self.pss_win = pss_win
        self.pss_draw = pss_draw
        self.pss_lose = pss_lose

    # source的欄位係以 資料庫欄位做為預設命名
    @staticmethod
    def from_dict(source: dict) -> User:
        user = User(
            line_user_id=source.get(u'line_user_id'),
            line_user_pic_url=source.get(u'line_user_pic_url'),
            line_user_nickname=source.get(u'line_user_nickname'),
            line_user_status=source.get(u'line_user_status'),
            line_user_system_language=source.get(u'line_user_system_language'),
            selected_style_id=source.get(u'selected_style_id'),
            blocked=source.get(u'blocked'),
            pss_win=source.get(u'pss_win',0),
            pss_draw=source.get(u'pss_draw',0),
            pss_lose=source.get(u'pss_lose',0)
        )

        return user

    def to_dict(self):
        user_dict = {
            "line_user_id": self.line_user_id,
            "line_user_pic_url": self.line_user_pic_url,
            "line_user_nickname": self.line_user_nickname,
            "line_user_status": self.line_user_status,
            "line_user_system_language": self.line_user_system_language,
            "selected_style_id": self.selected_style_id,
            "blocked": self.blocked,
            "pss_win": self.pss_win,
            "pss_draw": self.pss_draw,
            "pss_lose": self.pss_lose
        }
        return user_dict

    def __repr__(self):
        return (f'''User(
            line_user_id={self.line_user_id},
            line_user_pic_url={self.line_user_pic_url},
            line_user_nickname={self.line_user_nickname},
            line_user_status={self.line_user_status},
            line_user_system_language={self.line_user_system_language},
            selected_style_id={self.selected_style_id},
            blocked={self.blocked},
            pss_win={self.pss_win},
            pss_draw={self.pss_draw},
            pss_lose={self.pss_lose}
            )'''
                )