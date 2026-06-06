import json

import pytest
from playwright.sync_api import Playwright, expect, Page

from test_network import fakepayloadorderresponse

with open("Interview/Data3/Credentails.json") as f:
    testdata = json.load(f)
    credentails_list = testdata['user_credentails']



def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6a23267417ee3eabf4054")


@pytest.mark.parametrize('cred',credentails_list)
def test_network(page:Page,cred):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*" , intercept_request)
    page.locator("#userEmail").fill(cred['email'])
    page.locator("#userPassword").fill(cred['password'])
    page.locator("#login").click()
    page.locator("[routerlink ='/dashboard/myorders']").click()
    page.get_by_role("button" ,name ="ORDERS").click()
    page.get_by_role("button",name ="View").first.click()
    msg =page.get_by_text("You are not authorize to view this order").text_content()
    print(msg)


