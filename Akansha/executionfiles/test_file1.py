import time

from playwright.sync_api import Page, expect, Playwright

from Akansha.executionfiles.apiBase2 import APIUtils2


def test_method1(playwright):
    browser =playwright.chromium.launch(headless =False)
    context =browser.new_context()
    page =context.new_page()
    page.goto("https://eventhub.rahulshettyacademy.com/login")

def test_method2(playwright):
    browser=playwright.chromium.launch(headless= False)
    context =browser.new_context()
    page= context.new_page()
    page.goto("https://eventhub.rahulshettyacademy.com/login")
    page.get_by_role("link",name = "Register").click()

def test_method2(page:Page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")
    page.get_by_role("link",name = "Register").click()
    page.get_by_test_id("register-email").fill("akansha@gmail1.com")
    page.get_by_test_id("register-password").fill("Akansha@2611")
    page.get_by_placeholder("Repeat your password").fill("Akansha@2611")
    page.get_by_role("button",name ="Create Account").click()
    time.sleep(10)

def test_method2(page:Page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")
    page.get_by_placeholder("you@email.com").fill("akansha@gmail.com")
    page.locator("#password").fill("Anu")
    page.get_by_role("button",name ="Sign In").click()
    time.sleep(10)
    expect(page.get_by_text("Password must be at least 6 characters")).to_be_visible()

def test_method3(page:Page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")
    page.get_by_placeholder("you@email.com").fill("akansha@gmail.com")
    page.locator("#password").fill("Akansha@0000")
    page.get_by_role("button",name ="Sign In").click()
    error_toast = page.locator("div[aria-live='polite']")
    expect(error_toast).to_be_visible(timeout=5000)

def test_method3(page:Page):
    page.goto("https://eventhub.rahulshettyacademy.com/login")
    page.get_by_placeholder("you@email.com").fill("akansha@gmail.com")
    page.locator("#password").fill("Akansha@2611")
    page.get_by_role("button",name ="Sign In").click()
    page.get_by_role("link",name ="View all").click()
    page.get_by_placeholder("Search events, venues…").fill("Hollywood Monsoon Night — Los Angeles")
    time.sleep(10)
    page.get_by_role("link",name ="Book Now").click()
    page.get_by_role("button",name ="+").click()
    page.locator("#customerName").fill("Akansha Soni")
    page.locator("#customer-email").fill("akansha@gmail.com")
    page.locator("#phone").fill("7406927905")
    time.sleep(10)
    page.locator("#confirm-booking").click()
    expect(page.get_by_text("Booking Confirmed!")).to_be_visible()
    page.get_by_text("View My Bookings").click()
    expect(page.get_by_text("confirmed")).to_be_visible()

def test_method4(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("input[value='radio1']").click()
    #page.locator("label").filter(has_text="Radio1").get_by_role("radio").check()
    page.get_by_placeholder("Type to Select Countries").fill("India")
    page.get_by_text("India", exact=True).click()
    page.locator("#dropdown-class-example").select_option("Option2")
    page.locator("#checkBoxOption3").check()

    with page.expect_popup() as newPage_info:
        page.get_by_role("button", name="Open Window").click()
    childpage = newPage_info.value
    text= childpage.locator("._domain_125zm_10").text_content()
    print(text)
    childpage.close()
    page.bring_to_front()

    with page.expect_popup() as tab_info:
        page.get_by_role("link", name="Open Tab").click()
    new_tab = tab_info.value
    text = new_tab.locator("._domain_125zm_10").text_content()
    print(text)
    new_tab.close()
    page.bring_to_front()

    page.get_by_placeholder("Enter Your Name").fill("Akansha soni")
    page.locator("#alertbtn").click()
    page.on("dialog", lambda dialog: dialog.accept())

    element = page.get_by_role("button", name="Mouse Hover")
    element.hover()
    page.get_by_role("link",name="Top").click()


    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("#hide-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    page_frame= page.frame_locator("#courses-iframe")
    expect(page_frame.get_by_role("link",name="All Access plan")).to_be_visible()


    time.sleep(10)


def test_method5(playwright:Playwright):
    browser =playwright.chromium.launch(headless=False)
    context =browser.new_context()
    page =context.new_page()

    api_utils= APIUtils2()
    orderID2 = api_utils.createOrder(playwright)

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("akanshasoni.2611@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Anu@2611")
    page.locator("#login").click()

    context.close()








