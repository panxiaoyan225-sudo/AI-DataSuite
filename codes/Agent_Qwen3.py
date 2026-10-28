import yfinance as yf
from ollama import Client

def get_stock_news_and_impact(ticker):
    print(f"\n--- Fetching news for {ticker} ---")
    
    headlines = ""
    try:
        stock = yf.Ticker(ticker)
        news_list = stock.news
        
        if news_list:
            for item in news_list[:5]:
                # Safely extract title from varying yfinance payload structures
                content = item.get("content", item)
                title = content.get("title") or content.get("headline")
                if title:
                    headlines += f"- {title}\n"
    except Exception as e:
        print(f"Notice: Could not fetch live Yahoo finance news ({e}). Using fallback test data.")

    # Fallback mock headlines if live feed is empty/blocked, ensuring Qwen3 always runs
    if not headlines.strip():
        print(f"Using standard diagnostic headlines for {ticker}...")
        headlines = f"""
        - {ticker} reports stronger than expected quarterly earnings driven by strong sector demand.
        - Management issues forward guidance highlighting supply chain optimizations.
        - Analysts adjust price targets following recent market volatility.
        """

    print(f"--- Qwen3 is analyzing {ticker} locally ---")

    prompt = f"""
    Analyze these news headlines for {ticker} and explain their potential stock price impact.
    Provide:
    1. A brief summary of key themes
    2. Overall Sentiment (Bullish / Bearish / Neutral)
    3. Confidence Score (0-100%)
    
    Headlines:
    {headlines}
    """

    # Connect to your local Ollama instance running on port 11434
    client = Client(host="http://127.0.0.1:11434")

    try:
        # Call Qwen3 with streaming enabled
        stream = client.chat(
            model="Qwen3:latest",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )

        print("\n[Qwen3 Response]:")
        response_text = ""
        for chunk in stream:
            content = chunk["message"]["content"]
            print(content, end="", flush=True)
            response_text += content

        print("\n")
        return response_text

    except Exception as e:
        print(f"\nError communicating with local Ollama instance: {e}")
        print("Tip: Make sure Ollama is running in the background via `ollama serve`.")

if __name__ == "__main__":
    ticker_symbol = input("Enter ticker (e.g., MU, AAPL, TSLA): ").strip().upper()
    if ticker_symbol:
        get_stock_news_and_impact(ticker_symbol)