class User:  # parent class for users

    userID = 0
    password = ""
    companyID = 0
    settings = {}  # dict for user settings that will have a setting and a bool for if active or not

    def login(self):
        # attempt login to this account
        pass

    def logout(self):
        # logout of this account
        pass

    def change_user_settings(self):
        # change settings
        pass
