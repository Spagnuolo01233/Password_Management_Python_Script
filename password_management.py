import string
import secrets
from cryptography.fernet import Fernet
import csv
import os

# Generate a passsword with a specific length
def crea_password(length):
    '''
    Generate a random password of the specified length.
    '''
    alphabet = string.punctuation + string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Encrypt a password
def encrypt_password(password, encryption_key):
    '''
    Encrypt a password using Fernet encryption.
    '''
    f = Fernet(encryption_key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password


def create_or_open_CSV(name_file):
    '''
    Create or open a CSV file for storing passwords.
    '''

    # Header of the table.
    header_colonne = ['UserName','Password','Cryptography_key']
    # File path.
    repository = '/Users/pietrostriano/Desktop/file_CSV'
    # CSV file's name.
    file_csv = os.path.join(repository, name_file)

    # Check if file exist.
    if not os.path.isfile(file_csv):
        # if file doesn't exist, we create it.
        with open(file_csv, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header_colonne)
    return file_csv

# File_csv will take the absolute path of the file.
def add_password_to_csv(file_csv, username, password, encryption_key):
    '''
    Add a password to the CSV file.
    '''
     # Check if file exist.
    if not os.path.isfile(file_csv):
        print('File non esiste.')
    else:
        # Add the dates to the file.
        with open(file_csv, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([username, password, encryption_key])




if __name__ == "__main__":
    # Esempio di utilizzo
    name_file = "passwords.csv"
    file_csv = create_or_open_CSV(name_file)

    username = "utente1"
    password = crea_password(12)
    encryption_key = Fernet.generate_key()
    encrypted_password = encrypt_password(password, encryption_key)

    add_password_to_csv(file_csv, username, encrypted_password, encryption_key)

