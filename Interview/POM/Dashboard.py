from Interview.POM.Checkout import Checkout


class Dashboard:

    def __init__(self,page):
        self.page = page



    def selectorder(self):
         self.page.locator("[routerlink ='/dashboard/myorders']").click()
         check =Checkout(self.page)
         return check

