import requests
url = "https://www.careerpower.in/blog/paris-olympic-games-2024-medal-tally"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

response = requests.get(url, headers = headers )
print(response)

