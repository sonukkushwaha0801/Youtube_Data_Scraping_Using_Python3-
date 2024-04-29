import html5lib
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
working_link = "https://www.youtube.com/watch?v=iZFt8i3dnkI" # Link of the video
soup = BeautifulSoup(requests.get(working_link).content)
video_title = soup.text.title().split("|")[0].strip()
print("\t\n\n",video_title,"\n\n\n")
pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
description = pattern.findall(str(soup))[0].replace('\\n','\n')
print(description)
with open(f"{video_title}.txt", "wb") as f:  # Use "wb" for binary write
    f.write(f"{description}".encode())
f.close()