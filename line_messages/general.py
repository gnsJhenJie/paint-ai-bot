from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, CarouselTemplate, FlexSendMessage,
    CarouselColumn, ImageCarouselColumn, ImageCarouselTemplate, PostbackAction, QuickReply,
    QuickReplyButton, MessageAction
)
import random

def welcome():
    return [TextSendMessage(
        text='趕快輸入「開始使用」來試試看吧!無聊的時候也可以傳訊息找我聊天喔!',
        quick_reply=QuickReply(items=[
            QuickReplyButton(action=MessageAction(label="開始使用",text="開始使用"))
        ])
    )]

def s01_choose_artist():
    replys_1 = ["請選一位喜歡的藝術家吧：）", "請選一位喜歡的藝術家吧!", "請選一位喜歡的藝術家吧!啾啾啾", "請幫啾啾選擇一位喜歡的藝術家~"]
    return [TextSendMessage(text=replys_1[random.randint(0,len(replys_1)-1)]),
    TemplateSendMessage(
        alt_text='選擇一位喜歡的藝術家',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/artists/01_van_gogh.jpeg',
                    action=PostbackAction(
                        label='梵谷',
                        display_text='我喜歡梵谷',
                        data='s1_1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/artists/02_escher.jpeg',
                    action=PostbackAction(
                        label='艾雪',
                        display_text='我想選艾雪',
                        data='s1_2'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/artists/03_sakai_hoitsu.jpeg',
                    action=PostbackAction(
                        label='酒井抱一',
                        display_text='我選酒井抱一!',
                        data='s1_3'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/artists/04_Leonid_Afremov.jpeg',
                    action=PostbackAction(
                        label='阿夫列莫夫',
                        display_text='Leonid Afremov~',
                        data='s1_4'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/artists/05_frida_kahlo.jpeg',
                    action=PostbackAction(
                        label='芙烈達·卡蘿',
                        display_text='Frida Kahlo !!',
                        data='s1_5'
                    )
                )
            ]
        )
    )]

s_02_replys_1 = ["告訴啾啾你最喜歡哪幅畫吧~", "告訴啾啾你最喜歡哪幅畫吧!", "告訴啾啾你最喜歡哪幅畫吧:)", "請選擇一幅喜歡的畫作!", "選一幅畫給啾啾吧!"]

def s02_choose_artwork_01():
    return [TextSendMessage(text=s_02_replys_1[random.randint(0,len(s_02_replys_1)-1)]),
    TemplateSendMessage(
        alt_text='告訴啾啾你最喜歡哪幅畫吧~',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/01_01_starry_night.jpeg',
                    action=PostbackAction(
                        label='星夜',
                        display_text='我選梵谷的星夜!',
                        data='s2_1_1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/01_02_sunflowers.jpeg',
                    action=PostbackAction(
                        label='向日葵',
                        display_text='向日葵讚讚',
                        data='s2_1_2'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/01_03_the_yellow_house.jpeg',
                    action=PostbackAction(
                        label='黃房子',
                        display_text='我要選梵谷的黃房子',
                        data='s2_1_3'
                    )
                )
            ]
        )
    )]

def s02_choose_artwork_02():
    return [TextSendMessage(text=s_02_replys_1[random.randint(0,len(s_02_replys_1)-1)]),
    TemplateSendMessage(
        alt_text='告訴啾啾你最喜歡哪幅畫吧~',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/02_04_water_fall.jpeg',
                    action=PostbackAction(
                        label='瀑布',
                        display_text='瀑布!',
                        data='s2_2_4'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/02_05_ascending_and_descending.jpeg',
                    action=PostbackAction(
                        label='上下階梯',
                        display_text='啾啾!我要選艾雪的上下階梯',
                        data='s2_2_5'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/02_06_ralativity.jpg',
                    action=PostbackAction(
                        label='相對論',
                        display_text='我要艾雪的相對論~不是愛因斯坦的ㄛ',
                        data='s2_1_6'
                    )
                )
            ]
        )
    )]

