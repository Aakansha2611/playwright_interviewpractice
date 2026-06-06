import time

from playwright.sync_api import Page, expect ,Playwright



def test_playwrightbasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_playwrightShortCut(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK21")
    page.get_by_role("combobox").select_option("stud")
    page.locator("#terms").check()
    page.get_by_role("link" ,name= "terms and conditions").click()
    page.get_by_role("button" , name="Sign In").click()
    expect(page.get_by_text("Incorrect  username/password.")).to_be_visible()

def test_firefoxBrowser(playwright: Playwright):
    firefoxBrowser = playwright.firefox
    browser = firefoxBrowser.launch(headless=False)
    page =browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK21")
    page.get_by_role("combobox").select_option("stud")
    page.locator("#terms").check()
    page.get_by_role("link" ,name= "terms and conditions").click()
    page.get_by_role("button" , name="Sign In").click()
    expect(page.get_by_text("Incorrect  username/password.")).to_be_visible()













