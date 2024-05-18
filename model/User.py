import os.path

import Reader
class user:
    def __init__(self,login,password):
        self.login = login
        self.password = password
        if os.path.exists("Users.dat"):
            usList=Reader.Reader.reader.read_object("Users.dat")
            lenght=len(usList)
            self.user_number=lenght
        else:
             self.user_number=0