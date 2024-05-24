import requests
import re

url="https://live.douyin.com/webcast/ranklist/audience/?aid=6383&app_name=douyin_web&live_id=1&device_platform=web&language=zh-CN&enter_from=page_refresh&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&webcast_sdk_version=2450&room_id=7310891312956394278&anchor_id=3105476682717335&sec_anchor_id=MS4wLjABAAAA7xSjYn05waVPCOv-rmHb_1fZr1Tzuiz503_q367xe-K0zEcn8Q-Yh88kYXFijtVh&rank_type=30&msToken=wQ2HUYumO3miEz0ohX_5B10P5L2zIK-2_iWCB1tXfGsVe-0b-PC2ynTrBTSUsKJDbh4ZvyPlinf-JbqAYeU74tJFe9aG5d1WkfqSX8cBxMRUjpIv9w==&X-Bogus=DFSzswVY3DiANCMrtuh10l9WX7jX&_signature=_02B4Z6wo00001OIztVAAAIDAYjFPEX8iHaTiM7HAAF3.Zaid0ez.drO6-VvnK792peS21U.6Qjo5MdrqNCkHPTvaomKfxg5YcpDTZ1W1k43jSoWgJUYLUdSnpKi7UBAgr3DVJPbGqVfOdsAK98"


urlHtml="https://www.douyin.com/user/MS4wLjABAAAA7xSjYn05waVPCOv-rmHb_1fZr1Tzuiz503_q367xe-K0zEcn8Q-Yh88kYXFijtVh"

