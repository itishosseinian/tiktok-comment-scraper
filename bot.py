import requests,json

post_url = 'https://www.tiktok.com/@cakesbydammie_yyc/video/7401564223328881926'

post_id = post_url.split('/')[-1]

headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
  'cache-control': 'no-cache',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://www.tiktok.com/explore',
  'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

comments = []

comments.append({'post_url':post_url})

curs = 0

def req(post_id,curs):
    
    url = f'https://www.tiktok.com/api/comment/list/?WebIdLastTime=1729273214&aid=1988&app_language=en&app_name=tiktok_web&aweme_id={post_id}&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=20&cursor={curs}&data_collection_enabled=false&device_id=7427171842932786693&device_platform=web_pc&focus_state=true&from_page=video&history_len=6&is_fullscreen=false&is_page_visible=true&odinId=7427171704705188869&os=windows&priority_region=&referer=&region=CA&screen_height=1080&screen_width=1920&tz_name=Asia%2FTehran&user_is_login=false&webcast_language=en&msToken=U488DBL2ELMV88PxvXu7bOKQJVxuv7LnhKNHsWaOT2uQhpGyj5M-7EmUsXBIS9HbQ_bQ35u3Za-f_hVhHMMYsH-4mxWPeJoUeMhgOHOvQ-IaKb5lr3DlgBIYJXCUc9MCexCHXig1u4a98hVjnec74fs=&X-Bogus=DFSzswVYtfhANH-ltQ2xJbJ92U6T&_signature=_02B4Z6wo000017DRplgAAIDBt3uT.9qT9Zew0aLAAIsv87'
    
    response = requests.get(url=url, headers=headers)
    info = response.text
    raw_data = json.loads(info)
    print(f'we are on {curs} curser')
    return raw_data


def parser(data):
    comment = data['comments']

    for cm in comment:
        com = cm['share_info']['desc']

        if com == "":
            com = cm['text']
        #print(com)
        comments.append(com)

    return data


while 1:

    raw_data = req(post_id,curs)

    same_data = parser(raw_data)

    if same_data['has_more'] == 1:
        curs+=20
        print('moving to the next curser')
    else:
        print('no comments available')
        break

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(comments, f, ensure_ascii=False, indent=4)

print("\ndata has been saved...., good job amir")


