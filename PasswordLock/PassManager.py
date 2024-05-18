import os.path
import model
import Reader
import Writer
## zrobić krotke do zwracania w log_in
class PasswordManager:
    def __init__(self):
        if os.path.exists("Users.dat"):
            self.users_list = Reader.Reader.reader.read_object("Users.dat")
        else:
            self.users_list = []

    def create_account(self, username, password):
        new_user = model.User.user(username, password)
        self.users_list.append(new_user)
        Writer.Writer.writer.save_object(self.users_list, "Users.dat")

    def log_in(self, username, password):
        for user in self.users_list:
            if user.login == username and user.password == password:
                return True, user.user_number

        print("Invalid username or bad password")
        return False, None

    def show_users(self):
        if not self.users_list:
            print("No users available.")
        else:
            for user in self.users_list:
                print(f"Username: {user.username}, User Number: {user.user_number}")