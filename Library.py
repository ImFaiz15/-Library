# DSA Assignment 2 — Library Book Management System
# Author: Mohd Faiz
# Course: ENCS205 (Data Structures)
# Date: 2025-10-31
#
# Implementation:
# - Singly linked list for storing books
# - Stack for recording transactions (issue / return) to support undo
# - Functions: insertBook, deleteBook, searchBook, displayBooks, issueBook,
#   returnBook, undoTransaction, viewTransactions

class BookNode:
    def __init__(self, book_id: int, title: str, author: str, status: str = "Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None

class BookList:
    def __init__(self):
        self.head = None

    def insertBook(self, book_id: int, title: str, author: str):
        """Insert at end. Prevent duplicate BookID."""
        if self.searchBook(book_id, suppress_print=True):
            print(f"❌ Insert failed: Book ID {book_id} already exists.")
            return False

        new_book = BookNode(book_id, title, author)
        if not self.head:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print(f"✅ Book '{title}' (ID: {book_id}) added successfully.")
        return True

    def deleteBook(self, book_id: int):
        temp = self.head
        prev = None
        while temp and temp.book_id != book_id:
            prev = temp
            temp = temp.next

        if not temp:
            print(f"❌ Delete failed: Book ID {book_id} not found.")
            return False

        if prev:
            prev.next = temp.next
        else:
            self.head = temp.next

        print(f"🗑️ Book '{temp.title}' (ID: {book_id}) deleted successfully.")
        return True

    def searchBook(self, book_id: int, suppress_print: bool = False):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                if not suppress_print:
                    print(f"\n📘 Book Found:\nID: {temp.book_id}\nTitle: {temp.title}\nAuthor: {temp.author}\nStatus: {temp.status}")
                return temp
            temp = temp.next
        if not suppress_print:
            print(f"❌ Book ID {book_id} not found.")
        return None

    def displayBooks(self):
        if not self.head:
            print("📚 No books available in the library.")
            return
        print("\n📚 Current Books in Library:")
        temp = self.head
        while temp:
            print(f"ID: {temp.book_id}, Title: {temp.title}, Author: {temp.author}, Status: {temp.status}")
            temp = temp.next

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def peekAll(self):
        # returns a copy from top -> bottom
        return list(reversed(self.stack))

    def isEmpty(self):
        return len(self.stack) == 0

    def display(self):
        if self.isEmpty():
            print("🕓 No transactions yet.")
            return
        print("\n🔁 Recent Transactions (most recent first):")
        for entry in reversed(self.stack):
            action, book_id = entry
            print(f"{action.upper():6}  Book ID: {book_id}")

class TransactionSystem:
    def __init__(self):
        self.books = BookList()
        self.transactions = Stack()

    def issueBook(self, book_id: int):
        book = self.books.searchBook(book_id, suppress_print=True)
        if book and book.status == "Available":
            book.status = "Issued"
            # store transaction; we only need action and book_id to undo
            self.transactions.push(("issue", book_id))
            print(f"📕 Book '{book.title}' (ID: {book_id}) has been issued.")
            return True
        elif book:
            print(f"❌ Book '{book.title}' (ID: {book_id}) is already issued.")
            return False
        else:
            print(f"❌ Issue failed: Book ID {book_id} not found.")
            return False

    def returnBook(self, book_id: int):
        book = self.books.searchBook(book_id, suppress_print=True)
        if book and book.status == "Issued":
            book.status = "Available"
            self.transactions.push(("return", book_id))
            print(f"📗 Book '{book.title}' (ID: {book_id}) has been returned.")
            return True
        elif book:
            print(f"❌ Return failed: Book '{book.title}' (ID: {book_id}) is not currently issued.")
            return False
        else:
            print(f"❌ Return failed: Book ID {book_id} not found.")
            return False

    def undoTransaction(self):
        if self.transactions.isEmpty():
            print("❌ No transaction to undo.")
            return False

        action, book_id = self.transactions.pop()
        book = self.books.searchBook(book_id, suppress_print=True)
        if not book:
            # If book not found, we cannot undo status change — inform user.
            print("❌ Undo failed: Book not found for undo operation.")
            return False

        if action == "issue":
            book.status = "Available"
            print(f"↩️ Undo successful: Issue of Book '{book.title}' (ID: {book_id}) reverted — now Available.")
            return True
        elif action == "return":
            book.status = "Issued"
            print(f"↩️ Undo successful: Return of Book '{book.title}' (ID: {book_id}) reverted — now Issued.")
            return True
        else:
            print("❌ Undo failed: Unknown transaction type.")
            return False

    def viewTransactions(self):
        self.transactions.display()

def seed_sample_data(system: TransactionSystem):
    # Optional sample books to begin with (you can remove if not required)
    sample_books = [
        (101, "Introduction to Algorithms", "Cormen"),
        (102, "Discrete Mathematics", "Rosen"),
        (103, "Data Structures Using C", "Reema Thareja"),
        (104, "Operating Systems", "Tanenbaum"),
    ]
    for bid, title, author in sample_books:
        system.books.insertBook(bid, title, author)

def main():
    system = TransactionSystem()
    # Uncomment the next line to auto-populate sample books:
    seed_sample_data(system)

    while True:
        print("\n=== 📚 Library Book Management System ===")
        print("1. Insert Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Undo Last Transaction")
        print("8. View Transactions")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ").strip()
        if choice == '1':
            try:
                bid = int(input("Enter Book ID (integer): ").strip())
            except ValueError:
                print("❌ Invalid Book ID; it must be an integer.")
                continue
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()
            system.books.insertBook(bid, title, author)

        elif choice == '2':
            try:
                bid = int(input("Enter Book ID to delete: ").strip())
            except ValueError:
                print("❌ Invalid Book ID; it must be an integer.")
                continue
            system.books.deleteBook(bid)

        elif choice == '3':
            try:
                bid = int(input("Enter Book ID to search: ").strip())
            except ValueError:
                print("❌ Invalid Book ID; it must be an integer.")
                continue
            system.books.searchBook(bid)

        elif choice == '4':
            system.books.displayBooks()

        elif choice == '5':
            try:
                bid = int(input("Enter Book ID to issue: ").strip())
            except ValueError:
                print("❌ Invalid Book ID; it must be an integer.")
                continue
            system.issueBook(bid)

        elif choice == '6':
            try:
                bid = int(input("Enter Book ID to return: ").strip())
            except ValueError:
                print("❌ Invalid Book ID; it must be an integer.")
                continue
            system.returnBook(bid)

        elif choice == '7':
            system.undoTransaction()

        elif choice == '8':
            system.viewTransactions()

        elif choice == '9':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
