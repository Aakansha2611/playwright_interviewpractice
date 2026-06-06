import time


from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("stud")
    page.locator("#terms").check()
    page.get_by_role("link" ,name= "terms and conditions").click()
    page.get_by_role("button" , name="Sign In").click()
    IphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    IphoneProduct.get_by_role("button").click()
    NokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    NokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info :
        page.get_by_role("link", name="Free Access to InterviewQues/ResumeAssistance/Material").click()
        childpage = newPage_info.value
        text =childpage.locator(".red").text_content()
        print(text)
        print(text[26:48])






