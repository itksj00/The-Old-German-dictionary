# db_manager.py
# This file handles the database operations for word translations and search history.
# It includes functions to initialize the database, add new words, and search for words.

import sqlite3
import os

DB_FILE = "english_to_german_with_forms.db"

# Initialize the database if it does not exist
def initialize_database():
    if not os.path.exists(DB_FILE):  # First time the program runs, create the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create the 'translations' table for storing word translations and details
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS translations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            english_word TEXT NOT NULL UNIQUE,
            german_word TEXT NOT NULL,
            gender TEXT,
            verb_forms TEXT,
            category TEXT NOT NULL
        )
        """)

        # Create the 'search_history' table for storing the search history
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()
        print("Database initialized.")  # Print message when the database is initialized
    else:
        print("Database already exists.")  # Message if the database already exists

# Add a new word translation
def add_translation(english_word, german_word, gender=None, verb_forms=None, category=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO translations (english_word, german_word, gender, verb_forms, category) VALUES (?, ?, ?, ?, ?)",
                       (english_word, german_word, gender, verb_forms, category))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Prevent duplicate words from being added
    
    conn.close()

# Search for a word translation in the database
def search_translation(english_word):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT german_word, gender, verb_forms, category FROM translations WHERE english_word = ?", (english_word,))
    result = cursor.fetchone()

    if result:
        german_word, gender, verb_forms, category = result
        output = f"{english_word} => {german_word} ({category})"
        if gender:
            output += f" - Gender: {gender}"
        if verb_forms:
            output += f" - Verb Forms: {verb_forms}"
        conn.close()
        return output
    else:
        conn.close()
        return f"'{english_word}' is not in the database."
