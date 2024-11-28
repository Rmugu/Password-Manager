# Password Manager

A simple password manager application built with Python. It securely encrypts and stores passwords and retrieves them when needed.

---

## Features

- **Encryption:** Uses AES (Advanced Encryption Standard) for secure password storage.
- **Password Management:** Add, view, update, and delete passwords.
- **User-Friendly Interface:** Command-line based, easy to use.
- **Local Storage:** Passwords are stored securely in a JSON file.

---

## Installation

Follow these steps to set up the project on your local system:

1. Clone the repository:
   ```bash
   git clone https://github.com/Rmugu/Password-Manager.git

## Navigate to the project folder:

   cd password-manager

## Create a virtual environment:

   python -m venv venv

## Activate the virtual environment:

    Windows:

       venv\Scripts\activate

    macOS/Linux:

       source venv/bin/activate

## Install the required dependencies:

    pip install -r requirements.txt

## Run the application:

    python main.py

## Follow the on-screen instructions to manage your passwords:

    Add a new password
    Retrieve stored passwords
    Update existing passwords

## File Structure

  Below is the structure of the project:

    PasswordManager/
    │
    ├── main.py               # Main application script
    ├── README.md             # Project documentation
    ├── requirements.txt      # Python dependencies
    ├── password.json         # Stores encrypted passwords
    ├── key.key               # Encryption key
    └── venv/                 # Virtual environment folder

## Libraries Used

  The project uses the following Python libraries:

   1. cryptography: For AES encryption and decryption.
   2. json: For storing password data in a structured format.