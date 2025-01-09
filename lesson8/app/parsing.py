from bs4 import BeautifulSoup
import requests

def get_news():
    url = f"https://24.kg"
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, "lxml")

    all_news = soup.find_all("div" , class_ = 'title')[10:]
    new_list=[]

    for news in all_news:
        title = news.text
