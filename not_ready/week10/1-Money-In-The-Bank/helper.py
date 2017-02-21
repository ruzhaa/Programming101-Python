import hashlib
import random


def generate_salt():
    rbits = random.getrandbits(256)
    m = hashlib.sha256()
    m.update(str(rbits).encode('utf-8'))
    return m.hexdigest()


def hash_my_password(password, salt=None):
    m = hashlib.sha256()
    if salt is None:
        salt = generate_salt()

    m.update(password + salt).encode('utf-8')
    return (m.hexdigest(), salt)
