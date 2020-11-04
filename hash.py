import hashlib

      
def hash_text(plaintext):
    sha1_txt = hashlib.sha1(b'f"{plaintext}"')
    sha224_txt = hashlib.sha224(b'f"{plaintext}"')
    sha512_txt = hashlib.sha512(b'f"{plaintext}"')
    md5_txt = hashlib.md5(b'f"{plaintext}"')

    print('plain text: '+plaintext)
    print('hashed-sha1 :  '+sha1_txt.hexdigest())
    print('hashed-sha224 :  '+sha224_txt.hexdigest())
    print('hashed-sha512 :  '+sha512_txt.hexdigest())
    print('hashed-md5 :  '+md5_txt.hexdigest())



hash_text(str(input(('>>> '))))

