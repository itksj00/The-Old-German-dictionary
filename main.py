# main.py
# This is the main program file that handles user interaction and executes the core functions of the program.
# It allows users to search for English words, view search history, and add new words.

from db_manager import initialize_database, add_translation, search_translation
from search_history import record_search, view_search_history

def main():
    initialize_database()  # Initialize the database at the start

    while True:
        print("\n--- English Word -> German Word Search ---")
        print("1. Search Word")
        print("2. View Search History")
        print("3. Exit")
        
        choice = input("Please choose an option (1/2/3): ").strip()

        if choice == "1":
            word = input("Enter an English word: ").strip()
            print(search_translation(word))
            record_search(word)  # Automatically save the search word to history
        elif choice == "2":
            view_search_history()  # View the search history
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()  # Run the main program
