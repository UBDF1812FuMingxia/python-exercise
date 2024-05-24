# 链接
url = "https://us-xpc11.xpccdn.com/57a8f003-effc-41c0-b233-d99683d65dfb.mp4"

# 导入
import requests

# 读取url
req = requests.get(url)

# 打印
print(req.status_code)

open("第一个视频文件.mp4", "wb").write(req.content)
