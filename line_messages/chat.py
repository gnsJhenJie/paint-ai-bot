from linebot.models import (
    TextSendMessage, ImageSendMessage, TemplateSendMessage, CarouselTemplate, FlexSendMessage,
    CarouselColumn, ImageCarouselColumn, ImageCarouselTemplate, PostbackAction, QuickReply,
    QuickReplyButton, MessageAction
)
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.user import User
from daos.user_dao import UserDAO


def transform_messsage(message):
    return message.lower().replace("^","**",3).replace("＋","+",10).replace("－","-",10).replace('＊','*',10).replace('／','/',10).replace('（','(',6).replace('）',')',6).replace('÷','/',5).replace('×','*',5)

def is_hello(msg):
    return msg == 'hi' or msg == '哈囉' or msg == '嗨' or msg == '你好' or msg == '你好啊' or msg.find('bonjour') != -1 or msg.find('hola') != -1 or msg.find('hello') != -1

def hello(nickname):
    replys = ["Hi, "+nickname, "Hello, "+nickname, nickname+"你好啊~", "安安~", "Hola ~~", nickname+"Hola~",
             "安安啊!", nickname+"今天過得好嗎?", nickname+"有想我嗎", nickname+"多跟我玩玩嘛~", "Bonjour", "啾啾跟你說你好!"]
    return [TextSendMessage(text=replys[random.randint(0,len(replys)-1)])]

pss_replys_2 = ["","","","","","","","","","","","\n偷偷告訴你!輸入「剪刀石頭布」就能知道你有多厲害了喔!","\n啾啾告訴你一個秘密!傳「剪刀石頭布」就能知道你的勝率囉","\n傳「剪刀石頭布」給啾啾看看吧!","試著傳「剪刀石頭布」給我吧~"]

def is_scissors(msg):
    return msg == '剪刀' or msg == 'scissors' or msg == u'✂️' or msg == u'✌️' or msg == u'✌🏻' or msg == u'✌🏼' or msg == u'✌🏽' or msg == u'✌🏾' or msg == u'✌🏿'

