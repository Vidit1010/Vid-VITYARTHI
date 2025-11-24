📚 Book Rental System

A simple Python + Tkinter desktop application that allows users to rent, return, and manage books using a JSON-based database. The project is beginner-friendly and focuses on GUI programming, file handling, and basic CRUD operations.


---

🚀 Features

📘 Add new books to the library

🏷 Rent a book

🔄 Return a book

📁 Data stored in a lightweight JSON file

🖥 Simple GUI using Tkinter

🔍 View all available & rented books

💾 Automatic data saving



---

🛠 Tech Stack

Python 3.x

Tkinter – GUI Framework

JSON – Data Storage



---

📂 Project Structure

book-rental-system/
│── app.py              # Main Tkinter application  
│── data.json           # JSON database for books  
│── readme.md           # Documentation  
│── assets/ (optional)  # Images/icons


---

⚙ How to Run the Project

⿡ Install Python

Make sure Python 3.x is installed on your system.

⿢ Clone the Repository

git clone https://github.com/your-username/book-rental-system.git
cd book-rental-system

⿣ Run the App

python app.py


---

🧪 JSON File Structure (Example)

{
  "books": [
    {
      "id": 1,
      "title": "Harry Potter",
      "author": "J.K. Rowling",
      "available": true
    },
    {
      "id": 2,
      "title": "Atomic Habits",
      "author": "James Clear",
      "available": false
    }
  ]
