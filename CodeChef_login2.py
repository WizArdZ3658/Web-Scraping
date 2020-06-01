# script to login into CodeChef using BeautifulSoup

import requests
from bs4 import BeautifulSoup
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
login_data = {
    'name': 'ur_username',      # change username
    'pass': 'ur_password',      # change password
    'form_id': 'new_login_form',
    'op': 'Login'
}

with requests.Session() as s:
    url = 'https://www.codechef.com/'
    r = s.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html5lib')
    login_data['form_build_id'] = soup.find('input', attrs={'name': 'form_build_id'})['value']
    login_data['csrfToken'] = soup.find('input', attrs={'name': 'csrfToken'})['value']

    r = s.post(url, data=login_data, headers=headers)

    print(r.content)