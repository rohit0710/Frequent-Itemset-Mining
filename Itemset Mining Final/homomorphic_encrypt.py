import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast, sys

if len(sys.argv) < 2:
    print "ERROR!!"
    print "Usage : python encrypt.py <encrypt|decrypt> <input_file> <output_file>"
    sys.exit()

operation = sys.argv[1]
input_filename = sys.argv[2]
output_filename = sys.argv[3]
output_file = open(output_filename, "w+")
input_file = open(input_filename, "r")
out = ""
readsize = 127
writesize = 128

if operation == "encrypt":
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    public_key = key.publickey()
    private = key.exportKey(format='PEM', passphrase=None, pkcs = 1)
    private_key_file = open("private_key.pem", "w+")
    private_key_file.write(private)
    private_key_file.close()

    public = key.publickey().exportKey(format='PEM')
    public_key_file = open("public_key.pem", "w+")
    public_key_file.write(public)
    private_key_file.close()

    print "WARNING!!"
    print "Please use 'private_key.pem' and 'public_key.pem' files to decrypt. If you lose these keys, you can't recover your data."

    data = input_file.read()
    i = 0
    while True:
        if(data[i:i+readsize+1] == ""):
            break 
        inp = data[i:i+readsize]
        i = i + readsize
        enc_data = public_key.encrypt(inp, 32)[0]
        while len(enc_data) < writesize:
            enc_data = "\x00" + enc_data
        out = out + enc_data
elif operation == "decrypt":
    key_file = open("private_key.pem", "r")
    key_string = key_file.read()
    key_file.close()
    key = RSA.importKey(key_string, passphrase=None)

    data = input_file.read()
    j = 0
    while True:
        if(data[j:j+writesize+1] == ""):
            break
        inp = data[j:j+writesize]
        dec_data = key.decrypt(inp)
        j = j + writesize
        out = out + dec_data[:readsize]
else:
    print "ERROR!!"
    print "Select one of these \"encrypt\" or \"decrypt\""
    input_file.close()
    output_file.close()
    sys.exit()

output_file.write(out)

input_file.close()
output_file.close()
