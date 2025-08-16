import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_with_salt(password, salt=None):
    if not salt:
        salt = os.urandom(16).hex()
    return hashlib.sha256((password + salt).encode()).hexdigest(), salt

if __name__ == "__main__":
    pwd = input("Enter password: ")
    h = hash_password(pwd)
    print("SHA256 Hash:", h)

    hs, salt = hash_with_salt(pwd)
    print("Salted Hash:", hs)
    print("Salt:", salt)

    with open("hashes.txt", "a") as f:
        f.write(h + "\n")
