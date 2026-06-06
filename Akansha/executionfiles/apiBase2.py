import token

from playwright.sync_api import Playwright



orderPayLoad = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}

class APIUtils2:

    def get_token(self,playwright: Playwright,user_credentials):
      api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
      response =api_request_context.post("api/ecom/auth/login",
                               data ={"userEmail":user_credentials["user_email"],"userPassword":user_credentials["user_password"]})
      assert response.ok
      response_body =response.json()
      return response_body["token"]


    def createOrder(self,playwright:Playwright,user_credentials):
        token =self.get_token(playwright,user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response =api_request_context.post("api/ecom/order/create-order",
                                 data=orderPayLoad,
                                 headers={"Authorization": token,
                                          "content-type": "application/json"}
                                 )
        print(response.json())
