import json

import pytest
from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser
from typing_extensions import assert_type

from testplaywright_practice.PageObjects.dashboard import Dashboard
from testplaywright_practice.PageObjects.login import LoginPage
from testplaywright_practice.Utils.apiBaseframework import APIUtils

with open('testplaywright_practice/Data/credentails.json') as f:
    credentials = json.load(f)
    print(credentials)
    user_credentials_list = credentials['user_credentails']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentails',user_credentials_list)
def test_e2e_web_api(playwright: Playwright,browserInstance ,user_credentails):
    username= user_credentails["user_email"]
    password =user_credentails["user_password"]


    api_utils= APIUtils()
    orderID = api_utils.createOrder(playwright,user_credentails)

    loginpage= LoginPage(browserInstance)
    loginpage.navigate()
    dashboard=loginpage.login(username,password)
    orderHistoryPage=dashboard.navigation()
    OrderDetailspage=orderHistoryPage.view(orderID)
    OrderDetailspage.verify()







