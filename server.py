import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import storage
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, QuickReply, QuickReplyButton, MessageAction
from linebot.exceptions import LineBotApiError

import time
import os
from models.task import Task
import style_transfer
import matplotlib.pyplot as plt


'''
Configs
'''
# Use a service account
cred_path = os.environ["CRED_PATH"]
bucket_name = os.environ["USER_INFO_GS_BUCKET_NAME"]
styles = {
    1: "01_01_starry_night.jpeg",
    2: "01_02_sunflowers.jpeg",
    3: "01_03_the_yellow_house.jpeg",
    4: "02_04_water_fall.jpeg",
    5: "02_05_ascending_and_descending.jpeg",
    6: "02_06_ralativity.jpg",
    7: "03_07_unknown.jpeg",
    8: "03_08_flower_and_bird.jpeg",
    9: "03_09_flowers_and_birds_seasons.jpeg",
    10: "04_10_first_impression.jpeg",
    11: "04_11_unknown.jpeg",
    12: "04_12_unknown.jpeg",
    13: "05_13_frida_kahlo.jpeg",
    14: "05_14_frida_kahlo.jpeg",
    15: "05_15_frida_kahlo.jpeg"
}
iteration_times = int(os.environ["ITERATION_TIMES"])
line_channel_access_token = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

'''
'''
# Initialize CloudStorage
storage_client = storage.Client.from_service_account_json(cred_path)
bucket = storage_client.bucket(bucket_name)

# Initialize Line Bot Api
line_bot_api = LineBotApi(line_channel_access_token)

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Create a callback on_snapshot function to capture changes

tasks_ref = db.collection(u'tasks')


def on_snapshot(doc_snapshot, changes, read_time):
    for change in changes:
        print(change.document.id, "added")
        os.sleep(os.environ["DELTA"])
        task_ref = tasks_ref.document(change.document.id)
        task_doc = task_ref.get()
        if task_doc.exists:
            task = Task.from_dict(task_doc)
            if task.status == 0:
                task.status = 1
                task_ref.set(document_data=task.to_dict(), merge=True)
                print(change.document.id, "started")
                bucket.blob(task.content_pic_url).download_to_filename(
                    os.path.basename(task.content_pic_url))
                best_img, best_loss = style_transfer.run_style_transfer(
                    os.path.basename(task.content_pic_url), 'styles/'+styles[task.style_id], num_iterations=iteration_times)
                plt.imsave('done.jpg', best_img)

                # remove original image
                os.remove(os.path.basename(task.content_pic_url))

                # upload to CloudStorage
                destination_blob_name = f'{change.document.id}/image/done_{change.document.id}_{str(time.time())}.jpg'
                bucket.blob(destination_blob_name).upload_from_filename(
                    'done.jpg')

                # make it publicly readable
                bucket.blob(destination_blob_name).make_public()

                # delete task in FireStore
                task_ref.delete()

                # push message to user
                try:
                    line_bot_api.push_message(change.document.id, [
                        TextSendMessage(text="啾啾幫你畫好啦~"),
                        ImageSendMessage(
                            original_content_url=f'https://storage.googleapis.com/{bucket_name}/{destination_blob_name}',
                            preview_image_url=f'https://storage.googleapis.com/{bucket_name}/{destination_blob_name}'
                        ),
                        TextSendMessage(text="好不好看呢?\n歡迎多多抖內作者ㄛ~"),
                        TextSendMessage(text="如果想再請啾啾畫一張畫,請輸入「再來一張」",
                                        quick_reply=QuickReply(items=[
                                            QuickReplyButton(action=MessageAction(
                                                label="再來一張", text="再來一張"))
                                        ]))
                    ])
                except linebot.exceptions.LineBotApiError as e:
                    print(e.status_code)
                    print(e.request_id)
                    print(e.error.message)
                    print(e.error.details)


# Watch the document
doc_watch = tasks_ref.on_snapshot(on_snapshot)


while True:
    time.sleep(1)
