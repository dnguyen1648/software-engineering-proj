import User


class EndUser(User):  # subclass of user for extension

    secretkey = ""

    def create_secret_key(self):
        # use algorithm to generate private key
        pass

    def send_secret_key(self, target):
        # send private key to target
        pass
