import subprocess
import sys
import os
import time

fn = sys.argv[1]
ua = "--user-agent=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134\""
host = "https://translate.google.com/"
query = "translate_tts?ie=UTF-8&tl=zh-CN&client=tw-ob&q="

asset = "asset/"

name = os.path.splitext(fn)[0]
with open(fn, "r") as f:
    for idx, line in enumerate(f):
        line = line.strip()
        path = query + line
        subprocess.call(["wget", ua, host + path])
        subprocess.call(["mv", path, asset + name + str(idx)+".mp4"])
        time.sleep(1.5)
