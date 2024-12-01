from appium.webdriver.common.appiumby import AppiumBy

class LoginApp:
    def __init__(self, driver):
        self.driver = driver

    def input_username(self, username):
        username_input = self.driver.find_element(AppiumBy.ID, "com.example.app:id/username_input")
        username_input.send_keys(username)

    def input_password(self, password):
        password_input = self.driver.find_element(AppiumBy.ID, "com.example.app:id/password_input")
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(AppiumBy.ID, "com.example.app:id/login_button")
        login_button.click()
