
import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
    hrefs = []
    response = requests.get(url)

    if response.status_code == 200:
        obsah = response.text
        odkazy = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\']', obsah)
        for odkaz in odkazy:
            hrefs.append(odkaz)
    else:
        raise Exception("Stranku se nepodarilo stahnout")
    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)

        for odkaz in odkazy:
            print(odkaz)

    except Exception as e:
        print(f"Program skoncil chybou: {e}")
