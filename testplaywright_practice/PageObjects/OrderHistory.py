from playwright.sync_api import expect

from testplaywright_practice.PageObjects.OrderDetails import OrderDetails

class OrderHistory:

    def __init__(self,page):
        self.page =page

    def view(self,orderID):
        row = self.page.locator("tr").filter(has_text=orderID)
        row.get_by_role(role="button", name="View").click()
        OrderDetailspage = OrderDetails(self.page)
        return OrderDetailspage



