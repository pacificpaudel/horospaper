import asyncio, httpx
from bs4 import BeautifulSoup

SOURCES = [
    "https://www.onlinejyotish.com/rashiphal/daily/vrischika-rashi.php",
    "https://www.prokerala.com/astrology/rashifal/?sign=vrischika",
    "https://www.amarujala.com/astrology/horoscope/scorpio-daily-horoscope"
]

async def fetch(url):
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(url)
        r.raise_for_status()
        return r.text

def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")
    return " ".join(soup.stripped_strings)

async def main():
    tasks = [fetch(u) for u in SOURCES]
    raw = await asyncio.gather(*tasks)
    for src, txt in zip(SOURCES, raw):
        print(src, extract_text(txt)[:200], "...")

if __name__ == "__main__":
    asyncio.run(main())
