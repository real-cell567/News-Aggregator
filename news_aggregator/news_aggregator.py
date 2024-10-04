from flask import Flask, render_template, request, jsonify
from news_fetcher import fetch_news
from summarizer import summarize_text
from sentiment_analyzer import analyze_sentiment
from categorizer import categorize_article

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return jsonify({"message": "POST request received"}), 200
    else:
        articles = fetch_news() or []
        processed_articles = []

        for article in articles:
            # Ensure that description or content is available
            text_to_summarize = article.get('description') or article.get('content') or ""
            summary = summarize_text(text_to_summarize)
            sentiment = analyze_sentiment(summary)
            category = categorize_article(article['title'], article['description'])
            processed_articles.append({
                'title': article['title'],
                'summary': summary,
                'sentiment': sentiment,
                'category': category,
                'url': article['url']
            })

        return render_template('index.html', articles=processed_articles)

if __name__ == "__main__":
    app.run(debug=True)
