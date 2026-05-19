import yfinance as yf
from ollama import Client  # <-- 1. Import Client directly

def get_stock_news_and_impact(ticker):
    # Fetch news from Yahoo Finance
    print(f"--- Fetching news for {ticker} ---")
    stock = yf.Ticker(ticker)
    news_list = stock.news[:5]
    
    if not news_list:
        return "No recent news found."

    headlines = ""
    for item in news_list:
        title = item.get('title') or item.get('headline') or "No Title"
        headlines += f"- {title}\n"

    print(f"--- Local Model is thinking... ---")
    
    prompt = f"""
    Analyze these headlines for {ticker} and explain the price impact. 
    Provide a sentiment and a confidence score.
    
    Headlines:
    {headlines}
    """

    # 2. Point directly to the IP address of the background service that is holding that port
    client = Client(host='http://127.0.0.1:11434')

    response = client.chat(
        model='qwen2.5:3b',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response['message']['content']

if __name__ == "__main__":
    ticker_symbol = input("Enter ticker: ").strip().upper()
    print(get_stock_news_and_impact(ticker_symbol))