loginUser = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "Cookie":"__ac_nonce=0657590e700ad9e4eb00c; __ac_signature=_02B4Z6wo00f01jTPz8wAAIDCtM01jtia4Jo078tAAOhU31; ttwid=1%7Cx_rPrZVmfxMR6tuh_sl4VYFZByoofgdOqiSBCA1YCio%7C1702203623%7Cd53814efa149c4220fe7f62e3f1793f4bbdb44f57dd97c5fbc12b9aca7a9a2e4; device_web_cpu_core=8; device_web_memory_size=8; live_use_vvc=%22false%22; xgplayer_user_id=571391200610; csrf_session_id=03bfbfdc16dbde13ca1ea09c5fa7f534; webcast_leading_last_show_time=1702203625736; webcast_leading_total_show_times=1; ttcid=c8b8c7b950134f4abdad9bdbc0de198916; webcast_local_quality=ld; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; s_v_web_id=verify_lpzc4mrk_NVIVG00d_zi2E_4mh8_AVmN_1P1ddyJXprVk; bd_ticket_guard_client_web_domain=2; passport_csrf_token=b71af8e4ceb4b720d67af7befd49f6de; passport_csrf_token_default=b71af8e4ceb4b720d67af7befd49f6de; passport_assist_user=CkFb8GwFf_SltZrXv1ctxAyn8hSlRoNAYZqKhDEQX9M48JcDrsJgY_pOe-LvAT8xTomUBw0hlRyMXKeE0qUhWoUu6hpKCjyl4IBi8RV6FcBXzisP-PHxzhK5aMC8djaFieHr3GGtIE5vzjXcbSC_Y6Ye2cXsSzhrPO8SavMvJ5otg-QQ7sjDDRiJr9ZUIAEiAQNs6Qem; n_mh=bOzNxomSEACBKNsDteoLfhmemj7rl1tKEAagNTCXzWU; sso_uid_tt=4f91c982a6ed6668602de4a2a8794b34; sso_uid_tt_ss=4f91c982a6ed6668602de4a2a8794b34; toutiao_sso_user=d2f451a8d5f3a6a09eefe6f1c2f65ca6; toutiao_sso_user_ss=d2f451a8d5f3a6a09eefe6f1c2f65ca6; sid_ucp_sso_v1=1.0.0-KGQwMTMzM2E4M2RjMjMxYjU2ZjRiZTMyMDFlM2ViMjU5ZDA1NWVmNzYKHwidlvCpzvXKBRC6otarBhjvMSAMMKCnue4FOAZA9AcaAmxxIiBkMmY0NTFhOGQ1ZjNhNmEwOWVlZmU2ZjFjMmY2NWNhNg; ssid_ucp_sso_v1=1.0.0-KGQwMTMzM2E4M2RjMjMxYjU2ZjRiZTMyMDFlM2ViMjU5ZDA1NWVmNzYKHwidlvCpzvXKBRC6otarBhjvMSAMMKCnue4FOAZA9AcaAmxxIiBkMmY0NTFhOGQ1ZjNhNmEwOWVlZmU2ZjFjMmY2NWNhNg; passport_auth_status=947117d69d860d78238c743be8fccd93%2C; passport_auth_status_ss=947117d69d860d78238c743be8fccd93%2C; uid_tt=0a8fb6ab9af62f4e98aac262db20981b; uid_tt_ss=0a8fb6ab9af62f4e98aac262db20981b; sid_tt=868dc750fa77894ea7155f766bc8e47c; sessionid=868dc750fa77894ea7155f766bc8e47c; sessionid_ss=868dc750fa77894ea7155f766bc8e47c; __live_version__=%221.1.1.6165%22; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=949125701c151a714379945032db0dc5; __security_server_data_status=1; sid_guard=868dc750fa77894ea7155f766bc8e47c%7C1702203715%7C5183994%7CThu%2C+08-Feb-2024+10%3A21%3A49+GMT; sid_ucp_v1=1.0.0-KGI0YTU1MTk3M2JiOTlmODE1ZDQ2ZTgzM2MzYzVmYWY5YzY3ZDFjNzMKGwidlvCpzvXKBRDDotarBhjvMSAMOAZA9AdIBBoCbHEiIDg2OGRjNzUwZmE3Nzg5NGVhNzE1NWY3NjZiYzhlNDdj; ssid_ucp_v1=1.0.0-KGI0YTU1MTk3M2JiOTlmODE1ZDQ2ZTgzM2MzYzVmYWY5YzY3ZDFjNzMKGwidlvCpzvXKBRDDotarBhjvMSAMOAZA9AdIBBoCbHEiIDg2OGRjNzUwZmE3Nzg5NGVhNzE1NWY3NjZiYzhlNDdj; xg_device_score=7.421899828763008; download_guide=%223%2F20231210%2F0%22; pwa2=%220%7C0%7C2%7C0%22; live_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT1hIVk1IYmtUNkJjaFBBKzJkK3lHTUlXQTBnd2phbFJIV0wybnQ1SWU3UjNYWkJwUEZZNlR2MHR0S3NjMzE1Qkc3ZHhRekR4TDFGWnBCZzNpcjR0WjQ9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; passport_fe_beating_status=true; msToken=1-9L5Gy6Yj6WKuWtMi_XibQWYclkeDwb3i7wr9IAIJghdTZvqH1fPblBfTm31CS4F8Q1FgS-gtom8CyKzTrcfq8J5g8v0xEMkkO0LEZV8V4q7oBm-g==; IsDouyinActive=true; publish_badge_show_info=%220%2C0%2C0%2C1702204233144%22; msToken=wQ2HUYumO3miEz0ohX_5B10P5L2zIK-2_iWCB1tXfGsVe-0b-PC2ynTrBTSUsKJDbh4ZvyPlinf-JbqAYeU74tJFe9aG5d1WkfqSX8cBxMRUjpIv9w==; odin_tt=11bac9812deb1e9efb638d6e9a4137d76f47b5c6a42a9e366b8f8afbb5b3bd0daa5edb557c11d772ad9ea3e737d97dde54854f5168fd9cd43b2f27e82838137d; tt_scid=vYH.Jns6J.7-j1Mu1lML4bArJ-8Pr2pMAOp8l7gS3su1lC48sA9efq3sLzFz2iSYf095"}

res = requests.get(url, headers=loginUser)
json = res.json()
# print(json["status_code"])

userInfos = json["data"]["ranks"]

for userInfo in userInfos:
    user = userInfo["user"]
    # 打印用户信息以及主页地址
    # print(user["nickname"], user["gender"],"https://www.douyin.com/user/"+user["sec_uid"])


# 查询文本数据
resHtml = requests.get(urlHtml, headers=loginUser)
text = resHtml.text
# print(text)
findData = re.findall('<a href="https://www.12377.cn/" class="B3AsdZT9" target="_blank" rel="noopener noreferrer">(.*?)</a>',text)
# findData = re.findall('寒冰姐3。寒冰姐3的抖音主页、视频(.*?)、点赞量。来抖音，记录美好生活！', text)
print(findData)

