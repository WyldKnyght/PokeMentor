import fitz  # PyMuPDF
import sqlite3

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    
    # Use list comprehension to extract text from each page
    text = [page.get_text() for page in pdf_document]
    
    return '\n'.join(text)  # Join the list of text using line breaks

# Function to create database tables if they don't exist
def create_database_tables(database_path):
    try:
        # Use the 'with' statement to ensure proper closing of the connection
        with sqlite3.connect(database_path) as db_connection:
            db_cursor = db_connection.cursor()

            db_cursor.execute('''
                CREATE TABLE IF NOT EXISTS cards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    description TEXT
                )
            ''')

            db_cursor.execute('''
                CREATE TABLE IF NOT EXISTS rules (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    section TEXT,
                    content TEXT
                )
            ''')

            db_connection.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

# Function to insert text data into the database
def insert_text_data_into_database(text, database_path):
    try:
        # Use the 'with' statement to ensure proper closing of the connection
        with sqlite3.connect(database_path) as db_connection:
            db_cursor = db_connection.cursor()
            
            # Split the text into sections using "SECTION " as delimiter
            sections = text.split("SECTION ")[1:]  # Skip the initial empty string
            
            # Prepare the data as a list of tuples (section_id, section_text)
            data = [(section_id, section_text.strip()) 
                    for section_id, section_text in enumerate(sections, start=1)]

            # Define the SQL query with placeholders for section and content
            sql_insert = "INSERT INTO rules (section, content) VALUES (?, ?)"

            # Use executemany to efficiently insert multiple rows
            db_cursor.executemany(sql_insert, data)

            db_connection.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

if __name__ == "__main__":
    # Define the PDF file path and the desired database file path
    pdf_path = "M:\\DEV_Projects\\PokeMentor\\data\\pokemon_tcg_rules\\pal_rulebook_en.pdf"
    database_path = "M:\\DEV_Projects\\PokeMentor\\data\\pokemon_tcg_rules\\pokemon_tcg_rulebook.db"

    # Extract text from the PDF using list comprehension
    rulebook_text = extract_text_from_pdf(pdf_path)

    # Print a portion of the extracted text for verification
    print(rulebook_text[:1000])

    # Create or connect to the database and create tables (provide the database_path)
    create_database_tables(database_path)

    # Insert data into the database (provide the text and database_path)
    insert_text_data_into_database(rulebook_text, database_path)
