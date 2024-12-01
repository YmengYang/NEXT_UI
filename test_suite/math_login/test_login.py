import pytest

from pages.math.login_page import LoginApp

@pytest.mark.usefixtures("driver_init")
class TestApp:
    def test_login(self):
        login_page = LoginApp(self.driver)
        login_page.input_username("test_user")
        login_page.input_password("password123")
        login_page.click_login()