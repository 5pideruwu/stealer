 
import requests
from bs4 import BeautifulSoup

# List of URLs to scrape for proxies
urls = [
    'https://free-proxy-list.net/',
    'https://www.sslproxies.org/',
    'https://www.us-proxy.org/',
    'https://www.socks-proxy.net/'
]

def scrape_proxies(url):
    proxies = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        if table:
            rows = table.find_all('tr')
            for row in rows[1:]:  # Skipping the header row
                columns = row.find_all('td')
                if len(columns) >= 2:
                    ip = columns[0].get_text()
                    port = columns[1].get_text()
                    proxy = f'{ip}:{port}'
                    proxies.append(proxy)
    return proxies

all_proxies = []
for url in urls:
    proxies = scrape_proxies(url)
    all_proxies.extend(proxies)

print("Fresh Proxies:")
for proxy in all_proxies:
    print(proxy)
