from Akansha.pageobject2.weborderhistory import Weborderhistory


class WebdashboardPage:

    def __init__(self,page):
        self.page = page

    def navigationlink(self):
        self.page.get_by_role(role="button", name="ORDERS").click()
        weborderhistory = Weborderhistory(self.page)
        return weborderhistory

