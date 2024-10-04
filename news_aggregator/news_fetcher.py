import requests

API_KEY = '94658044c9904198ae6b140ee73a9d5f'
URL = 'https://newsapi.org/v2/top-headlines'
PARAMETERS = {
    'country': 'us',  # Example: Fetching top headlines from the US
    'category': 'technology',
    'apiKey': API_KEY
}

response = requests.get(URL, params=PARAMETERS)
articles = response.json().get('articles')

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}")
    print(f"URL: {article['url']}\n")
    

def fetch_news(country='us', category='technology'):
    parameters = {
        'country': country,
        'category': category,
        'apiKey': API_KEY
    }
    response = requests.get(URL, params=parameters)
    articles = response.json().get('articles')
    print(articles)  # Add this line to inspect the returned data
    return articles

