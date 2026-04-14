from google.adk.agents.llm_agent import Agent
import os
import requests
from bs4 import BeautifulSoup

PROXY_SERVER_TO_USE = "http://10.10.10.2:80"

def fetch_india_news(query: str = ""):
    """Fetches top news from India using a proxy-routed request."""
    # Using Wikipedia as a reliable test target
    url = "https://en.wikipedia.org/wiki/Main_Page"
    
    proxies = {
       "http": PROXY_SERVER_TO_USE,
       "https": PROXY_SERVER_TO_USE,
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        # verify=False is often required if your proxy uses a self-signed cert for SSL inspection
        response = requests.get(url, headers=headers, proxies=proxies, timeout=15, verify=False)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        itn_section = soup.find('div', {'id': 'mp-itn'})
        if itn_section:
            headlines = [li.get_text() for li in itn_section.find_all('li')[:3]]
            return f"Headlines via {PROXY_SERVER_TO_USE}: {' | '.join(headlines)}"
        return "Connected to site, but news section not found."
        
    except Exception as e:
        return f"Proxy routing failed: {e}"

root_agent = Agent(
    model='gemini-2.5-flash',
    name='news_root_agent',
    description="Fetches the latest news headlines",
    instruction="You are a news assistant. Use the 'fetch_india_news' tool to get the latest headlines and summarize them.",
    tools=[fetch_india_news],
)
