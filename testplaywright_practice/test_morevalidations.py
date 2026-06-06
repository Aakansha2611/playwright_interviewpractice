import time

from playwright.sync_api import Page, expect


def test_Uichecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role(role="button",name ="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

def test_Alerts(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_placeholder("Enter Your Name").fill("Akansha")
    page.on("dailog" ,lambda dailog:dailog.accept())
    page.get_by_role(role="button",name ="Confirm").click()

def test_frame(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link" ,name ="All Access plan").click()
    expect(page_frame.get_by_text("Happy Subscibers")).to_be_visible()
    #expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")

def test_webtables(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    page.locator("th")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            colvalue =index
            print(f"Price column value {colvalue}")
            break
    rice_row = page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(colvalue)).to_have_text("37")

def test_mousehover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role(role="link",name="Top").click()

















