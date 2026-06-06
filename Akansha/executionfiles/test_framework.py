import json

import pytest
from playwright.sync_api import Playwright

from Akansha.executionfiles.apiBase2 import APIUtils2
from Akansha.pageobject2.Webdashboardpage import WebdashboardPage
from Akansha.pageobject2.Webloginlpage import Webloginlpage
from Akansha.pageobject2.Weborderdetail import WeborderDetail

with open('Akansha/Data2/credentails.json') as f:
    json_data = json.load(f)
    transcendentals_list = json_data["user_credentials"]

@pytest.mark.parametrize('user_credentials', transcendentals_list) #give value of where is my testdata
def test_framework(playwright:Playwright,user_credentials,browserPage):


    username =user_credentials["user_email"]
    password =user_credentials["user_password"]

    api_utils= APIUtils2()
    orderID2 = api_utils.createOrder(playwright,user_credentials)
    webloginlpage = Webloginlpage(browserPage)
    webloginlpage.navigate()
    webdashboardPage=webloginlpage.login(username,password)
    weborderhistory =webdashboardPage.navigationlink()
    weborderDetail=weborderhistory.view(orderID2)
    weborderDetail.final()
