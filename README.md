# -Library
DSA Assignment 2 — Library Book Management System
Author - Mohd Faiz
Problem: Library Book Management System 
The Library Book Management System is a console-based application designed to manage 
book records, maintain borrowing history, and track undo operations related to book issue 
or return. The system will use single linked lists for book management and stacks for 
implementing undo functionality when recent transactions (issue/return) need to be 
reverted. 
Implementation Sub-Problems 
1. Use a single linked list to manage the dynamic list of books in the library. 
2. Implement a stack-based undo mechanism for recent issue or return operations. 
3. Provide functionalities to insert, delete, and search books using linked list operations. 
4. Allow users to undo the last issue or return action using stack operations. 
5. Display the current list of available books dynamically after each operation. 
Assignment Objectives 
 Develop a foundational understanding of implementing single linked lists and stacks. 
 Gain hands-on experience in managing dynamic data using linked lists. 
 Apply stack operations to support undo mechanisms. 
 Simulate real-world problem-solving scenarios in library management. 
 Demonstrate algorithmic thinking in designing efficient insert, delete, and undo 
operations. 
Assignment Instructions 
1. Book Record ADT Design 
Attributes: 
• BookID: Integer, unique identifier for the book. 
• BookTitle: String, title of the book. 
• AuthorName: String, author of the book. 
• Status: String (Available / Issued). 
Methods: 
• insertBook(data): Add a new book record to the linked list. 
• deleteBook(BookID): Remove a book record using its BookID. 
• searchBook(BookID): Retrieve details of a specific book. 
• displayBooks(): Display all books currently in the library. 
2. Transaction Management System 
Attributes: 
• BookList: A linked list to store all book records dynamically. 
• TransactionStack: A stack to record issue and return operations for undo functionality. 
Methods: 
• issueBook(BookID): Mark a book as issued and push this transaction onto the stack. 
• returnBook(BookID): Mark a book as returned and push this transaction onto the stack. 
• undoTransaction(): Revert the last transaction using stack pop operation. 
• viewTransactions(): Display all recent transactions.
Implementation Steps 
1. Define the Book Record ADT using single linked list. 
2. Implement functions for insert, delete, and search operations. 
3. Create a stack class to record issue and return actions. 
4. Develop the undoTransaction() functionality using stack pop operation. 
5. Display the final list of books and transaction history dynamically. 
Learning Outcomes 
 Apply single linked list to implement dynamic data management in real-world 
scenarios. 
 Use stack operations to manage undo mechanisms effectively. 
 Demonstrate ability to integrate two linear data structures into a functional application.
 
