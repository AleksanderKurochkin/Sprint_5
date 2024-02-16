import random
import string

def generate_random_email():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{username}@{domain}.com"