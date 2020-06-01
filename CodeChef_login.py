# script to login into CodeChef

import requests
from lxml import html
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
login_data = {
    'name': 'ur_username',      # change username
    'pass': 'ur_password',      # change password
    'form_id': 'new_login_form',
    'op': 'Login'
}
with requests.session() as s:
    url = 'https://www.codechef.com/'
    r = s.get(url, headers=headers, timeout=5)
    byte_data = r.content
    source_code = html.fromstring(byte_data)

    path = '//input[@name="form_build_id"]/@value'
    path2 = '//input[@name="csrfToken"]/@value'

    tree = source_code.xpath(path)
    tree2 = source_code.xpath(path2)

    login_data['form_build_id'] = tree[0]
    login_data['csrfToken'] = tree2[0]
    r = s.post(url, data=login_data, headers=headers)

    print(r.content)
