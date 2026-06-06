from Interview.POM.Dashboard import Dashboard


class LoginPage:

    def __init__(self,page):
        self.page = page



    def navigate(self):
         self.page.goto("https://rahulshettyacademy.com/client")

    def login(self,cred):
        self.page.locator("#userEmail").fill(cred['email'])
        self.page.locator("#userPassword").fill(cred['password'])
        self.page.locator("#login").click()
        dashboard = Dashboard(self.page)
        return dashboard
