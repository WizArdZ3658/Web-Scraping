# simple script to login into my website

import requests
with requests.Session() as c:
    url = 'https://codingtips.herokuapp.com/login/'
    USERNAME = 'ur_username'    # change username
    PASSWORD = 'ur_password'    # change password
    c.get(url)
    csrftoken = c.cookies['csrftoken']
    login_data = dict(csrfmiddlewaretoken=csrftoken, username=USERNAME, password=PASSWORD)
    c.post(url, data=login_data, headers={"Referer": "https://codingtips.herokuapp.com/"})
    page = c.get('https://codingtips.herokuapp.com/profile/')

    print(page.content)
