# db_manager.py
# This file handles the database operations for word translations and search history.
# It includes functions to initialize the database, add new words, and search for words.

import sqlite3
import os
import json

DB_FILE = "english_to_german_with_forms.db"
JSON_FILE = "words_data.json"  # Path to the JSON file with initial word data

# Initialize the database and import data from the JSON file
def initialize_database():
    if not os.path.exists(DB_FILE):  # If the database does not exist
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create the 'translations' table with the structure for noun/verb and forms
        cursor.execute("""
        CREATE TABLE translations (
            id INTEGER PRIMARY KEY,
            english_word TEXT NOT NULL,
            german_word TEXT NOT NULL,
            word_type TEXT NOT NULL,
            plural_form TEXT,
            past_form TEXT,
            present_form TEXT,
            future_form TEXT
        )
        """)

        # Load initial data from JSON file
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Insert data into the database
        for english_word, details in data.items():
            german_word = details["german"]
            word_type = details["type"]
            forms = details.get("forms", {})
            plural_form = forms.get("plural")
            past_form = forms.get("past")
            present_form = forms.get("present")
            future_form = forms.get("future")

            cursor.execute("""
            INSERT INTO translations (english_word, german_word, word_type, plural_form, past_form, present_form, future_form)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (english_word, german_word, word_type, plural_form, past_form, present_form, future_form))

        conn.commit()
        conn.close()

# Initialize the database if it does not exist and import words
initialize_database()
