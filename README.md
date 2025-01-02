# The-Old-German-dictionary
En: A Dictionary That Hasn't Kept Up with the Times / de: Ein Wörterbuch, das mit der Zeit nicht Schritt gehalten hat

🍺 While studying German, instead of focusing on the actual German learning, I came up with an idea related to it and ended up starting development..

## What is this? 🍺
### Features
---
#### 1. Word Search
**Description:**
- Users input an English word, and the system provides the German translation along with additional information like gender (for nouns) and verb forms (for verbs).

**Functionality:**
- The system searches the database for the input word.
- If the word is found, the German translation, gender (for nouns), and verb forms (for verbs) are displayed.
- If the word is not found in the database, it shows a message saying the word is not found.

---

#### 2. View Search History (Temp)
**Description:**
- Allows users to view a history of the words they have previously searched.

**Functionality:**
- Display a list of previously searched words along with the timestamps of when they were searched.
- The search history is shown in chronological order.

---

#### 3. Add Word
**Description:**
- Allows users to add new words to the database with their English translation, German translation, gender, and verb forms.

**Functionality:**
- Users can add new words with their German translation, gender (for nouns), verb forms (for verbs), and category.
- Duplicate words cannot be added to prevent redundancy.

---

#### 4. Initialize Database
**Description:**
- Initalizes the database when the program starts, creating essential tables for storing words and search history.

**Functionality:**
- If the database does not exist, it is created automatically along with required tables (word table, search history table).
- Words added by users and their search history are stored in these tables.

---

#### 5. Record Search History after Word Search
**Description:**
- After searching for a word, the search is automatically recorded in the search history.

**Functionality:**
- The word searched by the user is automatically added to the search history.
- This history can be viewed by the user through the "View Search History" option.

---

#### 6. Database Search
**Description:**
- Searches the database for the word input by the user and returns the results.

**Functionality:**
- The program searches for the word in the database and displays the result.
- If the word is not found, it shows a "word not found" message.

## File Structure
The file structure of this project is divided into separate files based on functionality.
Each file handles a specific feature, such as word management, search history management, and database management.

---

### Path
The-old-German-dictionary
-    db_manager.py
-    main.py
-    requirements.txt
-    search_history.py
-    translation.py

