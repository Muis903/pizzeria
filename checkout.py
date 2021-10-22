from data import staff_data as s_d

class CheckOut():
    """All tools to use checkout"""
    def __init__(self, login, password):
        """Arguments of checkout"""
        self.login = login
        self.password = password


    def sing_up(self):
        if self.login == s_d.manager['login'] and self.password == s_d.manager['password']:
            print("Welcome manager!")


test = CheckOut('7512077532', '210220022210')
test.sing_up()
