import sqlite3
import urllib.parse
from decouple import Config, Csv


# Function to validate a URL
def is_valid_url(url):
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


# Function to store a URL in the database
def store_url_in_database(cursor, url):
    try:
        # Check if the URL already exists in the database
        cursor.execute("SELECT COUNT(*) FROM urls WHERE url=?", (url,))
        count = cursor.fetchone()[0]

        if count == 0:
            # If the URL doesn't exist, add it to the database using a parameterized query
            cursor.execute("INSERT INTO urls (url) VALUES (?)", (url,))
            print(f"URL '{url}' added to the database.")
        else:
            print(f"URL '{url}' already exists in the database.")

    except sqlite3.Error as e:
        print(f"An error occurred while storing the URL: {e}")


# Main function to validate and store URLs
def main():
    # Create an instance of the Config class with the path to the .env file
    config = Config("config/.env")

    # Retrieve the values from the configuration
    database_path = config.get("HOW_TO_PLAY_URLS_DATABASE_PATH", default=None)
    url_list_file = config.get("HOW_TO_PLAY_URL_LIST_FILE_PATH", default=None)

    # Read URLs from the text file
    try:
        with open(url_list_file, "r") as file:
            urls_to_add = file.read().splitlines()
    except Exception as e:
        print(f"An error occurred while reading URLs from the file: {e}")
        urls_to_add = []

    # Use list comprehension to filter valid URLs
    valid_urls = [url for url in urls_to_add if is_valid_url(url)]

    # Remove duplicates from the list of URLs
    unique_urls = set(valid_urls)

    # Use context manager to handle the database connection and cursor
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()

        # Use executemany() method to insert multiple URLs into the database at once
        urls_to_insert = [(url,) for url in unique_urls]
        cursor.executemany("INSERT INTO urls (url) VALUES (?)", urls_to_insert)

        # Print the number of URLs inserted into the database
        count = len(urls_to_insert)
        print(f"{count} URLs added to the database.")

        # Print invalid URLs
        invalid_urls = set(urls_to_add) - unique_urls
        for i, url in enumerate(invalid_urls):
            print(f"{i+1}. Invalid URL: {url}")


if __name__ == "__main__":
    main()