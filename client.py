import requests
from bs4 import BeautifulSoup

data = {
    'action': 'myprefix_scrollist',
    'unik': '3568307',
    'dir': 'ned',
    'dict': 'saol'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
}

file = open("saol2018.csv", "a")


def main():
    for i in range(1, 12000):
        if i % 30 == 0:
            print(i)
        response = requests.post('https://svenska.se/wp-admin/admin-ajax.php', data=data, headers=headers)
        unik = parse_response(response)
        if unik == -1:
            break
        data['unik'] = unik

# Parse the html response from svenska.se
def parse_response(response):
    soup = BeautifulSoup(response.text, features="html.parser")
    links = soup.findAll("a", class_='slank')
    if len(links) == 0:
        return -1
    for link in links:
        gather_information(link)
    div = soup.findAll("div", class_='pilned')
    return div[0].a['unik']


def gather_information(link):
    span = link.findAll('span')
    file.write(span[0].getText().strip() +
               "," + span[1].getText().strip() +
               "," + span[2].getText().strip() +
               "," + span[3].getText().strip() +
               "," + link['href'].strip() + "\n")


if __name__ == '__main__':
    main()
