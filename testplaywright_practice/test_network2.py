import time

from playwright.sync_api import Page, Playwright, expect
from pytest_playwright.pytest_playwright import browser

from testplaywright_practice.Utils.apiBase import APIUtils


def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69d3e6d2f86ba51a654c44d2")



def test_network(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_request)
    page.get_by_placeholder("email@example.com").fill("akanshasoni.2611@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Anu@2611")
    page.locator("#login").click()
    page.get_by_role(role="button",name="ORDERS").click()
    page.get_by_role(role="button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session(playwright:Playwright):
    api_utils = APIUtils()
    getToken= api_utils.getToken(playwright)
    browser=playwright.chromium.launch(headless=False)
    context =browser.new_context()
    page=context.new_page()
    page.add_init_script(f"""localStorage.setItem("token","{getToken}")""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role(role="button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()










