import requests
from bs4 import BeautifulSoup
import csv
import datetime

# ===== USER KEYWORDS =====
keywords = ["startup", "seed fund", "grant", "incubation", "upcoming"]

# ===== TARGET WEBSITE =====
url = "https://www.startupindia.gov.in/"  # Change this

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

results = []

for link in soup.find_all("a"):
    text = link.get_text(strip=True).lower()
    href = link.get("href")

    if any(keyword in text for keyword in keywords):
        results.append({
            "title": text,
            "link": href
        })

# ===== SAVE CSV =====
filename = f"fund_results_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "link"])
    writer.writeheader()
    writer.writerows(results)

print(f"Saved {len(results)} results to {filename}")
