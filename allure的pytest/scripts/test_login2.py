from page.login_page import LoginPage
import  pytest


class TestLogin:
    def setup(self):
        self.login_page = LoginPage()


    def test_login1(self, username, password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

        assert 1