import pytest
from appium import webdriver
# , "appWaitActivity": "ru.yandex.weatherplugin.ui.activity.SplashActivity"
@pytest.fixture(scope="session")
def driver():
    desired_capabilities = {'platformName': "Android", 'platformVersion': "8", 'deviceName': "Android Emulator",
                            "app": "C:/Wildberries.apk", "appWaitActivity": "com.wildberries.ru.CountryListActivity"}
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)
    yield driver
    print("\nquit driver..")
    driver.quit()
