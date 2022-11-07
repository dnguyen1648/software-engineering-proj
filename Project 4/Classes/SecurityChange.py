class SecurityChange:  # this holds security changes that will go into effect
    # this is a batch of settings because the admin will change settings as they wish and whenever they click apply/save
    # changes it will create a SecurityChange Object

    refresh_timer = 0  # time between key refreshes
    key_size = 0
    password_reqs = {}  # dict holding certain bool requirements for passwords

    def __init__(self, refresh_timer, key_size, password_reqs):
        self.refresh_timer = refresh_timer
        self.key_size = key_size
        self.password_reqs = password_reqs
