from Crypto.Cipher import AES
import base64
import string
import random
import texttable as tt

class SM:
    number = 0
    car = 3
    def __init__(self):
        self.number = SM.number
        self.car = SM.car
        self.random = ''
        self.random_list = []

    def get_random_string(self):
        for i in range(15):
            self.random_list.append(random.choice(string.digits))
        self.random = ''.join(self.random_list)

    def key_generation(self):
        for i in range(3):
            msg_text = 'car'.rjust(32)
            my_randoms = self.random + str(random.randint(0,9))
            secret_key = my_randoms
            cipher = AES.new(secret_key, AES.MODE_ECB)
            encoded = base64.b64encode(cipher.encrypt(msg_text))
            # decoded = cipher.decrypt(base64.b64decode(encoded))
            # print(decoded.strip())
            return (encoded)

tab = tt.Texttable()
header = ['car' , 'key']
tab.set_deco(tab.HEADER | tab.VLINES)

tab.set_cols_width([18,45])
tab.header(header)
car = 0
for i in range(3):
    i = SM()
    car += 1
    i.get_random_string()
    row = ["{} {}".format("car", car) ,i.key_generation()]
    tab.add_row(row)
s = tab.draw()
print(s)