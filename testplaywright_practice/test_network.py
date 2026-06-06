import pytest
from playwright.sync_api import Page

fakepayloadorderresponse = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json= fakepayloadorderresponse
    )



@pytest.mark.smoke
def test_network(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)
    page.get_by_placeholder("email@example.com").fill("akanshasoni.2611@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Anu@2611")
    page.locator("#login").click()
    page.get_by_role(role="button",name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)




