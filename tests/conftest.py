import os
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from framework.demoqa_with_env import DemoQaWithEnv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attachments

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def demoshop(env):
    return DemoQaWithEnv(env)


@pytest.fixture(scope='session')
def cookie(demoshop):
    response = demoshop.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    return authorization_cookie


@pytest.fixture(scope='function')
def app(demoshop, cookie):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN_SELENOID')
    password = os.getenv('PASSWORD_SELENOID')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver
    browser.config.base_url = demoshop.demoqa.url
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    yield browser
    attachments.add_html(browser)
    attachments.add_screenshot(browser)
    attachments.add_logs(browser)
    attachments.add_video(browser)
    browser.quit()
    browser.quit()


@pytest.fixture(scope='session')
def reqres(env):
    return DemoQaWithEnv(env).reqres