def s02_choose_artwork_03():
    return [TextSendMessage(text=s_02_replys_1[random.randint(0,len(s_02_replys_1)-1)]),
    TemplateSendMessage(
        alt_text='告訴啾啾你最喜歡哪幅畫吧~',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/03_07_unknown.jpeg',
                    action=PostbackAction(
                        label='選擇這幅',
                        display_text='我要選酒井抱一的這幅畫~',
                        data='s2_3_7'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/03_08_flower_and_bird.jpeg',
                    action=PostbackAction(
                        label='花鳥圖屏風',
                        display_text='就決定是花鳥圖屏風了!',
                        data='s2_3_8'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/03_09_flowers_and_birds_seasons.jpeg',
                    action=PostbackAction(
                        label='四季花鳥圖屏風',
                        display_text='四季花鳥圖屏風~~',
                        data='s2_3_9'
                    )
                )
            ]
        )
    )]

def s02_choose_artwork_04():
    return [TextSendMessage(text=s_02_replys_1[random.randint(0,len(s_02_replys_1)-1)]),
    TemplateSendMessage(
        alt_text='告訴啾啾你最喜歡哪幅畫吧~',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/04_10_first_impression.jpeg',
                    action=PostbackAction(
                        label='第一印象',
                        display_text='啾啾請幫我畫Leonid Afremov的第一印象!',
                        data='s2_4_10'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/04_11_unknown.jpeg',
                    action=PostbackAction(
                        label='選擇這張',
                        display_text='啾啾!我要選這張~',
                        data='s2_4_11'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/04_12_unknown.jpeg',
                    action=PostbackAction(
                        label='選擇這張',
                        display_text='啾啾~我要選Afremov的這張畫~',
                        data='s2_4_12'
                    )
                )
            ]
        )
    )]

def s02_choose_artwork_05():
    return [TextSendMessage(text=s_02_replys_1[random.randint(0,len(s_02_replys_1)-1)]),
    TemplateSendMessage(
        alt_text='告訴啾啾你最喜歡哪幅畫吧~',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/05_13_frida_kahlo.jpeg',
                    action=PostbackAction(
                        label='選這張',
                        display_text='我要選這張~',
                        data='s2_5_13'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/05_14_frida_kahlo.jpeg',
                    action=PostbackAction(
                        label='選這張',
                        display_text='啾啾!我要這張',
                        data='s2_5_14'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://storage.googleapis.com/paint-ai-bot-bucket/000-elements/styles/05_15_frida_kahlo.jpeg',
                    action=PostbackAction(
                        label='選這張',
                        display_text='我要這張:)',
                        data='s2_5_15'
                    )
                )
            ]
        )
    )]

def s03_artwork_selected():
    replys = ['最後一步! 請拍一張或傳一張照片吧~\n啾啾會用你喜歡的畫風畫出來它喔~', "最後~請拍一張照或上傳一張照片吧!\n啾啾會馬上開始幫你畫喔~", "請拍一張或上傳一張照片給啾啾\n啾啾等等就去幫你畫出來~"]
    return [TextSendMessage(text=replys[random.randint(0,len(replys)-1)])]

def s04_drawing():
    replys_1 = ["啾啾正在努力幫你畫呦~因為太多人找我畫了,可能需要等待一天喔~", "啾啾開始畫囉~因為好多人找我畫畫,所以可能要等待一天喔", "我開始幫你畫囉!請耐心等待(好多人在排隊呢...),最多可能需要等待一天喔!"]
    replys_2 = [u"✌🏻",u'✌🏼',u'✌🏽',u'✌🏾',u'✌🏿',u'✌️']
    replys_3 = [u'✊',u'✊🏻',u'✊🏼',u'✊🏽',u'✊🏾',u'✊🏿']
    replys_4 = [u'🖐',u'🖐🏻',u'🖐🏼',u'🖐🏽',u'🖐🏾',u'🖐🏿',u'🤚',u'🤚🏻',u'🤚🏼',u'🤚🏽',u'🤚🏾',u'🤚🏿',u'✋',u'✋🏻',u'✋🏼',u'✋🏽',u'✋🏾',u'✋🏿']
    return [
        TextSendMessage(text=replys_1[random.randint(0,len(replys_1)-1)]),
        TextSendMessage(text="可以先來跟啾啾玩剪刀石頭布(直接傳訊息出拳)或是聊天喔~~", 
                        quick_reply=QuickReply(items=[
                            QuickReplyButton(action=MessageAction(label=replys_2[random.randint(0,len(replys_2)-1)], text="剪刀")),
                            QuickReplyButton(action=MessageAction(label=replys_3[random.randint(0,len(replys_3)-1)], text="石頭")),
                            QuickReplyButton(action=MessageAction(label=replys_4[random.randint(0,len(replys_4)-1)], text="布"))
                        ])
        )
    ]