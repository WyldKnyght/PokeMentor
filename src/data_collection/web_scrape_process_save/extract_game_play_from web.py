import requests
from bs4 import BeautifulSoup

## Read the list of URLs from the text file
with open("M:\\DEV_Projects\\PokeMentor\\docs\\data_collection\\how_to_play_urls.txt", "r") as file:
    urls = file.read().splitlines()

# Loop through each URL
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant information from the webpage and process it as needed
        # You may need to inspect the HTML structure of the pages to locate the rules and instructions
        # Use soup.find() or soup.find_all() to locate specific elements
        # Process the data and save it for further use
        
        # Example: Extract and print the page title
        page_title = soup.title.string
        print(f"Title of {url}: {page_title}")

    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")

