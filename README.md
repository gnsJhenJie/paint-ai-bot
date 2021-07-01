# Paint AI Bot

A Line bot who paints your images as paint from famous painters using neural style transfer. You can also play games and chat with it.

## Try it now

It's now deployed on https://gnsjhenjie.tech/pbot/ as "名畫產生器-啾啾".
![image](https://github.com/gnsJhenJie/paint-ai-bot/blob/010a43fea4fe469a76afd259f312e60a7d82210c/docs/images/IMG_6853.PNG)

## Requirements

- GCP Cloud Run (or other services that can run Docker)  
  (1 vCPU and 160 Mib memory is sufficient for normal usage)
- At least one server with high CPU performance with Python3.7
  (the performance decides the speed of generating images)
- Firebase Firestore

- GCP Cloud Storage

## Deployment

### **Environment Variables**

You should set those environment variables in both **Cloud Run (Docker)** and the **server with high CPU performance**.

### **For Cloud Run**

Build the whole project as a container

```shell
gcloud config set project YOUR-PROJECT-ID
gcloud builds submit  --tag gcr.io/$GOOGLE_CLOUD_PROJECT/paint-ai-bot:0.0.1
```

Then, run the container image on Cloud Run with the below environment variables set.

- `LINE_CHANNEL_ACCESS_TOKEN`: the channel access token of your Line bot.
- `LINE_CHANNEL_SECRET`: the channel secret of your Line bot.
- `USER_INFO_GS_BUCKET_NAME`: the name of the bucket in your GCP cloud storage.

(For more instructions, see [GCP docs](https://cloud.google.com/run/docs/quickstarts?hl=zh-tw) and [Line developer docs](https://developers.line.biz/en/docs/messaging-api/))

> If you are not running the container in GCP, you may need to change some code to specify the key of your GCP service account to access Firestore and Cloud Storage.

### **For high CPU performance server(s)**

You can run multiple high CPU performance servers.

```shell
pip install -r requirements.txt
python server.py
```

Make sure you execute `server.py` in Python3.7 with the below environment variables set.

- `CRED_PATH`: the credential(key) json file of your GCP service account.
- `USER_INFO_GS_BUCKET_NAME`: the name of the bucket in your GCP cloud storage.
- `ITERATION_TIMES`: the iteration times of the style transfer process.  
  (320 is recommended for basic usage, and 1000 for those who pursue perfect effect)
- `LINE_CHANNEL_ACCESS_TOKEN`: the channel access token of your Line bot.
- `DELTA`: For those who just run one `server.py` process, set it to 0. If you run `server.py` in more than one server(or process), set it to 0, 3, 6, 9... respectively. (The delta is the pause time to avoid different server(process) dealing with the same task)

## References

Thanks a lot to the contributors below to make me complete this project.

- [titu1994/Nerual-Style-Transfer](https://github.com/titu1994/Neural-Style-Transfer)
- [BingHongLi/ncu_gcp_ai_project](https://github.com/BingHongLi/ncu_gcp_ai_project)
