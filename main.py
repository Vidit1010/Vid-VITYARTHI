import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

DATA_FILE = "books.json"


# ---------------- JSON DATA HANDLING ---------------- #

def load_books():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=4)


# ---------------- OOP BOOK CLASS ---------------- #

class Book:
    def _init_(self, book_id, title, is_rented=False):
        self.book_id = book_id
        self.title = title
        self.is_rented = is_rented

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "is_rented": self.is_rented
        }


# ---------------- BOOK RENTAL SYSTEM ---------------- #

class BookRentalSystem:
    def _init_(self):
        self.books = load_books()

    def add_book(self, title):
        book_id = str(len(self.books) + 1)
        self.books[book_id] = Book(book_id, title).to_dict()
        save_books(self.books)

    def rent_book(self, book_id):
        if book_id not in self.books:
            return False, "Book not found"

        if self.books[book_id]["is_rented"]:
            return False, "Book already rented"

        self.books[book_id]["is_rented"] = True
        save_books(self.books)
        return True, "Book rented successfully"

    def return_book(self, book_id):
        if book_id not in self.books:
            return False, "Book not found"

        if not self.books[book_id]["is_rented"]:
            return False, "Book is not rented"

        self.books[book_id]["is_rented"] = False
        save_books(self.books)
        return True, "Book returned successfully"


# ---------------- TKINTER GUI ---------------- #

class BookRentalGUI:
    def _init_(self, root):
        self.system = BookRentalSystem()
        self.root = root
        root.title("Book Rental System")

        # Listbox to show books
        self.book_list = tk.Listbox(root, width=50, height=15)
        self.book_list.pack(pady=10)

        # Buttons
        tk.Button(root, text="Add Book", width=20, command=self.add_book).pack(pady=5)
        tk.Button(root, text="Rent Book", width=20, command=self.rent_book).pack(pady=5)
        tk.Button(root, text="Return Book", width=20, command=self.return_book).pack(pady=5)

        self.load_books_in_listbox()

    def load_books_in_listbox(self):
        self.book_list.delete(0, tk.END)
        for book_id, book in self.system.books.items():
            status = "Rented" if book["is_rented"] else "Available"
            self.book_list.insert(tk.END, f"{book_id}. {book['title']} - {status}")

    def add_book(self):
        title = simpledialog.askstring("Add Book", "Enter Book Title:")
        if title:
            self.system.add_book(title)
            self.load_books_in_listbox()
            messagebox.showinfo("Success", "Book added successfully!")

    def rent_book(self):
        selected = self.book_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a book first")
            return

        book_id = str(selected[0] + 1)
        success, msg = self.system.rent_book(book_id)
        messagebox.showinfo("Info", msg)
        self.load_books_in_listbox()

    def return_book(self):
        selected = self.book_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a book first")
            return

        book_id = str(selected[0] + 1)
        success, msg = self.system.return_book(book_id)
        messagebox.showinfo("Info", msg)
        self.load_books_in_listbox()


# ---------------- RUN APP ---------------- #

if _name_ == "_main_":
    root = tk.Tk()
    gui = BookRentalGUI(root)
    root.mainloop()
