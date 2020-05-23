import hashlib
from database import create_password_table, update_password_table


def password_hash(password):
    # Hashes received password
    hash_pw = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Splits the password hashes into 2 for storage
    head = hash_pw[:5]
    tail = hash_pw[5:]

    password_list = (head, tail)

    # Stores the passwords into the database using the call function
    create_password_table('contact', 'reg_password')
    update_password_table('contact', 'reg_password', password_list)

    return head


create_password_table('contact', 'reg_password')
