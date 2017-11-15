import requests
import time
count = 0
sub = 'all'
data = ''
# An loop here is needed because for some reason html.json()["data]["children"] fails for no reason sporadically
# Therefore if you loop it, it will eventually pass and return data.
attempts = 10000

while count < attempts:
    try:
        html = requests.get("https://www.reddit.com/r/" + sub + "/new.json")
        data = html.json()["data"]["children"]
        break
    except:
        pass
        count += 1
        time.sleep(2)  # 1 request every 2 seconds (30 requests per min) in accordance with reddit api guidelines
        if count > attempts:
            raise RuntimeError("Reddit experiment made too many attempts")
print(data)
