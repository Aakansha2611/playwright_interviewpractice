import json

import pytest
from playwright.sync_api import Playwright, expect, Page



with open("Interview/Data3/Credentails.json") as f:
    testdata = json.load(f)
    credentails_list = testdata['user_credentails']

fakepayloadorderresponse ={"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json =fakepayloadorderresponse
    )
@pytest.mark.parametrize('cred',credentails_list)
def test_network(page:Page,cred):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)
    page.locator("#userEmail").fill(cred['email'])
    page.locator("#userPassword").fill(cred['password'])
    page.locator("#login").click()
    page.locator("[routerlink ='/dashboard/myorders']").click()
    order_text= page.locator(".mt-4").text_content()
    print(order_text)

