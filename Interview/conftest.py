import json

import pytest
from playwright.sync_api import Playwright, Browser, BrowserContext


with open("Interview/Data3/Credentails.json") as f:
    testdata = json.load(f)
    credentails_list = testdata['user_credentails']

@pytest.fixture(scope="session")
def cred(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome or firefix"

    )

@pytest.fixture
def browser(playwright:Playwright,request):
    browsername = request.config.getoption("--browser_name")
    if browsername == "chrome":
       browser=playwright.chromium.launch(headless=True)
    elif browsername == "firefox":
        browser=playwright.firefox.launch(headless=True)
    context=browser.new_context()
    page=context.new_page()
    yield page
    context.close()
    browser.close()





