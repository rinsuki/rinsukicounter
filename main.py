import os
import requests
import datetime

def getSnowFlake(t: datetime.datetime):
    t = int(t.timestamp() * 1000)
    t = t << 16
    return t

now = datetime.datetime.now() - datetime.timedelta(days=1)

token = os.environ["ACCESS_TOKEN"]

max_id = getSnowFlake(datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1))
since_id = getSnowFlake(datetime.datetime(now.year, now.month, now.day))

toots = []

user_agent = "rinsukicounter/0.1 (+https://github.com/rinsuki/rinsukicounter)"

s = requests.Session()
s.headers["User-Agent"] = user_agent
s.headers["Authorization"] = "Bearer "+token

while True:
    r = s.get("https://imastodon.net/api/v1/accounts/28966/statuses", params={
        "since_id": since_id,
        "max_id": max_id,
        "limit": 80
    })
    if not r.ok:
        print(r.text)
        exit(1)
    r = r.json()
    if len(r) == 0:
        break
    max_id = r[-1]["id"]
    print(max_id, since_id)
    toots += r

rin_count = 0
rin_max = 0

for toot in toots:
    text = toot["content"]
    c = len(text.split("凛")) + len(text.split("りん")) - 2
    rin_count += c
    rin_max = max([c, rin_max])
text = "%04d/%02d/%02d は %d 回トゥートして、そのうち(凛|りん)は %d (max=%d) 個含まれていました。 #rinsukicounter" % (now.year, now.month, now.day, len(toots), rin_count, rin_max)

s.post("https://imastodon.net/api/v1/statuses", json = {
    "status": text
})