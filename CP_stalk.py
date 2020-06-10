import requests
from bs4 import BeautifulSoup

site_urls = {
    1: "https://www.codechef.com/users/",
    2: "https://atcoder.jp/users/",
    3: "https://codeforces.com/profile/",
    4: "https://leetcode.com/",
    5: "https://www.hackerearth.com/@"
}

while True:
    print("Enter username to find his/her CodeChef ratings or enter 0 to exit")
    s = input()
    if s == "0":
        break
    print("enter 1 for CodeChef, 2 for AtCoder, 3 for CodeForces, 4 for LeetCode, 5 for HackerEarth")
    option = int(input())
    if option < 1 or option > 5:
        print("Incorrect option. Try again")
        continue
    else:
        url = site_urls[option]
    url += s

    with requests.Session() as s:
        response = s.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html5lib')

            if option == 1:
                rating = soup.find('div', attrs={'class': 'rating-number'}).get_text(strip=True)
                print(rating)
            elif option == 2:
                rating = soup.find_all('span')[7]
                print(rating.get_text())
            elif option == 3:
                rating = soup.find_all('span')[21]
                print(rating.get_text())
            elif option == 4:
                ele = soup.find_all('span')[11]
                print(ele.get_text())
            elif option == 5:
                ele = soup.find_all('span')[11]
                print(ele.a.get_text())

        elif response.status_code == 404:
            print('Not Found. Please check your username.')
