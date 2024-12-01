import pytest
from appium import webdriver
import time


@pytest.fixture(scope="session", autouse=True)
def driver_init(request, pytestconfig):
    platform = pytestconfig.getoption('platform')  # 从命令行获取平台参数
    app_path = pytestconfig.getoption('app_path')  # 应用程序路径或包名
    device_name = pytestconfig.getoption('device_name')  # 设备名（模拟器或真机）
    appium_server = pytestconfig.getoption('appium_server')  # Appium 服务地址

    # Desired Capabilities 配置项
    desired_caps = {
        "platformName": "Android",  # 如 "Android" 或 "iOS"
        "deviceName": device_name,  # 设备名称或 "emulator-5554"
        "app": app_path,  # 应用路径或包名 (如 Android 包名)
        "automationName": "UiAutomator2" if platform == "Android" else "XCUITest",
        "noReset": True,  # 不重置应用状态
        "newCommandTimeout": 300,  # 新命令超时时间
    }

    # 初始化 Appium 驱动
    driver = webdriver.Remote(command_executor=appium_server, desired_capabilities=desired_caps)

    # 将 driver 挂载到测试类中，使其在测试用例中可用
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)  # 获取测试类对象
        setattr(cls.obj, "driver", driver)  # 动态设置 driver 属性,即self.driver=driver

    yield driver  # 测试执行时返回 driver 实例
    driver.quit()  # 测试结束后关闭 driver



