from appium import webdriver
import requests


def get_answer(api_url, params):
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get('答案')
    else:
        raise Exception(f"API请求失败，状态码：{response.status_code}")


def init_driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "emulator-5554",
        "appPackage": "com.example.app",
        "appActivity": ".MainActivity",
        "noReset": True,
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver


def get_app_options(driver, option_locator):
    elements = driver.find_elements_by_xpath(option_locator)
    options = {elem.text: elem for elem in elements}
    return options


def find_and_click_correct_option(driver, correct_answer, options):
    for text, element in options.items():
        if correct_answer in text:
            element.click()
            print(f"选择了正确选项：{text}")
            return True
    print("未找到正确选项")
    return False


def auto_answer_question(api_url, params, driver, option_locator):
    correct_answer = get_answer(api_url, params)
    options = get_app_options(driver, option_locator)
    find_and_click_correct_option(driver, correct_answer, options)


# 主程序
api_url = "https://example.com/get-answer"
params = {"question_id": 12345}
option_locator = "//android.widget.TextView[@resource-id='com.example.app:id/option_text']"

driver = init_driver()
try:
    auto_answer_question(api_url, params, driver, option_locator)
finally:
    driver.quit()
