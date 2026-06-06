from playwright.sync_api import expect


class Checkout:

    def __init__(self,page):
        self.page = page



    def orderhistory(self,orderID):
        view = self.page.locator("tr").filter(has_text=orderID)
        view.get_by_text("View").click()
        expect(self.page.get_by_text("Thank you for Shopping With Us")).to_be_visible()
