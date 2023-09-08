import requests
import sqlite3
from decouple import config

# Function to fetch data from a URL
def fetch_data_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text  # Return the HTML content of the webpage
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return None
    except Exception as e:
        print(f"An error occurred while fetching data from {url}: {e}")
        return None

# Function to store fetched data in the database
def store_data_in_database(url, data, database_path):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS fetched_data (url TEXT, data TEXT)''')

        # Insert the fetched data into the database
        cursor.execute("INSERT INTO fetched_data (url, data) VALUES (?, ?)", (url, data))
        conn.commit()
        print(f"Fetched data from {url} saved to the database.")
    except sqlite3.Error as e:
        print(f"An error occurred while storing the data in the database: {e}")
    finally:
        conn.close()

# Main function to fetch data from the database
def main():
    # Load configuration from .env file in the config directory
    config_path = "config/.env"
    database_path = config("HOW_TO_PLAY_URLS_DATABASE_PATH", default=None, config_file=config_path)

    # Connect to the database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Retrieve the list of URLs from the database
    cursor.execute("SELECT url FROM urls")
    urls = [row[0] for row in cursor.fetchall()]

    for url in urls:
        if data := fetch_data_from_url(url):
            # Store the fetched data in the database
            store_data_in_database(url, data, database_path)

    conn.close()

if __name__ == "__main__":
    main()
