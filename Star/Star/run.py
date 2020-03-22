import time
import os
import subprocess
import threading

while True:
    os.system("scrapy crawl star")
    time.sleep(60)

# def crawlByProcess():
#     subprocess.check_output(['scrapy','crawl','star'])
# timer = threading.Timer(3,crawlByProcess)
# timer.start()
