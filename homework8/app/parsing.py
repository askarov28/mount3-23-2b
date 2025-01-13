from aiohttp import ClientSession
from bs4 import BeautifulSoup

async def fetch_html(url : str) -> str:
    async with ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise ValueError(f"Ошибки запроса: {response.status}")
            return await response.text()
        
async def parse_website(url : str) -> str:
    html = await fetch_html(url)
    soup = BeautifulSoup(html , "html.parser")
    titles = soup.find_all("h2")
    if not titles:
        return "Данные не найдены "
    results = "\n" .join(f"{i+1}. {title.text.strip()}" for i , title in enumerate(titles))
    return results        

