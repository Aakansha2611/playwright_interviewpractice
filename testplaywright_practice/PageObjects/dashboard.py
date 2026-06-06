from playwright.sync_api import expect

from testplaywright_practice.PageObjects.OrderHistory import OrderHistory


class Dashboard:


    def __init__(self,page):
        self.page =page

    def navigation(self):
        self.page.get_by_role(role="button", name="ORDERS").click()
        orderHistoryPage =OrderHistory(self.page)
        return orderHistoryPage




