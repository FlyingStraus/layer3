from utils.libs import *

session = requests.Session()
session.headers.update({"Content-Type": "application/json",
"referer":"https://layer3.xyz/quests/",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
"accept-language": "ru-RU,ru;q=0.9",
# "cookie": "_cfuvid=3S5fabJ_P_TK9yw.nsrhxeDgMhVER0miEh39eTr30lE-1684010334723-0-604800000;layer3_access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjMyMjI0OSwiaWF0IjoxNjg0MDcwMjE0LCJleHAiOjE2ODQwNzM4MTR9.rqrUNzxVE_suvhJCsXuWD8sIkGvO0MGmvTSZKY4N8ig;",
})

def settings():
    with open("./config.json", "r", encoding="utf-8") as f:
        return dict(json.loads(f.read()))


CFG = settings()

TASKS_list = CFG.get("TASK", None)

