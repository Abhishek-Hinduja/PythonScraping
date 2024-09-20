import requests
from bs4 import BeautifulSoup

def scrape_paris_olympic_games_media():
    url = "https://www.careerpower.in/blog/paris-olympic-games-2024-medal-tally"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers = headers )

    if response.status_code != 200:
        print("Url is failing to retrieve data")

    soup = BeautifulSoup(response.content, 'html.parser')
    
    medal_table = soup.find('table') 
    print(medal_table)

    properties = []

    if medal_table:
        rows = medal_table.find_all('tr')

        for row in rows[1:]:
            columns = row.find_all('td')
            if len(columns) == 6:
                Ranks = columns[0].text.stript()
                Countries = columns[1].text.strip()
                Gold = columns[2].text.strip()
                Silver = columns[3].text.strip()
                Bronze = columns[4].text.strip()
                Total = columns[5].text.strip()

                properties.append({
                    'Ranks' : Ranks,
                    'Countries' : Countries,
                    'Gold':Gold,
                    'Silver':Silver,
                    'Bronze':Bronze,
                    'Total':Total
                })
            elif columns:
                val = [val.text.strip() for val in columns]
                print(val)
            else:
                print("Could not find the media table")

    for item in properties:
        print(item)
    
    return properties

scrape_paris_olympic_games_media()

    

