import random
import sys

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
        'abcdefghijklmnopqrstuvwxyz' + \
        '0123456789' + \
        ':.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\\t\n\xe2\x80\x93'

def generate_key():
    """Generate an key for our cipher"""
    shuffled = sorted(chars, key=lambda k: random.random())
    return dict(zip(chars, shuffled))

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    return ''.join(key[l] for l in plaintext)

def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    flipped = {v: k for k, v in key.items()}
    return ''.join(flipped[l] for l in ciphertext)

if len(sys.argv) < 2:
    print "ERROR!!"
    print "Usage : python encrypt.py <encrypt|decrypt> <input_file> <output_file>"
    sys.exit()

def get_readable_key(key):
    return ''.join(key[l] for l in chars)

def create_hash(key_string):
    key = {}
    for i in range(0, len(chars)):
        key[chars[i]] = key_string[i]
    return key

operation = sys.argv[1]
input_filename = sys.argv[2]
output_filename = sys.argv[3]
output_file = open(output_filename, "w+")
input_file = open(input_filename, "r")
out = ""

if operation == "encrypt":
    key = generate_key()
    key_file = open("key", "w+")
    key_string = key_file.write(get_readable_key(key))
    key_file.close()
    print "WARNING!!"
    print "Please use 'key' file to decrypt. If you lose this key, you can't recover your data."
    out = encrypt(key, input_file.read())
elif operation == "decrypt":
    key_file = open("key", "r")
    key_string = key_file.read()
    key_file.close()
    key = create_hash(key_string)
    out = decrypt(key, input_file.read())
else:
    print "ERROR!!"
    print "Select one of these \"encrypt\" or \"decrypt\""
    input_file.close()
    output_file.close()
    sys.exit()

output_file.write(out)

input_file.close()
output_file.close()
