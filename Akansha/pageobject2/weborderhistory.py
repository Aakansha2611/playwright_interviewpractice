from Akansha.pageobject2.Weborderdetail import WeborderDetail


class Weborderhistory():

    def __init__(self,page):
        self.page = page

    def view(self, orderID2):
        row = self.page.locator("tr").filter(has_text=orderID2)
        row.get_by_role(role="button", name="View").first.click()
        weborderDetail=WeborderDetail(self.page)
        return weborderDetail
