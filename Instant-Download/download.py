#! pip install bs4
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def request_url(input_url):
    try:
        response = requests.get(input_url)
        html = response.text
        return html
    except:
        print("Invalid Link!")
        return None

def find_image_url(request_url):
    soup = BeautifulSoup(request_url, 'html')
    image_url = soup.find('meta', property='og:image')
    print(image_url)
    print(image_url['content'])
    return image_url['content']

def download(image_url):
    image_name = "Insta" + datetime.now()
    print("Image name : ", image_name)

    request_url = requests.get(image_url)
    f = open(image_name + '.jpg', 'ab')
    f.write(request_url.content)
    print("Processing...")
    f.close()
    print("Download Complete")


def main():
    input_url = input("Input the Link : ")
    url = request_url(input_url)
    image_url = find_image_url(url)
    download(image_url)

if __name__ == "__main__":
    main()