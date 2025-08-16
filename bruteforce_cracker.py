import itertools
import hashlib

def brute_force(hash_val, charset, max_len):
    for length in range(1, max_len + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt_str = ''.join(attempt)
            if hashlib.sha256(attempt_str.encode()).hexdigest() == hash_val:
                return attempt_str
    return None

if __name__ == "__main__":
    target_hash = input("Enter target SHA256 hash: ").strip()
    charset = input("Enter charset (e.g. abc123): ")
    max_len = int(input("Enter max password length: "))

    result = brute_force(target_hash, charset, max_len)
    if result:
        print("Password cracked:", result)
    else:
        print("Password not found.")
