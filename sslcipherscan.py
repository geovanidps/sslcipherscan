#!/usr/bin/env python3
import time
import subprocess
from datetime import datetime

# Lista de cifras fracas
weak_ciphers = ['RC4', 'MD5', 'SSLv2', 'EXP', 'NULL', 'ADH', 'LOW', '3DES', 'DES']

def obtain_cipher_list():
    try:
        result = subprocess.check_output(["openssl", "ciphers", "ALL:eNULL"]).decode("utf-8")
        return result.split(":")
    except subprocess.CalledProcessError:
        return []

def test_cipher(server, cipher):
    try:
        result = subprocess.check_output(["openssl", "s_client", "-cipher", cipher, "-connect", server], stderr=subprocess.STDOUT).decode("utf-8")
        if "Cipher is " + cipher in result or "Cipher    :" in result:
            if cipher in weak_ciphers:
                return "YES, but it's a weak cipher"
            else:
                return "YES"
        else:
            return "UNKNOWN RESPONSE\n" + result
    except subprocess.CalledProcessError as e:
        return "NO ({})".format(e.output.decode("utf-8").split(":")[-1].strip())

def main():
    server = input("Enter the server address (e.g., example.com:443): ")
    delay = 1
    ciphers = obtain_cipher_list()

    print(f"Obtaining cipher list from OpenSSL version {subprocess.check_output(['openssl', 'version']).decode('utf-8')}.")

    for cipher in ciphers:
        print(f"Testing {cipher}...", end=" ")
        result = test_cipher(server, cipher)
        print(result)
        time.sleep(delay)

if __name__ == "__main__":
    main()


