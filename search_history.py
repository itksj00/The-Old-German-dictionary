# search_history.py
# This file handles the management of search history.
# It includes functions to record searches and view the search history.

import sqlite3

DB_FILE = "english_to_german_with_forms.db"

# Record a word search in the search history
def record_search(word):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO search_history (word) VALUES (?)", (word,))
    conn.commit()
    conn.close()

# View the search history of previously searched words
def view_search_history():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT word, timestamp FROM search_history ORDER BY timestamp DESC")
    history = cursor.fetchall()

    conn.close()

    if history:
        print("Search History:")
        for record in history:
            print(f"{record[0]} - {record[1]}")
    else:
        print("No search history.")
