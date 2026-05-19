import requests
from bs4 import BeautifulSoup
import csv


def is_site_reachable(url):
    try:
        response = requests.get(url, timeout=5)
        # We RETURN True if the status is 200 (OK), otherwise False
        return response.status_code == 200
    except:
        return False


# --- Using the 'Return' value ---
target_url = "https://magazine.qs.com/qs-insights-magazine-40/brand-new-problem"

# Here, the 'if' statement waits for the function to return its result
if is_site_reachable(target_url):
    print("Success! The site is up. Proceeding to scrape...")
    # You would call your scrape function here
else:
    print("Warning: Site is down or unreachable. Aborting.")


def scrape_headlines_to_csv(url, csv_filename):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for h in soup.find_all(['h1', 'h2', 'h3']):
        text = h.get_text(strip=True)
        if text:
            headlines.append(text)

    # 'w' mode handles the replacing/overwriting automatically!
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Headline'])
        for headline in headlines:
            writer.writerow([headline])

    return headlines  # <-- This allows you to print it later


# --- Main Script ---
#url = "https://www.theglobeandmail.com/investing/markets/stocks/LLY/pressreleases/37337994/should-you-buy-novo-nordisk-stock-on-oral-wegovys-strong-launch/"
# Added 'r' before the path to avoid backslash errors
csv_filename = r"C:\Python\export\scrape_headlines.csv"

# Save to variable and then print
results = scrape_headlines_to_csv(target_url, csv_filename)
print("Scraping Complete! Here are the headlines:")
print(results)
