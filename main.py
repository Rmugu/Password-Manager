from cryptography.fernet import Fernet
import os
import json

# Function to load or create the encryption key
def load_or_create_key():
    key_file = "key.key"
    if not os.path.exists(key_file):  # If the key file does not exist
        key = Fernet.generate_key()  # Generate a new encryption key
        with open(key_file, "wb") as file:  # Write the key to the file
            file.write(key)
    else:  # If the key file already exists
        with open(key_file, "rb") as file:  # Read the key from the file
            key = file.read()
    return key

# Function to save data to a JSON file
def save_data(data):
    with open("passwords.json", "w") as file:
        json.dump(data, file)

# Function to load data from a JSON file
def load_data():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            return json.load(file)
    return {}

# Function to add a new password
def add_password(data, key):
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    # Encrypt the password
    encrypted_password = Fernet(key).encrypt(password.encode()).decode()
    
    # Save the website, username, and encrypted password
    data[website] = {"username": username, "password": encrypted_password}
    print(f"Password for {website} saved successfully!")

# Function to retrieve a password
def get_password(data, key):
    website = input("Enter the website to retrieve the password: ")
    if website in data:
        encrypted_password = data[website]["password"]
        # Decrypt the password
        password = Fernet(key).decrypt(encrypted_password.encode()).decode()
        print(f"Username: {data[website]['username']}")
        print(f"Password: {password}")
    else:
        print(f"No details found for {website}")

# Main function to drive the program
def main():
    key = load_or_create_key()  # Load or create the encryption key
    data = load_data()  # Load existing passwords or start with an empty dictionary

    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            add_password(data, key)
            save_data(data)  # Save data after adding a new password
        elif choice == "2":
            get_password(data, key)
        elif choice == "3":
            print("Exiting Password Manager...")
            break
        else:
            print("Invalid option. Try again.")

# Run the program
if __name__ == "__main__":
    main()
