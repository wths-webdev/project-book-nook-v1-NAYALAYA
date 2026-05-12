# List of books

Books = []

# Print welcome message

print("Welcome to your library.")

# Print Menu

print("\nWelcome to...\n"
    "      ______ ______\n"
    "    _/      Y      \\_\n"
    "   // ~Book | ~~ ~  \\\n"
    "  // ~ ~ ~~ |  Nook~ \\\n"
    " //________.|.________\\\n"
    "`----------`-'----------'\n")

print("Menu:\n" 
"Add book (add)\n"
"Remove book (remove)\n"
"Show inventory count (count)\n"
"Quit (q)")

# Ask user what they wanna do
while True:
  
    ask = input("What would you like to do?")

# Ask for book

    if ask == "add":

        new_book = input("What book would you like to add?")
        Books.append(new_book.strip().lower())

        print(new_book, "has been added to your list.")

    for b in Books:
        print(b)

    # Remove a book

    if ask == "remove":
    
        removal = input("What book would you like to remove?")
        Books.remove(removal.strip().lower())
    
    # If user requests to remove a book that doesn't already exist in their list print out an apology statement

        if removal not in Books:
            print("Sorry, it appears you do not own this book.")

        for b in Books:
            print(b)

        # Show number of books

    if ask == "count":
        print(len(Books))
   
        # Quit

    if ask == "q":
        break