def scissors(nickname, user: User):
    replys = [
        ["我出剪刀!\n平手~", "剪刀!", "平手OuO", "剪刀: Scissors\n平手: Draw~", "啾啾出剪刀", "平手啦!"+nickname],
        ["石頭~~\n啦啦啦~我贏啦~", "Stone!", "You are too vegetable.", "啾啾出石頭~", "ㄏ~石頭!贏啦!", "嫩!啾啾都比你會玩~\n我出石頭你輸啦!"],
        ["布!你贏啦!\n算你厲害", "我出布!\n...啾啾輸了QQ", "Paper!幫你加1分", "啾啾出布!恭喜你贏了。", "布!不!我輸惹"]
    ]
    r = (random.randint(2,10)//4 + 1 )% 3
    if r==0:
        user.pss_draw+=1
    elif r==1:
        user.pss_lose+=1
    else:
        user.pss_win+=1
    UserDAO.save_user(user)
    return [TextSendMessage(text=replys[r][random.randint(0, len(replys[r])-1)]+pss_replys_2[random.randint(0,len(pss_replys_2)-1)])]

def is_stone(msg):
    return msg == '石頭' or msg == 'stone' or msg == u'✊' or msg == u'✊🏻' or msg == u'✊🏼' or msg == u'✊🏽' or msg == u'✊🏾' or msg == u'✊🏿'

def stone(nickname, user: User):
    replys = [
        ["石頭~~\n平手ㄏㄏ", "Stone!", "~Draw~", "啾啾出石頭~~", "石頭!平手~\n啊不就好棒棒!"],
        ["布!你輸啦!\n算啾啾厲害", "我出布!\n...啾啾贏啦", "Paper!嫩！", "啾啾出布!恭喜你輸了~", "布!你輸了哈哈!"],
        ["我出剪刀!\nSo sad...", "剪刀!輸給"+nickname+"了QQ", "難過@@\n下次一定贏"+nickname+"!", "剪刀:Scissors~\n輸了:Lose...", "輸了QQ\n我出剪刀...", "啾啾出...剪刀!"]
    ]
    r = random.randint(0,7)//3
    if r==0:
        user.pss_draw+=1
    elif r==1:
        user.pss_lose+=1
    else:
        user.pss_win+=1
    UserDAO.save_user(user)
    return [TextSendMessage(text=replys[r][random.randint(0, len(replys[r])-1)]+pss_replys_2[random.randint(0,len(pss_replys_2)-1)])]

def is_paper(msg):
    return msg == '布' or msg == 'paper' or msg == u'🖐' or msg == u'🖐🏻' or msg == u'🖐🏼' or msg == u'🖐🏽' or msg == u'🖐🏾' or msg == u'🖐🏿' or msg == u'🤚' or msg == u'🤚🏻' or msg == u'🤚🏼' or msg == u'🤚🏽' or msg == u'🤚🏾' or msg == u'🤚🏿' or msg == u'✋' or msg == u'✋🏻' or msg == u'✋🏼' or msg == u'✋🏽' or msg == u'✋🏾' or msg == u'✋🏿'

def paper(nickname, user: User):
    replys = [
        ["布!平手辣!", "我出Paper\nDraw!", "Paper!哼!", "啾啾出布呦!", "P-a-p-p-e-r!平手OuO"],
        ["我出剪刀!\nHappy!", "剪刀!", "Ya!", "剪刀:Scissors~\n贏了:Win...", "我出剪刀ㄏㄏ", nickname+"菜雞!我出剪刀"],
        ["石頭!!\n都欺負啾啾啊...", "Stone!", "啾啾難過...", "啾啾出石頭~~", "石頭!\n啊不就好棒棒!", "啾啾出石頭~~再來一次啊!!"]
    ]
    r = random.randint(2,8)//4
    if r==0:
        user.pss_draw+=1
    elif r==1:
        user.pss_lose+=1
    else:
        user.pss_win+=1
    UserDAO.save_user(user)
    return [TextSendMessage(text=replys[r][random.randint(0, len(replys[r])-1)]+pss_replys_2[random.randint(0,len(pss_replys_2)-1)])]

def is_pss_report(msg):
    return msg == '剪刀石頭布' or msg == 'paper scissors stone'

def pss_report(nickname, user: User):
    win_rate = round(user.pss_win/(user.pss_win+user.pss_lose+user.pss_draw+0.00000001),2)
    replys_1 = [
        f"<剪刀石頭布紀錄>\n你總共...\n贏我:{user.pss_win}次\n輸我:{user.pss_lose}次\n平手:{user.pss_draw}次\n勝率:{win_rate}",
        f"你贏我{user.pss_win}次,輸我{user.pss_lose}次,平手{user.pss_draw}次",
        f"You win {user.pss_win} time(s), lose {user.pss_lose} time(s), and draw {user.pss_draw} time(s).",
        f"你贏啾啾{user.pss_win}次,輸啾啾{user.pss_lose}次,和啾啾平手{user.pss_draw}次"
        ]
    if win_rate < 0.23:
        replys_2 = ["啾啾覺得你超嫩!", "慘不忍睹啊~", "菜雞出現!ㄘㄞˋㄐㄧ"+nickname, "啾啾瘋狂贏你耶!"]
    elif win_rate < 0.45:
        replys_2 = ["還行~還行~", "普普通通", "你比啾啾爛一點ㄏㄏ"]
    elif win_rate < 0.77:
        replys_2 = [nickname+"好像很強欸!", "啾啾把你當對手囉!", "馬上就要被我打趴ㄌ", "啾啾覺得你有點厲害ㄟ"]
    elif win_rate < 0.9:
        replys_2 = ["大師", "啾啾甘拜下風...", "啾啾覺得你超厲害", "太強了吧!!!"]
    else:
        replys_2 = ["好景不常的!", nickname+"根本大神來著!", "你是不是看透啾啾的心了...", "啾啾拜你為師~"]
    return [TextSendMessage(text=replys_1[random.randint(0,len(replys_1)-1)]), TextSendMessage(text=replys_2[random.randint(0,len(replys_2)-1)])]
    

def cannot_recongnized(message, user: User):
    replys = ['啾啾無言以對...', 'ㄛ干我', 'ㄛ\n乾我', message+"\n啊不就好棒棒?", "很酷ㄛ", "ㄛ好呦", message+"\nSounds good!", message, "歡迎你來跟我玩剪刀石頭布(直接輸入文字出拳~)"]
    return [TextSendMessage(text=replys[random.randint(0,len(replys)-1)])]